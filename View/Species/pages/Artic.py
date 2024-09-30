from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk


class Artic(Frame):
    def __init__(self, master=None, variable=None,controller= None):
        super().__init__(master)
        self.master = master
        self.configure(bg='#D9D9D9')
        self.pack(expand=True, fill='both')

        self.controller = controller

        self.VarSpecies = variable

        listeCat = ['SVERT', 'LCARN', 'Small pinnipeds', 'Large pinnipeds', 'Indeterminate Seal', 'Unidentified']
        
        listeSVERT = ['SVERT', 'CANF', 'VULPA', 'VULPI', 'LEPA', 'LAGO']
        listeSVERTLabel = ['Small vertebrate (indet.)', 'Canis familiaris', 'Vulpes lagopus', 'Vulpes sp.', 'Lepus arcticus', 'Lagaomorpha']

        listeLCARN = ['LCARN', 'URSM', 'URSA', 'URSAM', 'URSI', 'LUP']
        listeLCARNLabel = ['Large carnivore (indet.)', 'Ursus maritimus', 'Ursus arctos', 'Ursus americanus', 'Ursus sp.', 'Canis lupus']

        listeSP = ['SP', 'PG', 'PV', 'PH'] 
        listeSPLabel = ["Small pinniped (indet.)","Pagophilus groenlandicus I","Phoca vitulina","Phoca hispida"]

        listeLP = ['LP', 'EB', 'CC', 'HG','WAL']
        listeLPLabel= ["Large pinniped (indet.)","Erignathus barbatus","Cystophora cristata","Halichoerus grypus","Odobenus rosmarus"]

        listePSP =['PSP']
        listePSPLabel=['Indeterminate seal']

        listeU = ['MAM', 'UMM', 'UTM']
        listeULabel=["Unidentified mammal","Unidentified marine mammal","Unidentified terrestrial mammal"]

        self.tabMAM = ttk.Notebook(self, style='TNotebook')


        # Création et ajout des onglets pour chaque catégorie
        for i in listeCat:
            self.frame_cat = Frame(self.tabMAM, bd=1, relief=SOLID, bg='white')
            self.frame_cat.pack(expand=True, fill=BOTH, padx=10, pady=10)

            if i == 'SVERT':
                for id, s in enumerate(listeSVERT):
                    self.frame_s = Frame(self.frame_cat, bg='white')
                    self.frame_s.pack(anchor='w',fill='y',expand=True)
                    self.radio_svert = Radiobutton(self.frame_s, text=s, value=s,
                                              variable=self.VarSpecies, font=("Roboto 12"), bg="white",
                                              command=lambda val = s :self.controller.updateTaxon(val))
                    self.radio_svert.pack(side=LEFT)

                    self.label_svert = Label(self.frame_s, text=listeSVERTLabel[id], font=("Roboto 12"), 
                                        bg="white", fg='#45464b')
                    self.label_svert.pack(side=LEFT)


            if (i == 'LCARN'):
                for id,m2 in enumerate(listeLCARN):
                    self.FrameLCARN = Frame(self.frame_cat,bg='white')
                    self.FrameLCARN.pack(anchor='w',fill='y',expand=True)
                    self.RadioLCARN = Radiobutton(self.FrameLCARN, text=m2, value=m2,
                                                   variable=self.VarSpecies, font=("Roboto 12"), bg="white",
                                                   command=lambda val = m2 :self.controller.updateTaxon(val))
                    self.RadioLCARN.pack(side=LEFT)

                    self.LabelLCARN = Label(self.FrameLCARN, text=listeLCARNLabel[id], font=("Roboto 12"),
                                            bg="white",fg='#45464b')
                    self.LabelLCARN.pack(side=LEFT)

            if (i == 'Small pinnipeds'):
                for id,m23 in enumerate(listeSP):
                    self.FrameSP = Frame(self.frame_cat,bg='white')
                    self.FrameSP.pack(anchor='w',fill='y',expand=True)
                    self.RadioSP = Radiobutton(self.FrameSP, text=m23, value=m23,
                                                  variable=self.VarSpecies, font=("Roboto 12"), bg="white",
                                                  command=lambda val = m23 :self.controller.updateTaxon(val))
                    self.RadioSP.pack(side=LEFT)

                    self.LabelSP = Label(self.FrameSP, text=listeSPLabel[id], font=("Roboto 12"), 
                                           bg="white",fg='#45464b')
                    self.LabelSP.pack(side=LEFT)

            if (i == 'Large pinnipeds'):
                for id,m3 in enumerate(listeLP):
                    self.FrameLP = Frame(self.frame_cat,bg='white')
                    self.FrameLP.pack(anchor='w',fill='y',expand=True)
                    self.RadioLP = Radiobutton(self.FrameLP, text=m3, value=m3,
                                                   variable=self.VarSpecies, font=("Roboto 12"), bg="white",
                                                   command=lambda val = m3 :self.controller.updateTaxon(val))
                    self.RadioLP.pack(side=LEFT)

                    self.LabelLP = Label(self.FrameLP, text=listeLPLabel[id], font=("Roboto 12"), 
                                           bg="white",fg='#45464b')
                    self.LabelLP.pack(side=LEFT)


            if (i == 'Indeterminate Seal'):
                for id,m4 in enumerate(listePSP):
                    self.FramePSP = Frame(self.frame_cat,bg='white')
                    self.FramePSP.pack(anchor='w',fill='y',expand=True)
                    self.RadioPSP = Radiobutton(self.FramePSP, text=m4, value=m4,
                                                    variable=self.VarSpecies, font=("Roboto 12"), bg="white",
                                                    command=lambda val = m4 :self.controller.updateTaxon(val))
                    self.RadioPSP.pack(side=LEFT)

                    self.LabelPSP = Label(self.FramePSP, text=listePSPLabel[id], font=("Roboto 12"), 
                                           bg="white",fg='#45464b')
                    self.LabelPSP.pack(side=LEFT)


            if (i == 'Unidentified'):
                for id,m45 in enumerate(listeU):
                    self.FrameU = Frame(self.frame_cat,bg='white')
                    self.FrameU.pack(anchor='w',fill='y',expand=True)
                    self.RadioU = Radiobutton(self.FrameU, text=m45, value=m45,
                                                   variable=self.VarSpecies, font=("Roboto 12"), bg="white",
                                                   command=lambda val = m45 :self.controller.updateTaxon(val))
                    self.RadioU.pack(side=LEFT)

                    self.LabelU = Label(self.FrameU, text=listeULabel[id], font=("Roboto 12"), 
                                           bg="white",fg='#45464b')
                    self.LabelU.pack(side=LEFT)

            self.tabMAM.add(self.frame_cat, text=i)
            

        self.tabMAM.pack(expand=True, fill='both')
