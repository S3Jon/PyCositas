from tkinter import *
import tkinter as tk
from tkinter import filedialog
import os
from pygame import mixer
import fnmatch

mixer.init()

#crear ventana
ventana = tk.Tk()
ventana.title("ReproMusic")
ventana.geometry("300x400")
ventana.config(bg = 'black')

#path a carpeta + file filter
mpath = filedialog.askdirectory()
pattern = "*.mp3"


#funcionalidad botones
def select():
    label.config(text = listBox.get("anchor"))
    mixer.music.load(mpath + "\\" + listBox.get("anchor"))
    mixer.music.play()

def stop():
    mixer.music.stop()
    listBox.select_clear('active')
    
def pnext():
    next_song = listBox.curselection()
    next_song = next_song[0] + 1
    next_song_name = listBox.get(next_song)
    label.config(text = next_song_name)
    mixer.music.load(mpath + "\\" + next_song_name)
    mixer.music.play()
    listBox.select_clear(0, 'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)

def pprev():
    next_song = listBox.curselection()
    next_song = next_song[0] - 1
    next_song_name = listBox.get(next_song)
    label.config(text = next_song_name)
    mixer.music.load(mpath + "\\" + next_song_name)
    mixer.music.play()
    listBox.select_clear(0, 'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)

def pause():
    if pausButton["text"] == "Pause":
        mixer.music.pause()
        pausButton["text"] = "Play"
    else:
        mixer.music.unpause()
        pausButton["text"] = "Pause"

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

prevButton = tk.Button(ventana, bg = "green", text = "", image= back_img, command=pprev)
prevButton.pack(pady = 15, in_ = top, side = 'left')

playButton = tk.Button(ventana, bg = "green", text = "", image= play_img, command= select)
playButton.pack(pady = 15, in_ = top, side = "left")

pausButton = tk.Button(ventana, bg = "green", text = "Pause", image= paus_img, command=pause)
pausButton.pack(pady = 15, in_ = top, side = "left")

stopButton = tk.Button(ventana, bg = "green", text = "", image= stop_img, command=stop)
stopButton.pack(pady = 15, in_ = top, side = "left")

nextButton = tk.Button(ventana, bg = "green", text = "", image= next_img, command=pnext)
nextButton.pack(pady = 15, in_ = top, side = "left")

#filtrosfiles + poner musica en lista

for root, dirs, files in os.walk(mpath):
    for filename in fnmatch.filter(files, pattern):
        listBox.insert('end', filename)
        
ventana.mainloop()