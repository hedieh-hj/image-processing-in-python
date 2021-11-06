import cv2

img=cv2.imread('1.1.png',0)
cv2.imshow('1.1.png',img)
x=img.shape[0]      #height
y=img.shape[1]      #width

# print(x)
# print(y)

xx=x/8
yy=y/8
rangexx=[]
rangeyy=[]
for i in range(1,9):
    rangexx.append(xx*i)
print(rangexx[0])   # 0 = 65


for i in range(1,9):
    rangeyy.append(yy*i)



for i in range(x+1):
    for j in range(y+1):
#//////////////////////////////////////////////////////////////////  black  /////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////// soton 1
        if i<= rangexx[0] and j<=rangeyy[0]:
            img[i][j]=0

        if rangexx[1]<=i< rangexx[2] and j<=rangeyy[0]:
            img[i][j]=0

        if rangexx[3]<=i< rangexx[4] and j<=rangeyy[0]:
            img[i][j]=0   

        if rangexx[5]<=i< rangexx[6] and j<=rangeyy[0]:
            img[i][j]=0                
#////////////////////////////////////////////////////////// soton 2
        if rangexx[0]<=i< rangexx[1] and rangeyy[0]<=j<rangeyy[1]:
            img[i][j]=0

        if rangexx[2]<=i< rangexx[3] and rangeyy[0]<=j<rangeyy[1]:
            img[i][j]=0

        if rangexx[4]<=i< rangexx[5] and rangeyy[0]<=j<rangeyy[1]:
            img[i][j]=0   

        if rangexx[6]<=i< rangexx[7] and rangeyy[0]<=j<rangeyy[1]:
            img[i][j]=0
#////////////////////////////////////////////////////////// soton 3 mesl i hay soton 1 
        if i<= rangexx[0] and rangeyy[1]<=j<rangeyy[2]:
            img[i][j]=0

        if rangexx[1]<=i< rangexx[2] and rangeyy[1]<=j<rangeyy[2]:
            img[i][j]=0

        if rangexx[3]<=i< rangexx[4] and rangeyy[1]<=j<rangeyy[2]:
            img[i][j]=0   

        if rangexx[5]<=i< rangexx[6] and rangeyy[1]<=j<rangeyy[2]:
            img[i][j]=0
#////////////////////////////////////////////////////////// soton 4 mesl i hay soton 2 
        if rangexx[0]<=i< rangexx[1] and rangeyy[2]<=j<rangeyy[3]:
            img[i][j]=0

        if rangexx[2]<=i< rangexx[3] and rangeyy[2]<=j<rangeyy[3]:
            img[i][j]=0

        if rangexx[4]<=i< rangexx[5] and rangeyy[2]<=j<rangeyy[3]:
            img[i][j]=0   

        if rangexx[6]<=i< rangexx[7] and rangeyy[2]<=j<rangeyy[3]:
            img[i][j]=0
#////////////////////////////////////////////////////////// soton 5 mesl i hay soton 1 
        if i<= rangexx[0] and rangeyy[3]<=j<rangeyy[4]:
            img[i][j]=0

        if rangexx[1]<=i< rangexx[2] and rangeyy[3]<=j<rangeyy[4]:
            img[i][j]=0

        if rangexx[3]<=i< rangexx[4] and rangeyy[3]<=j<rangeyy[4]:
            img[i][j]=0   

        if rangexx[5]<=i< rangexx[6] and rangeyy[3]<=j<rangeyy[4]:
            img[i][j]=0
#////////////////////////////////////////////////////////// soton 6 mesl i hay soton 2
        if rangexx[0]<=i< rangexx[1] and rangeyy[4]<=j<rangeyy[5]:
            img[i][j]=0

        if rangexx[2]<=i< rangexx[3] and rangeyy[4]<=j<rangeyy[5]:
            img[i][j]=0

        if rangexx[4]<=i< rangexx[5] and rangeyy[4]<=j<rangeyy[5]:
            img[i][j]=0   

        if rangexx[6]<=i< rangexx[7] and rangeyy[4]<=j<rangeyy[5]:
            img[i][j]=0
#////////////////////////////////////////////////////////// soton 7 mesl i hay soton 1 
        if i<= rangexx[0] and rangeyy[5]<=j<rangeyy[6]:
            img[i][j]=0

        if rangexx[1]<=i< rangexx[2] and rangeyy[5]<=j<rangeyy[6]:
            img[i][j]=0

        if rangexx[3]<=i< rangexx[4] and rangeyy[5]<=j<rangeyy[6]:
            img[i][j]=0   

        if rangexx[5]<=i< rangexx[6] and rangeyy[5]<=j<rangeyy[6]:
            img[i][j]=0
#////////////////////////////////////////////////////////// soton 8 mesl i hay soton 2
        if rangexx[0]<=i< rangexx[1] and rangeyy[6]<=j<rangeyy[7]:
            img[i][j]=0

        if rangexx[2]<=i< rangexx[3] and rangeyy[6]<=j<rangeyy[7]:
            img[i][j]=0

        if rangexx[4]<=i< rangexx[5] and rangeyy[6]<=j<rangeyy[7]:
            img[i][j]=0   

        if rangexx[6]<=i< rangexx[7] and rangeyy[6]<=j<rangeyy[7]:
            img[i][j]=0
