import Analyze.audio_in as a_in
import scripts.facialrecog as f_rec
from queue import Queue
from threading import Thread
import Translator.translator as translate

import keyboard as kb

def main():
    # Thread 1
    # Gets the audio, translates it to text, and translates the text
    # Returns the text
    # AudioTextQueue = ATQ
    ATQ = Queue()
    T1 = Thread(target=a_in.main(), args=(ATQ,))
    T2 = Thread(target=)
    # Thread 2
    # 

    # Thread 3
    # Gets the video and Finds the face
    # Creates a grid alongside the video
    # Prints the text at the location of the face
    f_rec.video_stream()

    print(phrase)
