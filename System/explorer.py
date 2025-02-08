import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox, Canvas, NW
import os
from PIL import Image as PILImage, ImageTk, ImageSequence
import pygame

class taskbar:
    def __init__(self, window):
        c = Canvas(window, bg="black", height=1080, width=1920)
        c.create_rectangle(0, 1080, 1940, 1020, fill="light grey")
        bg_image = PILImage.open("System/images/desktopbg.jpeg")
        bg_image = bg_image.resize((1920, 1080), PILImage.LANCZOS)
        bg_image_tk = ImageTk.PhotoImage(bg_image)
        c.create_image(0, 0, image=bg_image_tk, anchor=NW)
        c.pack()
