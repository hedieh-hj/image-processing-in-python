import cv2
import cvzone
import numpy as np 



flag = 0

def change_face(frame,f):

    faces = face_detector.detectMultiScale(frame ,1.3)

    for (x , y , w , h) in faces:
        emoji_resized = cv2.resize(face_emoji , (w,h))
        frame = cvzone.overlayPNG(frame, emoji_resized, [x,y])
        
    f = 1

    return frame,f


def change_eyes(frame,f):

    faces = eyes_detector.detectMultiScale(frame ,1.1, minSize=(20,20),maxSize=(35,35))

    for (x , y , w , h) in faces:
        emoji_resized = cv2.resize(eyes_emoji , (w,h))
        frame = cvzone.overlayPNG(frame, emoji_resized, [x,y])
        
    f = 2

    return frame,f



def change_lips(frame,f):

    faces = lips_detector.detectMultiScale(frame , 1.34, 29)

    for (x , y , w , h) in faces:
        emoji_resized = cv2.resize(lips_emoji , (w,h))
        frame = cvzone.overlayPNG(frame, emoji_resized, [x,y])
        
    f = 3

    return frame,f


def blur_face(frame,f):

    faces = face_detector.detectMultiScale(frame , 1.2)

    for (x , y , w , h) in faces:

        image_blur = frame[y:y+h,x:x+w]
        image_blur = cv2.resize(image_blur,(int(w//10),int(h//10)))
        image_blur = cv2.resize(image_blur,(w,h))
        frame[y:y+h,x:x+w] = image_blur
        
    f = 4

    return frame,f


def opaque(frame,f,x,y):

    
    target=frame[x//2 -130 : x//2 +130 ,y//2 -150:y//2 +150 ]

    kernel=np.ones((45,45))/2025
    frame=cv2.filter2D(frame,-1,kernel)

    frame[x//2 -130 : x//2 +130 ,y//2 -150:y//2 +150 ]=target

    cv2.rectangle (frame, ( y//2 -150 ,x//2 -130 ),(y//2 +150 , x//2 +130 ),None,1)
   
    return frame,f



def blur_face2(frame,f,x1,y1):

    faces = face_detector.detectMultiScale(frame , 1.2)

    for (x , y , w , h) in faces:

        # #cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        select = frame[y:y+h, x:x+w]
        
        select = cv2.GaussianBlur(select, (49, 49), 30)
      
        frame[y:y+select.shape[0], x:x+select.shape[1]] = select       


     
    f = 6

    return frame,f



face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyes_detector = cv2.CascadeClassifier('haarcascade_eye.xml')
lips_detector = cv2.CascadeClassifier('haarcascade_smile.xml')

face_emoji = cv2.imread('emoji.png',cv2.IMREAD_UNCHANGED)
eyes_emoji = cv2.imread('eye2.png',cv2.IMREAD_UNCHANGED)
lips_emoji = cv2.imread('smile2.png',cv2.IMREAD_UNCHANGED)


vedio_cap = cv2.VideoCapture(0)

while 1:

    ret , frame = vedio_cap.read()

    if ret == False:
        break

    frame = cv2.resize(frame, (0, 0), fx=0.75 , fy=0.75)
    x,y,z=frame.shape
    #frame,flag =change_face(frame, flag)


    press = cv2.waitKey(1)
    if press == ord('0'):
        flag = 0
    if press == ord('7'):
        break
    if press == ord('1') or flag == 1:
        frame,flag = change_face(frame, flag)
    if press == ord('2') or flag == 2:
        frame, flag = change_eyes(frame, flag)
    if press == ord('3') or flag == 3:
        frame, flag = change_lips(frame, flag)
    if press == ord('4') or flag == 4:
        frame, flag = blur_face(frame, flag)
    if press == ord('5') or flag == 5:
        frame, flag = opaque(frame, flag,x,y)
    if press == ord('6') or flag == 6:
        frame, flag = blur_face2(frame, flag,x,y)       
    
    cv2.imshow('result', frame)
    
    




