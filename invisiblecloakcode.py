# Project - INVISIBLE CLOAK
# BY-ANUPAM SRIVASTAVA

'''
hello guys,
    During this LOCKDOWN of COVID19 i was so bored at home so i started 
    seeing harry potter series and i was so amazed 
    seen his invisible cloak so i thought to make make for me :)
    LETS TRY :0
    THEN-----------------
'''
# importing essential librarys
# importing opencv(cv2), Numpy array(numpy),time
import cv2 
import numpy as np
import time
print('Hey Guys lets get invisible.........')

'''
Syntax : cv2.putText(frame, Text, org, font, color, thickness)
Parameters:
frame: current running frame of the video.
Text: The text string to be inserted.
org: bottom-left corner of the text string
font: the type of font to be used.
color: the colour of the font.
thickness: the thickness of the font
'''
##reading from the webcam 
cap = cv2.VideoCapture(0)

## Allow the system to sleep for 3 seconds before the webcam starts
time.sleep(3)
background=0

## Capture the background in range of 30
for i in range(30):
    ret,background = cap.read()

background = np.flip(background,axis=1)

## Read every frame from the webcam, until the camera is open
while(cap.isOpened()):
	ret, img = cap.read()

    # Flipping the image
	img = np.flip(img,axis=1)
    # Converting image to HSV color space.
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	value = (35, 35)
	
	blurred = cv2.GaussianBlur(hsv, value,0)
	
	# Defining lower range for red color detection i.e Generating masks to detect red color
	lower_red = np.array([0,120,70])
	upper_red = np.array([10,255,255])
    #mask 1
	mask1 = cv2.inRange(hsv,lower_red,upper_red)
	
	# Defining upper range for red color detection
	lower_red = np.array([170,120,70])
	upper_red = np.array([180,255,255])
    #mask 2
	mask2 = cv2.inRange(hsv,lower_red,upper_red)
	
	# Addition of the two masks to generate the final mask.
	mask = mask1+mask2
	# first we will do EROSION then followed by dilation 
    # we can do both this step by MORPH_OPEN or by mophologyEx
    # purpose being to remove white noise and to mask the red color from cloak  
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5,5),np.uint8))
	
	# Replacing pixels corresponding to cloak with the background pixels.
	img[np.where(mask==255)] = background[np.where(mask==255)]
	cv2.imshow('Invisible cloak Window By-Anupam Srivastava',img)
	k = cv2.waitKey(10)
    # catpure key press escape so for that the key is 27.
	if k == 27:
		break

