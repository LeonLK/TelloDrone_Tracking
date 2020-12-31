from Tello_util import *
from cv2 import cv2

t = initTello()
w,h = 360,240
while True:
    '''
    Step 1: 
    '''
    img = getFrame(t,w,h)

    cv2.imshow('Image',img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        t.land()
        break
