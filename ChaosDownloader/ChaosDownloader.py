import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pytube import YouTube
from youtubesearchpython import VideosSearch
import deezepy


class ChaosDownloader(object):
    def __init__(self):
        self.author = "ChillatoDev and PiccioneFire"

    def info_song_spoify(self, client_id:str=None, client_secret:str=None, url: str=None):
        sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
        t = sp.track(url.split('track')[1].replace('/', '').split('?')[0], market="IT")
        return t
    
    def info_song_deezer(self, url: str=None):
        dee = deezepy.Client()
        trackinfo = dee.get_track(url.split("track")[1].replace("/", ""))
        return {
            "titolo": trackinfo.title,
            "artista": trackinfo.artist.name
        }
    
    def download(self, name: str):
        videosSearch = VideosSearch(name, limit = 1)
        result = videosSearch.result()
    
        if result['result']:
            video_url = result['result'][0]['link']
            
            yt = YouTube(video_url)
            f = yt.streams.get_lowest_resolution()
            f.download(output_path="songs", filename=f"{name}.mp3")
            return True
        else:
            return False
