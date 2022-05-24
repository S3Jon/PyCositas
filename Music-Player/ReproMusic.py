from tkinter import *
import tkinter as tk
from tkinter import filedialog
import os
import pygame
import fnmatch

#path a carpeta + file filter
mpath = "C:/Users/jonsa/Desktop/x"
pattern = "*.mp3"

#crear ventana
ventana = tk.Tk()
ventana.title("ReproMusic")
ventana.geometry("300x400")
ventana.config(bg = 'black')

#listarmusica

listBox = tk.Listbox(ventana, fg="green", bg="black", width=100)
listBox.pack(padx = 15, pady = 15)

label = tk.Label(ventana, text = '', bg = "black", fg = "yellow")
label.pack(pady = 15)

#imagen_iconos
play_img = tk.PhotoImage(file= "Play.png")
back_img = tk.PhotoImage(file= "Back.png")
next_img = tk.PhotoImage(file= "Next.png")
paus_img = tk.PhotoImage(file = "Pause.png")

#botones

top = tk.Frame(ventana, bg = "black")
top.pack(padx = 10, pady = 5, anchor = 'center') #anchor para poner todos los botones en hz

prevButton = tk.Button(ventana, text = "", image= back_img)
prevButton.pack(pady = 15, in_ = top, side = 'left')

stopButton = tk.Button(ventana, text = "", image= play_img)
stopButton.pack(pady = 15, in_ = top, side = "left")

stopButton = tk.Button(ventana, text = "", image= paus_img)
stopButton.pack(pady = 15, in_ = top, side = "left")

stopButton = tk.Button(ventana, text = "", image= next_img)
stopButton.pack(pady = 15, in_ = top, side = "left")

#filtrosfiles + poner musica en lista

for root, dirs, files in os.walk(mpath):
    for filename in fnmatch.filter(files, pattern):
        listBox.insert('end', filename)
        
ventana.mainloop()