import re
import json

name = "Jana"

def remove_name():
    file = open(name + "/" + name + "-Formatiert.txt", "r", encoding = "utf8")
    newtext = ""
    for line in file.readlines():  
        newline = line     
        if "daniel m" in line:
            newline = newline.replace("daniel m", "")           
        if "arweiler" in line:
            newline = newline.replace("arweiler", "")
        if "seis" in line:
            newline = newline.replace("seis", "")           
        if name.lower() in line:
            newline = newline.replace(name.lower(), "")
        newtext += newline
        
    newfile = open(name + "/" + name + "-FormatiertOhneNamen.txt", "w+", encoding = "utf8")
    newfile.write(newtext)
    file.close()
    newfile.close()

def analysis():
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
        newdict.clear()
        indices = getindex(u, allwords) 
        #print(word + "ggg")  
        u += 1
        for o in indices:
            #print(words[o])
            #print(words[o+1])
            if o == len(words)-1:
                break
            if words[o+1] not in newdict:
                newdict[words[o+1]] = 1
            else:
                newdict[words[o+1]] += 1
        alldicts.append(newdict)
        wordfile.write(word.upper() +" ")
        num = dict()
        num.clear()
        allezahlen = []
        allezahlen.clear()
        allezahlen = list(newdict.values())
        allezahlen.sort()
        allezahlen.reverse()
        alleworter = []
        alleworter.clear()
        alleworter = list(newdict.keys())
        for index in allezahlen:
            #if index not in num.values():
            for item in alleworter:
                if newdict[item] == index and item not in num:
                    num[item] = index
                    wordfile.write(item + " " + str(num[item])+", ")
        wordfile.write("\n")
        #wordfile.write(word + "  " +  json.dumps(newdict) + "\n")

    wordfile.close()
    source.close()


def getindex(wordindex, allwords):
    source = open(name + "/" + name + "-FormatiertOhneNamen.txt", "r", encoding = "utf8")
    sourcetxt = source.read()
    alltext = sourcetxt.split()
    results = []
    offset = -1
    while True:
        try:
            offset = alltext.index(allwords[wordindex], offset + 1)
        except ValueError:
            #print(allwords[wordindex])
            #print(results)
            return results  
        results.append(offset)
    source.close()

#remove_name()
analysis()
#print(getindex(0))