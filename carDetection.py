import cv2

# imgFile = './car2.jpg'
# img = cv2.imread(imgFile)

trainedData = './cars.xml'
carDetector = cv2.CascadeClassifier(trainedData)

videoCapture = cv2.VideoCapture('./testvideo.mp4')


while True:
    ret, frame = videoCapture.read()

    if ret:
        grayscaled = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break
    
    carCoordinates = carDetector.detectMultiScale(grayscaled)


    for i in range(len(carCoordinates)):
        (x, y, w, h) = carCoordinates[i]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2) # imgfile, coordinates1, coordinates2, color, thickness
        # print("x: ", x, "y: ", y, "width from offset: ", w, "height from offset: ", h)


    cv2.imshow('Video', frame) #display
    # cv2.waitKey(1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

videoCapture.release()
cv2.destroyAllWindows()





print("Tyler's car detection")