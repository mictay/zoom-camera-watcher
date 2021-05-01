from PIL import ImageGrab
from functools import partial
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)
import os
import sys
import pyautogui
import time
from playsound import playsound
import pygame

print (os.path.dirname(sys.executable))
pygame.mixer.init()
pygame.mixer.music.load("sound_ping.mp3")

searchTime = 10

continueForEver = True
r = None

while continueForEver:
    print("Searching every {0} seconds".format(searchTime))

    while r is None:
        r = pyautogui.locateOnScreen(image=r'calc_9.png', grayscale=True)
        if r is not None:
            break
        pygame.mixer.music.play()
        time.sleep(searchTime)

    print(r)
    r = None

    pygame.mixer.music.stop()
    pygame.mixer.music.load("sound_scorp.mp3")
    pygame.mixer.music.play()
    time.sleep(2)
    playsound('sound_get_over_here.mp3', False)

    choice = pyautogui.confirm(text='Click OK(Sleep 30 minutes) or Snooze(seconds)', title='Found a Match', buttons=['OK', 'Snooze'])
    pygame.mixer.music.stop()

    if choice == 'OK':
        print("Sleeping for 30 minutes")
        time.sleep(1800)
    else:
        snooze = pyautogui.prompt("Snooze for how many seconds?")
        print("Snoozing for " + snooze + " seconds")
        time.sleep(int(snooze))

    pygame.mixer.music.load("sound_ping.mp3")