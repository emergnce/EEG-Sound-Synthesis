
#_______________________________________________________________________________________________________________________________________________________________

#Introduction:


#                                            ~ ~ ~   EEG-Sound-Synthesis V3  (created by https://github.com/emergnce) ~ ~ ~


#                  "This Python script imports EEG data from .tsv and/or .bdf files and uses the measured voltages to generate randomized .wav (sound) files."


#                                    - Please read the readme-file on my github for this code's background and further documentation! -


#                                        If you feel like giving me some feedback or advice, I would highly appreciate that!


#______________________________________________________________________________________________________________________________________________________________
#Changelog:
# -uniting several lines to reduce length of the code
# -clarification and extension of the explanations
# -exchanging the brain wave frequencies through the F-tone frequency and its multiples for creative and artistic reasons

#_______________________________________________________________________________________________________________________________________________________________



# importing the requiered packages:


from scipy.io.wavfile import write
import numpy as np
import pandas as pd                 # used for reading .tsv files
from pyedflib import highlevel      # used for reading .bdf files



# defining the function which will be used for sound synthesis:

# the parameters are as following:
    # file = "name.tsv" of the .tsv/.bdf-file
    # file_wav = "name.wav" of the resulting wav.-file
    # n_layers = an integer determining the number of sound layers
    # multiples_max = an integer defining the highest multiple of the given frequencies (limiting the total frequency scale)


# creating the main function with the parameters:

def eeg_sound_synthesis(file, file_wav, n_layers, multiples_max):

    # reading the files:

    if "tsv" in file:                                                   # checks whether the file is a .tsv or .bdf type

            raw_data_array = np.delete(np.array(pd.read_csv(file, sep="\t")), 0, 1)   # reads the .tsv file and stores it in raw_data, converts raw_data into a NumPy array                                                                    # and removes the first column which contains the EEG-channel names as strings (which will not be used)
            data = raw_data_array.sum(axis=1) / 3         # for simplification-reasons (described in readme-file), the raw data owning three columns (X,Y,Z = electrode postions) is being averaged


    else:

            signals, signal_headers, header = highlevel.read_edf(file)  # reads the .bdf file and stores it in a NumPy array

            data = -1*100*signals.sum(axis=0) / (len(signals.sum(axis=0)))          # for simplification-reasons (described in readme-file), the average is being calculated
                                                                                    # factor -100  is being used for amplification and getting the absolute value

    # generating sound:


    def soundgenerator(integer):
        number_of_layers = 0 + n_layers                                 # determines the number of sound layers to be generated

        f1 = 43.65  # base frequency 1 [F_1 tone]
        f2 = 87.31   # base frequency 2 [F_2 tone]
        f3 = 174.61  # base frequency 3 [F_3 tone]
        f4 = 349.23  # base frequency 4 [F_4 tone]
        f5 = 698.46  # base frequency 5 [F_5 tone]

        a_i = amplitudes_iterable = {i: j for i, j in enumerate(data)}   # dictionary containing the enumerated voltage values for later iteration (0-211)
        f_i = frequency_iterable = {1: f1, 2: f2, 3: f3, 4: f4, 5: f5}     # dictionary with the numbered base frequencies for later iteration (0-4)
        m_i = multiples_iterable = [2*i for i in range(1, multiples_max)]  # list with integers 1-10000 for generation of higher modes of the base frequencies, factor 2 to always get an octave step

        f_sampling = 44100  # sampling rate
        t_n = 10  # length of one period in seconds
        n = f_sampling * t_n  # number of values per period

        sound_layers = []   # list with the generated sound layers


        def sonicvibration(number_of_layers):                            # the following code uses the numbered amplitudes, frequencies and multiples to generate randomized sound
            for i in range(0, number_of_layers):
                t = np.linspace(0, 1, n, endpoint=False)                 # t = array with time values, p = array with the calculated sound waves (using np.sin and randint for randomizing)
                p = a_i[np.random.randint(0, 212)] * np.sin(2 * np.pi * m_i[np.random.randint(0, multiples_max - 1)] * f_i[np.random.randint(1, 6)] * t)
                sound_layers.append(p)

        sonicvibration(number_of_layers)

        def sigmasum(start=0, end=number_of_layers):                     # the sigmasum function calculates the sum of all the layers to fuse them to one single sound signal
            generated_sound = 0
            for i in range(start, end):
                generated_sound += sound_layers[i]

            return generated_sound

        filename_wav = file_wav                                         # here you can choose a name for the resulting file
        write(filename_wav, f_sampling, sigmasum(0, number_of_layers))  # this writes the data previously genereated into a .wav file (can be found in the directory of this Python file)
    soundgenerator(n_layers)

#________________________________________________________________________


# executes the EEG-Sound-Synthesis function:


eeg_sound_synthesis(file="sub-17_eeg_sub-17_task-ImaginedEmotion_electrodes.tsv", file_wav="sound.wav",  n_layers=100, multiples_max=50)

    #!!! Note: Due to the fact that this programm is not optimized performance-wise, very high values for n_layers and multiples_max can lead to a high RAM usage!!!

#________________________________________________________________________







































