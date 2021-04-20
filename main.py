"""
    main.py
    --------------
    This is the main module. Implements the UI and business logic.

"""
import sys
import serial
import streaming
import threading
from PyQt5 import QtWidgets, QtGui, QtCore
from WiSSCI import Ui_MainWindow
import serial_WiSSCI
from LostConnDialog import Ui_Dialog as Form
import load_config
import numpy as np
from functools import partial
import xipppy as xp

# Define status icons
ICON_RED_LED = "Icons/led-red-on.png"
ICON_GREEN_LED = "Icons/green-led-on.png"


class WissciGui(QtWidgets.QMainWindow):
    """Create the UI, based on PyQt5.
        The UI elements are defined in "WiSSCI.ui", created in QT Designer.
        To update "WiSSCI.py":
            Run "pyuic5.exe --from-imports WiSSCI.ui -o WiSSCI.py"
        Note: Never modify "WiSSCI.py" manually.
        """
    def __init__(self):
        super().__init__()

        # Create the main window
        self.ui = Ui_MainWindow()

        # initialize params to be sent to the WiSSCI
        self.params = bytearray(886)
        self.param_file = None
        # set up the UI
        self.ui.setupUi(self)

        # set up the dialog
        self.dialog = QtWidgets.QDialog()
        self.dialog.ui = Form()
        self.dialog.ui.setupUi(self.dialog)

        # Object for locking the serial port while sending/receiving data
        self.lock = threading.Lock()

        # Get a list of available serial ports (e.g. "COM1" in Windows)
        self.serial_ports = serial_WiSSCI.get_serial_ports()

        # Populate the "COM port" combo box with available serial ports
        self.ui.ComPort_Combo.addItems(self.serial_ports)

        # serial comm object for BL654 dongle
        self.ser = serial.Serial()
        serial_WiSSCI.setup_bt(self.ser, self.ui.ComPort_Combo.currentText(), self.lock)

        # Create QThread object to read and process the incoming data
        self.thread = streaming.StreamingThread(ser=self.ser, lock=self.lock, binlength=50)

        # Connect signals and slots
        self.setup_ui_logic()

    def setup_ui_logic(self):
        # Connect buttons, etc to logic
        self.ui.ConnectBT_Button.clicked.connect(self.bt_reset)
        self.thread.bool_signal_BTStatus.connect(lambda x: self.bt_update(x))
        self.thread.str_signal_SentWiSSCI.connect(lambda x: self.write_WiSSCI_sent(x))
        self.thread.str_signal_RecvdWiSSCI.connect(lambda x: self.write_WiSSCI_recvd(x))
        self.ui.ApplyConfig_Button.clicked.connect(self.apply_config)
        self.ui.Parameters_Button.clicked.connect(self.load_config)
        self.ui.OfflineData_Button.clicked.connect(self.start_streaming_offline)
        self.ui.StartNomad_Button.clicked.connect(self.start_streaming_nomad)
        self.ui.StopStreaming_Button.clicked.connect(self.stop_streaming)

        # start with buttons except connect bluetooth disabled
        self.ui.ApplyConfig_Button.setEnabled(False)
        self.ui.StartNomad_Button.setEnabled(False)
        self.ui.OfflineData_Button.setEnabled(False)
        self.ui.StopStreaming_Button.setEnabled(False)

    # start streaming from nomad
    def start_streaming_nomad(self):
        self.stop_streaming()

        # connect to nomad
        print("Connecting to Nomad . . . ", end=' ')
        with xp.xipppy_open(True):
            print("Connected")
            self.ui.NomadStatus_LED.setPixmap(QtGui.QPixmap(ICON_GREEN_LED))
            self.thread.set_src("nomad")
            self.thread.start()

    # start streaming offline data
    def start_streaming_offline(self):
        self.stop_streaming()
        # open dialog to allow selection of text file
        dlg = QtWidgets.QFileDialog(directory="Test Data")
        dlg.setFileMode(QtWidgets.QFileDialog.ExistingFile)
        dlg.setNameFilter("Text files (*.txt)")
        if dlg.exec_():
            # get filename
            filename = dlg.selectedFiles()
            # set thread src and start thread
            self.thread.set_src("offline", filename[0])
            self.thread.start()
            self.ui.OfflineData_LED.setPixmap(QtGui.QPixmap(ICON_GREEN_LED))
        else:
            print("no file selected")

        self.ui.StopStreaming_Button.setEnabled(True)

    # stop streaming if already streaming
    def stop_streaming(self):
        if self.thread.isRunning():
            self.thread.stop()

        self.ui.OfflineData_LED.setPixmap(QtGui.QPixmap(ICON_RED_LED))
        self.ui.NomadStatus_LED.setPixmap(QtGui.QPixmap(ICON_RED_LED))

    # connect to/reset the bt dongle/see if it connects
    # TODO: periodically check for msgs like "Disconnected"
    # TODO: handle invalid COM port
    def bt_reset(self):
        serial_WiSSCI.reset_bt(self.ser, self.ui.ComPort_Combo.currentText(), self.lock)
        msg = serial_WiSSCI.read_bt(self.ser, self.lock)
        if msg == "## Connected!":
            print("connected!")
            self.bt_update(True)
        else:
            print("didn't connect!")
            self.bt_update(False)
            # open dialog telling us we didn't connect
            self.open_dialog()

    # update the status of bt connection (LED + variable)
    def bt_update(self, connected):
        if connected:
            self.ui.BTStatus_LED.setPixmap(QtGui.QPixmap(ICON_GREEN_LED))
            # enable buttons to start streaming
            self.ui.StartNomad_Button.setEnabled(True)
            self.ui.OfflineData_Button.setEnabled(True)
        else:
            self.stop_streaming()
            self.ui.BTStatus_LED.setPixmap(QtGui.QPixmap(ICON_RED_LED))
            self.open_disconnect_dialog()
            # disable buttons to start/stop streaming or apply configuration
            self.ui.StartNomad_Button.setEnabled(False)
            self.ui.OfflineData_Button.setEnabled(False)
            self.ui.StopStreaming_Button.setEnabled(False)
        # enable button only if params are previously loaded
        self.ui.ApplyConfig_Button.setEnabled(self.param_file is not None)

    # write what was sent to the WiSSCI to the appropriate tab
    def write_WiSSCI_sent(self, msg):
        self.ui.Sent_WiSSCI_text.append(msg)

    # write what was recvd from the WiSSCI to the appropriate tab
    def write_WiSSCI_recvd(self, msg):
        self.ui.Recvd_WiSSCI_text.append(msg)

    # apply loaded configuration file to the connected WiSSCI
    def apply_config(self):
        try:
            # if polling thread is running, stop it
            self.stop_streaming()

            # send msg to tell WiSSCI to enter config mode
            # TODO: add information to this msg (# channels, type of filter, etc)
            serial_WiSSCI.send_bt_msg(self.ser, self.lock, b'##########################')
            msg = serial_WiSSCI.read_bt(self.ser, self.lock)

            # check if config mode has started or not
            # TODO: recover if config mode isn't started (right now that is undefined)
            if msg == "Config mode started on WiSSCI":
                print("Entered Config Mode")

            # Check if params has been initialized (via the browse button)
            # TODO: recover if no params have been selected
            if not np.any(self.params):
                print("Params file has not been selected")

            # send selected params to the WiSSCI
            serial_WiSSCI.send_bt_msg(self.ser, self.lock, self.params)

            # get and print the WiSSCI response (tells errors, etc)
            # TODO: do something with this rather than just printing
            msg = serial_WiSSCI.read_bt(self.ser, self.lock)
            print(msg)

            # receive msg from WiSSCI telling us it completed
            # TODO: handle if config mode hasn't stopped
            msg = serial_WiSSCI.read_bt(self.ser, self.lock)
            if msg == "Config mode stopped on WiSSCI":
                self.ui.ParamsFile_Label.setText("Applied " + self.param_file)
                print("Stopped Config Mode")
        except Exception as e:
            print("Problem applying config\n"
                  "Exception: " + str(e)+"\n")

    # open the disconnect dialog
    def open_disconnect_dialog(self):
        self.dialog.show()

    # load configuration from user input and selected file
    # TODO: implement algorithms other than LDA
    def load_config(self):
        dlg = QtWidgets.QFileDialog(directory="Config Files")
        dlg.setFileMode(QtWidgets.QFileDialog.ExistingFile)
        dlg.setNameFilter("Mat files (*.mat)")

        if dlg.exec_():
            # get filename
            filename = dlg.selectedFiles()
            # parse for display
            idx = filename[0].rfind('/') + 1
            self.param_file = filename[0][idx:]
            # display that we loaded filename
            self.ui.ParamsFile_Label.setText("Loaded " + self.param_file)
            # grab input from classes box
            classes = self.ui.Class_Nums_Line.text().split(',')
            no_rest_thresh = int(self.ui.MAV_Sum_Line.text())
            self.params = load_config.load_lda(filename[0], classes, no_rest_thresh)
            # TODO: check if loaded params are valid
            # enable the apply config button
            self.ui.ApplyConfig_Button.setEnabled(True)


if __name__ == "__main__":
    # Create the QT application
    app = QtWidgets.QApplication(sys.argv)

    # Create the main window
    win = WissciGui()
    win.show()

    # Start QT application
    sys.exit(app.exec_())
