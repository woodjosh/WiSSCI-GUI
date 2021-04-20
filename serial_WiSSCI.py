import time
import datetime
import serial
from serial.tools import list_ports


# return a list of all serial ports found
def get_serial_ports():
    return sorted([port.device for port in list_ports.comports()])


# set initial parameters for the bt dongle connection
def setup_bt(ser, port, lock):
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


# reads from bt with a user specified timeout
def read_bt_timeout(ser, lock, timeout):
    try:
        msg = b''
        time1 = datetime.datetime.now()
        while (datetime.datetime.now() - time1).total_seconds() < timeout:
            with lock:
                if ser.in_waiting:
                    msg += ser.read(ser.in_waiting)
        msg = msg.decode("utf-8")
        star1 = msg.find('*')
        star2 = msg.find('*', star1+1)
        msg = msg[star1+1:star2]
        return msg
    except Exception as e:
        print("Problem reading serial port w/ timeout\n"
              "Exception: " + str(e)+"\n")


# read a line from bluetooth (timeout defaults to 10 seconds)
# TODO: handle the timeout
def read_bt(ser, lock, timeout_in=10):
    ser.timeout = timeout_in
    try:
        with lock:
            reading = ser.readline()
            if reading == b'':
                raise Exception("WiSSCI took too long to respond")
            msg = reading.decode("utf-8")
            msg = msg.replace("\n", "")
            return msg
    except Exception as e:
        print("Problem reading serial port\n"
              "Exception: " + str(e)+"\n")


# send a message over bluetooth to the WiSSCI
def send_bt_msg(ser, lock, msg):
    with lock:
        ser.write(msg)


# flush the buffers of the bt connection
def flush_bt_buffers(ser, lock):
    with lock:
        ser.flush()
        ser.reset_output_buffer()
        ser.reset_input_buffer()


# reset the bt module and try to connect to the WiSSCI
def reset_bt(ser, port, lock):
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
