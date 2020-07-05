#Code de l'ordinateur qui donnera des ordres au rover et qui recevra des donnees du rover
"""
import socket

#TODO: IP localhost a changer lorsqu'on saura l'IP du robot.
HOST = '127.0.0.1'
PORT = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('En attente de connexion...')
s.connect((HOST, PORT))

#TODO: code a modifier
# demande de videos
# demande de donnees
# controle du robot a distance
## bras et roues
s.send('Hello world')
data = s.recv(1024)
#TODO envoyer les informations sur l'interface
print('Message du serveur: ', repr(data))""
"""

from vidgear.gears import NetGear
import cv2

#define netgear client with `receive_mode = True` and default settings
client = NetGear(receive_mode = True)

# infinite loop
while True:
    # receive frames from network
    frame = client.recv()

    # check if frame is None
    if frame is None:
        #if True break the infinite loop
        break

    # do something with frame here

    # Show output window
    cv2.imshow("Output Frame", frame)

    key = cv2.waitKey(1) & 0xFF
    # check for 'q' key-press
    if key == ord("q"):
        #if 'q' key-pressed break out
        break

# close output window
cv2.destroyAllWindows()
# safely close client
client.close()