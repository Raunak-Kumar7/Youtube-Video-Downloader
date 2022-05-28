#https://pytube.io/en/latest/

#pip install pytube3
#python -m pip install --upgrade pytube
#/Applications/Python\ 3.7/Install\ Certificates.command     <-- for mac,change the verison of python according to installed


from pytube import YouTube

url = 'https://www.youtube.com/shorts/2ZQFlGLVtXg'
my_video=YouTube(url)

print('Video Title is ')
print(my_video.title)

print('Thumbnail of the video is')
print(my_video.thumbnail_url)

print('Downloading video')
#first selecting the resolution of the video

my_video=my_video.streams.get_highest_resolution()

#to get all the resolutions 
#my_video=my_video.streams.first()
#for stream in my_video.streams:
#   print(stream)

my_video.download()