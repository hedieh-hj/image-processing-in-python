import cv2
import numpy as np #ketabkhone matrix

img=cv2.imread('2.2.png',0)
black=cv2.imread('black.png',0)
white=cv2.imread('white.png',0)
#cv2.imshow('final2.png',black)
r,c=img.shape

img_black=np.zeros((r,c),dtype='uint8')
img_black=img*black

img_white=np.zeros((r,c),dtype='uint8')
img_white=img*white

cv2.imwrite('final1.png',img_black)
cv2.imshow('final1.png',img_black)

cv2.imwrite('final2.png',img_white)
cv2.imshow('final2.png',img_white)

cv2.waitKey()