import queue as Queue
import cv2 as cv
import datetime as dt

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

def OverlayMesh(frame, coords, p_bottom, cs, out_of_frame, start_time):

    max_time = dt.timedelta(microseconds=float(200))
    if len(coords) > 0:
        for (x, y, w, h) in coords:
                if (x > (cs[0] + 10) or x < (cs[0] - 10)) or (y > (cs[1] + 10) or y < (cs[1] - 10)):
                    out_of_frame = True
                    if out_of_frame:
                        end_time = dt.datetime.now()
                        if ((end_time - start_time) > max_time):
                            cs[0], cs[1], cs[2], cs[3] = x,y,w,h
                            out_of_frame = False
                            start_time = dt.datetime.now()
                            cv.putText(frame, 'Bottom', (int((2*cs[0] + cs[2])/2), int((cs[1]+cs[3]) + 20)), cv.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
                        else:
                            cv.putText(frame, 'Bottom', (int((2*cs[0] + cs[2])/2), int((cs[1]+cs[3]) + 20)), cv.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
                    else:
                        start_time = dt.datetime.now()
                        cv.putText(frame, 'Bottom', (int((2*cs[0] + cs[2])/2), int((cs[1]+cs[3]) + 20)), cv.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
                        out_of_frame = False
                else:
                    cv.putText(frame, 'Bottom', (int((2*cs[0] + cs[2])/2), int((cs[1]+cs[3]) + 20)), cv.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
                    out_of_frame = False
    else:
        cv.putText(frame, 'Bottom', (int((2*cs[0] + cs[2])/2), int((cs[1]+cs[3]) + 20)), cv.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
    
    return frame, p_bottom, cs, out_of_frame, start_time

'''
        if (y+h+40) > 480:
            p_bottom = False
        if (y-40) < 0:
            p_bottom = True

        if p_bottom:
            cv.putText(frame, 'Bottom', (int((2*x + w)/2), int((y+h) + 20)), cv.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
        else:
            cv.putText(frame, 'Top', (int((2*x + w)/2), int((y) - 20)), cv.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

    return frame, p_bottom, coordinate_state, out_of_frame, start_time
    '''