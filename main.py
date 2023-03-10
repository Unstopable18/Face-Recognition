import cv2
import os
import pickle
import face_recognition
import numpy as np

cap=cv2.VideoCapture(1)
cap.set(3,640)
cap.set(4,480)

imgBackground=cv2.imread("D:\Python\Face-Recognition\Resources\\background.png")
folderModePath="D:\Python\Face-Recognition\Resources\Modes"
modePathList=os.listdir(folderModePath)
# print(modePathList)
imgPathList=[]
for path in modePathList:
    imgPathList.append(cv2.imread(os.path.join(folderModePath,path)))
# print(len(imgPathList))

print("Loading Encode File....")
file=open('D:\Python\Face-Recognition\Encode.p','rb')
encodeListKnownWithIds=pickle.load(file)
file.close()
encodeListKnown,studId=encodeListKnownWithIds
# print(studId)
print("Encode File Loaded")

while True:
    success, img=cap.read()
    imgS=cv2.resize(img,(0,0),None,0.25,0.25)
    imgS=cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)

    faceCurrrentFrame=face_recognition.face_locations(imgS)
    encodeCurrentFrame=face_recognition.face_encodings(imgS,faceCurrrentFrame)

    imgBackground[162:162+480,55:55+640]=img
    imgBackground[44:44+633,808:808+414]=imgPathList[0]

    for encodeFace,faceLoc in zip(encodeCurrentFrame,faceCurrrentFrame):
        print('........')
        faceMatches=face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDist=face_recognition.face_distance(encodeListKnown,encodeFace)
        # print('faceMatches',faceMatches)
        # print('faceDist',faceDist)
        matchIndex=np.argmin(faceDist)
        # print("Match Index",matchIndex)
        if faceMatches[matchIndex]:

            print("Known Face Detected\n",studId[matchIndex])
        else:
            print("Unknown Face Detected XXXXXXXXXXX")
        

    #cv2.imshow('Web Cam',img)
    cv2.imshow('Face attendance',imgBackground)
    cv2.waitKey(1)
