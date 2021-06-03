"""
    stream_nomad.py
    ----------
    Defines the class NomadStream, which enables streaming
    from the nomad
"""
import xipppy as xp
import numpy as np
import struct
from datetime import datetime

class NomadStream:
    """streams from the nomad"""
    def __init__(self, binlength):
        """initialize the nomad"""
        self.buffSize = binlength*2  # samples at 2 kHz
        self.numOutChans = 12          # we can only send 12 channels
        print("Connecting to Nomad . . . ", end=' ')
        with xp.xipppy_open(True):
            self.elecs = xp.list_elec('micro')
            self.numActiveChans = len(self.elecs)
            print("Connected")

    # gets the last binlength msgs.
    def get_msg(self, data_in):
        """gets the last binlength msgs
            returns in sendable format and printable format"""
        try:
            send_msg = bytearray(36)
            bipolar_data = np.zeros((self.numOutChans, self.buffSize))
            # reshape data into numChans by bufferSize matrix
            data = np.reshape(data_in, (self.numActiveChans, self.buffSize))
            size = np.shape(data)
            # if num samples is greater than 0, process it
            if size[1] > 0:
                idx = 0
                for i in range(0, self.numOutChans*2, 2):
                    # Perform differentation to get bipolar channels
                    bipolar_data[idx, :] = data[i, :] - data[i+1, :]
                    idx = idx + 1
                # calculate mav
                mav = np.sum(np.abs(bipolar_data), axis=1)/self.buffSize
                # pack mav into output buffer and print buffer
                to_pack = [np.int16(i) for i in mav]
                struct.pack_into('2c', send_msg, 0, bytes('-', 'ascii'), bytes('>', 'ascii'))
                struct.pack_into(f'{12}h', send_msg, 2, *to_pack)

                time = datetime.now().strftime("%M%S%f,")
                struct.pack_into('10s', send_msg, 26, time.encode('UTF-8'))
                # return values
                return send_msg, to_pack, time
        except Exception as e:
            print("Problem getting nomad stream msg\n"
                  "Exception: " + str(e) + "\n")
