import eel
import pygame
import os

# Initialize Eel
eel.init('web')


def StartUp():
    global playlist
    global filepath
    global playing
    global i

    # Create a list to store the names of the mp3 files
    userfolder = os.path.expanduser('~') + "/Music"
    playlist = [file for file in os.listdir(userfolder) if file.endswith('.mp3')]
    filepath = userfolder + "/"

    # Initialize playback variables
    playing = False
    i = 0

    # Play the first track if available
    if playlist:
        play_track(filepath + playlist[i])
        playing = True
        eel.rename(playlist[i])  # Update the song title on the webpage
    else:
        print("No MP3 files found in the Music folder.")
        playing = False


def play_track(track_path):
    pygame.mixer.init()
    pygame.mixer.music.load(track_path)
    pygame.mixer.music.play()


@eel.expose
def PlayPause():
    global playing
    if playing:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()
    playing = not playing


@eel.expose
def nextTrack():
    global i
    if i < len(playlist) - 1:
        i += 1
        play_track(filepath + playlist[i])
        eel.rename(playlist[i])


@eel.expose
def previousTrack():
    global i
    if i > 0:
        i -= 1
        play_track(filepath + playlist[i])
        eel.rename(playlist[i])


# Start the Eel application
StartUp()
eel.start('index.html', block=False)

while True:
    if not pygame.mixer.music.get_busy() and playing:
        nextTrack()
    eel.sleep(1)
