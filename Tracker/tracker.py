import socket
import os
import cv2
import mediapipe
import time
from mss import mss
from PIL import Image
from handDetector import HandDetector
import math
import numpy as np
loop = True
#create mediapipe tools
drawingModule = mediapipe.solutions.drawing_utils
handsModule = mediapipe.solutions.hands
bounding_box = {'top': -200, 'left': -200, 'width': 5000, 'height': 5000}
sct = mss()
ClientSocket = socket.socket()
#start trying to communicate with the server 
host = '10.0.0.13'
port = 8080
print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
   print(str(e))
Response = ClientSocket.recv(1024)
#analyze the video coming from the raspberry pi 
capture = cv2.VideoCapture('http://10.0.0.27:8000/stream.mjpg')
#set mediapipe settings to defaults 
ret, fram = capture.read()
(h, w) = fram.shape[:2]
(cX, cY) = (w // 2, h // 2)
# rotate our image by 45 degrees around the center of the image
M = cv2.getRotationMatrix2D((cX, cY), 180, 1.0)
frame = cv2.warpAffine(fram, M, (w, h))
frameWidth = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frameHeight = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
handDetector = HandDetector(min_detection_confidence=0.7)
with handsModule.Hands(static_image_mode=False, min_detection_confidence=0.7, min_tracking_confidence=0.7, max_num_hands=2) as hands:
    xCoord = 0
    yCoord = 0
    count = 0
    pixelCoordinatesLandmark = (0, 0)
    pixelCoordinatesLandmark1 = (0, 0)
    count1 = 0
    change = False
    fist = 0
    while (True):
        #send the hand position from previous frame or if hand goes out of frame, send the last known position
        try:
            xCoord = int(pixelCoordinatesLandmark[0]) + 100
            yCoord = int(pixelCoordinatesLandmark[1]) + 100
        except:
            xCoord = xCoord 
            yCoord = yCoord
        if(change == True):
            pixelCoordinatesLandmark1 = pixelCoordinatesLandmark
            count1 = count
            change = False
        else:
            change = True
        data = ("pi" + "(" + str(xCoord) + ", " + str(yCoord) + str(fist))
        fist = 0
        ClientSocket.send(str.encode(data))
        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            cv2.destroyAllWindows()
            break
        ret, rotated_image = capture.read()
        results = hands.process(cv2.cvtColor(rotated_image, cv2.COLOR_BGR2RGB))
         #analyze the frame with mediapipe tools
        if results.multi_hand_landmarks != None:
            for handLandmarks in results.multi_hand_landmarks:
                x = 0
                for point in handsModule.HandLandmark:
                    #draw each tracking point on the frame
                    normalizedLandmark = handLandmarks.landmark[point]
                    pixelCoordinatesLandmark = drawingModule._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, frameWidth, frameHeight)
                    cv2.circle(rotated_image, pixelCoordinatesLandmark, 5, (0, 255, 0), -1)
        #display the final image
        cv2.imshow('Test hand', rotated_image)
        if cv2.waitKey(1) == 27:
            break
        status, image = capture.read()
        handLandmarks = handDetector.findHandLandMarks(image=image, draw=True)
        count=0
        #figure out which finger is up
        if(len(handLandmarks) != 0):
 
            if handLandmarks[4][3] == "Right" and handLandmarks[4][1] > handLandmarks[3][1]:       #Right Thumb
                count = count+1
            elif handLandmarks[4][3] == "Left" and handLandmarks[4][1] < handLandmarks[3][1]:       #Left Thumb
                count = count+1
            if handLandmarks[8][2] < handLandmarks[6][2]:       #Index finger
                count = count+1
            if handLandmarks[12][2] < handLandmarks[10][2]:     #Middle finger
                count = count+1
            if handLandmarks[16][2] < handLandmarks[14][2]:     #Ring finger
                count = count+1
            if handLandmarks[20][2] < handLandmarks[18][2]:     #Little finger
                count = count+1
        #if none of the fingers are up, send fist command
        try:
            if(((pixelCoordinatesLandmark[0] - pixelCoordinatesLandmark1[0]) != 0)):
                fist = 1
            else:
                print("")
        except:
            print("")
ClientSocket.close()
cv2.destroyAllWindows()
capture.release()



