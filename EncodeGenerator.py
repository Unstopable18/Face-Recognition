import cv2
import face_recognition
import pickle
import os

folderPath="D:\Python\Face-Recognition\Images"
pathList=os.listdir(folderPath)
# print(PathList)
imgList=[]
studId=[]
for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath,path)))
    studId.append(os.path.splitext(path)[0])
# print(len(imgList))
# print(studId)


def findEncodings(imageslist):
    encodeList=[]
    for img in imageslist:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode=face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

print('Encoding started.....')
encodeListKnown=findEncodings(imgList)
encodeListKnownWithIds=[encodeListKnown,studId]
# print(encodeListKnownWithIds)
print('Encoding Complete')

file=open('Encode.p','wb')
pickle.dump(encodeListKnownWithIds,file)
file.close()
print('File Saved.....')