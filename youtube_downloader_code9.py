from pytube import YouTube
import urllib.request, urllib.error


# yt = YouTube('https://youtu.be/KSX4cwWRzis')
# yt.streams.get_by_itag(17)

def on_download_progress(stream, chunk, bytes_remaining):
    bytes_downloaded = stream.filesize - bytes_remaining
    percent = bytes_downloaded * 100 / stream.filesize
    print(f"Progression du téléchargement {int(percent)}%")
    

    print(f"progresyon telechajema {int(percent)}%")

def checkURL(link):
    verf=False
    try:
        f= urllib.request.urlopen(link)
        verf=True
        f.close()
    except:
        print("Lyen telechajeman pa konpatib")
    return verf

link = input("Antre lien youtube ou vle telechaje a\n")
verf= checkURL(link)

while(not verf):
    link = input("Antre lien youtube ou vle telechaje a\n")
    verf= checkURL(link)

yt = YouTube(link)
yt.register_on_progress_callback(on_download_progress)
<<<<<<< HEAD


=======
>>>>>>> cc6ba223426e55af029d6faf96b0ee116d1ea424

print("#TITLE : ",yt.title,  "#VIEWS :", yt.views,"\n")
# print(yt.thumbnail)

chwaFoma=-1

while(chwaFoma < 1 or chwaFoma > 6):
    chwaFoma = int(input("Peze [1, 2, 3, 4, 5, 6] pou w fe chwa \n ***Video*** \n 1- 144px \n 2- 360px \n 3- 720px \n 4- 1080px \n\n ***Audio*** \n 5- 128kbps \n 6- 160kbps \n"))
    if(chwaFoma ==1):
        stream = yt.streams.get_by_itag(17)
        print("Téléchargement...")
        stream.download()

    elif(chwaFoma ==2):
        stream = yt.streams.get_by_itag(18)
        print("Téléchargement...")
        stream.download()

    if(chwaFoma ==3):
        stream = yt.streams.get_by_itag(22)
        print("Téléchargement...")
        stream.download()

    if(chwaFoma ==4):
        stream = yt.streams.get_by_itag(137)
        print("Téléchargement...")
        stream.download()

    if(chwaFoma ==5):
        stream = yt.streams.get_by_itag(140)
        print("Téléchargement...")
        stream.download()

    if(chwaFoma ==6):
        stream = yt.streams.get_by_itag(251)
        print("Téléchargement...")
        stream.download()
