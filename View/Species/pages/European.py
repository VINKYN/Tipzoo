from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk


class European(Frame):
    def __init__(self, master=None, variable=None,controller= None):
        super().__init__(master)
        self.master = master
        self.configure(bg='#D9D9D9')
        self.pack(expand=True, fill='both')
        self.controller = controller

        self.VarSpecies = variable

        listeCat = ['NID by size class', 'SVERT', 'SCAR', 'LCAR',
                    'MAM1', 'MAM2', 'MAM2/3', 'MAM3', 'MAM4', 'MAM4/5', 'MAM5']
        

        listeSvert = ['LAGO', 'LEP', 'ORY', 'MARM', 'CAST']

        listeSvertLabel = ['Lagomorpha', 'Lepus sp.', 'Orycto/agus sp.', 'Marmota sp.', 'Castor sp.']

        listeSCAR = ['SCARN', 'VULPI', 'VULPV', 'VULPA', 'MUST', 'MELES', 'LYNX', 'FELIS']

        listeSCARLabel = ['Small carnivorel', 'Vulpinae', 'Vulpes vulpes', 'Vulpes lagopusl', 'Mustelidae', 'Meles meles', 'Lynx sp.', 'Felis silvestris']

        listeLCAR = ['LCARB', 'LUP', 'CROC', 'PLEO', 'PPAR', 'URSI', 'URSS', 'URSA']

        listeLCARLabel = ['Large carnivore', 'Canis lupus', 'Crocuta crocuta', 'Panthera leo', 'Panthera pardus', 'Ursus sp.', 'Ursus spe/aeus', 'Ursus arctos']


        listeMAM1 = ['CAPREO', 'RUPI']
        
        listeMAM2 = ['RANG', 'CAPRA', 'SUS', 'DAMA', 'SAGA']

        listeMAM23 = ['CEL', 'HYDR']

        listeMAM3 = ['CAB', 'EQUID']

        listeMAM4 = ['BB', 'MEG']

        listeMAM5 = ['PROBO']

        listeMAM45 = ['RHINO']

        listeNid = ['MAMI', 'MAM2', 'MAM12', 'MAM3', 'MAM23', 'MAM4', 'MAM34', 'MAM5', 'MAM45']

        self.tabMAM = ttk.Notebook(self, style='TNotebook')
       

        for i in listeCat:
            self.frame_cat = Frame(self.tabMAM, bd=1, relief=SOLID, bg='white')
            self.frame_cat.pack(expand=True, fill=BOTH, padx=10)

            if (i == 'SVERT'):
                for id,s in enumerate(listeSvert):
                    self.FrameS = Frame(self.frame_cat,bg='white',padx=50)
                    self.FrameS.pack(anchor='w',fill='y',expand=True)
                    self.RadioSvert = Radiobutton(self.FrameS, text=s, value=s,
                                                   variable=self.VarSpecies, font=("Roboto 12"), bg="white",
                                                   command=lambda val = s :self.controller.updateTaxon(val))
                    self.RadioSvert.pack(side=LEFT)

                    self.LabelSvert = Label(self.FrameS, text=listeSvertLabel[id], font=("Roboto 12"), 
                                            bg="white",fg='#45464b')
                    self.LabelSvert.pack(side=LEFT)


            if (i == 'SCAR'):
                for id,sc in enumerate(listeSCAR):
                    self.FrameSc = Frame(self.frame_cat,bg='white')
                    self.FrameSc.pack(anchor='w',fill='y',expand=True,padx=50)
                    self.RadioSCAR = Radiobutton(self.FrameSc, text=sc, value=sc,
                                                   variable=self.VarSpecies, font=("Roboto 12"), bg="white",
                                                   command=lambda val = sc :self.controller.updateTaxon(val))
                    self.RadioSCAR.pack(side=LEFT)

                    self.LabelScar = Label(self.FrameSc, text=listeSCARLabel[id], font=("Roboto 12"),
                                            bg="white",fg='#45464b')
                    self.LabelScar.pack(side=LEFT)


            if (i == 'LCAR'):
                for id,lc in enumerate(listeLCAR):
                    self.FrameLC = Frame(self.frame_cat,bg='white')
                    self.FrameLC.pack(anchor='w',fill='y',expand=True,padx=50)
                    self.RadioLCAR = Radiobutton(self.FrameLC, text=lc, value=lc,
                                                  variable=self.VarSpecies, font=("Roboto 12"), bg="white",
                                                  command=lambda val = lc :self.controller.updateTaxon(val))
                    self.RadioLCAR.pack(side=LEFT)

                    self.LabelLcar = Label(self.FrameLC, text=listeLCARLabel[id], font=("Roboto 12"), 
                                           bg="white",fg='#45464b')
                    self.LabelLcar.pack(side=LEFT)

            if (i == 'MAM1'):
                for m1 in listeMAM1:
                    self.FrameM1 = Frame(self.frame_cat,bg='white')
                    self.FrameM1.pack(anchor='w',fill='y',expand=True,padx=50)
                    self.RadioMAM1 = Radiobutton(self.FrameM1, text=m1, value=m1,
                                                   variable=self.VarSpecies, font=("Roboto 12"), bg="white",
                                                   command=lambda val = m1 :self.controller.updateTaxon(val))
                    self.RadioMAM1.pack(side=LEFT)

            if (i == 'MAM2'):
                for m2 in listeMAM2:
                    self.FrameM2 = Frame(self.frame_cat,bg='white')
                    self.FrameM2.pack(anchor='w',fill='y',expand=True,padx=50)
                    self.RadioMAM2 = Radiobutton(self.FrameM2, text=m2, value=m2,
                                                   variable=self.VarSpecies, font=("Roboto 12"), bg="white",
                                                   command=lambda val = m2 :self.controller.updateTaxon(val))
                    self.RadioMAM2.pack(side=LEFT)

            
            if (i == 'NID by size class'):
                for nid in listeNid:
                    self.FrameNID = Frame(self.frame_cat,bg='white')
                    self.FrameNID.pack(anchor='w',fill='y',expand=True,padx=50)
                    self.RadioNID = Radiobutton(self.FrameNID, text=nid, value=nid,
                                                   variable=self.VarSpecies, font=("Roboto 12"), bg="white",
                                                   command=lambda val = nid :self.controller.updateTaxon(val))
                    self.RadioNID.pack(side=LEFT)

            
            if (i == 'MAM2/3'):
                for m23 in listeMAM23:
                    self.FrameM23  = Frame(self.frame_cat,bg='white')
                    self.FrameM23.pack(anchor='w',fill='y',expand=True,padx=50)
                    self.RadioMAM23 = Radiobutton(self.FrameM23, text=m23, value=m23,
                                                    variable=self.VarSpecies, font=("Roboto 12"), bg="white",
                                                    command=lambda val = m23 :self.controller.updateTaxon(val))
                    self.RadioMAM23.pack(side=LEFT)


            if (i == 'MAM3'):
                for m3 in listeMAM3:
                    self.FrameM3 = Frame(self.frame_cat,bg='white')
                    self.FrameM3.pack(anchor='w',fill='y',expand=True,padx=50)
                    self.RadioMAM3 = Radiobutton(self.FrameM3, text=m3, value=m3,
                                                   variable=self.VarSpecies, font=("Roboto 12"), bg="white",
                                                   command=lambda val = m3 :self.controller.updateTaxon(val))
                    self.RadioMAM3.pack(side=LEFT)


            if (i == 'MAM4'):
                for m4 in listeMAM4:
                    self.FrameM4 = Frame(self.frame_cat,bg='white')
                    self.FrameM4.pack(anchor='w',fill='y',expand=True,padx=50)
                    self.RadioMAM4 = Radiobutton(self.FrameM4, text=m4, value=m4,
                                                    variable=self.VarSpecies, font=("Roboto 12"), bg="white",
                                                    command=lambda val = m4 :self.controller.updateTaxon(val))
                    self.RadioMAM4.pack(side=LEFT)

            if (i == 'MAM4/5'):
                for m45 in listeMAM45:
                    self.FrameM45 = Frame(self.frame_cat,bg='white')
                    self.FrameM45.pack(anchor='w',fill='y',expand=True,padx=50)
                    self.RadioMAM45 = Radiobutton(self.FrameM45, text=m45, value=m45,
                                                    variable=self.VarSpecies, font=("Roboto 12"), bg="white",
                                                    command=lambda val = m45 :self.controller.updateTaxon(val))
                    self.RadioMAM45.pack(side=LEFT)

            if (i == 'MAM5'):
                for m5 in listeMAM5:
                    self.FrameM5 = Frame(self.frame_cat,bg='white')
                    self.FrameM5.pack(anchor='w',fill='y',expand=True,padx=50)
                    self.RadioMAM5 = Radiobutton(self.FrameM5, text=m5, value=m5,
                                                    variable=self.VarSpecies, font=("Roboto 12"), bg="white",
                                                    command=lambda val = m5 :self.controller.updateTaxon(val))
                    self.RadioMAM5.pack(side=LEFT,pady=(5,0))



            self.tabMAM.add(self.frame_cat, text=i)
            



        self.tabMAM.pack(expand=True, fill='both')


        