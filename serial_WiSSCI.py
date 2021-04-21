"""
    serial_WiSSCI.py
    ----------
    Functions for communicating with the WiSSCI
    through the serial port to the bluetooth dongle.
    All functions sending/recving the serial port need the lock.
"""
import time
import datetime
import serial
from serial.tools import list_ports


def get_serial_ports():
    """return a list of all serial ports found"""
    return sorted([port.device for port in list_ports.comports()])


def setup_bt(ser, port, lock):
    """set initial parameters for the bt dongle connection"""
    try:
        with lock:
            ser.baudrate = 115200
            ser.port = port
            ser.bytesize = serial.EIGHTBITS
            ser.stopbits = serial.STOPBITS_ONE
            ser.parity = serial.PARITY_NONE
            ser.rtscts = True
            ser.timeout = None
    except Exception as e:
        print("Problem initializing serial port\n"
              "Exception: " + str(e)+"\n")


def read_bt_timeout(ser, lock, timeout):
    """reads from bt with a user specified timeout"""
    try:
        msg = b''
        # get starting time
        time1 = datetime.datetime.now()
        # get incoming msg buffer while we haven't passed timeout
        while (datetime.datetime.now() - time1).total_seconds() < timeout:
            with lock:
                if ser.in_waiting:
                    # add waiting bytes to msg
                    msg += ser.read(ser.in_waiting)
        # decode msg
        msg = msg.decode("utf-8")
        # remove asterisks to get the actual response
        # TODO: handle if we don't get both asterisks
        star1 = msg.find('*')
        star2 = msg.find('*', star1+1)
        msg = msg[star1+1:star2]
        return msg
    except Exception as e:
        print("Problem reading serial port w/ timeout\n"
              "Exception: " + str(e)+"\n")


# TODO: handle the timeout
def read_bt(ser, lock, timeout_in=10):
    """read a line from bluetooth (timeout defaults to 10 seconds)"""
    ser.timeout = timeout_in
    with lock:
        reading = ser.readline()
        if reading == b'':
            return ""
        msg = reading.decode("utf-8")
        msg = msg.replace("\n", "")
        return msg


def send_bt_msg(ser, lock, msg):
    """send a message over bluetooth to the WiSSCI"""
    with lock:
        ser.write(msg)


def flush_bt_buffers(ser, lock):
    """flush the buffers of the bt connection"""
    with lock:
        ser.flush()
        ser.reset_output_buffer()
        ser.reset_input_buffer()


def reset_bt(ser, port, lock):
    """reset the bt module and try to connect to the WiSSCI"""
    print("Connecting: "+port)
    try:
        with lock:
            if not ser.isOpen():
                ser.open()
            time.sleep(0.1)
            ser.reset_output_buffer()
            ser.setRTS(True)
            ser.setDTR(True)
            # restart program on bt dongle
            ser.send_break(0.2)
            ser.timeout = None
            time.sleep(0.1)
            ser.reset_input_buffer()
            ser.flush()
    except Exception as e:
        print("Problem resetting serial port\n"
              "Exception: " + str(e)+"\n")
