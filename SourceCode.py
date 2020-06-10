import youtube_dl
import os
import pygame
import urllib.request
import urllib.parse
import re

def install_dependencies():
    os.system("pip install youtube_dl pygame")
    
def search_video(query):
    video_found = False
    while video_found == False:
        query_string = urllib.parse.urlencode({"search_query" : query})
        html_content = urllib.request.urlopen("http://www.youtube.com/results?"+query_string)
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        if len(search_results) != 0:
            video_found = True
            song_url = "http://www.youtube.com/watch?v=" + search_results[0]
    return(song_url)

def download(song_url):
    os.chdir('.\\songs')
    config_options = {
        'outtmpl': '%(id)s.mp4', # name the file the ID of the video
        'format':'bestaudio/best',
        'extract_flat':True,
        'postprocessors': [{
                    'key':'FFmpegExtractAudio',
                    'preferredcodec':'mp3',
                    'preferredquality':'192',
                }],
    }
    with youtube_dl.YoutubeDL(config_options) as ydl:
        ydl.download([song_url + ' --avoid-throttling --http-chunk-size 10M'])
        metadata = ydl.extract_info(song_url, download=False)
    
    os.chdir('../')
    return(metadata['id'])

def play(query):
    if query != "":
        song_id = download(search_video(query))
        os.chdir('.\\songs')
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(song_id + '.mp3')
        pygame.mixer.music.play()
        os.chdir('../')

def stop():
    pygame.mixer.music.stop()