import numpy as np
from scipy.io import wavfile

def generate_sine_wave(freq, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = 0.5 * np.sin(2 * np.pi * freq * t)
    return wave

def save_wave(filename, wave, sample_rate):
    wave = (wave * 32767).astype(np.int16)  
    wavfile.write(filename, sample_rate, wave)  

# Example usage
freq_Hz = 100
duration_ms = 1000
sample_rate = 441000  
wave = generate_sine_wave(freq_Hz, duration_ms / 1000, sample_rate)

save_wave("sine_wave.wav", wave, sample_rate)

