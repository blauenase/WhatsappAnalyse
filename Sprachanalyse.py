import re
import json

name = "Jana"
#test2
"""def remove_name():
    file = open(name + "/" + name + "-Formatiert.txt", "r", encoding = "utf8")
    newtext = ""
    for line in file.readlines():       
        if "daniel m" in line:
            newline = line.replace("daniel m", "")
            newtext += newline
        if "arweiler" in line:
            newline = line.replace("arweiler", "")
            newtext += newline
        if name.lower() in line:
            newline = line.replace(name.lower(), "")
            newtext += newline
        
    newfile = open(name + "/" + name + "-FormatiertOhneNamen.txt", "w+", encoding = "utf8")
    newfile.write(newtext)
    file.close()
    newfile.close()"""

def remove_name():
    file = open("formatiert")
    lines = ()
    lines = file.readlines()
    print(lines)
    lines.remove(0)

def synthese():
    source = open(name + "/" + name + "-FormatiertOhneNamen.txt", "r", encoding = "utf8")
    sourcetxt = source.read()
    words = sourcetxt.split()
    #print(words)
    allwords = []
    for word in words:
        if word not in allwords:
            allwords.append(word)
    #print(len(allwords))
    alldicts =[]
    wordfile = open(name + "/" + name + "-Sprachanalyse.txt", "w+", encoding = "utf8")
    u = 0
    wordssorted = list()
    for word in allwords:
        if word in wordssorted:
            continue
        else:
            wordssorted.append(word)
        newdict = dict()             #name des dict = allwords(index) index von dict
        indices = getindex(u)    
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


def getindex(wordindex):
    source = open(name + "/" + name + "-FormatiertOhneNamen.txt", "r", encoding = "utf8")
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

#
# remove_name()
analysis()
#print(getindex(0))