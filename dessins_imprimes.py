#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#interface de conversion de dessins vers STL
#dependances python-tk, openscad, python3, potrace, pstoedit, imagemagick
# Licence GNU-GPL
# Julien RAT pour les Petits Debrouillards et les amis

from tkinter import *
import tkinter.filedialog
import subprocess
myFormats = [
    ('Fichier STL','*.stl'),   
    ]
myFormatsinput = [
    ('Fichier image BMP','.bmp'), ('Fichier image JPG','.jpg'), ('Fichier image PNG','.png')
    ]
def Ouvrir():
	file_path = tkinter.filedialog.askopenfilename(filetypes=myFormatsinput )
	var.set(str(file_path))    
	fen1.update_idletasks()

	
	
def Enregistrer():
	file2_path = tkinter.filedialog.asksaveasfile(mode='w',filetypes=myFormats ,title="Enregistrer le fichier STL sous ...") #tkFileDialog.asksaveasfilename(**self.file_opt)
	cible.set(str(file2_path.name))    
	fen1.update_idletasks()

def Convertir():
	subprocess.call("convert "+ str(var.get()) +" dessin.bmp", shell=True)
	subprocess.call("potrace dessin.bmp -o dessin.eps", shell=True)
	subprocess.call("pstoedit -dt -f dxf:-polyaslines dessin.eps dessin.dxf", shell=True )	
	f = open('dessin.scad','w')
	f.write('linear_extrude(height = 3, center = false, convexity = 10)  import (file = "dessin.dxf");')
	f.close()
	subprocess.call("openscad -o"+ str(cible.get()) +" dessin.scad", shell=True )	


fen1 = Tk()
fen1.title("Convertisseur BMP vers STL")
frame1 = Frame (fen1,width=600, height=100)
frame1.pack()

var = StringVar()
var.set('Selectionnez le fichier source')
tex1 = Label(frame1,textvariable =var, fg='black')
tex1.grid(sticky=E,row=2, column=1)
cible = StringVar()
cible.set('Selectionnez le fichier cible')
tex2 = Label(frame1,textvariable =cible, fg='black')
tex2.grid(sticky=E,row=3, column=1)


bou1 = Button(frame1, text='Selectionner le fichier BMP a convertir', command = Ouvrir)
bou1.grid(sticky=W,row=2, column=0)


bou4 = Button(frame1, text='Selectionner le fichier STL de destination', command = Enregistrer)
bou4.grid(sticky=W,row=3, column=0)

bou2 = Button(frame1, text='Convertir', command = Convertir)
bou2.grid(sticky=W,row=5, column=0)


bou3 = Button(frame1, text='Quitter', command = fen1.destroy)
bou3.grid(sticky=E,row=5, column=1)

fen1.mainloop()


