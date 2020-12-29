#!/usr/bin/python3

# SPDX-License-Identifier: MIT
#
# Copyright (c) 2020 Kontron Electronics GmbH
# Author: Frieder Schrempf
#

import colorsys
import time
from numpy import arange
from lib import neopixel_spidev as np

# Init 56 LEDs on SPI bus 2, cs 0 with colors ordered green, red, blue
with np.NeoPixelSpiDev(2, 0, n=56, pixel_order=np.GRB) as pixels:
    try:
        # Scroll all LEDs through the color wheel using the HSV color model
        i = 0.0
        while True:
            for i in arange(0.0, 1.0, 0.01):            # Scroll through hue values
                c = colorsys.hsv_to_rgb(i, 1, 1)        # Convert HSV color to RGB tuple
                c = tuple([int(v * 255.0) for v in c])  # Scale RGB values to range [0, 255] and convert to integer
                pixels.fill(c)                          # Fill all LEDs with calculated color
                time.sleep(0.03)                        # Limit framerate
    except KeyboardInterrupt:
        pass
