import atexit
import time
import random
from pathlib import Path
import nn

import cv2
import numpy as np
# import yolopy



minb, ming, minr, maxb, maxg, maxr = 22, 67, 96, 255, 255, 255
AREA  = False
once = True

find_truba = False
find_dtp = True
find_people = True


DIST_METER = 1825  # ticks to finish 1m
CAR_SPEED = 1630
THRESHOLD = 200
CAMERA_ID = '/dev/video0'
ARDUINO_PORT = '/dev/ttyUSB0'

GO = 'GO'
STOP = 'STOP'
CROSS_STRAIGHT = 'CROSS_STRAIGHT'
CROSS_RIGHT = 'CROSS_RIGHT'
CROSS_LEFT = 'CROSS_LEFT'
_CROSS_LEFT_STRAIGHT = '_CROSS_LEFT_STRAIGHT'
_CROSS_LEFT_LEFT = '_CROSS_LEFT_LEFT'
_CROSS_LEFT_STRAIGHT_AGAIN = '_CROSS_LEFT_STRAIGHT_AGAIN'

PREV_SUBSTATE = None
SUBSTATE = None

START_ACTION = False

STATE = GO
PREV_STATE = None

# cap = find_camera(fourcc="MJPG", frame_width=1280, frame_height=720)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

if not cap.isOpened():
    print('[ERROR] Cannot open camera ID:', CAMERA_ID)
    quit()


while True:
    # start_time = time.time()
    ret, frame = cap.read()
    # end_frame = time.time()
    if not ret:
        break
    
    orig_frame = frame.copy()
    unloading_area = frame.copy()
    
    if nn.find_people(unloading_area) and find_people:
        print("Detect people")
        STATE = STOP



    hsv = cv2.cvtColor(unloading_area, cv2.COLOR_BGR2HSV)
    
    mask_truba = cv2.inRange(hsv,(82, 189, 70), (255, 255, 255))
    mask_dtp = cv2.inRange(hsv,(0, 84, 206), (187, 255, 255))

    h = mask_truba.shape[0]
    w= mask_truba.shape[1]

    truba = np.sum(mask_truba[h//2: h, w//2: w])
    print(truba)

    dtp = np.sum(mask_dtp[h//2: h, w//2: w])
    print(dtp)

    if truba > 8_000_000 and find_truba:
        ZNAK = True
        STATE = STOP
        print("TRUBA")

    if dtp > 4_000_000 and find_dtp:
        DTP = True
        STATE = STOP
        print("DTP")
    

   