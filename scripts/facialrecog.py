import cv2 as cv
import numpy as np
import overlaymesh as om
import datetime as dt

def video_stream():
    """
    Creates a video stream using openCV
    :return: Active video stream with translated text output tracking user's face
    """

    vid = cv.VideoCapture(0)

    face_classifier = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_alt.xml")

    def convert_data(framedata, classifier):
        """
        Converts frame data to grey scale, necessayr for API to recognize face tracking box
        :param framedata: Information about frame
        :param classifier: Object necessary for tracking face box of user within frame
        :return: Greyscale translated frame with user facebox size information
        """

        gray = cv.cvtColor(framedata, cv.COLOR_BGR2GRAY)
        face = classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=9, minSize=(40,40))

    # comment back in to show face tracking box on video output
    # for (x, y, w, h) in face:
    #    cv.rectangle(framedata, (x,y), (x + w, y + h), (0, 255, 0), 4)
        return framedata, face

    # variables that set a standard text location, which updates only if
    # the user's face box strays too far from said location. Continually updates 
    # box location to accurately follow user's face while not updating too much as
    # to cause update lag delay
    p_bottom = True
    cs = [0, 0, 320, 240]
    out_of_frame = False
    start_time = dt.datetime.now()

    # continuous output video stream
    while True:
        ret, frame = vid.read() # reads in video frame

        rgbimage, coords = convert_data(frame, face_classifier)

        # creates frame data necessary for facial tracking and text output box location
        rgbimage, p_bottom, cs, out_of_frame, start_time = om.OverlayMesh(rgbimage, coords, p_bottom, cs, out_of_frame, start_time)

        cv.imshow("frame", rgbimage)

        # exits video stream if user enters 'q'
        if cv.waitKey(1) == ord('q'):
            break
    
    vid.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    video_stream()
