import re
import matplotlib.pyplot as plt
import numpy as np

monattrans = {1:"Januar", 2:"Februar", 3:"März", 4:"April", 5:"Mai", 6:"Juni", 7:"July", 8:"August", 9:"September", 10:"Oktober", 11:"November", 12:"Dezember"}
zuanalysieren = "Jana" 
name = zuanalysieren
file = open(zuanalysieren + ".txt", "r", encoding = "utf8")
file_string = file.readlines()
i = 0
almost_formated_file = list()
for line in file_string:
    almost_formated_file.append(re.sub(r'[^\w\s]','',line))
    i += 1

formated_file = list()
j = 0
for line in almost_formated_file:
    formated_file.append(almost_formated_file[j].lower())
    j += 1

zahl = 0
dayDict = dict()
for day in range(1,32):
    dayDict[day] = 0
monthDict = dict()
for month in range(1,13):
    monthDict[month] = 0
yearDict = dict()
for year in range(14,20):
    yearDict[year] = 0

ganzerDict = dict()

for line in formated_file:
    date = line[0:6]
    if str(date).isdigit():
        dayDict[int(date[0:2])] += 1
        monthDict[int(date[2:4])] += 1
        yearDict[int(date[4:6])] += 1
        trans = monattrans[int(date[2:4])] + " '" + str(date[4:])
        if trans in ganzerDict:
            ganzerDict[trans] +=1
        else:
            ganzerDict[trans] = 1

print(dayDict)
print(monthDict)
print(yearDict)

ergebnis_file = open(zuanalysieren + "/" + name + "-ErgebnisDatum.txt","w+", encoding = "utf8")
for item in dayDict:
    ergebnis_file.write("Tag:" + str(item) + "  " + str(dayDict[item]) + " Nachrichten\n")
ergebnis_file.close()

ergebnis_file = open(zuanalysieren + "/" + name + "-ErgebnisDatum.txt","a", encoding = "utf8")
for item in monthDict:
    ergebnis_file.write(monattrans[item] + ":  " + str(monthDict[item]) + " Nachrichten\n")

for item in yearDict:
    ergebnis_file.write("Jahr:" + str(item) + "  " + str(yearDict[item]) + " Nachrichten\n")

for item in ganzerDict:
    ergebnis_file.write(str(item) + "  " + str(ganzerDict[item]) + " Nachrichten\n")
    
print(ganzerDict)
ergebnis_file.close()
file.close()

plt.rc('xtick', labelsize=7)
plt.plot(ganzerDict.keys(), ganzerDict.values())
plt.show()

