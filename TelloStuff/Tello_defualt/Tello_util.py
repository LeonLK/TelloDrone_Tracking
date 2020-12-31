from djitellopy import Tello
from cv2 import cv2

def initTello():
    t = Tello()
    t.connect()
    t.fb_vel = 0  #forward,backward velocity
    t.lr_vel = 0  #left, right velocity
    t.ud_vel = 0  #up, down veloicty
    t.yaw = 0     #yaw angle
    t.speed = 0   #speed
    print(t.get_battery())
    print("hello")
    t.streamoff()
    t.streamon()
    return t

def getFrame(t,w = 360, h = 240):
    myFrame = t.get_frame_read()
    myFrame = myFrame.frame
    img = cv2.resize(myFrame,(w,h))
    return img
