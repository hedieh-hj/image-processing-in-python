import cv2
import numpy as np #ketabkhone matrix

img=cv2.imread('2.1.jpg',0)
cv2.imshow('img.jpg',img)
r,c=img.shape
print(r,c)

x = 255 - img
gradiant = cv2.GaussianBlur(x,(33,33), 0)
y=255-gradiant

result=img/y
result=result*255

cv2.imwrite('gradiant1.png',gradiant)
cv2.imshow('gradiant1.png',gradiant)

cv2.imwrite('final33.png',result)
#cv2.imshow('final33.png',result)               #check picture that save in directory (!!!!!!!!!!!!!!!!!!!!!!!!)

cv2.waitKey()