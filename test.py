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