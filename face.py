import face_recognition as fr
import cv2
from cv2 import VideoCapture
from test2 import *

cam = cv2.VideoCapture(0)

face = cv2.imread("img.jpeg")
faceencd = fr.face_encodings(face)[0]

face_encod_list = [faceencd]

face_encod = []
s=True
face_coordinate = []

while True:
    rt, frame = cam.read()

    resize_farme = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    resize_farme_rgb = resize_farme[:, :, ::-1]

    if s:
        face_coordinate = fr.face_locations(resize_farme_rgb)
        face_encod = fr.face_encodings(resize_farme_rgb, face_coordinate)

        for face in face_encod:
            matches = fr.compare_faces(face_encod_list, face)
            if matches[0] == True:
                cam.release()
                cv2.destroyAllWindows()
                taskexecution()
    cv2.imshow("test", frame)
    cv2.waitKey(1)

cam.release()
cv2.destroyAllWindows()