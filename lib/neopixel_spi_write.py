# SPDX-License-Identifier: AGPL-3.0
#
# Derived from https://github.com/joosteto/ws2812-spi/blob/master/ws2812.py
# by 'joosteto'.
#

import numpy

SPEED_HZ = int(4 / 1.25e-6) # 4 SPI bits for one period of 1.25µs

# See: https://github.com/joosteto/ws2812-spi/blob/master/ws2812.py
def neopixel_spi_write(spi, data):
    d = numpy.array(data).ravel()
    tx = numpy.zeros(len(d) * 4, dtype = numpy.uint8)
    for ibit in range(4):
        tx[3 - ibit::4] = ((d >> (2 * ibit + 1)) & 1) * 0x60 + \
                          ((d >> (2 * ibit + 0)) & 1) * 0x06 + 0x88
    spi.xfer(tx.tolist(), SPEED_HZ)
