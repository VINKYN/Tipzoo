from tkinter import Tk


class App(Tk):

       def __init__(self):
        super().__init__()

        width = self.winfo_screenwidth()               
        height = self.winfo_screenheight()               
        self.geometry("%dx%d" % (width, height))

        self.title("TIPZOO")
        self.iconbitmap("img/tipzoo_icon.ico")
