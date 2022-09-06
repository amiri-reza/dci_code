import time
import vlc

def clip():
    media_player = vlc.MediaPlayer()
    
    # media object
    media = vlc.Media("simple.mp4")
    
    # setting media to the media player
    media_player.set_media(media)
    
    
    # start playing video
    media_player.play()
    
    # wait so the video can be played for 5 seconds
    # irrespective for length of video
    time.sleep(2)
    
    return(clip)

clip()

print("Hello, Good Morning! Do you want another video?")

choice = input("\n If yes, Press Y \n if no, Press N : \n ")
if choice == "y" :
    clip()
else:
    print("Ok then, have a nice day!")

