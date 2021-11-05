import cv2

img1=cv2.imread('1.2.jpg',0)
img2=cv2.imread('1.22.jpg',0)

img1=cv2.rotate(img1,cv2.ROTATE_180)
img2=cv2.rotate(img2,cv2.ROTATE_180)

cv2.imwrite('new1.2.png',img1)
cv2.imshow('new1.2.png',img1)
cv2.imwrite('new1.22.png',img2)
cv2.imshow('new1.22.png',img2)
cv2.waitKey()