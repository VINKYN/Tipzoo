from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk

class Treeview_haut(Frame):
    def __init__(self, master=None):
        super().__init__(master)

        font_ecriture =("Helvetica  10" )

        color_police ='#1b1b1b'

         # Création des en-têtes du tableau
        headers = ['ID', 'Taxon', 'Class', 'Anat', 'Side', 'Détail', 'Last Change']
        for col, header in enumerate(headers):
            label = Label(self, text=header,bg='#b9e2f9',font=font_ecriture,fg=color_police)
            label.grid(row=0, column=col,sticky='nsew')
            self.grid_columnconfigure(col, weight=1)

        # Données factices pour remplir le tableau
        contacts = [('bip', 'boup', 'bop','bang','bing','boung','bug')]

        # Ajout des données dans le tableau d'Entry
        for row, data in enumerate(contacts, start=1):
            for col, value in enumerate(data):
                entry = Entry(self)
                entry.insert(0, value)
                entry.configure(state='disabled', disabledbackground="white",font=font_ecriture)
               
                entry.grid(row=row, column=col, sticky='nsew',columnspan=len(headers))