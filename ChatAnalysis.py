import re
import json
import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

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
    formated_file = open(directory + name + "/" + name + "-Formatiert.txt", "w+", encoding = "utf8")   #Neue Datei erstellen
    formated_file.write("")                       #falls vorhanden leeren
    original_file = open(file.name, encoding = "utf8").readlines()
    for line in original_file:
        res1 = re.sub(r'[^\w\s]','',line)      #punkte und kommas entfernen
        res2 = re.sub(r'\d+', '', res1)                 #Zahlen entfernen
        res3 = res2.lower()          #alles klein
        while res3[0] == " ":
            res3 = res3[1:]
        formated_file.write(res3)
    formated_file.close()
    return formated_file

def remove_name(file, directory, name):
    file = open(directory + name + "/" + name + "-Formatiert.txt", "r", encoding = "utf8")
    file_withoutnames = open(directory + name + "/" + name + "-Formatiert_ohne_Namen.txt", "w+", encoding = "utf8")
    lines = file.readlines()
    del lines[0]                #Standardnachricht entfernen     
    #print(lines[0])
    #print(lines[0].index(" "))
    erstername = lines[0][:lines[0].index(" ")]
    zweitername = lines[1][:lines[1].index(" ")]
    print(erstername,zweitername)
    möglicher_ersternachname = lines[0][lines[0].index(" ")+1:][:lines[0][lines[0].index(" ")+1:].index(" ")]
    möglicher_zweiternachname = lines[1][lines[1].index(" ")+1:][:lines[1][lines[1].index(" ")+1:].index(" ")]
    result1 = tk.messagebox.askyesno("Nachname", "Ist das ein Nachname einer Person? " + möglicher_ersternachname.capitalize())
    result2 = tk.messagebox.askyesno("Nachname", "Ist das ein Nachname einer Person? " + möglicher_zweiternachname.capitalize())
    if result1:
        erstername = erstername + " " +  möglicher_ersternachname
    if result2:
        zweitername = zweitername + " " + möglicher_zweiternachname
    print(erstername,zweitername)
    for line in lines:
        res1 = line.replace(erstername,"",-1)
        res2 = res1.replace(zweitername,"",-1)
        file_withoutnames.write(res2)
    
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

def word_count(directory, name):
    wortanzahl = 0
    wortdict = dict()
    wortdict.clear()
    words = open(directory + name + "/" + name + "-Formatiert.txt", "r", encoding = "utf8").read().split()
    for word in words:       
        if word in wortdict:         
            wortdict[word] += 1
        else:
            wortdict[word] = 1       
            wortanzahl += 1
    #Alphasort Anfang
    print(alphavar)
    words_alphabet_sorted = list(wortdict.keys())   #Alle Wöter
    words_alphabet_sorted.sort()                    #sortiert
    ergebnis_file_alpha = open(directory + name + "/" + name + "-Ergebnis_alphabetisch_sortiert.txt","a+", encoding = "utf8")   #Neue Datei
    ergebnis_file_alpha.write("Wortschatz: " + str(wortanzahl) +"\n")
    for wort in words_alphabet_sorted:
        ergebnis_file_alpha.write(wort + " " + str(wortdict[wort]) + "\n")
    print("Alpha fertig")
    #Alphasort fertig - Numsort Anfang
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
    print("Num fertig")
     

    ergebnis_file_alpha.close()
    ergebnis_file_numerical.close()
    
def synthese(directory, name):
    source = open(directory + name + "/" + name + "-Formatiert_ohne_Namen.txt", "r", encoding = "utf8")
    sourcetxt = source.read()
    words = sourcetxt.split()
    #print(words)
    allwords = []
    for word in words:
        if word not in allwords:
            allwords.append(word)
    #print(len(allwords))
    alldicts =[]
    wordfile = open(directory + name + "/" + name + "-BeispielText.txt", "w+", encoding = "utf8")
    u = 0
    wordssorted = list()
    for word in allwords:
        if word in wordssorted:
            continue
        else:
            wordssorted.append(word)
        newdict = dict()             #name des dict = allwords(index) index von dict
        indices = getindex(u, directory, name)    
        u += 1
        for o in indices:
            if o == len(words)-1:
                break
            if words[o+1] not in newdict:
                newdict[words[o+1]] = 1
            else:
                newdict[words[o+1]] += 1
        alldicts.append(newdict)
        wordfile.write(word + "  " +  json.dumps(newdict) + "\n")
    
    print(newdict)
    wordfile.close()
    source.close()

def getindex(wordindex, directory, name):
    source = open(directory + name + "/" + name + "-Formatiert_ohne_Namen.txt", "r", encoding = "utf8")
    sourcetxt = source.read()
    allwords = sourcetxt.split()
    #print(allwords[wordindex])
    results = []
    offset = -1
    while True:
        try:
            offset = allwords.index(allwords[wordindex], offset + 1)
        except ValueError:
            return results  
        results.append(offset)
    source.close()

def starte_analyse():
    file, directory, name = getfile()
    createfolder(directory, name)
    #formatedstring = format(file, directory, name)
    format(file, directory, name)
    word_count(directory, name)
    remove_name(file, directory, name)
    synthese(directory, name)
    tk.messagebox.showinfo("Fertig", "Die Analyse ist fertig")

def createfolder(directory, name):
    try:
        os.mkdir(directory + name)
    except FileExistsError:         #Falls Ordner schon existiert -> Löschen
        shutil.rmtree(directory + name, ignore_errors=True)
        os.mkdir(directory + name)

openwindow()



    
    