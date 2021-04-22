"""
    stream_offline.py
    ----------
    Defines the class OfflineStream, which enables streaming data
    saved into a text file from matlab
"""

import struct
import numpy as np


class OfflineStream:
    """streams from a txt file"""
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
        """gets next msg from the loaded data"""
        try:
            send_msg = bytearray(26)
            msg = self.lines[self.i]
            to_pack = [np.int16(i) for i in msg]
            struct.pack_into('2c', send_msg, 0, bytes('-', 'ascii'), bytes('>', 'ascii'))
            struct.pack_into(f'{12}h', send_msg, 2, *to_pack)
            self.i = self.i + 1
            # return values
            return send_msg, to_pack
        except Exception as e:
            print("Problem getting offline stream msg\n"
                  "Exception: " + str(e) + "\n")