import serial

# Ouvrir une connexion série
ser = serial.Serial('COM4', 9600)

# Envoyer une commande
ser.write(b'8H')