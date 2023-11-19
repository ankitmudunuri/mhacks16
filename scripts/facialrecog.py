import cv2 as cv
import numpy as np
import overlaymesh as om
import datetime as dt

def video_stream():
    vid = cv.VideoCapture(0)

    face_classifier = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")

    def convert_data(framedata, classifier):
        gray = cv.cvtColor(framedata, cv.COLOR_BGR2GRAY)
        face = face_classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=9, minSize=(40,40))

        for (x, y, w, h) in face:
            cv.rectangle(framedata, (x,y), (x + w, y + h), (0, 255, 0), 4)

        return framedata, face

    p_bottom = True
    cs = [0, 0, 320, 240]
    out_of_frame = False
    start_time = dt.datetime.now()

    while True:
        ret, frame = vid.read()

        rgbimage, coords = convert_data(frame, face_classifier)

        rgbimage, p_bottom, cs, out_of_frame, start_time = om.OverlayMesh(rgbimage, coords, p_bottom, cs, out_of_frame, start_time)

        cv.imshow("frame", rgbimage)

        if cv.waitKey(1) == ord('q'):
            break
    
    vid.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    video_stream()
