import cv2
import numpy as np


film=cv2.VideoCapture(0)
sticker=cv2.imread('sticker1.png')
#sticker2=cv2.imread('st1.png')
sticker2=cv2.imread('st3.png')
smilest=cv2.imread('smile.jpg')
eyest=cv2.imread('eye.jpg')
#eye2st=cv2.imread('st2.png')

face_detector = cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_frontalface_default.xml")
smile_detector=cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_smile.xml")
eye_detector=cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_eye.xml")


while True:
    ret , frame=film.read()

    if ret==False:
        break


    frame=cv2.resize(frame,(400,550)) #taghir size 
    #frame_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  # sefid o siah


    faces = face_detector.detectMultiScale(frame ,1.5)
    smile=smile_detector.detectMultiScale(frame ,1.5)
    eye=eye_detector.detectMultiScale(frame ,1.5)
    

    for x , y , w , h in faces:
    
        cv2.rectangle(frame , (x,y) , (w+x,h+y) , (0,255,0) , 4)



        cv2.rectangle(frame , (x,y) , (w+x,h+y) , (0,255,0) , 4)
        sticker_resized = cv2.resize(sticker2 , (w,h))
        frame[y:y+h,x:x+w] = sticker_resized
        
       #####  censor  #####


        cv2.rectangle(frame , (x,y) , (w+x,h+y) , (0,255,0) , 4)
        select = frame[y:y+h, x:x+w]
        # applying a gaussian blur over this new rectangle area
        select = cv2.GaussianBlur(select, (49, 49), 30)
        # impose this blurred image on original image to get final image
        frame[y:y+select.shape[0], x:x+select.shape[1]] = select



       #####  emoji  #####

        for (sx, sy, sw, sh) in smile:
            cv2.rectangle(frame, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255),1)
            sticker_resized = cv2.resize(smilest , (sw,sh))
            frame[sy:sy+sh,sx:sx+sw] = sticker_resized
            


        for (ex, ey, ew, eh) in eye:
            cv2.rectangle(frame, (ex, ey), ((ex + ew), (ey + eh)), (0, 0, 255), 1)
            sticker_resized = cv2.resize(eyest , (ew,eh))
            frame[ey:ey+eh,ex:ex+ew] = sticker_resized  
              


    cv2.imshow('video',frame)
    cv2.waitKey(10) #time midim ke chand saniye be saniye avaz kone frame ra 
    
