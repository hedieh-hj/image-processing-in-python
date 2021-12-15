import numpy as np 
import cv2

cap=cv2.VideoCapture(0)

while True:

    ret , frame =cap.read()

    if  ret  == False:
        break

    x,y,z=frame.shape

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    target=frame[x//2 -180 : x//2 +180 ,y//2 -250:y//2 +250 ]

    kernel=np.ones((45,45))/2025
    frame=cv2.filter2D(frame,-1,kernel)

    frame[x//2 -180 : x//2 +180 ,y//2 -250:y//2 +250 ]=target

    cv2.rectangle (frame, ( y//2 -250 ,x//2 -180 ),(y//2 +250 , x//2 +180 ),None,1)

    x=np.average(target)

    if x < 50 :
        cv2.putText(frame,"Black",(10,40),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0))

    if x >50 and x<170:
        cv2.putText(frame,"Gray",(10,40),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0))

    if x  >= 170  :
        cv2.putText(frame,"White",(10,40),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0))

    


    cv2.imshow('result',frame)
    if cv2.waitKey(1) == ord('q'):
            break



