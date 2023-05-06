from pytube import YouTube

link = input("Paste the link to download: ")
yt = YouTube(link)

for stream in yt.streams.filter(progressive=True):
    print(stream)
    print('\n')