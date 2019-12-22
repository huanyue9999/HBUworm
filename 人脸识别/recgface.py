import cv2 as cv
import numpy as np

pathj = './111.png'
pathf = 'D:\envs\\tensorflow\Lib\site-packages\cv2\data\\haarcascade_frontalface_default.xml'
pathe = 'D:\envs\\tensorflow\Lib\site-packages\cv2\data\\haarcascade_eye.xml'//按照格式进行配置，具体文件参加readme

face_cascade = cv.CascadeClassifier(pathf)
#face_cascade.load(pathf)
eye_cascade = cv.CascadeClassifier(pathe)
#eye_cascade.load(pathe)
img = cv.imread(pathj)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray,1.1,3)
#print(faces)
for(x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,x+h),(255,0,0),2)
    face_re = img[y:y+h, x:x+h]
    face_re_g=gray[y:y+h, x:x+h]
    eyes = eye_cascade.detectMultiScale(face_re_g)
    for(ex,ey,ew,eh) in eyes:
        cv.rectangle(face_re,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()