import serial 
import tkinter
import pyfirmata

serie=serial.Serial('COM4',9600)
broche=pyfirmata.Arduino('COM4', 13)
pin13=broche.get_pin('d:13:o')

fenetre = tkinter.Tk()
fenetre.title("Interface graphique Arduino")
fenetre.geometry("200x150")

def ledOn():
   pin13.write(1)

def ledOff():
    pin13.write(0)

bouton1=tkinter.Button(fenetre, text="LED On", command=ledOn )
bouton1.grid(column=1, row=0)

bouton2=tkinter.Button(fenetre, text="LED Off", command=ledOff)
bouton2.grid(column=1, row=1)

fenetre.mainloop()