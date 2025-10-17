# pip install pytubefix

from pytubefix import YouTube
from pytubefix.cli import on_progress


url = input("Insira a URL do video: ")


yt = YouTube(url,on_progress_callback=on_progress)
ys = yt.streams.get_highest_resolution()

ys.download(output_path='/home/kaua/Downloads')

