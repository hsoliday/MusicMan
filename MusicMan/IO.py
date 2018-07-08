import pyaudio
import wave

def record_for_time(audio_format,audio_channel,bitrate,chunk_size,record_time):
	pa = pyaudio.PyAudio()
	stream = pa.open(format=audio_format, channels=audio_channel,rate=bitrate,input=True,frames_per_buffer=chunk_size)
	audioframes = []
	for i in range(0, int(bitrate / chunk_size * record_time)):
    		inputdata = stream.read(chunk_size)
    		audioframes.append(inputdata)
 	stream.stop_stream()
	stream.close()
	pa.terminate()
	return audioframes
def write_to_file(audioframes,audio_channel,bitrate,audio_format,file_name):
	waveFile = wave.open(file_name, 'wb')
	waveFile.setnchannels(audio_channel)
	waveFile.setsampwidth(audio.get_sample_size(audio_format))
	waveFile.setframerate(bitrate)
	waveFile.writeframes(b''.join(audioframes))
	waveFile.close()

