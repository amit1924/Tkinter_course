# Import the tkinter module
from tkinter import *

# Create a Tkinter window
window = Tk()

photo = PhotoImage(file="icon.png")

# Create a Label widget and place it in the window
label = Label(
    window,
    text="Hello Tkinter",
    font=("bold"),
    fg="green",
    bd=10,
    relief=RAISED,
    image=photo,
    compound="bottom",
)

# Use pack() method to place the label in the window
label.pack()

# Use place() method to specify the exact position of the label within the window
label.place(x=0, y=0)

# Enter the Tkinter event loop to display the window and handle events
window.mainloop()
