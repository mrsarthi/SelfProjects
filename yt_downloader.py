import moviepy.editor as mpe
from pytube import YouTube

link = input("Paste the link to download: ")
yt = YouTube(link)

for stream in yt.streams.filter(adaptive=True):
    print(stream)
    print('\n')

link = input("Enter the link to download: ")
yt = YouTube(link)
print(yt.title)
print(yt.streams.filter(progressive=True))

# stream = yt.streams.get_by_itag(299)
# stream.download()

clip = mpe.VideoFileClip("LG 4K DEMO HDR 2018 (60FPS) ELBA.mp4")
audio_bg = mpe.AudioFileClip("audio.mp4")
final_audio = mpe.CompositeAudioClip([audio_bg])
final_clip = clip.set_audio(final_audio)
final_clip.write_videofile("final.mp4")


# from sys import argv

# link = input("Enter the link to download: ")
# yt = YouTube(link)

# print("Title: ", yt.title)

# print("View: ", yt.views)

# yd = yt.streams.get_highest_resolution()

# # ADD FOLDER HERE
# yd.download('./YTfolder')