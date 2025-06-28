from distutils.core import setup
import py2exe
import numpy as np
import sys
from scipy.io import wavfile
import simpleaudio as sa

excludes = []
includes = ["scipy.special", "scipy.linalg", "numpy"]

opts = {
    "py2exe": {
        "includes":includes,
        "excludes":excludes
    }
}

setup(console=['main.py'], options=opts,)