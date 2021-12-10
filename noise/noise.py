import numpy as np 
import cv2

def noise(img , state):

    if int(state) == 3 :

        result=np.zeros(img.shape)  #yeki mesl pic misazim 
        mask=np.ones((3,3))/9  #3 dar 3 - 9 ta khone (matris ba meghdar 1 )
        rows,cols =img.shape

        for i in range(1,rows-1):
            for j in range(1,cols-1): #satr o soton aval dar nazra nemigirim 
                small_img= img[i-1:i+2,j-1:j+2]  # az i nemishe shoro kard , va akharesh ham yeki ezafe minevisim 
                #small img haamon 9 ta khone hast 
                result[i][j]=np.sum(small_img*mask)

        cv2.imwrite('new(3.3).png',result)   

#####################################################################################    
#             
    if int(state) == 5 :

        result=np.zeros(img.shape)  #yeki mesl pic misazim 
        mask=np.ones((5,5))/25  #5 dar 5 - 25 ta khone (matris ba meghdar 1 )
        rows,cols =img.shape

        for i in range(2,rows-2):
            for j in range(2,cols-2): #satr o soton aval dar nazra nemigirim 
                small_img= img[i-2:i+3,j-2:j+3]  # az i nemishe shoro kard , va akharesh ham yeki ezafe minevisim  
                result[i][j]=np.sum(small_img*mask)

        cv2.imwrite('new(5.5).png',result)
#####################################################################################

    if int(state) == 7 :

        result=np.zeros(img.shape)  #yeki mesl pic misazim 
        mask=np.ones((7,7))/49  #3 dar 3 - 9 ta khone (matris ba meghdar 1 )
        rows,cols =img.shape

        for i in range(3,rows-3):
            for j in range(3,cols-3): #satr o soton aval dar nazra nemigirim 
                small_img= img[i-3:i+4,j-3:j+4]  # az i nemishe shoro kard , va akharesh ham yeki ezafe minevisim 
                result[i][j]=np.sum(small_img*mask)

        cv2.imwrite('new(7.7).png',result)        

#####################################################################################

    if int(state) == 15 :

        result=np.zeros(img.shape)  #yeki mesl pic misazim 
        mask=np.ones((15,15))/225  #3 dar 3 - 9 ta khone (matris ba meghdar 1 )
        rows,cols =img.shape

        for i in range(7,rows-7):
            for j in range(7,cols-7): #satr o soton aval dar nazra nemigirim 
                small_img= img[i-7:i+8,j-7:j+8]  # az i nemishe shoro kard , va akharesh ham yeki ezafe minevisim  
                result[i][j]=np.sum(small_img*mask)

        cv2.imwrite('new(15.15).png',result)
        
#####################################################################################

    if int(state) == 0 :

        x=int(input('enter your value ? '))

        result=np.zeros(img.shape)  #yeki mesl pic misazim 
        mask=np.ones((x,x))/(x*x)  #x dar x - x*x ta khone (matris ba meghdar 1 )
        rows,cols =img.shape
        x1=x//2
        x2=x1+1
        for i in range(x1,rows-x1):
            for j in range(x1,cols-x1): #satr o soton aval dar nazra nemigirim 
                small_img= img[i-x1:i+x2,j-x1:j+x2]  # az i nemishe shoro kard , va akharesh ham yeki ezafe minevisim 
                #small img haamon 9 ta khone hast 
                result[i][j]=np.sum(small_img*mask)

        cv2.imwrite('new(x.x).png',result)   

#####################################  main   ################################################


i=1
while 1:
    img=cv2.imread('---.png')  #--- =enter the name of your picture with its format e.g.(name.png)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #siah sefid kardn


    print("""menu 
    filter 3*3 --> enter 3 
    filter 5*5 --> enter 5
    filter 7*7 --> enter 7
    filter 15*15 --> enter 15
    filter x*x --> enter 0 (if you want to set a value)
    """)

    x=int(input("enter your choise : "))

    noise(img,x)

    i=int(input(" do you want try agian ? enter 1 = yes    enter 2= no "))


cv2.waitKey()



