import random

name = "Jana"
currentword = "wir"
length = 200
file = open(name + "/" + name + "-Sprachanalyse.txt", "r", encoding = "utf8")
lines = file.readlines()

def getnextword(word):
    for line in lines:      
        if word.upper() == line.split()[0]:
            zahl = random.randint(0,100)
            #return line.split()[1]
            try:
                if zahl < 10:
                    return line.split()[1]
                elif zahl < 20:
                    return line.split()[3]
                elif zahl < 30:
                    return line.split()[5]
                elif zahl < 40:
                    return line.split()[7]
                elif zahl < 50:
                    return line.split()[9]
                elif zahl < 60:
                    return line.split()[11]
                elif zahl < 70:
                    return line.split()[13]
                elif zahl < 80:
                    return line.split()[15]
                elif zahl < 90:
                    return line.split()[17]
                else:
                    return line.split()[19]
            except:
                return line.split()[1]

text = ""
for i in range(0,length):
    text = text + " " + currentword
    nextword = getnextword(currentword)
    currentword = nextword
#print(getnextword("sind"))
print(text)
file.close()


