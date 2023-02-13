import cv2

# Pribavljanje konkretnog klassifiera koji nam je potreban za detekciju lica.
# https://github.com/opencv/opencv/tree/master/data/haarcascades
faceClassifier = cv2.CascadeClassifier('C:/Users/Petar/Desktop/haarcascade_frontalface_default.xml')

def faceDetector(image):
    # Pretvaranje slike u sivu radi lakseg poredjenja
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Poslednja dva parametra zelimo da drzimo na zadatke vrednosti
    faces = faceClassifier.detectMultiScale(gray, 1.3, 5)
    # Funkcija vraca broj detektovanih lica kao Tuple
    # Ako je Tuple prazan vraticemo samo tu sliku
    # Ako nije nacrtacemo pravougaonik oko lica
    if len(faces) == 0:
        return image
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x,y), (x + w, y + h), (255, 0, 0), 2)
    return image


cap = cv2.VideoCapture(0)
# Funkcija vraca dva parametra
# ret da li je kamera detektovana
# frame konkretan frame uhvacen od kamere
ret, frame = cap.read()
if ret:
    print("Kamera uspesno detektovana")
else:
    print("Kamera nije detektovana :()")
while True:
    ret, frame = cap.read()
    if ret: 
        # Ako je kamera detektovana, poslacemo taj konkretan frame funkciji
        # A funkcija ce da vrati sliku sa pravougaonikom ako je detektovano lice
        cv2.imshow("Face And Eye detection", faceDetector(frame))
    # Ako se detektuje da je pritisnut enter prekinuti program
    if cv2.waitKey(1) == 13:
        break
# Unistiti sva prozora koja su aktivna
cv2.destroyAllWindows()