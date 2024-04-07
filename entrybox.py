from tkinter import *

# Create the Tkinter window
window = Tk()


# Function to be executed when the submit button is clicked
def submit():
    # Retrieve the text entered in the entry widget
    username = entry.get()
    entry.config(state=DISABLED)  # Disable the entry widget
    # Print a message using the retrieved username
    print(f"Hello {username}")


def delete():
    entry.delete(0, END)


def backspace():
    # Delete one character from the end of the entry's text
    entry.delete(len(entry.get()) - 1, END)


# Create an Entry widget for user input
entry = Entry(window, font=("Arial", 50), show="*")

# Pack the entry widget into the window, placing it on the left side
entry.pack(side=LEFT)

entry.insert(0, "Hello GUI")
# Create a submit button that calls the submit function when clicked
submit_button = Button(window, text="Submit", command=submit)
delete_button = Button(window, text="Delete", command=delete)
delete_button.pack(side=RIGHT)
# Create a backspace button that calls the backspace function when clicked
backspace_button = Button(window, text="Backspace", command=backspace)
backspace_button.pack(side=RIGHT)

# Pack the submit button into the window
submit_button.pack()

# Enter the Tkinter event loop to display the window and handle events
window.mainloop()