#//////////////////////////////////////////////////////////////////  white  /////////////////////////////////////////////////////////

        if rangexx[0]<=i< rangexx[1] and j<=rangeyy[0]:
            img[i][j]=255

        if rangexx[2]<=i< rangexx[3] and j<=rangeyy[0]:
            img[i][j]=255

        if rangexx[4]<=i< rangexx[5] and j<=rangeyy[0]:
            img[i][j]=255

        if rangexx[6]<=i< rangexx[7] and j<=rangeyy[0]:
            img[i][j]=255 
#////////////////////////////////////////////////////////// soton 2
        if i<= rangexx[0] and rangeyy[0]<=j<rangeyy[1]:
            img[i][j]=255

        if rangexx[1]<=i< rangexx[2] and rangeyy[0]<=j<rangeyy[1]:
            img[i][j]=255

        if rangexx[3]<=i< rangexx[4] and rangeyy[0]<=j<rangeyy[1]:
            img[i][j]=255 

        if rangexx[5]<=i< rangexx[6] and rangeyy[0]<=j<rangeyy[1]:
            img[i][j]=255
#////////////////////////////////////////////////////////// soton 3 mesl i hay soton 1 
        if rangexx[0]<i<= rangexx[1] and rangeyy[1]<=j<rangeyy[2]:
            img[i][j]=255

        if rangexx[2]<=i< rangexx[3] and rangeyy[1]<=j<rangeyy[2]:
            img[i][j]=255

        if rangexx[4]<=i< rangexx[5] and rangeyy[1]<=j<rangeyy[2]:
            img[i][j]=255 

        if rangexx[6]<=i< rangexx[7] and rangeyy[1]<=j<rangeyy[2]:
            img[i][j]=255
#////////////////////////////////////////////////////////// soton 4 mesl i hay soton 2
        if i<= rangexx[0] and rangeyy[2]<=j<rangeyy[3]:
            img[i][j]=255

        if rangexx[1]<=i< rangexx[2] and rangeyy[2]<=j<rangeyy[3]:
            img[i][j]=255

        if rangexx[3]<=i< rangexx[4] and rangeyy[2]<=j<rangeyy[3]:
            img[i][j]=255

        if rangexx[5]<=i< rangexx[6] and rangeyy[2]<=j<rangeyy[3]:
            img[i][j]=255
#////////////////////////////////////////////////////////// soton 5 mesl i hay soton 1 
        if rangexx[0]<i<= rangexx[1] and rangeyy[3]<=j<rangeyy[4]:
            img[i][j]=255

        if rangexx[2]<=i< rangexx[3] and rangeyy[3]<=j<rangeyy[4]:
            img[i][j]=255

        if rangexx[4]<=i< rangexx[5] and rangeyy[3]<=j<rangeyy[4]:
            img[i][j]=255 

        if rangexx[6]<=i< rangexx[7] and rangeyy[3]<=j<rangeyy[4]:
            img[i][j]=255
#////////////////////////////////////////////////////////// soton 6 mesl i hay soton 2
        if i<= rangexx[0] and rangeyy[4]<=j<rangeyy[5]:
            img[i][j]=255

        if rangexx[1]<=i< rangexx[2] and rangeyy[4]<=j<rangeyy[5]:
            img[i][j]=255

        if rangexx[3]<=i< rangexx[4] and rangeyy[4]<=j<rangeyy[5]:
            img[i][j]=255

        if rangexx[5]<=i< rangexx[6] and rangeyy[4]<=j<rangeyy[5]:
            img[i][j]=255
#////////////////////////////////////////////////////////// soton 7 mesl i hay soton 1 
        if rangexx[0]<i<= rangexx[1] and rangeyy[5]<=j<rangeyy[6]:
            img[i][j]=255

        if rangexx[2]<=i< rangexx[3] and rangeyy[5]<=j<rangeyy[6]:
            img[i][j]=255

        if rangexx[4]<=i< rangexx[5] and rangeyy[5]<=j<rangeyy[6]:
            img[i][j]=255 

        if rangexx[6]<=i< rangexx[7] and rangeyy[5]<=j<rangeyy[6]:
            img[i][j]=255
#////////////////////////////////////////////////////////// soton 8 mesl i hay soton 2
        if i<= rangexx[0] and rangeyy[6]<=j<rangeyy[7]:
            img[i][j]=255

        if rangexx[1]<=i< rangexx[2] and rangeyy[6]<=j<rangeyy[7]:
            img[i][j]=255

        if rangexx[3]<=i< rangexx[4] and rangeyy[6]<=j<rangeyy[7]:
            img[i][j]=255

        if rangexx[5]<=i< rangexx[6] and rangeyy[6]<=j<rangeyy[7]:
            img[i][j]=255

      

cv2.imwrite('new1.1.png',img)
cv2.imshow('new1.1.png',img)
cv2.waitKey()
