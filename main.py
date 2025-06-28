import numpy as np
import sys
from scipy.io import wavfile
import simpleaudio as sa
from generator import *

def main():
    wavegen = WaveGenerator()
    sample_rate = 192000  
    #freq_Hz, duration_ms = wavegen.get_params_args()
    freq_Hz, duration_ms = wavegen.get_params_ui()
    
    if freq_Hz <= 0 or duration_ms <= 0:
        print("Frequency and duration must be positive integers.")
        return  
    print("Generating a sine wave of " + str(freq_Hz) + "Hz for " + str(duration_ms) + "ms...")
    
    filename = "out/sine_wave" + str(freq_Hz) + "_" + str(duration_ms) + ".wav"

    wave = wavegen.generate_sine_wave(freq_Hz, duration_ms/1000.0, sample_rate)

    wavegen.save_wave(filename, wave, sample_rate)
    wavegen.play_wave(filename)

while True:
    main()