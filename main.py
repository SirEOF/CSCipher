import sys, os, Tkinter
from caesar import getCaesarResult, getCaesarKey
from Tkinter import *
import tkMessageBox

# Setup application interface
app = Tkinter.Tk()
app.title("CSCipher")
app.geometry("660x500+200+200")

# Setup menu bar
def Open():
    print "hello!"
def Save():
    print "hello!"
def Save():
    print "hello!"
    
menubar = Menu(app)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", accelerator="Ctrl+O", command=hello)
filemenu.add_command(label="Save", accelerator="Ctrl+S", command=hello)
filemenu.add_separator()
filemenu.add_command(label="Exit", accelerator="Ctrl+Q", command=app.quit)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut", accelerator="Ctrl+X", command=lambda: mywindow.focus_get().event_generate('<<Cut>>'))
editmenu.add_command(label="Copy", accelerator="Ctrl+C", command=lambda: mywindow.focus_get().event_generate('<<Copy>>'))
editmenu.add_command(label="Paste", accelerator="Ctrl+V", command=lambda: mywindow.focus_get().event_generate('<<Paste>>'))
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=hello)
menubar.add_cascade(label="Help", accelerator="Ctrl+H", menu=helpmenu)

app.config(menu=menubar)

# Create the funtions to call from the GUI
def callback():
    global string
    string = labelText.get()
    determineMethod()

def beenClicked():
    global cipherType
    cipherType = relStatus.get()

def determineMethod():
    global cipherType
    global string
    try:
        if cipherType == "Caesar":
            caesarDecoded = getCaesarResult(string)
            caesarKey = getCaesarKey(String)
        elif cipherType == "Vigenere":
            tkMessageBox.showinfo("Vigenere","Vigenere")
        elif cipherType == "Baconian":
            tkMessageBox.showinfo("Baconian","Baconian")
        elif cipherType == "Affine":
            tkMessageBox.showinfo("Affine","Affine")
        elif cipherType == "ROT 13":
            tkMessageBox.showinfo("ROT 13","ROT 13")
        elif cipherType == "Binary":
            tkMessageBox.showinfo("Binary","Binary")
        elif cipherType == "Atbash":
            tkMessageBox.showinfo("Atbash","Atbash")
        elif cipherType == "Base 64":
            tkMessageBox.showinfo("Base 64","Base 64")
        elif cipherType == "Morse":
            tkMessageBox.showinfo("Morse","Morse")
        elif cipherType == "Auto":
            tkMessageBox.showinfo("Auto","Auto")
        else:
            tkMessageBox.showinfo("You broke it and idk how", cipherType)
    except NameError as noBoxSelected:
        tkMessageBox.showinfo("Error", "You must select a type of cipher")
    except ZeroDivisionError as noTextEntered:
        tkMessageBox.showinfo("Error", "You must enter something into the text box")
# Make and put the buttons on a grid on the window
# Start with the textBox and Submit Button
labelText = StringVar(None)
textEntry = Entry(app, width=57, justify=CENTER, textvariable=labelText).grid(row=1, columnspan=4, padx=5, pady=5)
submitButton = Button(app, text="Start", width=10, command=callback).grid(row=1, column=4, pady=5)

# Then put down the options for what cipher to use
relStatus = StringVar()
relStatus.set("Caesar")
Radiobutton(app, text="Caesar", value="Caesar", variable=relStatus, command=beenClicked).grid(row=2, column=0)
Radiobutton(app, text="Vigenere", value="Vigenere", variable=relStatus, command=beenClicked).grid(row=2, column=1)
Radiobutton(app, text="Baconian", value="Baconian", variable=relStatus, command=beenClicked).grid(row=2, column=2)
Radiobutton(app, text="Affine", value="Affine", variable=relStatus, command=beenClicked).grid(row=2, column=3)
Radiobutton(app, text="ROT13", value="ROT13", variable=relStatus, command=beenClicked).grid(row=2, column=4)

Radiobutton(app, text="Binary", value="Binary", variable=relStatus, command=beenClicked).grid(row=3, column=0)
Radiobutton(app, text="Atbash", value="Atbash", variable=relStatus, command=beenClicked).grid(row=3, column=1)
Radiobutton(app, text="Base 64", value="Base 64", variable=relStatus, command=beenClicked).grid(row=3, column=2)
Radiobutton(app, text="Morse", value="Morse", variable=relStatus, command=beenClicked).grid(row=3, column=3)
Radiobutton(app, text="Auto", value="Auto", variable=relStatus, command=beenClicked).grid(row=3, column=4)

# Start the application
app.mainloop()
