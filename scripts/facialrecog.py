import cv2 as cv
import numpy as np

def video_stream():
    vid = cv.VideoCapture(0)

    face_classifier = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")

    def convert_data(framedata, classifier):
        gray = cv.cvtColor(framedata, cv.COLOR_BGR2GRAY)
        face = face_classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(40,40))

        for (x, y, w, h) in face:
            cv.rectangle(framedata, (x,y), (x + w, y + h), (0, 255, 0), 4)

        return framedata

    while True:
        ret, frame = vid.read()

        rgbimage = convert_data(frame, face_classifier)

        cv.imshow("frame", rgbimage)

        if cv.waitKey(1) == ord('q'):
            break
    
    vid.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    video_stream()