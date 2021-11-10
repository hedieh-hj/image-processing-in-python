import cv2
import numpy as np #ketabkhone matrix


image=0
for i in range(15):
    img = cv2.imread(f'image/h{i}.jpg', 0)
    image += img//15


cv2.imwrite('final.png',image)
cv2.imshow('final.png',image)

cv2.waitKey()