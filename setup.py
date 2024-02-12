from setuptools import setup

setup(
    name="ChaosDownloader",
    version="1.0",
    description="this library is downloader music",
    url="https://github.com/ChaosRevelation/ChaosDownloader",
    license="MIT",
    author="ChillatoDev and PiccioneFire",
    keywords="python, spotify, deezer, soundcloud, music, downloader",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    install_requires=["spotipy", "pytube", "youtubesearchpython", "deezepy"],
    packages=["ChaosDownloader"],
)