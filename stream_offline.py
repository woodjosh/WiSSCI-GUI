import struct
import numpy as np


class OfflineStream:
    def __init__(self, filename):
        try:
            self.filename = filename
            self.i = 0
            # load test data to send to WiSSCi (exported from matlab)
            with open(self.filename) as inFile:
                self.lines = [line.strip().split(',') for line in inFile]
        except Exception as e:
            print("Problem initializing offline stream\n"
                  "Exception: " + str(e) + "\n")

    def get_msg(self):
        try:
            send_msg = bytearray(26)
            msg = self.lines[self.i]
            to_pack = [np.uint8(int(i)) for i in msg]
            struct.pack_into(f'{26}B', send_msg, 0, *to_pack)
            print_msg = ''.join(f'{i} ' for i in msg[2:])
            self.i = self.i + 1
            return send_msg, print_msg
        except Exception as e:
            print("Problem getting offline stream msg\n"
                  "Exception: " + str(e) + "\n")