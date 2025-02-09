import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox, Canvas, NW, Button
import os
from PIL import Image as PILImage, ImageTk, ImageSequence
import pygame
import random

class taskbar:
    def __init__(self, window):
        c = Canvas(window, bg="black", height=1080, width=1920)
        c.create_rectangle(0, 1080, 800, 1020, fill="white")
        # self.create_rounded_rectangle(0, 1080, 800, 1020, 50, "white")

        bg_image = PILImage.open("System/images/desktopbg.jpeg")
        bg_image = bg_image.resize((1920, 1080), PILImage.LANCZOS)
        bg_image_tk = ImageTk.PhotoImage(bg_image)
        c.create_image(0, 0, image=bg_image_tk, anchor=NW)
        # Display the button in the middle-bottom position with transparent background
        self.start_button_normal = self.load_image_with_transparency("System/System32/StartButton/Normal.png", (50, 50))
        self.start_button_mouse_on = self.load_image_with_transparency("System/System32/StartButton/MouseOn.png", (50, 50))
        self.start_button_clicked = self.load_image_with_transparency("System/System32/StartButton/Clicked.png", (50, 50))
        
        button_x_position = 0
        button_y_position = 1025
        
        self.start_button = Button(c, image=self.start_button_normal, bd=0, command=self.on_button_click)
        self.start_button.bind("<Enter>", self.on_button_enter)
        self.start_button.bind("<Leave>", self.on_button_leave)
        self.start_button.bind("<ButtonPress-1>", self.on_button_press)
        self.start_button.bind("<ButtonRelease-1>", self.on_button_release)
        self.start_button_window = c.create_window(button_x_position, button_y_position, anchor=NW, window=self.start_button)

        c.pack()

    def load_image_with_transparency(self, path, size):
        image = PILImage.open(path).convert("RGBA")
        image = image.resize(size, PILImage.LANCZOS)
        return ImageTk.PhotoImage(image)

    def on_button_click(self):
        print("Button clicked")
    
    def on_button_enter(self, event):
        self.start_button.config(image=self.start_button_mouse_on)

    def on_button_leave(self, event):
        self.start_button.config(image=self.start_button_normal)

    def on_button_press(self, event):
        self.start_button.config(image=self.start_button_clicked)

    def on_button_release(self, event):
        self.start_button.config(image=self.start_button_mouse_on)

