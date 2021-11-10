import cv2
import numpy as np #ketabkhone matrix

img1=cv2.imread('a.tif',0)
img2=cv2.imread('b.tif',0)

print (img1.shape)
print (img2.shape)


result =cv2.subtract(img2,img1)


cv2.imwrite('new2.1.tif',result)
cv2.imshow('new2.1.tif',result)


cv2.waitKey()
