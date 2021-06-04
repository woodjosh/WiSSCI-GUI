"""
    streaming.py
    ----------
    Implements a QThread for sending data to the WiSSCI from selected src
"""
from PyQt5 import QtCore
import serial_WiSSCI
import stream_offline
import stream_nomad
import xipppy as xp
from contextlib import ExitStack
from datetime import datetime
import struct


class StreamingThread(QtCore.QThread):
    """streams data to the WiSSCI from selected src"""
    # Signals handling the pixmap icon (red or green led) indicating the BT status
    bool_signal_BTStatus = QtCore.pyqtSignal(bool)
    list_signal_SentWiSSCI = QtCore.pyqtSignal(list)
    str_signal_RecvdWiSSCI = QtCore.pyqtSignal(str)
    str_signal_timeSent = QtCore.pyqtSignal(str)

    def __init__(self, ser, lock, binlength):
        super().__init__()
        self.ser = ser
        self.src = 'dummy'
        self.offline_filename = None
        self.elecs = None
        self.lock = lock
        self.binlength = binlength  # in ms
        self._running = False
        self.streaming_src = None

    def set_src(self, src, filename=None):
        """set the src of the data to stream"""
        self.src = src
        if src == "offline":
            self.offline_filename = filename
            self.streaming_src = stream_offline.OfflineStream(self.offline_filename)
        elif src == "nomad":
            # self.elecs = elecs
            self.streaming_src = stream_nomad.NomadStream(self.binlength)

    def stop(self):
        """Stop the running thread gracefully."""
        print("Stopping Streaming thread...")
        self._running = False

        # Wait for the thread to stop
        self.wait()
        print("Streaming Thread stopped")

    def run(self):
        """run the thread"""
        print("Starting Streaming thread from " + self.src + "...")
        self._running = True

        with ExitStack() as stack:
            if self.src == "nomad":
                stack.enter_context(xp.xipppy_open(True))

        # this loop runs until we ask it to stop
        while self._running:
            try:
                if self.src == "dummy":
                    send_msg = bytearray(36)
                    struct.pack_into('2c', send_msg, 0, bytes('-', 'ascii'), bytes('>', 'ascii'))

                    plot_msg = [0]*12
                    struct.pack_into(f'{12}h', send_msg, 2, *plot_msg)

                    time_msg = datetime.now().strftime("%M%S%f,")
                    struct.pack_into('10s', send_msg, 26, time_msg.encode('UTF-8'))
                elif self.src == "nomad":
                    # get data from nomad
                    elecs = xp.list_elec('micro')
                    data_in, _ = xp.cont_hires(2 * self.binlength, elecs)
                    send_msg, plot_msg, time_msg = self.streaming_src.get_msg(data_in)
                elif self.src == "offline":
                    send_msg, plot_msg, time_msg = self.streaming_src.get_msg()
                else:
                    raise Exception("invalid streaming source")

                # send the msg to the WiSSCI
                serial_WiSSCI.send_bt_msg(self.ser, self.lock, send_msg)
                # send the print version to the scrolling window
                self.list_signal_SentWiSSCI.emit(plot_msg)
                # send the time message to be logged
                self.str_signal_timeSent.emit(time_msg)

                # get the response from the WiSSCI (with specific timeout)
                msg = serial_WiSSCI.read_bt_timeout(self.ser, self.lock, self.binlength / 1000)
                if msg == "":
                    # no message was received in time
                    self.str_signal_RecvdWiSSCI.emit("dropped packet")
                    serial_WiSSCI.flush_bt_buffers(self.ser, self.lock)
                elif "## Disconnected!" in msg:
                    # bluetooth was disconnected
                    self.stop()
                    self.bool_signal_BTStatus.emit(False)
                else:
                    # we got a valid response
                    self.str_signal_RecvdWiSSCI.emit(msg)
                    continue

            except Exception as e:
                print("Problem in streaming thread\n"
                      "Exception: " + str(e) + "\n")
