import queue as Queue
import cv2 as cv

def SpeechForBox(q, char_limit):
    cur_string = ""
    char_count = 0

    while not q:
        str_size = len(q[0])
        cur_string.append(q.pop(0) + " ")
        char_count += str_size
        yield cur_string

        if char_count + len(q[0]) > char_limit:
            cur_string = ""
            char_count = 0

    return

def OverlayMesh(frame, coords):
    for (x, y, w, h) in coords:
       # frame = cv.rectangle(frame, (x+w, int(y+(h/2))), (x+w + 200, int(y+(h/2)+200)), (36,255,12), 1)
        cv.putText(frame, 'Hello', ((x+w) + 100, int((y+(h/2))+100)), cv.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
    return frame