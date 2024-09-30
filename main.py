from tkinter import *
from Controller.HomeController import HomeController
from View.Home import HomeInterface
from tkinter.ttk import *
from Controller.Bulk import Bulk
from PIL import Image, ImageTk , ImageColor,ImageStat
from tkinter import colorchooser
import tkinter.ttk as ttk
from tkinter import messagebox
import os
import sqlite3
from collections import Counter
import pandas as pd
import datetime
from tkinter import simpledialog



def main():
    root = Tk()
    width = root.winfo_screenwidth()               
    height = root.winfo_screenheight()               
    root.geometry("%dx%d" % (width, height))

    root.title("TIPZOO")    
    icon = PhotoImage(file= 'View/img/icon.png')
    #root.iconbitmap("C:/Users/vince/OneDrive/Bureau/Tipzoo Vincent/View/img/tipzoo_icon.ico")
    root.iconphoto(False,icon)  
    bulk = Bulk()
    home_controller = HomeController(master=root,bulk=bulk)
    
    

    
    # Création de la vue principale en passant le contrôleur en tant qu'argument
    home_view = HomeInterface(master=root, controller=home_controller)

    root.mainloop()

if __name__ == "__main__":
    main()