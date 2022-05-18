from pytube import YouTube
import os
from tkinter import *
from tkinter import messagebox as MessageBox

def accion():
    enlace=videos.get()
    video = YouTube(enlace)
    descarga = video.streams.filter(only_audio=True).first()
    out_file = descarga.download()
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

root = Tk()
root.config(bd=15)
root.title("Programa para descargar videos")

imagen = PhotoImage(file="youtube.png")
foto = Label(root, image=imagen, bd=0)
foto.grid(row=0, column=0)

instrucciones = Label(root, text="Programa creado por X")
instrucciones.grid(row=1, column=0)

videos = Entry(root)
videos.grid(row=2, column=0)

boton = Button(root, text="Descargar", command=accion)
boton.grid(row=3, column=0)

root.mainloop()