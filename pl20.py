# import soundfile as sf
# import matplotlib.pyplot as plt
# import numpy as np
# audio, sample_rate = sf.read('C:/Users/Taksh/OneDrive/Desktop/Python_labs/sample-12s.wav')
# print(audio)
# print(type(audio))
# print(type(sample_rate))
# sf.write('New_audio.wav',audio,sample_rate)
# time=np.linspace(0,len(audio)/sample_rate,num=len(audio))
# plt.plot(time,audio)
# plt.show()

import soundfile as sf
audio, sample_rate = sf.read('C:/Users/Taksh/OneDrive/Desktop/Python_labs/sample-12s.wav')
import soundfile as sf
sf.write('new_audio_file.wav', audio, sample_rate)

# from pydub import AudioSegment
# audio = AudioSegment.from_file('C:/Users/Taksh/OneDrive/Desktop/Python_labs/sample-12s.wav')
# audio_fade_in = audio.fade_in(2000)
# audio_fade_in.export('audio_file_fade_in.wav', format='wav')
