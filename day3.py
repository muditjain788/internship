#!/usr/bin/python3
# importing time library
import time
import webbrowser
import subprocess
import pafy
import vlc
option='''
Press 1 to start your vlc media player :
Press 2 to play your fav song in youtube :
Press 3 to search something on google :
Pres  4 to send whatsapp message to your fav number
Press 5 to check current time  and date :
Press 6 to reboot your machine :
'''
print(option)
choice=input()
#input function will take input in str format
#conditional state
if choice =='5' :
   #to connect our BIOS time
   current_time=time.ctime()
   print(current_time)
elif choice =='2' :
    url="https://www.youtube.com/watch?v=4JYE-rZmWsg"
    video=pafy.new(url)
    best=video.getbest()
    playurl=best.url
    Instance = vlc.Instance() 
    player = Instance.media_player_new()
    Media = Instance.media_new(playurl)
    Media.get_mrl()
    player.set_media(Media)
    player.play()

elif choice == '1':
   #to connect to os level application we use sub process
   subprocess.getoutput('vlc')
elif choice == '3' :
   data=input("type your search:--->")
   webbrowser.open_new_tab("https://www.google.com/search?q="+data)
else :
   print("hiii")
		



