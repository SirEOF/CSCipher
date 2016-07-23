import sys, os
import Tkinter
from caesar import caesar
from Tkinter import *

# Setup application interface
app = Tkinter.Tk()
app.title("CSCipher")
app.geometry("650x500+200+200")

# Create the funtions to call from the GUI
def callback():
    string = textEntry.get()
    caesar(string)

# Make and put the buttons on a grid on the window
textEntry = Entry(app, width=57, justify=CENTER).set(none).grid(row=1, column=1)
submitButton = Button(app, text="Start", width=10, command=callback).grid(row=1, column=2)

# Start the application
app.mainloop()
