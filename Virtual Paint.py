import cv2
import numpy as np

cap=cv2.VideoCapture(0)
cap.set(3,480)
cap.set(4,640)
cap.set(10,100)
myColor=[[0 ,126, 0 ,179, 255, 255]]
myColorValues=[[0,204,0]]
#BGR
mypoints=[] #[x,y,colorId]



def drawoncanvas(myPoints,myColorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)


def getCountours(img):
    contours,Hiearchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h=0,0,0,0
    for cntr in contours:
        area=cv2.contourArea(cntr)
        print(area)
        if area>500:
            #cv2.drawContours(imgResult, cntr, -1, (255, 0,0 ), 2)
            peri=cv2.arcLength(cntr,True)
            print(peri)
            approx=cv2.approxPolyDP(cntr,0.02*peri,True)
            print(len(approx))
            objCor=len(approx)
            x,y,w,h=cv2.boundingRect(approx)
    return (x+w//2)+5,y


def findColor(img,myColor,myColorValues):
    count=0
    newpoints=[]
    for i in myColor:
        lower = np.array(i[0:3])
        upper = np.array(i[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x,y=getCountours(mask)
        cv2.circle(imgResult,(x,y),10,myColorValues[count],cv2.FILLED)
        if(x!=0) and (y!=0):
            newpoints.append([x,y,count])
        count+=1
        #cv2.imshow(str(i[0]),mask)
    return newpoints


while True:
    success,img=cap.read()
    img=cv2.flip(img,1)
    imgResult=img.copy() #imgContour
    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    newpoints=findColor(imgHSV,myColor,myColorValues)
    if len(newpoints)>0:
        for point in newpoints:
            mypoints.append(point)
    if len(mypoints)>0:
        drawoncanvas(mypoints,myColorValues)


    cv2.imshow('img',imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



