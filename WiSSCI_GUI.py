"""
    WiSSCI_GUI.py
    ----------
    Defines the class WissciGui, which has all functions to create the GUI,
    connect the logic, and high level functions to interact with the WiSSCI
"""
import threading

import numpy as np
import serial
from PyQt5 import QtWidgets, QtGui
from datetime import datetime

import load_config
import serial_WiSSCI
import streaming
from LostConnDialog import Ui_Dialog as Form
from WiSSCI import Ui_MainWindow

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
        """initialize the gui"""
        super().__init__()

        # Create the main window
        self.ui = Ui_MainWindow()

        # initialize logging parameters
        self.logging = False
        self.logfile = None
        self.logstarted = False

        # initialize params to be sent to the WiSSCI
        self.params = bytearray(886)
        self.param_file = None
        # set up the UI
        self.ui.setupUi(self)

        # initialize buffer, plots, and curves
        self.plot_buffer = [[0 for _ in range(12)] for _ in range(200)]
        plots = (self.ui.Plot_Layout.itemAt(i).widget() for i in range(self.ui.Plot_Layout.count()))
        self.plot_curve = []
        i = 0
        for plot in plots:
            self.plot_curve.append(plot.plot(range(200), [row[i] for row in self.plot_buffer]))
            i = i + 1

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

        # Create QThread object to read and process the incoming data
        self.thread = streaming.StreamingThread(ser=self.ser, lock=self.lock, binlength=50)

        # Connect signals and slots
        self.setup_ui_logic()

    def setup_ui_logic(self):
        """connect buttons, etc to logic"""
        self.ui.ConnectBT_Button.clicked.connect(self.bt_reset)

        # Connect event from changed serial port combo box
        self.ui.ComPort_Combo.currentIndexChanged.connect(self.setup_bluetooth_device)

        self.thread.bool_signal_BTStatus.connect(lambda x: self.bt_update(x))
        self.thread.str_signal_RecvdWiSSCI.connect(lambda x: self.write_wissci_recvd(x))
        self.thread.str_signal_timeSent.connect(lambda x: self.log_cmp_time(x))
        self.ui.ApplyConfig_Button.clicked.connect(self.apply_config)
        self.ui.Parameters_Button.clicked.connect(self.load_config)
        self.ui.OfflineData_Button.clicked.connect(self.start_streaming_offline)
        self.ui.StartNomad_Button.clicked.connect(self.start_streaming_nomad)
        self.ui.StopStreaming_Button.clicked.connect(self.stop_streaming)
        self.ui.StartLogging_Button.clicked.connect(self.start_logging)
        self.ui.StopLogging_Button.clicked.connect(self.stop_logging)
        self.thread.list_signal_SentWiSSCI.connect(lambda x: self.plot_wissci_sent(x))

        # adjust plot settings
        plots = (self.ui.Plot_Layout.itemAt(i).widget() for i in range(self.ui.Plot_Layout.count()))
        for plot in plots:
            plot.setRange(xRange=(0, 200), yRange=(0, 350))
            plot.enableAutoRange('xy', False)
            plot.setMouseEnabled(x=False, y=False)
            plot.showAxis('bottom', False)
            plot.showAxis('left', False)

        # start with buttons disabled
        self.ui.ApplyConfig_Button.setEnabled(False)
        self.ui.StartNomad_Button.setEnabled(False)
        self.ui.OfflineData_Button.setEnabled(False)
        self.ui.StopStreaming_Button.setEnabled(False)
        self.ui.ConnectBT_Button.setEnabled(False)

    def setup_bluetooth_device(self):
        self.stop_streaming()
        if self.ui.ComPort_Combo.currentText() != "<Select port>":
            serial_WiSSCI.setup_bt(self.ser, self.ui.ComPort_Combo.currentText(), self.lock)
            self.ui.ConnectBT_Button.setEnabled(True)

    def start_dummy_streaming(self):
        # set thread src and start thread
        self.thread.set_src("dummy")
        self.thread.start()

    def start_streaming_nomad(self):
        """start streaming from nomad"""
        self.thread.stop()
        self.thread.set_src("nomad")
        self.thread.start()
        self.ui.NomadStatus_LED.setPixmap(QtGui.QPixmap(ICON_GREEN_LED))
        # now that streaming has started, enable the stop streaming button
        self.ui.StopStreaming_Button.setEnabled(True)

    def start_streaming_offline(self):
        """start streaming offline data"""
        self.thread.stop()
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
        # now that streaming has started, enable the stop streaming button
        self.ui.StopStreaming_Button.setEnabled(True)

    def stop_streaming(self):
        """stop streaming if already streaming"""
        if self.thread.isRunning():
            self.thread.stop()
            self.start_dummy_streaming()
        # update LED indicators
        self.ui.OfflineData_LED.setPixmap(QtGui.QPixmap(ICON_RED_LED))
        self.ui.NomadStatus_LED.setPixmap(QtGui.QPixmap(ICON_RED_LED))

    # TODO: periodically check for msgs like "Disconnected"
    # TODO: handle invalid COM port
    def bt_reset(self):
        """connect to/reset the bt dongle/see if it connects"""
        # reset the bluetooth dongle with a break command
        serial_WiSSCI.reset_bt(self.ser, self.ui.ComPort_Combo.currentText(), self.lock)
        # get the response
        msg = serial_WiSSCI.read_bt(self.ser, self.lock)
        if msg == "## Connected!":
            print("connected!")
            self.bt_update(True)
        else:
            print("didn't connect!")
            self.bt_update(False)

    def start_logging(self):
        """start the logging with a new file"""
        logfilename = datetime.now().strftime("logs/log_%Y_%m_%d-%I_%M_%S_%p.csv")
        self.logfile = open(logfilename, 'x')
        # write header
        self.logfile.write("Ch1, Ch2, Ch3, Ch4, Ch5, Ch6, Ch7, Ch8, Ch9, Ch10, Ch11, Ch12, CMP Time (mmssffffff), WiSSCI Time, Decode\n")
        # set flags and LED
        self.logging = True
        self.ui.Logging_LED.setPixmap(QtGui.QPixmap(ICON_GREEN_LED))

    def stop_logging(self):
        """stop the logging and close file"""
        self.logfile.close()
        # set flags and LED
        self.logging = False
        self.logstarted = False
        self.ui.Logging_LED.setPixmap(QtGui.QPixmap(ICON_RED_LED))

    def bt_update(self, connected):
        """update the status of bt connection (LED + variable)"""
        if connected:
            self.ui.BTStatus_LED.setPixmap(QtGui.QPixmap(ICON_GREEN_LED))
            # enable buttons to start streaming
            self.ui.StartNomad_Button.setEnabled(True)
            self.ui.OfflineData_Button.setEnabled(True)
            self.start_dummy_streaming()
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

    def plot_wissci_sent(self, to_plot):
        """plot what was sent to the WiSSCI on the channel tabs"""
        try:
            self.plot_buffer.remove(self.plot_buffer[0])
            self.plot_buffer.append(to_plot)
            i = 0
            for curve in self.plot_curve:
                curve.setData(y=[row[i] for row in self.plot_buffer])
                i = i + 1
        except Exception as e:
            print("Problem plotting\n"
                  "Exception: " + str(e)+"\n")

        if self.logging:
            self.logstarted = True
            for val in to_plot:
                self.logfile.write(str(val) + ',')

    def log_cmp_time(self, time):
        if self.logging and self.logstarted:
            self.logfile.write(time)

    def write_wissci_recvd(self, msg):
        """write what was recvd from the WiSSCI to the appropriate tab"""
        self.ui.Recvd_WiSSCI_text.append(msg)

        if self.logging and self.logstarted:
            # write the WiSSCI time
            self.logfile.write(msg[3:13] + ',')
            # write the decode result
            self.logfile.write(msg[1] + '\n')

    def apply_config(self):
        """apply loaded configuration file to the connected WiSSCI"""
        try:
            # if polling thread is running, stop it
            self.stop_streaming()
            self.ui.StopStreaming_Button.setEnabled(False)
            # send msg to tell WiSSCI to enter config mode
            # TODO: add information to this msg (# channels, type of filter, etc)
            serial_WiSSCI.send_bt_msg(self.ser, self.lock, b'####################################')
            msg = serial_WiSSCI.read_bt(self.ser, self.lock)

            # check if config mode has started or not
            if msg == "Config mode started on WiSSCI":
                print("Entered Config Mode")
            else:
                print("Configure mode not started")
                return

            # Check if params has been initialized (via the browse button)
            if not np.any(self.params):
                print("Params file has not been selected")
                return

            # send selected params to the WiSSCI
            serial_WiSSCI.send_bt_msg(self.ser, self.lock, self.params)

            # get and print the WiSSCI response (tells errors, etc)
            msg = serial_WiSSCI.read_bt(self.ser, self.lock)
            if msg == "Packet Written to flash":
                print(msg)
            else:
                print(msg)
                return

            # receive msg from WiSSCI telling us it completed
            msg = serial_WiSSCI.read_bt(self.ser, self.lock)
            if msg == "Config mode stopped on WiSSCI":
                self.ui.ParamsFile_Label.setText("Applied " + self.param_file)
                print("Stopped Config Mode")
            else:
                print("Config mode never stopped")

            self.start_dummy_streaming()

        except Exception as e:
            print("Problem applying config\n"
                  "Exception: " + str(e)+"\n")

    def open_disconnect_dialog(self):
        """open the disconnect dialog"""
        self.dialog.show()

    # TODO: implement algorithms other than LDA
    def load_config(self):
        """load configuration from user input and selected file"""
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
