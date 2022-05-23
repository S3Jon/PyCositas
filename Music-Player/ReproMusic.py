from tkinter import *
import tkinter as tk
from tkinter import filedialog
import os
import pygame

class ReproMusic:
    def __init__(self, root):
        root.title("music player")
        root.geometry('500x500')
        root.resizable(0, 0)
        pygame.init()
        mydir = r"C:\Users\jonsa\Desktop\x"
        songs = filter(lambda x: x.endswith('.mp3'), os.listdir(mydir))
        play_button = Button(root, text="Play", command=lambda: self.play(currentsong))
        play_button.grid(row=5, column=0)
    
    def play(self, currentsong):
        self.currentsong = currentsong
        print(currentsong)
        pygame.mixer.init()
        pygame.mixer.music.load(str(currentsong))
        pygame.mixer.music.play()
        while (pygame.mixer.get_busy() ):
            time.sleep(400)

        
        
root = Tk()
ReproMusic(root)
mainloop()