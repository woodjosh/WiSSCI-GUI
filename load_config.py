"""
    load_config.py
    ----------
    loads lda params from matlab file
    packs them into a uint8 packet to be sent to the WiSSCI
"""
import scipy.io as sio
import numpy as np
import struct


# load lda params from matlab file
# pack them into a uint8 packet to be sent to the WiSSCI
def load_lda(filename, classes, no_rest_thresh):
    try:
        mat = sio.loadmat(filename, struct_as_record=False, squeeze_me=True)

        classes = np.uint8(classes)
        no_rest_thresh = np.uint8(no_rest_thresh)

        max_chans = 12  # do not change this without adjusting code on WiSSCi
        num_classes = 6  # do not change this without adjusting code on WiSSCi
        chans = mat['xpcCHANS']
        nstate = mat['xpcNUMSTATES']
        chans = np.uint8(chans[np.nonzero(chans)])
        nmeas = len(chans)

        mu = mat['xpcMU']
        mu = [mu[i][range(nmeas)] for i in range(nstate)]

        invCov = mat['xpcINVCOV']
        invCov = [invCov[0][i] for i in range(nmeas*nmeas)]
        invCov = np.reshape(invCov, (nmeas, nmeas))

        export_params = bytearray(886)

        struct.pack_into('2B', export_params, 0, np.uint8(nmeas), np.uint8(nstate))
        poff = 2

        struct.pack_into(f'{nmeas}B', export_params, poff, *chans)
        poff = poff+max_chans

        struct.pack_into(f'{nstate}B', export_params, poff, *classes)
        poff = poff + num_classes

        for i in range(nstate):
            struct.pack_into(f'{nmeas}f', export_params, poff + 4*nmeas*i, *mu[i])
        poff = poff + max_chans * num_classes * 4

        for i in range(nmeas):
            struct.pack_into(f'{nmeas}f', export_params, poff + 4*nmeas*i, *invCov[i])
        poff = poff + max_chans * max_chans * 4

        struct.pack_into('h', export_params, poff, np.uint16(no_rest_thresh))

        return export_params
    except Exception as e:
        print("Problem Loading mat file\n"
              "Exception: " + str(e)+"\n")


