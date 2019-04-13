import re
import os
import shutil
import tkinter as tk
from tkinter import filedialog

ausnahmen = {"robin", "m", "daniel", "batu", "justus", "jana", "giuliano", "arweiler", "katha", "irina", "mama", "papa", "oma", "medien", "ausgeschlossen"}


file = None
filename = None
name = None
alphavar = None
numvar = None
directory = None
formated_file = None

def getfile():
    file = tk.filedialog.askopenfile(mode = "r")
    filename = file.name
    print(filename)
    i = 0
    dirbestimmt = False
    namebestimmt = False
    while not dirbestimmt:
        i = i+1
        if filename[-(i+1)] == "/" and not namebestimmt or filename[-(i+4):-(i+1)] == "mit" and not namebestimmt:
            name = filename[-i:-4]
            print("Name " + name)
            namebestimmt = True
        if filename[-(i+1)] == "/":
            directory = filename[:-i]
            print("Dir " + directory)
            dirbestimmt = True
    label.config(text = filename)
    print(name)
    return file, directory, name

def openwindow():
    root = tk.Tk()

    canvas = tk.Canvas(root, width = "200", height = "200")
    canvas.pack()

    alphavar = tk.IntVar()
    alphacheckbox = tk.Checkbutton(canvas, text ="Sort alphabetically", variable = alphavar)
    alphacheckbox.pack()

    numvar = tk.IntVar()
    numcheckbox = tk.Checkbutton(canvas, text ="Sort nummerically", variable = numvar)
    numcheckbox.pack()
    
    #button = tk.Button(canvas, text = "Select", command = getfile)
    #button.pack()

    global label
    label = tk.Label(canvas)
    label.pack()
    button = tk.Button(canvas, text = "Analyse!", command = starte_analyse)
    button.pack()

    tk.mainloop()

def format(file, directory, name):
    original_file = open(file.name, encoding = "utf8").read()
    res1 = re.sub(r'[^\w\s]','',original_file)      #punkte und kommas entfernen
    res2 = re.sub(r'\d+', '', res1)                 #Zahlen entfernen
    formated_file_as_string = res2.lower()          #alles klein
    formatiert_file = open(directory + name + "/" + name + "-Formatiert.txt", "w+", encoding = "utf8")   #Neue Datei erstellen
    formatiert_file.write("")                       #falls vorhanden leeren
    formatiert_file.write(formated_file_as_string)
    formatiert_file.close()
    original_file.close()
    return formated_file_as_string

def count_chars(file_as_string, name):
    numLines = 0
    numWords = 0
    numChars = 0
    for line in file_as_string:
        wordsList = line.split()
        numLines += 1
        numWords += len(wordsList)
        numChars += len(line)
    ergebnis_file_alpha = open(directory + name + "/" + name + "-Ergebnis.txt","w+", encoding = "utf8")
    ergebnis_file_alpha.write("Lines %i  Words %i   Chars %i \n" % (numLines,numWords,numChars))
    ergebnis_file_alpha.close()

def word_count(file_as_string, directory, name):
    wortanzahl = 0
    wortdict = dict()
    wortdict.clear()
    words = file_as_string.split()
    for word in words:       
        if word in wortdict and word not in ausnahmen:         
            wortdict[word] += 1
        else:
            wortdict[word] = 1       
            wortanzahl += 1
    words_alphabet_sorted = list(wortdict.keys())   #Alle Wöter
    words_alphabet_sorted.sort()                    #sortiert
    ergebnis_file_alpha = open(directory + name + "/" + name + "-Ergebnis_alphabetisch_sortiert.txt","a+", encoding = "utf8")   #Neue Datei
    ergebnis_file_alpha.write("Wortschatz: " + str(wortanzahl) +"\n")
    for wort in words_alphabet_sorted:
        ergebnis_file_alpha.write(wort + " " + str(wortdict[wort]) + "\n")
    num = dict()
    ergebnis_file_numerical = open(directory + name + "/" + name + "-Ergebnis_nach_Häufigkeit_sortiert.txt","a+", encoding = "utf8")
    allezahlen = list(wortdict.values())            #Alle Zahlen
    allezahlen.sort()                               #sortiert
    for zahl in allezahlen:
        if zahl not in num.values():
            for item in words_alphabet_sorted:
                if wortdict[item] == zahl:
                    num[item] = zahl
                    ergebnis_file_numerical.write(item + " " + str(num[item]) + "\n")
     

    ergebnis_file_alpha.close()
    ergebnis_file_numerical.close()
    file.close()
    
def starte_analyse():
    file, directory, name = getfile()
    createfolder(directory, name)
    formatedstring = format(file, directory, name)
    word_count(formatedstring, directory, name)

def createfolder(directory, name):
    try:
        os.mkdir(directory + name)
    except FileExistsError:         #Falls Ordner schon existiert -> Löschen
        shutil.rmtree(directory + name, ignore_errors=True)
        os.mkdir(directory + name)

openwindow()



    
    