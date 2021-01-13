import cv2

imgFile = './carsss.jpg'

img = cv2.imread(imgFile)
trainedData = './cars.xml'




grayscaledImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
carDetector = cv2.CascadeClassifier(trainedData)

carCoordinates = carDetector.detectMultiScale(grayscaledImg)

for i in range(len(carCoordinates)):
    (x, y, w, h) = carCoordinates[i]
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2) # imgfile, coordinates1, coordinates2, color, thickness
    print("x: ", x, "y: ", y, "width from offset: ", w, "height from offset: ", h)



cv2.imshow("Cars", img)

cv2.waitKey()




print("Tyler's car detection")