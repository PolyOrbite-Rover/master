#Code de l'ordinateur qui donnera des ordres au rover et qui recevra des donnees du rover
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
print('Message du serveur: ', repr(data))