from tkinter import *
import time
import random
from PIL import Image as PILImage, ImageTk, ImageSequence
import pygame
from System import explorer as exp
import os

# Create a class for the main window
class MainWin:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Micro OS 1.0")
        self.tk.geometry("1920x1080")
        self.tk.config(cursor="none") # Hide the mouse cursor
        self.c = Canvas(self.tk, bg="black", height=1080, width=1920)
        
        # Load the GIF image using PIL and resize it
        self.gif = PILImage.open("System/Boot/StartUp/Win11Dark/loading-win11Dark.gif")
        self.frames = [ImageTk.PhotoImage(frame.resize((50, 50), PILImage.LANCZOS)) for frame in ImageSequence.Iterator(self.gif)]
        self.frame_index = 0
        
        # Calculate position for the GIF image (centered horizontally, near the bottom)
        gif_x_position = (1920 - 50) // 2
        gif_y_position = 1080 - 200  # Adjust this value to position the image closer to the bottom
        
        # Display the first frame of the GIF
        self.image_on_canvas = self.c.create_image(gif_x_position, gif_y_position, image=self.frames[self.frame_index], anchor=NW)
        
        # Load the PNG image using PIL and resize it
        self.logo = PILImage.open("System/Boot/StartUp/logo.png")
        self.logo = self.logo.resize((200, 200), PILImage.LANCZOS)
        self.logo_image = ImageTk.PhotoImage(self.logo)
        
        # Calculate position for the PNG image (centered horizontally, near the top)
        logo_x_position = (1920 - 200) // 2
        logo_y_position = 200  # Adjust this value to position the image closer to the top
        
        # Display the PNG image
        self.logo_on_canvas = self.c.create_image(logo_x_position, logo_y_position, image=self.logo_image, anchor=NW)
        
        self.c.pack()
        self.tk.update()
        
        # Start the animation
        self.animate()
        
        # Schedule hiding the images after a random delay
        delay = random.randint(2000, 8000)  # Random delay between 2 and 8 seconds (in milliseconds)
        self.tk.after(delay, self.hide_images)

    def animate(self):
        self.frame_index = (self.frame_index + 1) % len(self.frames)
        self.c.itemconfig(self.image_on_canvas, image=self.frames[self.frame_index])
        self.tk.after(10, self.animate)  # Set the tick to 10 milliseconds

    def hide_images(self):
        self.c.itemconfig(self.image_on_canvas, state='hidden')
        self.c.itemconfig(self.logo_on_canvas, state='hidden')
        
        # Change the background to a new image
        self.bg_image = PILImage.open("System/images/bg.jpg")
        self.bg_image = self.bg_image.resize((1920, 1080), PILImage.LANCZOS)
        self.bg_image_tk = ImageTk.PhotoImage(self.bg_image)
        self.c.create_image(0, 0, image=self.bg_image_tk, anchor=NW)
        
        # Load and display the user image
        self.user_image = PILImage.open("System/Icons/users.png")
        self.user_image = self.user_image.resize((300, 300), PILImage.LANCZOS)
        self.user_image_tk = ImageTk.PhotoImage(self.user_image)
        user_x_position = (1920 - 300) // 2
        user_y_position = 200
        self.c.create_image(user_x_position, user_y_position, image=self.user_image_tk, anchor=NW)
        
        # Play the startup music
        pygame.mixer.init()
        pygame.mixer.music.load("System/Boot/StartUp/startup.mp3")
        pygame.mixer.music.play()
        
        # Display the button in the middle-bottom position with transparent background
        self.start_button_normal = self.load_image_with_transparency("System/System32/StartButton/Normal.png", (100, 100))
        self.start_button_mouse_on = self.load_image_with_transparency("System/System32/StartButton/MouseOn.png", (100, 100))
        self.start_button_clicked = self.load_image_with_transparency("System/System32/StartButton/Clicked.png", (100, 100))
        
        button_x_position = (1920 - 100) // 2
        button_y_position = 1080 - 300
        
        self.start_button = Button(self.tk, image=self.start_button_normal, bd=0, command=self.on_button_click)
        self.start_button.bind("<Enter>", self.on_button_enter)
        self.start_button.bind("<Leave>", self.on_button_leave)
        self.start_button.bind("<ButtonPress-1>", self.on_button_press)
        self.start_button.bind("<ButtonRelease-1>", self.on_button_release)
        self.start_button_window = self.c.create_window(button_x_position, button_y_position, anchor=NW, window=self.start_button)

    def load_image_with_transparency(self, path, size):
        image = PILImage.open(path).convert("RGBA")
        image = image.resize(size, PILImage.LANCZOS)
        return ImageTk.PhotoImage(image)

    def on_button_click(self):
        print("Button clicked")
        self.start_button.destroy()
        self.wel = self.c.create_text(1920/2, 1080/2 + 100, text="Welcome", font=("Arial", 44), fill="white")
        
        # Load and display the new GIF image
        new_gif = PILImage.open("System/Boot/StartUp/Win10/loading-win10.gif")
        new_frames = [ImageTk.PhotoImage(frame.resize((50, 50), PILImage.LANCZOS)) for frame in ImageSequence.Iterator(new_gif)]
        self.new_frame_index = 0
        new_gif_x_position = 1920 // 2 - 200
        new_gif_y_position = 1080 // 2 + 70
        self.new_image_on_canvas = self.c.create_image(new_gif_x_position, new_gif_y_position, image=new_frames[self.new_frame_index], anchor=NW)
        
        self.new_frames = new_frames
        self.animate_new_gif()
        self.tk.after(random.randint(500, 4000), self.hide_new_gif)
    def hide_new_gif(self):
        self.c.itemconfig(self.new_image_on_canvas, state='hidden')
        self.c.itemconfig(self.wel, state='hidden')
        self.c.itemconfig(self.user_image_tk, state='hidden')
        exp.taskbar(self.c)


    def animate_new_gif(self):
        self.new_frame_index = (self.new_frame_index + 1) % len(self.new_frames)
        self.c.itemconfig(self.new_image_on_canvas, image=self.new_frames[self.new_frame_index])
        self.tk.after(30, self.animate_new_gif)

    def on_button_enter(self, event):
        self.start_button.config(image=self.start_button_mouse_on)

    def on_button_leave(self, event):
        self.start_button.config(image=self.start_button_normal)

    def on_button_press(self, event):
        self.start_button.config(image=self.start_button_clicked)

    def on_button_release(self, event):
        self.start_button.config(image=self.start_button_mouse_on)

# Create an instance of the MainWin class to run the application
if __name__ == "__main__":
    app = MainWin()
    app.tk.mainloop()