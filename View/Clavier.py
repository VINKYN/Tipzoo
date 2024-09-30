from tkinter import *
from tkinter import simpledialog

def enumerate_row_column(iterable, num_cols):
    for idx, item in enumerate(iterable):
        row = idx // num_cols
        col = idx % num_cols
        yield row,col,item

class NumpadEntry(Entry):
    def __init__(self,parent=None,**kw):
        Entry.__init__(self,parent,**kw)
        self.bind('<FocusIn>',self.numpadEntry)
        self.bind('<FocusOut>',self.numpadExit)
        self.edited = False
    def numpadEntry(self,event):
        if self.edited == False:
            self['bg']= 'white'
            self.edited = True
            new = numPad(self)
        else:
            self.edited = False
    def numpadExit(self,event):
        self['bg']= 'white'

    

class numPad(simpledialog.Dialog):
    def __init__(self,master=None,textVariable=None):
        self.top = Toplevel(master=master)
        self.top.configure(bg='white')
        self.top.protocol("WM_DELETE_WINDOW",self.ok)
        self.createWidgets()
        self.master = master

        

        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        
        # Calculez les coordonnées du coin supérieur gauche pour centrer la fenêtre du clavier numérique
        pad_width = 300  # Largeur du clavier numérique
        pad_height = 320  # Hauteur du clavier numérique
        x = (screen_width - pad_width) // 2
        y = (screen_height - pad_height) // 2
        
        # Placez le clavier numérique à ces coordonnées
        self.top.geometry(f"{pad_width}x{pad_height}+{x}+{y}")

        self.top.bind('<Return>', self.ok)
        master.bind('<KeyPress-Return>', self.close_on_enter)
        
        
    def createWidgets(self):

        font_button = ("Helvetica  9 bold" )

        color_police ='#1b1b1b'
        color_button = '#F2E2CE'

        btn_list = ['7',  '8',  '9','Close', '4',  '5',  '6','Del', '1',  '2',  '3','Ent', '-',  '0',  '.','/']
        # create and position all buttons with a for-loop
        btn = []
        # Use custom generator to give us row/column positions
        for r,c,label in enumerate_row_column(btn_list,4):
            
            # partial takes care of function and argument
            cmd = lambda x = label: self.click(x)
            # create the button
            cur = Button(self.top, text=label, width=8, height=4, command=cmd,bg=color_button,bd=0,fg=color_police,font=font_button,
                         activebackground='#f0f0f0')
            if label == 'Close' or label=='Del' or label == 'Ent' :
                cur.configure(bg='#1b1b1b',fg='white')
            if label == '-' or label=='.' or label == '/' :
                cur.configure(bg='#b9e2f9')
            # position the button
            cur.grid(row=r, column=c,padx=5,pady=5)                                              
            btn.append(cur)
            
    def click(self,label):
        if label == 'Del':
            currentText = self.master.get()
            self.master.delete(0, END)
            self.master.insert(0, currentText[:-1])
        elif label == 'Close' or label=="Ent":
            self.ok()
        else:
            currentText = self.master.get()
            self.master.delete(0, END)
            self.master.insert(0, currentText+label)

    def close_on_enter(self, event):
        self.ok(event)
        
    def ok(self,event=None):
        self.top.destroy()


