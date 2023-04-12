
import matplotlib.pyplot as plt
import os
from pydub import AudioSegment
import numpy as np
from scipy.io import wavfile
from tempfile import mktemp
from scipy import signal
from PIL import Image


#mp3_audio = AudioSegment.from_file('/Users/matthewhagg/Desktop/Life/College/AI/DiscoverAI/output.wav', format="wav")  # read mp3
try:
    i = 0
    for file in os.scandir('/Users/matthewhagg/Desktop/Life/College/AI/DiscoverAI/archive-2/mp3/practice'):
        file_name, file_extension = os.path.splitext(os.path.abspath(file))
        o=0
        while (file_extension == ".mp3")&(o<1):
            fileDir = os.path.abspath(file)
            print(fileDir)
            #newExportDir = "/Users/matthewhagg/Desktop/Life/College/AI/DiscoverAI/zarchive-2/mp3/converted/" + fileDir[77:len(fileDir)]
            #print(newExportDir + "\n")
            
            mp3_audio = AudioSegment.from_file(fileDir, format="mp3")
            #extract = mp3_audio[0:10000]
            #extract.export(newExportDir, format="mp3")
            print(len(mp3_audio))
            print(len(mp3_audio)%10000)
            numOfSplits = ((len(mp3_audio)-(len(mp3_audio)%10000))//10000)

            print(numOfSplits)
            g=1
            newExportDir = "/Users/matthewhagg/Desktop/Life/College/AI/DiscoverAI/archive-2/mp3/newDataSet/" + fileDir[77:(len(fileDir))-4]
            while g <= numOfSplits:
                print("PLOTTING")
                print("---------------")
                print("FILEDIR: "+ fileDir)
                
                newExportDir2 = str(newExportDir)+ "-"+str(g)+ ".wav"

                check = "/Users/matthewhagg/Desktop/Life/College/AI/DiscoverAI/archive-2/Spectrograms/" + fileDir[79:len(fileDir)-5] + str(g) +".png"
                print("CHECK = "+ check)
                if os.path.isfile(check) == True:
                    print("File Exist, Skipped")
                elif os.path.isfile(check) == False:
                    print("doesnt")
                    print("NEW" + newExportDir2)

                    extract = mp3_audio[((g-1)*10000):((g)*10000)]
                    extract = extract.set_channels(1)
                    extract.export(newExportDir2, format="wav")
                    removeMp3 = newExportDir + ".mp3"
                    #os.remove(removeMp3)

                    #MAKE THE PICTURE
                    fileDir = newExportDir2
                    print("FIELDIR" + fileDir)
                    samplingFrequency, signalData = wavfile.read(fileDir)
                    plt.figure(dpi=400)

                    # Plot the signal read from wav file
                    plt.title('Spectrogram of ' + fileDir[78:len(fileDir)-11] + ' bird call')
                    plt.subplot(211)
                    plt.specgram(signalData,Fs=samplingFrequency)
                    plt.xlabel('Time')
                    plt.ylabel('Frequency')
                    plotPath = "/Users/matthewhagg/Desktop/Life/College/AI/DiscoverAI/archive-2/Spectrograms/" + fileDir[79:len(fileDir)-4] + '.png'
                    
                    print("Plotpath= " + plotPath)
                    
                    plt.savefig(plotPath,format='png')
                    
                    im = Image.open(plotPath)

                    im_crop = im.crop((325, 245, 2300, 895))
                    #os.remove(plotPath)
                    print("/Users/matthewhagg/Desktop/Life/College/AI/DiscoverAI/archive-2/Spectrograms/" + fileDir[79:len(fileDir)-4] + '.png')
                    print()
                    im_crop.save(plotPath, quality=100)
                    os.remove(newExportDir2)

                g = g+1
                #print(g)
                print("---------------\n")
            os.remove(os.path.abspath(file))
            o=o+1
            
except IsADirectoryError:
    print("")

print("---------------")

"""
for file in os.scandir('/Users/matthewhagg/Desktop/Life/College/AI/DiscoverAI/zarchive-2/mp3/converted'):
    fileDir = os.path.abspath(file)
    print(fileDir)
    sound = AudioSegment.from_mp3(fileDir)
    sound = sound.set_channels(1)
    wavName = "/Users/matthewhagg/Desktop/Life/College/AI/DiscoverAI/zarchive-2/mp3/converted" +fileDir[77:len(fileDir)-4] + ".wav"
    
    print(wavName)
    sound.export(wavName, format="wav")
    os.remove(fileDir)
"""
"""
print("#################")
for file in os.scandir('/Users/matthewhagg/Desktop/Life/College/AI/DiscoverAI/zarchive-2/mp3/converted'):
    # Read the wav file (mono)
    fileDir = os.path.abspath(file)
    print(fileDir)
    samplingFrequency, signalData = wavfile.read(fileDir)

    # Plot the signal read from wav file
    #plt.subplot(211)
    plt.title('Spectrogram of ' + fileDir[78:len(fileDir)-11] + ' bird call')
    #plt.plot(signalData)
    #plt.xlabel('Sample')
    #plt.ylabel('Amplitude')
    plt.subplot(211)
    plt.specgram(signalData,Fs=samplingFrequency)
    plt.xlabel('Time')
    plt.ylabel('Frequency')
    plt.savefig("/Users/matthewhagg/Desktop/Life/College/AI/DiscoverAI/zarchive-2/Spectrograms" + fileDir[77:len(fileDir)-4],format='png')
    
    im = Image.open("/Users/matthewhagg/Desktop/Life/College/AI/DiscoverAI/zarchive-2/Spectrograms" + fileDir[77:len(fileDir)-4])

    im_crop = im.crop((80, 58, 577, 227))
    os.remove("/Users/matthewhagg/Desktop/Life/College/AI/DiscoverAI/zarchive-2/Spectrograms" + fileDir[77:len(fileDir)-4])
    im_crop.save("/Users/matthewhagg/Desktop/Life/College/AI/DiscoverAI/zarchive-2/Spectrograms" + fileDir[77:len(fileDir)-4] + '.png', quality=100)
    
    
    #plt.show()
"""
