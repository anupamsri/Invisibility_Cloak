# Invisibility_Cloak
hello guys,
During this LOCKDOWN of COVID19 i was so bored at home so i started seeing harry potter series and i was so amazed seen his invisible cloak so i thought to make make for me :)
As Being a harry potter fan in childhood and using an invisibility cloak are still dream of many Childrens. Well it turns out that using simple image processing tricks 
So this code turns a red colour cloth into an invisibility cloak :)
LETS TRY :0

# Requirements
* python 3.5 and above
* opencv
* numpy
* time

![alt-text](https://media.giphy.com/media/fADgaoX8gUp6tYWvQ7/giphy.gif)

>- It's a fun application which you will enjoy using.
>- You can learn some key functions of opencv from this project. 

##  This is how it works
This project aims to emulate an invisibility cloak like in Harry Potter.

1) Clone this project.

2) Run invisiblecloacode.py & get away from the screan so that it can record the area. 

3) Now come in front of the screen when the window pop out on your desktop.

4) Grab a red cloth and Let the magic begin !!

5) Congratulations!! You are now a wizard!!

6) Press q to quit on any of the open camera windows.


## Now Lets see the code:
- Install all requirement in python:
```
pip install opencv-contrib-python
```
The code has been written to recognize RED color as cloak for now.
```
lower_range = np.array([0,120,50])
higher_range = np.array([10,255,255])
```
You can change the color bound according to yourself.The color range for HSV value are available [here](http://colorizer.org/).Saturation range is [0,255] and Value range is [0,255]. Different softwares use different scales. So if you are comparing OpenCV values with them, you need to normalize these ranges.

- Masking is one of the key features for this project:
```
mask1 = cv2.inRange(hsv,lower_red,upper_red)
```
The above forms a mask of the area we want to make invisible to frame-feed.

- The next task is to extract the above mask from the frame,background and foreground.
```
#segmenting out cloth color
mask2 = cv2.inRange(hsv,lower_red,upper_red)

Addition of the two masks to generate the final mask.
mask = mask1+mask2
# first we will do EROSION then followed by dilation 
# we can do both this step by MORPH_OPEN or by mophologyEx
# purpose being to remove white noise and to mask the red color from cloak  
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5,5),np.uint8))

```
- This is now where the magic happens:
```
- Run code:- invisiblecloakcode.py
```
