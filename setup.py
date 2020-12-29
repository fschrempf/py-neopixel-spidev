import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py-neopixel-spidev",
    version="1.0.0",
    author="Frieder Schrempf",
    author_email="frieder.schrempf@kontron.de",
    description="A module that can be used to control WS2812 addressable \
        RGB LEDs via SPI on Linux devices using the generic Linux SPIdev driver",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fschrempf/py-neopixel-spidev",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Linux",
    ],
    install_requires=[
        'numpy',
        'spidev'
    ],
    python_requires='>=3.6',
)
