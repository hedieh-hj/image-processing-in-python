import numpy as np 
import cv2

def noise_filter(img):


        result=np.zeros(img.shape)  #yeki mesl pic misazim 
        mask=np.ones((25,25))/625  #25 dar 25 - 625 ta khone (matris ba meghdar 1 )
        rows,cols =img.shape


        #threshold
        for i in range(rows):
            for j in range(cols):

                if  img[i][j]  < 170:
                    img[i][j] -=15
                    if img[i][j] >170 :
                        img[i][j] =5
                    
                else:
                    img[i][j]=img[i][j] 



        # for i in range(8,rows-8):
        #     for j in range(8,cols-8): #satr o soton aval dar nazra nemigirim 

        #         if img[i][j] < 180:  # baray ghesmati ke roshan hast (flower) noise ijad nakon

        #             small_img= img[i-8:i+9,j-8:j+9]  # az i nemishe shoro kard , va akharesh ham yeki ezafe minevisim  
        #             result[i][j]=np.sum(small_img*mask)

        #         else:
        #               result[i][j]=img[i][j]  
            

        for i in range(12,rows-12):
            for j in range(12,cols-12): #satr o soton aval dar nazra nemigirim 

                if img[i][j] < 200:  # baray ghesmati ke roshan hast (flower) noise ijad nakon

                    small_img= img[i-12:i+13,j-12:j+13]  # az i nemishe shoro kard , va akharesh ham yeki ezafe minevisim  
                    result[i][j]=np.sum(small_img*mask)

                else:
                      result[i][j]=img[i][j]              

        #cv2.imwrite('newflower(17.17).png',result)
        cv2.imwrite('newflower6(25.25).png',result)



#####################################  main   ################################################



img=cv2.imread('flower.jpg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #siah sefid kardn

noise_filter(img)



cv2.waitKey()



