def remove_elems(begin,end,audio_frames):
	for i in range(begin,end):
		audio_frames.remove(i)
	return audio_frames
def append_audio(audio_frames1,audio_frames2):
	audio_frames1.append(audio_frames2)
	return audio_frames1
	


