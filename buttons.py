from tkinter import *

# Create the Tkinter window
window = Tk()

# Load the icon image
icon = PhotoImage(file="icon.png")

# Define a global variable to keep track of the number of clicks
count = 0


# Function to be executed when the button is clicked
def click():
    global count  # Access the global count variable
    count += 1  # Increment the count
    print(
        f"Button is clicked {count} times"
    )  # Print a message indicating the button is clicked and the count


# Create a Button widget
button = Button(
    window,
    text="Click Me",
    command=click,  # Call the click function when the button is clicked
    font=("Comic Sans", 30),  # Set the font of the button text
    bg="red",  # Set the background color of the button
    state=ACTIVE,  # Set the initial state of the button to active
)

# Pack the button into the window
button.pack()

# Enter the Tkinter event loop to display the window and handle events
window.mainloop()
