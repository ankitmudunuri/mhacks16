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
    frameq = Queue()
    #t3 = Thread(target=f_rec.video_stream, args=(ttq,frameq, OnSwitch))
    t1.start()
    t2.start()
    #t3.start()
    
    vid = cv.VideoCapture(0)
    now = datetime.datetime.now()
    text = ""
    p_bottom = True
    cs = [0, 0, 320, 240]
    out_of_frame = False
    start_time = datetime.datetime.now()
    length = 0
    
    while True:
        ret, frame = vid.read()
        if not ttq.empty():
            now = datetime.datetime.now()
            if (now - start_time).microseconds > 50000:
                text = str(ttq.get())
                if len(text.split(" ")) > 6 and abs(length - len(text.split(" "))) >= 1 and len(text) != 0:
                    text = text.split(" ")
                    length = len(text)
                    text = " ".join(text[-6:])
                    
                start_time = datetime.datetime.now()
            else:
                pass
        f_rec.video_stream(frame, True, text, p_bottom, cs, out_of_frame, start_time)
        if cv.waitKey(1) & 0xFF == ord('q'):
            t1.join()
            t2.join()
            vid.release()
            cv.destroyAllWindows()
            sys.exit(0)

   

    # Thread 3
    # Gets the video and Finds the face
    # Creates a grid alongside the video
    # Prints the text at the location of the face

main()