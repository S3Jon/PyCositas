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

#botones

top = tk.Frame(ventana, bg = "black")
top.pack(padx = 10, pady = 5, anchor = 'center') #anchor para poner todos los botones en hz

prevButton = tk.Button(ventana, text = "Anterior")
prevButton.pack(pady = 15, in_ = top, side = 'left')

stopButton = tk.Button(ventana, text = "Play")
stopButton.pack(pady = 15, in_ = top, side = "left")

stopButton = tk.Button(ventana, text = "Stop")
stopButton.pack(pady = 15, in_ = top, side = "left")

stopButton = tk.Button(ventana, text = "Next")
stopButton.pack(pady = 15, in_ = top, side = "left")

#filtrosfiles

for root, dirs, files in os.walk(mpath):
    for filename in fnmatch.filter(files, pattern):
        listBox.insert('end', filename)
        
ventana.mainloop()