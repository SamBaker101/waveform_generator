import numpy as np
import sys
from scipy.io import wavfile
import simpleaudio as sa

def generate_sine_wave(freq, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = 0.5 * np.sin(2 * np.pi * freq * t)
    return wave

def save_wave(filename, wave, sample_rate):
    wave = (wave * 32767).astype(np.int16)  
    wavfile.write(filename, sample_rate, wave)  

def play_wave(filename):
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()  # Wait until sound has finished playing

def main():
    freq_Hz = int(sys.argv[1]) if len(sys.argv) > 1 else 440
    duration_ms = int(sys.argv[2]) if len(sys.argv) > 2 else 1000
    sample_rate = 192000  
    filename = "out/sine_wave" + str(freq_Hz) + "_" + str(duration_ms) + ".wav"

    wave = generate_sine_wave(freq_Hz, duration_ms/1000.0, sample_rate)

    save_wave(filename, wave, sample_rate)
    play_wave(filename)

main()