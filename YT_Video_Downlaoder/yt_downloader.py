from pytube import YouTube

link = input("Enter the link to download: ")
yt = YouTube(link)
print(yt.title)
# print(yt.streams.filter(progressive=True))

stream = yt.streams.get_by_itag(22)
stream.download()



# from sys import argv

# link = input("Enter the link to download: ")
# yt = YouTube(link)

# print("Title: ", yt.title)

# print("View: ", yt.views)

# yd = yt.streams.get_highest_resolution()

# # ADD FOLDER HERE
# yd.download('./YTfolder')