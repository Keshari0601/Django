import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.utils import make_chunks
import csv

#AUDIO_FILE = path.join(path.dirname(path.realpath(C:/Users/ayush/Desktop)), "theaudio.wav")


DIRNAME = r'c:/Users/ayush/desktop/chunks'
OUTFILE = r'c:/Users/ayush/desktop/output.csv'

def get_file_paths(dirname):
	file_paths = []
	for root , directories , files in os.walk(dirname):
		for filename in files:
			filepath = os.path.join(root , filename)
			file_paths.append(filepath)
	return file_paths

def process_file(file):
	r = sr.Recognizer()
	a = ''
	with sr.AudioFile(file) as source:
		audio = r.record(source)
		try:
			a = r.recognize_google(audio)
		except Exception as e:
			print(e)
	return a 

def main():
	# chunking the audio and exporting it to a directory
	audio = AudioSegment.from_wav("theaudio.wav")
	chunk_len_ms = 10000
	chunks = make_chunks(audio , chunk_len_ms)
	for i , chunk in enumerate(chunks):
		chunk_name = "chunk{0}.wav".format(i)
		chunk.export("C:/Users/ayush/Desktop/chunks/chunk{0}.wav".format(i) , format = "wav")


	files = get_file_paths(DIRNAME)
	for file in files:
		(filepath , ext) = os.path.splitext(file)
		file_name = os.path.basename(file)
		if ext == '.wav':
			a = process_file(file)
			with open(OUTFILE, 'a') as f:
				writer = csv.writer(f)
				#writer.writerow(['file_name' , 'google'])
				writer.writerow(['' , a])

if __name__ == '__main__':
	main()

'''
r = sr.Recognizer()
#audio = 'theaudio.wav'
audio = AudioSegment.from_wav("theaudio.wav")
chunk_len_ms = 10000
chunks = make_chunks(audio , chunk_len_ms)
text = ""
#chunk1 = {}
for i , chunk in enumerate(chunks):
	chunk_name = "chunk{0}.wav".format(i)
	chunk.export("C:/Users/ayush/Desktop/chunks/chunk{0}.wav".format(i) , format = "wav")
	
	'
	with sr.AudioFile(chunk_name) as source:
		music = r.record(source)

	try:
		text += r.recognize_google(music)
	except Exception as e:
		print(e)


print(text)
'''



'''
ten_seconds = 5 * 1000
text = ""
while(audio):
	first_10_seconds = audio[:ten_seconds]
	audio = audio[ten_seconds:]
	with sr.AudioFile(first_10_seconds) as source:
		music = r.record(source)

	try:
		text = r.recognize_google(music)
		print(text)
	except Exception as e:
		print(e)

print(text)



with sr.AudioFile(audio) as source:
	audio = r.record(source)

try:
	text = r.recognize_google(audio)
	print(text)

except Exception as e:
	print(e)



try:
	print("The audio file contains :" + r.recognize_google(audio))
except sr.UnknownValueError:
	print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
	print("Could not request results from Google Speech Recognition service:{0}".format(e))
'''