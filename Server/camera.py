import cv2
#debut de la capture de video avec la webcam
video=cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    check, frame = video.read()
    #affichage de la capture
    cv2.imshow("Webcam", frame)
    #on quitte quand on appuie la touche "q"
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

video.release()

cv2.destroyAllWindows()