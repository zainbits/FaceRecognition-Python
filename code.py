import cv2

def getimage(value):
    data = cv2.CascadeClassifier("recdata.xml")
    img=cv2.imread(value)
    grayimage = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=data.detectMultiScale(grayimage, scaleFactor=1.05, minNeighbors=5)
    for x, y, w, h in faces:
        img=cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
