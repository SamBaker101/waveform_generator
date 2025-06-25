# Waveform Generator

## Overview

The goal of this repository is to generate waveforms in the .wav format based on inputted frequency(Hz) and duration(ms).

## Requirements

numpy - store wave form data as linspace and complete math functions
sys - pass arguments from commandline
scipy - create and write wavefile
simpleaudio - play audio

## Usage

There are two different get_param functions which can be selected by uncommenting/commenting them in the main function. One prompts the user to enter their parameters while the other takes them from command line arguments based on the following syntax.

    python <path> <freq> <duration ms>
    python ./main.py 440 4000
