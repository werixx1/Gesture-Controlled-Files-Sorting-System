import tkinter as tk
from tkinter import *
from tkinter import filedialog
#from tkinter import ttk
from PIL import Image, ImageTk
from os.path import join
from glob import glob
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

    ## BASIC CONFIG
        self.title("Testing window")
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        self.geometry("%dx%d" % (width, height)) # window fills whole screen
        self.resizable(False, False)
        self.config(background="black")
        self.picked_directory = ""

    ## DRAG AND DROP FUNCTIONALITY
        # function for staring the event when mouse is clicked
        def drag_start(event):
            widget = event.widget
            widget.startX = event.x
            widget.startY = event.y

        # function for starting the event when mouse button is being hold
        def drag_motion(event):
            widget = event.widget
            x = widget.winfo_x() - widget.startX + event.x
            y = widget.winfo_y() - widget.startY + event.y
            widget.place(x=x,y=y)

    ## TESTING LOADING IMAGE
        # function for getting from user directory to work with and loading test image to the screen (as a label widget)
        def ask_directory():
            self.picked_directory = filedialog.askdirectory(initialdir="C:/")
            valid_img_types = ('*.png', '*.jpg')
            image_list = []
            for file_format in valid_img_types:
                image_path = join(self.picked_directory, file_format)
                reformat = image_path.replace("/", "\\")  # match path type
                image_list.extend(glob(reformat))

            size = 60, 60
            im = Image.open(image_list[0])  # load first image from picked directory
            im.thumbnail(size, Image.Resampling.LANCZOS)  # resizing image to 60x60
            self.test_img = ImageTk.PhotoImage(im)

            self.label = Label(self,
                               bg="red",
                               width=60,
                               height=60,
                               image=self.test_img)
            self.label.place(x=0, y=0) # place at the start of screen for now
            # self.label.pack(side=LEFT)
            self.label.bind("<Button-1>", drag_start)  # binds -> connect an event passed in the widget
            self.label.bind("<B1-Motion>", drag_motion)


    ## CHOOSE DIRECTORY TO GET IMAGES FROM AND LOAD SAMPLE IMAGE
        self.choose_dir_button = Button(self,
                                        text="Choose directory to load images from",
                                        command=ask_directory,
                                        bg="red", fg="white",
                                        font=("Comic Sans MS", 15))
        self.choose_dir_button.pack(side = RIGHT)

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()  # displays window


