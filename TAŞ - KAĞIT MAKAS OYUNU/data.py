import numpy as np
import cv2
import os
import sys

PATH = os.getcwd()+'\\'
cap = cv2.VideoCapture(0)

label = "scissor"

SAVE_PATH = os.path.join(PATH, label)

try:
    os.mkdir(SAVE_PATH)
except FileExistsError:
    pass

ct = 0
maxCt = 10
print("Hit Space to Capture Image")

while True:
    ret, frame = cap.read()
    cv2.imshow('Get Data : '+label,frame[50:350,150:450])
    if cv2.waitKey(1) & 0xFF == ord(' '):
        cv2.imwrite(SAVE_PATH+'\\'+label+'{}.jpg'.format(ct),frame[50:350,150:450])
        print(SAVE_PATH+'\\'+label+'{}.jpg Captured'.format(ct))
        ct+=1
    if ct >= maxCt:
        break

cap.release()
cv2.destroyAllWindows()