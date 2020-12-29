# Python NeoPixel SPIdev

The py-neopixel-spidev Python module can be used to control WS2812 addressable
RGB LEDs via SPI on Linux devices using the generic Linux SPIdev driver.

Only the MOSI signal of the SPI bus is used to control the DIN of the chained
LEDs. To emulate the protocol for the LEDs, each bit of LED data is made up of
4 SPI bits.

## Dependencies

The following Python modules are needed:

* [NumPy](https://numpy.org/)
* [Python Spidev](https://github.com/doceme/py-spidev)

## Attributions

This module barely contains any new code, but mainly bundles code from existing
projects for easier usage. Thanks to all the authors and contributors.

### Adafruit CircuitPython Pypixelbuf

We reuse the Pixelbuf class from [Adafruit CircuitPython Pypixelbuf](https://github.com/adafruit/Adafruit_CircuitPython_Pypixelbuf/blob/master/adafruit_pypixelbuf.py).

**File:** [`lib/pixelbuf.py`](lib/pixelbuf.py)  
**License:** [MIT](licenses_thirdparty/LICENSE.MIT.CircuitPython)   
**Copyright:** Copyright (c) 2019-2020 Roy Hooper  
**Authors:** Damien P. George, Limor Fried, Scott Shawcroft, Roy Hooper  

### Adafruit CircuitPython NeoPixel

Further we use the NeoPixel class from [Adafruit CircuitPython NeoPixel](https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel/blob/master/neopixel.py)
with some slight modifications to use the SPIdev bus as backend.

**File:** [`lib/neopixel_spidev.py`](lib/neopixel_spidev.py)  
**License:** [MIT](licenses_thirdparty/LICENSE.MIT.CircuitPython)    
**Copyright:** Copyright (c) 2016 Damien P. George, Copyright (c) 2017 Scott Shawcroft for Adafruit Industries, Copyright (c) 2019 Carter Nelson, Copyright (c) 2019 Roy Hooper  
**Authors:** Damien P. George, Scott Shawcroft, Carter Nelson, Roy Hooper

### ws2812-spi

To emulate the protocol data, we use the code from the [ws2812-spi](https://github.com/joosteto/ws2812-spi/blob/master/ws2812.py) project.

**File:** [`lib/neopixel_spi_write.py`](lib/neopixel_spi_write.py)  
**License:** [AGPL](licenses_thirdparty/LICENSE.AGPL.ws2812-spi)  
**Author:** joosteto  

## Usage

See the examples in `examples/` and the docs for the [Adafruit
NeoPixel class](https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel#usage-example).

## Copyright

Copyright (c) 2020 Kontron Electronics GmbH  
Author: Frieder Schrempf

## License

The code is licensed under the [MIT](LICENSE) license, unless the source code
files specify a different license.
