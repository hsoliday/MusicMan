import numpy

def apply_matrix(audioframes, matrix):
	mid = len(matrix)/2
	for i in range(1,len(audioframes)):
		if i < mid:
			pass
		else:
			tmp = 0
			for j in range(1,len(matrix)):
				tmp+=audioframes[(i+j)-mid]
				audioframes[i]=tmp
	return audio_frames
def fourier_transform(audio_frames):
	return numpy.fft.fft(audio_frames)
def reverse_fourier_transform(audio_frames):
	return numpy.fft.ifft(audio_frames)
def blindAdd(audio_frames,add_factor):
	for i in audio_frames:
		i+=add_factor
def resize(audio_frames,scale_factor):
	for i in audio_frames:
		i*=scale_factor
