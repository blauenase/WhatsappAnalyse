import tkinter as tk
from tkinter import filedialog

def getfile():
    file = tk.filedialog.askopenfilename()
    print(file)
    i = 0
    finished = False
    while not(finished):
        i = i+1
        #print(file[-(i+4):-(i+1)])
        if file[-(i+1)] == "/" or file[-(i+4):-(i+1)] == "mit":
            name = file[-i:-4]
            finished = True
    label.config(text = file)
    print(name)
    return file


def openwindow():
    root = tk.Tk()

    canvas = tk.Canvas(root, width = "200", height = "200")
    canvas.pack()

    alphacheckbox = tk.Checkbutton(canvas, text ="Sort alphabetically")
    alphacheckbox.pack()

    numcheckbox = tk.Checkbutton(canvas, text ="Sort nummerically")
    numcheckbox.pack()
    
    button = tk.Button(canvas, text = "Select", command = getfile)
    button.pack()

    global label
    label = tk.Label(canvas)
    label.pack()

    button = tk.Button(canvas, text = "Analyse!", command = analyse)
    button.pack()

    tk.mainloop()

openwindow()