import cv2
import imageio
import os 
import random



backgorund_pic=cv2.imread('bg9.jpeg')

rows=backgorund_pic.shape[0]
cols=backgorund_pic.shape[1]

for j in range (50):

    backgorund_pic=cv2.imread('bg9.jpeg')
    for ii in range(75):
        cv2.circle(backgorund_pic, (random.randint(0,cols), random.randint(0,rows)),3, (255,255,255), -1)   

    cv2.imwrite(f'christmas_pic2/{j}.jpg' , backgorund_pic)


image_list = []
 
for file_name in os.listdir('christmas_pic2'):  #pic esm folder ke aksa onja hast 
    image=imageio.imread(f'christmas_pic2/{file_name}')  
    image_list.append(image)

 
# Convert to gif using the imageio.mimsave method
imageio.mimsave('christmas.gif', image_list, fps=70) #fps mishe taghir dad 
