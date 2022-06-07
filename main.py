import cv2

capture = cv2.VideoCapture(0)
timeF = 25
i = 0

while True:
    ret, image = capture.read()
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    face_cascade = cv2.CascadeClassifier(r"haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.04, minNeighbors=25)
    for x, y, w, h in faces:
        img2 = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)
    if (i % timeF == 0):
        print(i)
    i = i + 1
    cv2.imshow('video', image)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

capture.release()

cv2.destroyAllWindows()
