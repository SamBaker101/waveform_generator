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
    try: 
        
        wavfile.write(filename, sample_rate, wave)  
    except Exception as e:
        print("Error saving wave file:", filename, " : ", e)

def play_wave(filename):
    try: 
        wave_obj = sa.WaveObject.from_wave_file(filename)
        play_obj = wave_obj.play()
        play_obj.wait_done()  # Wait until sound has finished playing
    except Exception as e:
        print("Error playing wave file:", filename, " : ", e)

def get_params_args():
    freq_Hz = int(sys.argv[1]) if len(sys.argv) > 1 else 440
    duration_ms = int(sys.argv[2]) if len(sys.argv) > 2 else 1000
    return freq_Hz, duration_ms

def get_params_ui():
    print("Enter frequency in Hz (default is 440):")
    freq_Hz = input()
    freq_Hz = int(freq_Hz) if freq_Hz.isdigit() else 440
    print("Enter duration in milliseconds (default is 1000):")
    duration_ms = input()
    duration_ms = int(duration_ms) if duration_ms.isdigit() else 1000
    return freq_Hz, duration_ms

def main():
    sample_rate = 192000  
    #freq_Hz, duration_ms = get_params_args()
    freq_Hz, duration_ms = get_params_ui()
    
    if freq_Hz <= 0 or duration_ms <= 0:
        print("Frequency and duration must be positive integers.")
        return  
    print("Generating a sine wave of " + str(freq_Hz) + "Hz for " + str(duration_ms) + "ms...")
    
    filename = "out/sine_wave" + str(freq_Hz) + "_" + str(duration_ms) + ".wav"

    wave = generate_sine_wave(freq_Hz, duration_ms/1000.0, sample_rate)

    save_wave(filename, wave, sample_rate)
    play_wave(filename)

while True:
    main()