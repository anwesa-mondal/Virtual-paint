import cv2

faceCascade=cv2.CascadeClassifier(r"C:\Users\ANWESA\PycharmProjects\pythonProject\haarcascade_frontalface_default.xml")

cap=cv2.VideoCapture(0)
cap.set(3,720)
cap.set(4,540)
cap.set(10,100)

while True:
    success,img=cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(img, "Face", (x + (w // 2) - 10, y - 10), cv2.FONT_HERSHEY_PLAIN, 1, 255)
        cv2.imshow("Paint On Face", img)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break