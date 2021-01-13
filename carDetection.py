import cv2

imgFile = 'https://www.gannett-cdn.com/-mm-/333c1271c2393e4d5375c5f38ce5fedd5ad275a2/c=0-122-2400-1478/local/-/media/2018/06/25/USATODAY/USATODAY/636655326420239659-PedestrianDeath-crossing-Gratiot2.jpg'

img = cv2.imread(imgFile)


cv2.imshow("Cars", img)


print("Tyler's car detection")