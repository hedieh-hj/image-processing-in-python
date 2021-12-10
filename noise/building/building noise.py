import numpy as np 
import cv2

img=cv2.imread('building.tif')
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #siah sefid kardn

result=np.zeros(img.shape)  #yeki mesl aksemon misazim 

mask=np.array([[-1,-1,-1],    #new building 2 
                [0,0,0],
                [1,1,1]])

#mask=np.array([[-1,0,1],      # new building 1 
#                 [-1,0,1],
#                 [-1,0,1]])

rows,cols =img.shape

for i in range(1,rows-1):
    for j in range(1,cols-1): #satr o soton aval dar nazra nemigirim 
       small_img= img[i-1:i+2,j-1:j+2]  # az i nemishe shoro kard , va akharesh ham yeki ezafe minevisim 
       #small img haamon 9 ta khone hast 
       result[i][j]=np.sum(small_img*mask)

cv2.imwrite('new_building2.png',result)       
cv2.imshow('new',result)

cv2.waitKey()



