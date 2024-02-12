
##  CHAOSDOWNLOADER

simple library that allows you to download music via spotify and deezer links

# Spotify exemple:
```python
from ChaosDownloader import ChaosDownloader

chaos = ChaosDownloader()
spotify = chaos.info_song_spotify(client_id="", client_secret="", url="link")
download = chaos.download(spotify['name'] + "- " + spotify["artists"][0]["name"])

if download:
  print("song downloaded successfully")
else:
  print("error")
```

# SAME EXAMPLE APPLIES FOR DEEZER JUST SEE THE FILE ChaosDownloader.py

