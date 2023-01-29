from serial import *
import tkinter
#from pyfirmata import Arduino

serie=Serial('COM4',9600)
#broche=Arduino('COM4', 13)
#pin13=serie.get_pin('d:13:o')

fenetre = tkinter.Tk()
fenetre.title("Interface graphique Arduino")
fenetre.geometry("200x150")

def ledOn():
   serie.write(b'H')

def ledOff():
    serie.write(b'L')

bouton1=tkinter.Button(fenetre, text="LED On", command=ledOn )
bouton1.grid(column=1, row=0)

bouton2=tkinter.Button(fenetre, text="LED Off", command=ledOff)
bouton2.grid(column=1, row=1)

fenetre.mainloop()
serie.close()