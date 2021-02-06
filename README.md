# EEG-Sound-Synthesis
"This Python script imports EEG data from .tsv and/or .bdf files and uses the measured voltages to generate RANDOMIZED .wav (sound) files."

Due to a requirement for my latest musicial project, I needed to implement the idea of translating EEG data into sound. 
As I had just started to learn programming with Python, I decided to let it be my first attempt to program something useful. 

The programm itself uses the packages "scipy.io.wavfile", "NumPy", "Pandas" and "pyedflib".

First, I'd like to adress the general code-structure:

    -Importing the needed data from the files storing the raw EEG information:
      -.tsv-files: You need to insert the file name (including .tsv) in the following way: "name.tsv"
      -.bdf-files: You need to insert the file name (including .bdf) in the following way: "name.bdf"
       
    -Then, the 
