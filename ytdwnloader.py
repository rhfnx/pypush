import pytube

#3gp format only i think 
#this is stupid

link = input("Enter you link: ")
yt = pytube.YouTube(link)
yt.streams.first().download()
print("Downloaded!",link)