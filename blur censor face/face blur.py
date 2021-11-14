import numpy as np
import cv2


image = cv2.imread('obama.png')

image = cv2.resize(image , (0,0) , fx=0.5 , fy=0.5)
face_detect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_data = face_detect.detectMultiScale(image, 1.3, 5)
  

for (x, y, w, h) in face_data:
    #cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    select = image[y:y+h, x:x+w]
    # applying a gaussian blur over this new rectangle area
    select = cv2.GaussianBlur(select, (49, 49), 30)
    # impose this blurred image on original image to get final image
    image[y:y+select.shape[0], x:x+select.shape[1]] = select

cv2.imshow('out2' , image)
cv2.imwrite('out2.png',image)
cv2.waitKey()   