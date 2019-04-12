import re
import os
import shutil
import tkinter as tk
from tkinter import filedialog

zuanalysieren = "Jana"      ### Hier Name einfügen

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
    finished = False
    while not(finished):
        i = i+1
        #print(file[-(i+4):-(i+1)])
        if filename[-(i+1)] == "/" or filename[-(i+4):-(i+1)] == "mit":
            name = filename[-i:-4]
            directory = filename[:-i]
            print(directory)
            finished = True
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
    s = open(file.name, encoding = "utf8").read()
    res1 = re.sub(r'[^\w\s]','',s) #punkte und kommas entfernen
    res2 = re.sub(r'\d+', '', res1) #Zahlen entfernen
    res3 = res2.lower() #alles klein
    formatiert_file = open(directory + name + "/" + name + "-Formatiert.txt", "w+", encoding = "utf8")   #Neue Datei erstellen
    formatiert_file.write("") #falls vorhanden leeren
    formatiert_file.write(res3)
    formated_string = res3
    formatiert_file.close()
    return formated_string

def count_chars(file_as_string, name):
    numLines = 0
    numWords = 0
    numChars = 0
    for line in file_as_string:
        wordsList = line.split()
        numLines += 1
        numWords += len(wordsList)
        numChars += len(line)
    #print("Lines %i  Words %i   Chars %i" % (numLines,numWords,numChars))
    ergebnis_file_alpha = open(zuanalysieren + "/" + name + "-Ergebnis.txt","w+", encoding = "utf8")
    ergebnis_file_alpha.write("Lines %i  Words %i   Chars %i \n" % (numLines,numWords,numChars))
    ergebnis_file_alpha.close()

def word_count(file_as_string, directory, name):
    anzahl = 0
    alpha = dict()
    alpha.clear()
    words = file_as_string.split()
    maxanzahl = 0
    topwort = list()
    topwort.clear()
    for word in words:
        
        if word in alpha:           
            if alpha[word] > maxanzahl and word not in ausnahmen and word not in topwort:
                maxanzahl = alpha[word]
                #if word not in topwort:
                    #topwort.append(word)
                    #ausnahmen2.append(word)
                    #print(word)
            alpha[word] += 1
        else:
            alpha[word] = 1       
            anzahl += 1
    worter = list(alpha.keys())
    worter.sort()
    ergebnis_file_alpha = open(directory + name + "/" + name + "-Ergebnis_alpha.txt","a+", encoding = "utf8") #Neue Datei
    ergebnis_file_alpha.write("Wortschatz: " + str(anzahl) +"\n")
    #for i in range(0,10):
    #    ergebnis_file.write("Platz" + " " + str(i+1) + ": " + topwort[i] + " mit " + str(alpha[topwort[i]]) + "\n")
    for item in worter:
        #print(item, counts[item])
        ergebnis_file_alpha.write(item + " " + str(alpha[item]) + "\n")
    num = dict()
    ergebnis_file_numerical = open(directory + name + "/" + name + "-Ergebnis_numerical.txt","a+", encoding = "utf8")
    allezahlen = list(alpha.values())
    allezahlen.sort()
    for index in allezahlen:
        if index not in num.values():
            for item in worter:
                if alpha[item] == index:
                    num[item] = index
                    ergebnis_file_numerical.write(item + " " + str(num[item]) + "\n")
     

    ergebnis_file_alpha.close()
    ergebnis_file_numerical.close()
    file.close()
    
def starte_analyse():
    file, directory, name = getfile()
    createfolder(directory, name)
    formatedstring = format(file, directory, name)
    #count_chars(formated_file, zuanalysieren)
    word_count(formatedstring, directory, name)

def createfolder(directory, name):
    try:
        os.mkdir(directory + name)
    except FileExistsError:
        shutil.rmtree(directory + name, ignore_errors=True)
        os.mkdir(directory + name)

#file = open(zuanalysieren + ".txt","r", encoding = "utf8")
#formated_file = format(file, zuanalysieren)

openwindow()


file.close()



    
    