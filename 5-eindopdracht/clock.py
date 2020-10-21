# module importeren 
from tkinter import * 
from tkinter.ttk import *
  
 
#strftime-functie importeren en
# systeemtijd ophalen 
from time import strftime 
  
# maken van een tkinter window 
root = Tk() 
root.title('Clock') 
  
# Deze functie is er om tijd in het label de zetten
def time(): 
    string = strftime('%H:%M:%S %p') 
    lbl.config(text = string) 
    lbl.after(1000, time) 
  
# Het stylen van de klok 
lbl = Label(root, font = ('impact', 40, 'bold'), 
            background = 'green', 
            foreground = 'white') 
  
# De klok in het midden zetten
lbl.pack(anchor = 'center') 
time() 
  
mainloop() 