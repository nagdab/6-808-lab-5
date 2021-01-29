import sounddevice as sd
import soundfile as sf

# Playback

# data, fs = sf.read("samples/PinnedYah.wav", dtype="float32")
# sd.play(data, fs)
# status = sd.wait()

#------------------------------------------------------

# Recording

# fs = 44100 # sample rate
# duration = 10  # seconds

# print(f"recording for {duration} seconds")
# myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
# sd.wait()

# print("playing recording")
# sd.play(myrecording, fs)
# sd.wait()

#------------------------------------------------------

# Playback and Recording Simeltaneously

data, fs = sf.read("samples/pPinnedYah.wav", dtype="float32")

print(f"recording and playing simeltaneously")
myrecording = sd.playrec(data, fs, channels=1)
sd.wait()

print("playing recording")
sd.play(myrecording, fs)
sd.wait()

