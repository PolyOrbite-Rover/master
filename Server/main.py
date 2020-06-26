#Code du rover, qui recevra des ordres ou des demandes d'un ordinateur
import socket

#TODO: IP localhost a changer lorsqu'on saura l'IP du robot.
HOST = '127.0.0.1' 
PORT = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
print('En attente de connexion...')
s.listen(1)
connection, address = s.accept()
print('CONNEXION REUSSI AVEC : ', address)

while True:
    #rover recoit les demandes de l'ordinateur
    # TODO: code a modifier
    data = connection.recv(1024)
    if not data:
        break
    # envoie des images (video)
    # envoie d'informations
    # controle des moteurs (roues et bras)
    connection.send(data)
connection.close()