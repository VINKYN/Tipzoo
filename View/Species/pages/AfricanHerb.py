from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk


class AfricanHerb(Frame):
    def __init__(self, master=None, variable=None,controller= None):
        super().__init__(master)
        self.master = master
        self.configure(bg='#D9D9D9')
        self.pack(expand=True, fill='both')
        self.controller = controller
        self.VarSpecies = variable

        listeCat = ['MAM1', 'MAM2', 'MAM2/3', 'MAM3', 'MAM4', 'MAM4/5', 'MAM5']
        
        listeMAM1 = ['MAD', 'NEO', 'CEPH', 'RAPHI', 'OREO', 'SYLVI', 'OURE', 'SBOV']
        listeMAM1Label = ['Madoqua sp.', 'Neotragus sp.', 'Cephalophus sp.', 'Raphicerus sp.', 'Oreotragus sp.', 'Sylvicapra sp.', 'Ourebia sp.', 'Small bovid']

        listeMAM2 = ['ANTID', 'REDUN', 'PELE', 'AEPY']
        listeMAM2Label = ['Antidorcas sp.', 'Redunca sp.', 'Pelea sp.','Aepyceros sp.']

        listeMAM23 = ['KOB', 'TRAG', 'DAM', 'MALC', 'SUID', 'MBOV'] 
        listeMAM23Label = ['Kobus sp.', 'Tragelaphus sp.', 'Damaliscus sp.', 'Medium alcelaphines!', 'Suidae', 'Medium bovid']

        listeMAM3 = ['ALCE', 'CONNO', 'HIPPOT', 'EQUID']
        listeMAM3Label= ['Alcelaphus sp.', 'Connochaetes sp.', 'Hippotragus sp.', 'Equus sp.']

        listeMAM4 =['SYNC','TAURO','LBOV']
        listeMAM4Label=['Syncerus sp.', 'Taurotragus sp.', 'Large bovid']

        listeMAM45 = ['RHINO', 'Hippop', 'GIRAF']
        listeMAM45Label=['Rhinocerotidae', 'Hippopotamidae', 'Giraffidae']

        listeMAM5 = ['PROBO']
        listeMAM5Label =['Proboscidea']


        self.tabMAM = ttk.Notebook(self, style='TNotebook')


        # Création et ajout des onglets pour chaque catégorie
        for i in listeCat:
            self.frame_cat = Frame(self.tabMAM, bd=1, relief=SOLID, bg='white')
            self.frame_cat.pack(expand=True, fill=BOTH, padx=10, pady=10)
            
            if i == 'MAM1':
                for id, s in enumerate(listeMAM1):
                    self.frameMA1 = Frame(self.frame_cat, bg='white')
                    self.frameMA1.pack(anchor='w',fill='y',expand=True)
                    self.radio_svert = Radiobutton(self.frameMA1, text=s, value=s,
                                              variable=self.VarSpecies, font=("Roboto 12"), bg="white",
                                              command=lambda val = s :self.controller.updateTaxon(val))
                    self.radio_svert.pack(side=LEFT)

                    self.label_svert = Label(self.frameMA1, text=listeMAM1Label[id], font=("Roboto 12"), 
                                        bg="white", fg='#45464b')
                    self.label_svert.pack(side=LEFT)


            if (i == 'MAM2'):
                for id,m2 in enumerate(listeMAM2):
                    self.Framem2 = Frame(self.frame_cat,bg='white')
                    self.Framem2.pack(anchor='w',fill='y',expand=True)
                    self.RadioM2 = Radiobutton(self.Framem2, text=m2, value=m2,
                                                   variable=self.VarSpecies, font=("Roboto 12"), bg="white",
                                                    command=lambda val = m2 :self.controller.updateTaxon(val))
                    self.RadioM2.pack(side=LEFT)

                    self.Labelm2 = Label(self.Framem2, text=listeMAM2Label[id], font=("Roboto 12"),
                                            bg="white",fg='#45464b')
                    self.Labelm2.pack(side=LEFT)

            if (i == 'MAM2/3'):
                for id,m23 in enumerate(listeMAM23):
                    self.Framem23 = Frame(self.frame_cat,bg='white')
                    self.Framem23.pack(anchor='w',fill='y',expand=True)
                    self.RadioM23 = Radiobutton(self.Framem23, text=m23, value=m23,
                                                  variable=self.VarSpecies, font=("Roboto 12"), bg="white",
                                                  command=lambda val = m23 :self.controller.updateTaxon(val))
                    self.RadioM23.pack(side=LEFT)

                    self.LabelM23 = Label(self.Framem23, text=listeMAM23Label[id], font=("Roboto 12"), 
                                           bg="white",fg='#45464b')
                    self.LabelM23.pack(side=LEFT)

            if (i == 'MAM3'):
                for id,m3 in enumerate(listeMAM3):
                    self.FrameM3 = Frame(self.frame_cat,bg='white')
                    self.FrameM3.pack(anchor='w',fill='y',expand=True)
                    self.RadioMAM3 = Radiobutton(self.FrameM3, text=m3, value=m3,
                                                   variable=self.VarSpecies, font=("Roboto 12"), bg="white",
                                                   command=lambda val = m3 :self.controller.updateTaxon(val))
                    self.RadioMAM3.pack(side=LEFT)

                    self.LabelM3 = Label(self.FrameM3, text=listeMAM3Label[id], font=("Roboto 12"), 
                                           bg="white",fg='#45464b')
                    self.LabelM3.pack(side=LEFT)


            if (i == 'MAM4'):
                for id,m4 in enumerate(listeMAM4[:3]):
                    self.FrameM4 = Frame(self.frame_cat,bg='white')
                    self.FrameM4.pack(anchor='w',fill='y',expand=True)
                    self.RadioMAM4 = Radiobutton(self.FrameM4, text=m4, value=m4,
                                                    variable=self.VarSpecies, font=("Roboto 12"), bg="white",
                                                    command=lambda val = m4 :self.controller.updateTaxon(val))
                    self.RadioMAM4.pack(side=LEFT)

                    self.LabelM4 = Label(self.FrameM4, text=listeMAM4Label[id], font=("Roboto 12"), 
                                           bg="white",fg='#45464b')
                    self.LabelM4.pack(side=LEFT)


            if (i == 'MAM4/5'):
                for id,m45 in enumerate(listeMAM45):
                    self.FrameM45 = Frame(self.frame_cat,bg='white')
                    self.FrameM45.pack(anchor='w',fill='y',expand=True)
                    self.RadioMAM45 = Radiobutton(self.FrameM45, text=m45, value=m45,
                                                   variable=self.VarSpecies, font=("Roboto 12"), bg="white",
                                                   command=lambda val = m45 :self.controller.updateTaxon(val))
                    self.RadioMAM45.pack(side=LEFT)

                    self.LabelM45 = Label(self.FrameM45, text=listeMAM45Label[id], font=("Roboto 12"), 
                                           bg="white",fg='#45464b')
                    self.LabelM45.pack(side=LEFT)


            if (i == 'MAM5'):
                for id,m5 in enumerate(listeMAM5):
                    self.FrameM5 = Frame(self.frame_cat,bg='white')
                    self.FrameM5.pack(anchor='w',fill='y',expand=True)
                    self.RadioMAM5 = Radiobutton(self.FrameM5, text=m5, value=m5,
                                                   variable=self.VarSpecies, font=("Roboto 12"), bg="white",
                                                   command=lambda val = m5 :self.controller.updateTaxon(val))
                    self.RadioMAM5.pack(side=LEFT)

                    self.LabelM5 = Label(self.FrameM5, text=listeMAM5Label[id], font=("Roboto 12"), 
                                           bg="white",fg='#45464b')
                    self.LabelM5.pack(side=LEFT)


            self.tabMAM.add(self.frame_cat, text=i)
            

        self.tabMAM.pack(expand=True, fill='both')



