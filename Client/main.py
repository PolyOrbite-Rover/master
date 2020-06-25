#Code de l'ordinateur qui donnera des ordres au rover et qui recevra des donnees du rover
import socket

#IP localhost a changer lorsqu'on saura l'IP du robot.
HOST = '127.0.0.1'
PORT = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('En attente de connexion...')
s.connect((HOST, PORT))

#TODO: code a modifier
s.send('Hello world')
data = s.recv(1024)

print('Message du serveur: ', repr(data))