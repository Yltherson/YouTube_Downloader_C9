from pytube import YouTube
import urllib.request, urllib.error
import os
from pathlib import Path

# https://youtu.be/KSX4cwWRzis
# yt.streams.get_by_itag(17)


# kreyasyon chemen repetwa pou telechajeman
urep=Path.home()
paf="Downloads"
rep=os.path.join(urep, paf)



# fonksyon pou afiche progresyon telechajeman
def on_download_progress(stream, chunk, bytes_remaining):
    bytes_downloaded = stream.filesize - bytes_remaining
    percent = bytes_downloaded * 100 / stream.filesize

    print(f"progresyon telechajeman {int(percent)}%")

# fonksyon pou verifye lien anh
def checkURL(link):
    verf=False
    try:
        f= urllib.request.urlopen(link)
        verf=True
        f.close()
    except:
        print("Lyen telechajeman pa konpatib")
    return verf
repons = "O"
while(repons == "O"):
    print("----------------------------------------------------------------------\n")
    print("\t\t\t\tYouTube Downloader\n")
    print("\t\t\t\tWELCOME\n")
    print("----------------------------------------------------------------------\n")
    link = input("Antre lien youtube ou vle telechaje a\n")
    verf= checkURL(link)

    while(not verf):
        link = input("Antre lien youtube ou vle telechaje a\n")
        verf= checkURL(link)

    yt = YouTube(link)
    yt.register_on_progress_callback(on_download_progress)

    # print(f"Progression du téléchargement {int(percent)}%")

    # enfo sou media
    print("#TITLE : ",yt.title,  "#VIEWS :", yt.views,"\n")

    # kod modifikasyon tit kontni anh si li egziste
    tit = yt.title
    # paf = os.getcwd()
    if(os.path.exists(rep)):
        lpaf = str(len(os.listdir(rep))-1)
        tit2  = tit + lpaf

    yt.title = tit2

    # chwa foma videyo oubyen odyo a
    chwaFoma = input("Peze [1, 2, 3, 4, 5, 6] pou w fe chwa \n ***Video*** \n 1- 144px \n 2- 360px \n 3- 720px \n 4- 1080px \n\n ***Audio*** \n 5- 128kbps \n 6- 160kbps \n")

    lisFoma = ['1', '2', '3', '4', '5', '6']

    while(chwaFoma not in lisFoma):
        chwaFoma = int(input("Peze [1, 2, 3, 4, 5, 6] pou w fe chwa \n ***Video*** \n 1- 144px \n 2- 360px \n 3- 720px \n 4- 1080px \n\n ***Audio*** \n 5- 128kbps \n 6- 160kbps \n"))



    if(chwaFoma =='1'):
        stream = yt.streams.get_by_itag(17)
        print("Téléchargement...")
        stream.download(rep)

    elif(chwaFoma =='2'):
        stream = yt.streams.get_by_itag(18)
        print("Téléchargement...")
        stream.download(rep)

    if(chwaFoma =='3'):
        stream = yt.streams.get_by_itag(22)
        print("Téléchargement...")
        stream.download(rep)

    if(chwaFoma =='4'):
        stream = yt.streams.get_by_itag(137)
        print("Téléchargement...")
        stream.download(rep)

    if(chwaFoma =='5'):
        stream = yt.streams.get_by_itag(140)
        print("Téléchargement...")
        stream.download(rep)

    if(chwaFoma == '6'):
        stream = yt.streams.get_by_itag(251)
        print("Téléchargement...")
        stream.download(rep)

    repons = input("Tape sou [O] pou w rete nan program nan \n oubyen tape sou nenpot lot touch pou w kite\n").upper()
