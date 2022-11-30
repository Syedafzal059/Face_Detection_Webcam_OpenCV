#import the modules
import cv2 as cv
import os
 
print("Press 'D' to stop the Feed")


#making an instant for the classifier
haar_cascade = cv.CascadeClassifier(r"Q3\haarcascade_frontalface_default.xml")

#Selecting the webcam(0) to capture the video feed
capture = cv.VideoCapture(0)

#frame counter
frame_counts=0
while True:
    ifTrue, frame = capture.read()
    frame = cv.flip(frame,1)                                                                 #Fliping the frame Horizontally
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)                                             #Converting frame to gray scale
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor =1.1, minNeighbors=3)       #appliying the classifier
    for (x,y,w,h) in faces_rect:
        cv.rectangle(frame, (x,y), (x+w, y+h), color=(222,0,0), thickness=2)                 #Placing the rectangle on face location
        
       
    cv.putText(frame, str(frame_counts), (10,30), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0),2) #Placing the frame No. on the frame
    cv.imshow(f"Welcome! S M AFZAL Face Detector :) (Pess D => Stop) ",frame)
    cv.imwrite(fr"Q3\frames\frame_{frame_counts}.jpg",frame)                                 #Saving the frames in frame folder
    
    frame_counts=frame_counts+1 
    if cv.waitKey(20) & 0xFF ==ord("d"):    #press "D" to break the loop
        break

cv.waitKey(0)

