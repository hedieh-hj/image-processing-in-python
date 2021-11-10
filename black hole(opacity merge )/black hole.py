
import cv2
import numpy as np #ketabkhone matrix


def concat_tile(im_list_2d):
    return cv2.vconcat([cv2.hconcat(im_list_h) for im_list_h in im_list_2d])



images=[]
result=0
for i in range(1,6):
    img=cv2.imread(f'1/{i}.jpg')
    images.append(img)

for i in images:
    result+=i//5

cv2.imshow('new1.jpg',result)
cv2.imwrite('new1.jpg',result)

########################################################
images2=[]
result2=0
for i in range(1,6):
    img=cv2.imread(f'2/{i}.jpg')
    images2.append(img)

for i in images2:
    result2+=i//5

cv2.imshow('new2.jpg',result2)
cv2.imwrite('new2.jpg',result2)


########################################################
images3=[]
result3=0
for i in range(1,6):
    img=cv2.imread(f'3/{i}.jpg')
    images3.append(img)

for i in images3:
    result3+=i//5

cv2.imshow('new3.jpg',result3)
cv2.imwrite('new3.jpg',result3)


########################################################

images4=[]
result4=0
for i in range(1,6):
    img=cv2.imread(f'4/{i}.jpg')
    images4.append(img)

for i in images4:
    result4+=i//5

cv2.imshow('new4.jpg',result4)
cv2.imwrite('new4.jpg',result4)



finalimg = concat_tile([[result,result2],[result3,result4]])

cv2.imshow('newfinal.jpg',finalimg)
cv2.imwrite('newfinal.jpg',finalimg)
cv2.waitKey()

=======

