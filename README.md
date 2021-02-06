# EEG-Sound-Synthesis
________________________________________________________________________________________________________________________________________
Short Description:
"This Python script imports EEG data from .tsv and/or .bdf files and uses the measured voltages to generate randomized .wav (sound) files."
________________________________________________________________________________________________________________________________________

~~~ Introduction ~~~

Due to a requirement for my current musicial project, I needed to implement the idea of translating EEG data into sound. 
As I had just started to learn programming with Python, I decided to let it be my first attempt to program something useful. 

Note: This programm/script is my first programming project using Python. It needs definitely improvement and optimization.
      There aren't any updates planned on this one, but if there is time or feedback, I will try to tweak it!


~~~ Background Story ~~~

Initially, I found two promising EEG-datasets on openneuro.org which I then tried to transfer into NumPy arrays.
Both EEG files were different types (.tsv and .bdf) and I eventually managed to access their data.
Considering my goal of actually making sound using these files, I focused on extracting the voltage-values the EEG-electrodes once measured.
These values correlate with the brain activity depending on different emotions and brain processes.
A sound wave (or better sound signal) is characterised by an amplitude and a frequency (and a phase).
Although I knew that I could not translate brain waves directly to sound waves, I aimed for a accurate (yet creative) approach.
Therefore, I interpreted the voltages as amplitudes controlling the initial loudness of the particular sound.
Besides that, typical brain frequencies are identified as the brain wave frequencies (alpha, beta, theta, gamma, ...).
These frequencies are quite low, so a direct translation would lead to frequencies below 100 Hz, which aren't that exciting to listen to.
I then came up with the idea of layering these frequencies to achieve a more distinguished sound.
When it comes to musicial experimentation and sound exploration, I always love to play around with concepts like randomness or chaos.
That's why when executing the .py file, amplitude and frequency are randomly picked. 
So each time running the file, a new unique sound will be created!
That being said, let's continue with explaining the code:


~~~ Explaining The Code ~~~

# Note: Detailed comments and explanations can be found directly in the .py file.

# The program uses the packages "scipy.io.wavfile", "NumPy", "Pandas" and "pyedflib".

1) The main function is "eeg_sound_synthesis(...)" which requires the .tsv/.bdf - file name and other parameters.
   Scroll to the end of the code to adjust the parameters and therefore the resulting sound.
   
2) Importing the voltage data from the files storing the raw EEG information:

.tsv-files: You need to insert the file name (including .tsv) in the following way: "name.tsv"
.bdf-files: You need to insert the file name (including .bdf) in the following way: "name.bdf"

Depending on the file type, either Pandas or pyedflib will automatically import the EEG data to NumPy arrays. 

3) Based on the given parameters "n_layers" and "multiples_max", the function will randomly pick an amplitude from the NumPy array,
   randomly pick a frequency and repeat this process n-times (n_layers).
   These n layers will be expressed as sound in .wav-file using "scipy.io.wavfile".
 

________________________________________________________________________________________________________________________________________
                                                        
                                                        Thank you for reading!
                            
                                I highly appreciate feedback, because there is still so much to learn!
                                                                            
                                                                            ~ JP alias emergnce_music
________________________________________________________________________________________________________________________________________
 



       
       
  

