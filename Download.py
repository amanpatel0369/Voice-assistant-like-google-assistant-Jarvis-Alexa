import Song_Recommendation
import urllib.request
import re
import youtube_dl
import pywhatkit

def download_song():
    song_list = Song_Recommendation.song_recommendations()
    for i in range(1,2):
        url = song_list[i].replace(" ", "+")
        print(url)
        pywhatkit.playonyt(url)  
    return song_list
