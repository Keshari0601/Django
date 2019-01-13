import os
import ffmpeg
import moviepy.editor as mp 

def vtoo()

	class Video(object):
		def __init__(self,path):
			self.path = path

		def play(self):
			from os import startfile
			startfile(self.path)

	class Movie_MP4(Video):
		type = "MP4"

	if __name__=="__main__":
		movie = Movie_MP4(r"C:/Users/dell/Documents/python_project/Videos/video.mp4")
		if input("Press enter to play, anything else to exit") == '':
			movie.play()
		clip = mp.VideoFileClip(r"C:/Users/dell/Documents/python_project/Videos/video.mp4")
		clip.audio.write_audiofile("theaudio.wav")
