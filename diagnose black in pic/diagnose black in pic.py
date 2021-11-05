import cv2

img=cv2.imread('1.3.jpg',0)

x,y=img.shape

for i in range(x):
    for j in range (y):

        if 101<=img[i][j]<=150:
            img[i][j]=150

        if 80<=img[i][j]<=100:
            img[i][j]=90

        if 50<=img[i][j]<80:
            img[i][j]=50

        if img[i][j]< 50:
            img[i][j]=0

        else:
            img[i][j]=255

cv2.imwrite('new1.3.jpg',img)
cv2.imshow('new1.3.jpg',img)
cv2.waitKey()