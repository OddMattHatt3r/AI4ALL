
import matplotlib.pyplot as plt
import os
from pydub import AudioSegment
import numpy as np
from scipy.io import wavfile
from tempfile import mktemp
from scipy import signal
from PIL import Image

"""
from playsound import playsound
import sounddevice as sd
from scipy.io.wavfile import write

#playsound('/Users/matthewhagg/Desktop/Life/College/AI/DiscoverAI/archive-2/mp3/Acrocephalus-arundinaceus-178787.mp3')


fs = 44100  # Sample rate
seconds = 3  # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()  # Wait until recording is finished
write('UserInput.wav', fs, myrecording)  # Save as WAV file 
print("AHHHH")

"""

mp3_audio = AudioSegment.from_file('/Users/matthewhagg/Desktop/Life/College/AI/DiscoverAI/output.wav', format="wav")  # read mp3
try:
    i = 0
    for file in os.scandir('/Users/matthewhagg/Desktop/Life/College/AI/DiscoverAI/archive-2/mp3/practice'):
        fileDir = os.path.abspath(file)
        print(fileDir)
        newExportDir = "/Users/matthewhagg/Desktop/Life/College/AI/DiscoverAI/archive-2/mp3/converted/" + fileDir[77:len(fileDir)]
        print(newExportDir + "\n")
        
        mp3_audio = AudioSegment.from_file(fileDir, format="mp3")
        extract = mp3_audio[0:10000]
        extract.export(newExportDir, format="mp3")
        
except IsADirectoryError:
    print("")

print("---------------")

for file in os.scandir('/Users/matthewhagg/Desktop/Life/College/AI/DiscoverAI/archive-2/mp3/converted'):
    fileDir = os.path.abspath(file)
    print(fileDir)
    sound = AudioSegment.from_mp3(fileDir)
    sound = sound.set_channels(1)
    wavName = "/Users/matthewhagg/Desktop/Life/College/AI/DiscoverAI/archive-2/mp3/converted" +fileDir[77:len(fileDir)-4] + ".wav"
    
    print(wavName)
    sound.export(wavName, format="wav")
    os.remove(fileDir)

print("#################")
for file in os.scandir('/Users/matthewhagg/Desktop/Life/College/AI/DiscoverAI/archive-2/mp3/converted'):
    # Read the wav file (mono)
    fileDir = os.path.abspath(file)
    print(fileDir)
    samplingFrequency, signalData = wavfile.read(fileDir)

    # Plot the signal read from wav file
    #plt.subplot(211)
    plt.title('Spectrogram of ' + fileDir[78:len(fileDir)-11] + ' bird call')
    """plt.plot(signalData)
    plt.xlabel('Sample')
    plt.ylabel('Amplitude')"""
    plt.subplot(211)
    plt.specgram(signalData,Fs=samplingFrequency)
    plt.xlabel('Time')
    plt.ylabel('Frequency')
    plt.savefig("/Users/matthewhagg/Desktop/Life/College/AI/DiscoverAI/archive-2/Spectrograms" + fileDir[77:len(fileDir)-4],format='png')
    
    im = Image.open("/Users/matthewhagg/Desktop/Life/College/AI/DiscoverAI/archive-2/Spectrograms" + fileDir[77:len(fileDir)-4])

    im_crop = im.crop((80, 58, 577, 227))
    os.remove("/Users/matthewhagg/Desktop/Life/College/AI/DiscoverAI/archive-2/Spectrograms" + fileDir[77:len(fileDir)-4])
    im_crop.save("/Users/matthewhagg/Desktop/Life/College/AI/DiscoverAI/archive-2/Spectrograms" + fileDir[77:len(fileDir)-4] + '.png', quality=100)
    
    
    #plt.show()
