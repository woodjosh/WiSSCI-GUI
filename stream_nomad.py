import xipppy as xp
import numpy as np
import struct


class NomadStream:
    def __init__(self, elecs, binlength):
        self.elecs = elecs
        self.buffSize = binlength*2  # it gets 2 samples per ms
        self.numActiveChans = len(elecs)
        self.numOutChans = 12          # we can only send 12 channels

    def get_msg(self):
        try:
            send_msg = bytearray(26)
            bipolar_data = np.zeros(self.numOutChans, self.buffSize)
            mav = np.zeros(self.numOutChans)
            # get data from nomad
            data_in = xp.cont_hires(self.buffSize, self.elecs)
            # reshape data into numChans by bufferSize matrix
            data = np.reshape(data_in, (self.numActiveChans, self.buffSize))
            size = np.shape(data)
            # if num samples is greater than 0, process it
            if size[1] > 0:
                idx = 0
                for i in range(0, self.numOutChans, 2):
                    # Perform differentation to get bipolar channels
                    bipolar_data[idx, :] = data[i, :] - data[i+1, :]
                    idx = idx + 1
                # calculate mav
                mav = np.sum(np.abs(bipolar_data), axis=1)/self.buffSize
                # pack mav into output buffer and print buffer
                to_pack = [np.uint8(i) for i in mav]
                struct.pack_into('2c', send_msg, 0, '->')
                struct.pack_into(f'{24}B', send_msg, 2, *to_pack)
                print_msg = ''.join(f'{i} ' for i in mav)
                # return values
                return send_msg, print_msg
        except Exception as e:
            print("Problem getting nomad stream msg\n"
                  "Exception: " + str(e) + "\n")
