#!/usr/bin/python3

# SPDX-License-Identifier: MIT
#
# Copyright (c) 2020 Kontron Electronics GmbH
# Author: Frieder Schrempf
#

import time
from lib import neopixel_spidev as np
from lib.pixelbuf import wheel

# Init 56 LEDs on SPI bus 2, cs 0 with colors ordered green, red, blue
with np.NeoPixelSpiDev(2, 0, n=56, pixel_order=np.GRB) as pixels:
    try:
        while True:
            for i in range(255):
                # Use wheel function from pixelbuf module to calculate RGB color
                pixels.fill(wheel(i))
                time.sleep(0.03)
    except KeyboardInterrupt:
        pass
