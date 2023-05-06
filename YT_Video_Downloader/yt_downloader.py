import moviepy.editor as mpe
from pytube import YouTube

q_dict_adap = {"1080p, 60": 299, "1080p, 30": 137, "720p, 60": 298}
q_dict_prog = {"720p, 30": 22, "144": 17}
audio_itag = 251

link = input("Paste the link to download: ")
yt = YouTube(link)

qual = input("Enter the desired quality in format (quality, fps)"
             "Ex. 480p, 30: ")


def combiner():
    clip = mpe.VideoFileClip(yt.title+".mp4")
    audio_bg = mpe.AudioFileClip(yt.title+".webm")
    final_audio = mpe.CompositeAudioClip([audio_bg])
    final_clip = clip.set_audio(final_audio)
    final_clip.write_videofile("final_video.mp4")

    
if qual == "720p, 60":
    print("Pls make sure the video is available in the quality and fps you desire: ")
    itag = q_dict_adap.get(qual)
    print('Downloading: ')
    yt.streams.get_by_itag(itag).download()
    yt.streams.get_by_itag(audio_itag).download()
    combiner()
elif qual == "1080p, 30":
    itag = q_dict_adap.get(qual)
    print('Downloading: ')
    yt.streams.get_by_itag(itag).download()
    yt.streams.get_by_itag(audio_itag).download()
    combiner()
elif qual == "1080p, 60":
    itag = q_dict_adap.get(qual)
    print('Downloading: ')
    yt.streams.get_by_itag(itag).download()
    yt.streams.get_by_itag(audio_itag).download()
    combiner()
else:
    print('Downloading: ')
    itag = q_dict_prog.get(qual)
    yt.streams.get_by_itag(itag).download()

# yt.streams.get_by_itag(itag).download()


# link = input("Enter the link to download: ")
# yt = YouTube(link)
# print(yt.title)   
# print(yt.streams.filter(progressive=True))