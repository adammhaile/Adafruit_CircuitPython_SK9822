
Adafruit CircuitPython SK9822
==============================

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-sk9822/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/sk9822/en/latest/
    :alt: Documentation Status

.. image :: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://travis-ci.org/adafruit/Adafruit_CircuitPython_SK9822.svg?branch=master
    :target: https://travis-ci.org/adafruit/Adafruit_CircuitPython_SK9822
    :alt: Build Status

Higher level SK9822 driver that presents the strip as a sequence. It is the
same api as the `NeoPixel library <https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel>`_.

Colors are stored as tuples by default. However, you can also use int hex syntax
to set values similar to colors on the web. For example, ``0x100000`` (``#100000``
on the web) is equivalent to ``(0x10, 0, 0)``.

If you send a tuple with 4 values, you can control the brightness value, which appears in SK9822 but not NeoPixels.
It should be a float. For example, (0xFF,0,0, 1.0) is the brightest red possible, (1,0,0,0.01) is the dimmest red possible.

.. note:: The int hex API represents the brightness of the white pixel when
  present by setting the RGB channels to identical values. For example, full
  white is 0xffffff but is actually (0xff, 0xff, 0xff) in the tuple syntax.

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Usage Example
=============

This example demonstrates using four SK9822 pixels and setting them to Red, Green, Blue, White

.. code-block:: python

    import board
    import adafruit_sk9822

    pixels = adafruit_sk9822.SK9822(board.SCK, board.MOSI, 4, brightness=1.0)
    pixels[0] = (255, 0, 0)
    pixels[1] = (0, 255, 0)
    pixels[2] = (0, 0, 255)
    pixels[3] = (255, 255, 255)

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Building locally
================

To build this library locally you'll need to install the
`circuitpython-build-tools <https://github.com/adafruit/circuitpython-build-tools>`_ package.

.. code-block:: shell

    python3 -m venv .env
    source .env/bin/activate
    pip install circuitpython-build-tools

Once installed, make sure you are in the virtual environment:

.. code-block:: shell

    source .env/bin/activate

Then run the build:

.. code-block:: shell

    circuitpython-build-bundles --filename_prefix adafruit-circuitpython-sk9822 --library_location .

Sphinx documentation
-----------------------

Sphinx is used to build the documentation based on rST files and comments in the code. First,
install dependencies (feel free to reuse the virtual environment from above):

.. code-block:: shell

    python3 -m venv .env
    source .env/bin/activate
    pip install Sphinx sphinx-rtd-theme

Now, once you have the virtual environment activated:

.. code-block:: shell

    cd docs
    sphinx-build -E -W -b html . _build/html

This will output the documentation to ``docs/_build/html``. Open the index.html in your browser to
view them. It will also (due to -W) error out on any warning like Travis will. This is a good way to
locally verify it will pass.
