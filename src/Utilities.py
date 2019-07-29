from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class GUIPicker:
    def __init__(self, master):
        self.__master = master

    # Image Label
    def pickImageLabel(self, path):
        img = self.pickImage(path)
        label = ttk.Label(self.__master, image=img)
        label.image = img
        return label

    def pickImage(self, path):
        img = ImageTk.PhotoImage(Image.open(path))
        return img

    # Image Button
    def pickImageButton(self, imagePath, callback=None, cursorType='hand2'):
        buttonImage = ImageTk.PhotoImage(Image.open(imagePath))
        button = ttk.Button(self.__master, image=buttonImage,
                            cursor=cursorType, command=callback)
        button.image = buttonImage
        return button

    # Entry
    def pickEntry(self):
        entry = ttk.Entry(self.__master)
        return entry


if __name__ == "__main__":
    print('Performing Test in Utilities Module\n')
