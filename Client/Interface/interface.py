from tkinter import *

class Interface(Frame):
    #fonction qui cree l'interface
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master = master
        self.init_interface()
    
    #fonction qui initialise les parametres de l'interface
    def init_interface(self):
        #titre
        self.master.title("Interface Rover")
        #taille de l'interface dans le root
        self.pack(fill=BOTH, expand=1)
        #creation d'un bouton
        quitButton = Button(self, text="Quitter", command=self.client_exit)
        #emplacement du bouton
        quitButton.place(x=0, y=0)

    def client_exit(self):
        exit()

root = Tk()
#taille du root
root.geometry("400x300")

app = Interface(root)

root.mainloop()