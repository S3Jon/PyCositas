from tkinter import *
import tkinter as tk
from tkinter import filedialog
import os
from pygame import mixer
import fnmatch

#path a carpeta + file filter
mpath = "C:/Users/jonsa/Desktop/x"
pattern = "*.mp3"

mixer.init()

#crear ventana
ventana = tk.Tk()
ventana.title("ReproMusic")
ventana.geometry("300x400")
ventana.config(bg = 'black')

#funcionalidad botones
def select():
    label.config(text = listBox.get("anchor"))
    mixer.music.load(mpath + "\\" + listBox.get("anchor"))
    mixer.music.play()

def stop():
    mixer.music.stop()
    listBox.select_clear('active')

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
stop_img = tk.PhotoImage(file = "Stop.png")

#botones

top = tk.Frame(ventana, bg = "black")
top.pack(padx = 10, pady = 5, anchor = 'center') #anchor para poner todos los botones en hz

prevButton = tk.Button(ventana, bg = "green", text = "", image= back_img)
prevButton.pack(pady = 15, in_ = top, side = 'left')

playButton = tk.Button(ventana, bg = "green", text = "", image= play_img, command= select)
playButton.pack(pady = 15, in_ = top, side = "left")

pausButton = tk.Button(ventana, bg = "green", text = "", image= paus_img)
pausButton.pack(pady = 15, in_ = top, side = "left")

stopButton = tk.Button(ventana, bg = "green", text = "", image= stop_img, command=stop)
stopButton.pack(pady = 15, in_ = top, side = "left")

nextButton = tk.Button(ventana, bg = "green", text = "", image= next_img)
nextButton.pack(pady = 15, in_ = top, side = "left")

#filtrosfiles + poner musica en lista

for root, dirs, files in os.walk(mpath):
    for filename in fnmatch.filter(files, pattern):
        listBox.insert('end', filename)
        
ventana.mainloop()