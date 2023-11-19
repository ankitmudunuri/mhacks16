import queue as Queue
import cv2 as cv
import datetime as dt

# Variables related to output text
RGB_TUPLE = (0,0,0)
FONT_CHOICE = cv.FONT_HERSHEY_SIMPLEX
FONT_SCALE = 1.1
FONT_THICKNESS = 2

def SpeechForBox(q, char_limit):
    """
    Actively manages frame output string, clearing each time the string reaches maximum size for text box
    :param q: input queue of words to be appended to text box
    :param char_limit: maximum number of characters allowed before output string is cleared
    :return: Current output string to be placed in frame text box
    """
    cur_string = ""
    char_count = 0

    # while words exist on queue to be outputed
    while not q:
        str_size = len(q[0])
        cur_string.append(q.pop(0) + " ")
        char_count += str_size
        yield cur_string

        # resets variables and output string if character limit is reached
        if char_count + len(q[0]) > char_limit:
            cur_string = ""
            char_count = 0

    return

def OverlayMesh(frame, coords, p_bottom, cs, out_of_frame, start_time):
    """
    Creates text box to be actively streamed along side frames brought in from camera
    :param frame: frame data provided by facialrecog.py
    :param coords: coordinate set of text box to output data in to
    :param p_bottom: boolean, when set true text box is placed below user's face, above user's face when false
    :param cs: coordinate state of text box to output if user's face box does not leave offset box for more than 200 microseconds
    :param out_of_frame: boolean indicating whether previous frames' face box was outside of offset box
    :param start_time: datetime variable indicating when out_of_frame was set to true
    :return: Dynamically shifting text box, reacting to location of user's face box
    """

    max_time = dt.timedelta(microseconds=float(200))

    # true if face box was recognized in current frame
    if len(coords) > 0:
        for (x, y, w, h) in coords:

            # updates p_bottom boolean if face box gets too close to top or bottom of screen
            if (y+h+80) > 480:
                p_bottom = False
            if (y-60) < 0:
                p_bottom = True

            # true if current face box location is outside of offset box
            if (x > (cs[0] + 10) or x < (cs[0] - 10)) or (y > (cs[1] + 10) or y < (cs[1] - 10)):
                out_of_frame = True
                
                if out_of_frame:
                    end_time = dt.datetime.now()

                    if ((end_time - start_time) > max_time): # true if time out of frame is larger than 200 microseconds
                        cs[0], cs[1], cs[2], cs[3] = x,y,w,h # updates text box constant state variables
                        out_of_frame = False
                        start_time = dt.datetime.now()

                        if p_bottom: # for all similar (4 other) if/else in function - checks p_bottom to print text above/below user face
                            cv.putText(frame, 'Bottom dlfkjsdkl', (int((cs[0])/2), int((cs[1]+cs[3]) + 20)), FONT_CHOICE, FONT_SCALE, RGB_TUPLE, FONT_THICKNESS)
                        else:
                            cv.putText(frame, 'Top', (int((cs[0])/2), int((cs[1]) - 20)), FONT_CHOICE, FONT_SCALE, RGB_TUPLE, FONT_THICKNESS)

                    else:
                        if p_bottom:
                            cv.putText(frame, 'Bottom dlfkjsdkl', (int((cs[0])/2), int((cs[1]+cs[3]) + 20)), FONT_CHOICE, FONT_SCALE, RGB_TUPLE, FONT_THICKNESS)
                        else:
                            cv.putText(frame, 'Top', (int((cs[0])/2), int((cs[1]) - 20)), FONT_CHOICE, FONT_SCALE, RGB_TUPLE, FONT_THICKNESS)

                else:
                    start_time = dt.datetime.now()
                    if p_bottom:
                        cv.putText(frame, 'Bottom dlfkjsdkl', (int((cs[0])/2), int((cs[1]+cs[3]) + 20)), FONT_CHOICE, FONT_SCALE, RGB_TUPLE, FONT_THICKNESS)
                    else:
                        cv.putText(frame, 'Top', (int((cs[0])/2), int((cs[1]) - 20)), FONT_CHOICE, FONT_SCALE, RGB_TUPLE, FONT_THICKNESS)
                    out_of_frame = False

            else:
                if p_bottom:
                    cv.putText(frame, 'Bottom dlfkjsdkl', (int((cs[0])/2), int((cs[1]+cs[3]) + 20)), FONT_CHOICE, FONT_SCALE, RGB_TUPLE, FONT_THICKNESS)
                else:
                    cv.putText(frame, 'Top', (int((cs[0])/2), int((cs[1]) - 20)), FONT_CHOICE, FONT_SCALE, RGB_TUPLE, FONT_THICKNESS)
                out_of_frame = False

    else: # if no face box detected, provides text box using most recent text box coordinate state
        if p_bottom:
            cv.putText(frame, 'Bottom dlfkjsdkl', (int((cs[0])/2), int((cs[1]+cs[3]) + 20)), FONT_CHOICE, FONT_SCALE, RGB_TUPLE, FONT_THICKNESS)
        else:
            cv.putText(frame, 'Top', (int((cs[0])/2), int((cs[1]) - 20)), FONT_CHOICE, FONT_SCALE, RGB_TUPLE, FONT_THICKNESS)
    
    return frame, p_bottom, cs, out_of_frame, start_time