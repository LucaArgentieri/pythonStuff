#!/usr/bin/env python3

from pyboy import PyBoy, WindowEvent
pyboy = PyBoy('pokemon-rosso.gb', window_scale=3)
while not pyboy.tick():
    pass