from django.shortcuts import render
from django.http import HttpResponse
import pytube 
import os
import ffmpeg
import moviepy.editor as mp 
import requests
import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.utils import make_chunks
import csv
SAVE_PATH = "C:/Users/dell/Documents/python_project/Videos" #to_do 
DIRNAME = r'c:/Users/dell/Documents/python_project/chunks'
OUTFILE = r'c:/Users/dell/Documents/python_project/chunks'
out_path = os.path.join("c:/Users/dell/Documents/python_project/outfile" , "hello.json")

# Create your views here.
def index(request):
    #return HttpResponse('inside the main')
    return render(request, 'main/index.html')

def detail(request, link):
    return HttpResponse("You're looking at link "+link)

def udaka(request):
    link=request.POST.get('link')
    yt = pytube.YouTube(link) 
    stream= yt.streams.first()
    stream.download(SAVE_PATH)
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

    def get_file_paths(dirname):
        file_paths = []
        for root , directories , files in os.walk(dirname):
            for filename in files:
                filepath = os.path.join(root , filename)
                file_paths.append(filepath)
        return file_paths
    os.walk(SAVE_PATH)
    os.rename('C:/Users/dell/Documents/python_project/Videos/'+stream.default_filename,'C:/Users/dell/Documents/python_project/Videos/video.mp4')
    class Video(object):
        def __init__(self,path):
            self.path = path
        def play(self):
            from os import startfile
            startfile(self.path)
    class Movie_MP4(Video):
        type = "MP4"
    movie = Movie_MP4(r"C:/Users/dell/Documents/python_project/Videos/video.mp4")
    clip = mp.VideoFileClip(r"C:/Users/dell/Documents/python_project/Videos/video.mp4")
    clip.audio.write_audiofile("C:/Users/dell/Documents/python_project/Videos/theaudio.wav")
    audio = AudioSegment.from_wav("C:/Users/dell/Documents/python_project/Videos/theaudio.wav")
    chunk_len_ms = 10000
    chunks = make_chunks(audio , chunk_len_ms)
    
    for i , chunk in enumerate(chunks):
        chunk_name = "chunk{0}.wav".format(i)
        chunk.export("c:/Users/dell/Documents/python_project/chunks/chunk{0}.wav".format(i) , format = "wav")
    files = get_file_paths(DIRNAME)
    for file in files:
        (filepath , ext) = os.path.splitext(file)
        file_name = os.path.basename(file)
        if ext == '.wav':
            a = process_file(file)
            with open(out_path, 'a') as f:
                f.write(a)
	

    return HttpResponse("You're looking at link "+link)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})
