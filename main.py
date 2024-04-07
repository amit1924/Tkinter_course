# Import the tkinter module
from tkinter import *

# Create a Tkinter window
window = Tk()

# Set the size of the window
window.geometry("420x420")

# Set the title of the window
window.title("GUI Window")

# Set the icon of the window
icon = PhotoImage(file="icon.png")
window.iconphoto(True, icon)

# Set the background color of the window
window.config(background="black")

# Enter the Tkinter event loop to display the window and handle events
window.mainloop()
