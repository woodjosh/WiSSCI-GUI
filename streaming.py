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


class StreamingThread(QtCore.QThread):
    """streams data to the WiSSCI from selected src"""
    # Signals handling the pixmap icon (red or green led) indicating the BT status
    bool_signal_BTStatus = QtCore.pyqtSignal(bool)
    str_signal_SentWiSSCI = QtCore.pyqtSignal(str)
    str_signal_RecvdWiSSCI = QtCore.pyqtSignal(str)

    def __init__(self, ser, lock, binlength):
        super().__init__()
        self.ser = ser
        self.src = None
        self.offline_filename = None
        self.lock = lock
        self.binlength = binlength  # in ms
        self._running = False

    def set_src(self, src, filename=None):
        """set the src of the data to stream"""
        self.src = src
        if src == "offline":
            self.offline_filename = filename

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

        # initialize streaming_src to the correct source
        if self.src == "offline":
            streaming_src = stream_offline.OfflineStream(self.offline_filename)
        elif self.src == "nomad":
            elecs = xp.list_elec('micro')
            streaming_src = stream_nomad.NomadStream(elecs, self.binlength)
        else:
            raise Exception("invalid streaming source")

        # this loop runs until we ask it to stop
        while self._running:
            try:
                # this is implemented by both source types
                # future source types should have this fn
                send_msg, print_msg = streaming_src.get_msg()

                # send the msg to the WiSSCI
                serial_WiSSCI.send_bt_msg(self.ser, self.lock, send_msg)
                # send the print version to the scrolling window
                self.str_signal_SentWiSSCI.emit(print_msg)

                # get the response from the WiSSCI (with specific timeout)
                msg = serial_WiSSCI.read_bt_timeout(self.ser, self.lock, self.binlength/1000)
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




