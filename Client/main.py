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
from tkinter import *
from PIL import Image, ImageTk


import numpy as np
import cv2

#fonctions

#classes

#Initalisation de l'interface et des connexion
interface = Tk()
interface.wm_title("Interface du Rover")
interface.config(background="#FFFFFF")

#Initialisation du visionnement de la webcam dans l'interface
webcam_stream = Frame(interface, width=600, height=500)
webcam_stream.grid(row=0, column=0, padx=10, pady=2)

##define netgear client with `receive_mode = True` and default settings
client = NetGear(receive_mode = True)

window = Label(webcam_stream)
window.grid(row=0, column=0)

print("debut de stream dans le client...")
def show_stream():
    webcam_frame = client.recv()
    #webcam_frame = cv2.flip(webcam_frame, 1)
    #cv2image = cv2.cvtColor(webcam_frame, cv2.COLOR_BGR2RGBA)
    #img = Image.fromarray(cv2image)
    #imgtk = ImageTk.PhotoImage(image=img)
    window.imgtk = imgtk
    window.configure(image=imgtk)
    window.after(1, show_stream)

show_stream()
interface.mainloop()
"""
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

print("fin de stream provenant du serveur")
# close output window
cv2.destroyAllWindows()
"""
# safely close client
client.close()
print("fin de connexion cote client")