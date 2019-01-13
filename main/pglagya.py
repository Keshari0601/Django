


import sys
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
from gensim.summarization import summarize

file = open('input.txt', 'r')
text = file.read().replace('\n' , '')

#with open('audiotext.txt', 'r') as myfile:
    #text=myfile.read().replace('\n', '')
with open('c:/Users/ayush/desktop/sample2.txt', 'w') as f: 
    sys.stdout = f 
    print(summarize(text , ratio = 0.16))
































'''from google.cloud import speech_v1p1beta1 as speech
import io
client = speech.SpeechClient()

speech_file = 'chunk5.wav'

with io.open(speech_file, 'rb') as audio_file:
    content = audio_file.read()

audio = speech.types.RecognitionAudio(content=content)
config = speech.types.RecognitionConfig(
    encoding=speech.enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=8000,
    language_code='en-US',
    # Enable automatic punctuation
    enable_automatic_punctuation=True)

response = client.recognize(config, audio)

for i, result in enumerate(response.results):
    alternative = result.alternatives[0]
    print('-' * 20)
    print('First alternative of result {}'.format(i))
    print('Transcript: {}'.format(alternative.transcript))
'''