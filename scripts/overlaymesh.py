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

def OverlayMesh(frame, coords, p_bottom):
    for (x, y, w, h) in coords:

        if (y+h+40) > 480:
            p_bottom = False
        if (y-40) < 0:
            p_bottom = True

        if p_bottom:
            cv.putText(frame, 'Bottom', (int((2*x + w)/2), int((y+h) + 20)), cv.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
        else:
            cv.putText(frame, 'Top', (int((2*x + w)/2), int((y) - 20)), cv.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
    return frame, p_bottom