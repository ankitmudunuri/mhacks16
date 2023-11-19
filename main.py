import Analyze.audio_in as a_in
import sys
path1 = __file__.replace("/main.py", "/scripts/")
sys.path.append(path1)
import facialrecog as f_rec
from queue import Queue
from threading import Thread
import Translator.translator as translate
import datetime
import cv2 as cv
import time

import keyboard as kb

def main():
    # Thread 1
    # Gets the audio, translates it to text, and translates the text
    # Returns the text
    # AudioTextQueue = ATQ
    atq = Queue()
    # TranslatedTextQueue = TTQ
    ttq = Queue()
    OnSwitch = True
    # t1 = Speech-to-Text
    t1 = Thread(target=a_in.main, args=(atq,))
    # t2 = Text Translation
    t2 = Thread(target=translate.main, args=(atq,ttq))
    # t3 = Overlay Mesh Map
    vid = cv.VideoCapture(0)
    time.sleep(5)
    t3 = Thread(target=f_rec.video_stream, args=(vid,ttq,OnSwitch))
    t1.start()
    t2.start()
    t3.start()
    
    start = datetime.datetime.now()
    
    while True:
        end = datetime.datetime.now()
        if end - start > datetime.timedelta(seconds=5):
            OnSwitch = False
        if end - start > datetime.timedelta(seconds=10):
            OnSwitch = True
        if end - start > datetime.timedelta(seconds=15):
            break
    
    t1.join()
    t2.join()
    t3.join()

   

    # Thread 3
    # Gets the video and Finds the face
    # Creates a grid alongside the video
    # Prints the text at the location of the face
    f_rec.video_stream()

main()