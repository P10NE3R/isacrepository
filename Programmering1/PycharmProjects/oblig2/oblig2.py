print("--------------")
print("╎ Pakkeliste ╎")
print("--------------")
print("                 ")

print("1 legg til noe til lista")
print("2 fjern noe fra lista")
print("3 skriv ut hele lista")
print("x for å stoppe program")
li = []
x = 1
while x == 1 == True:
    val = input("Velg hva du vil gjøre her:")
    if val == "1":
        li.append(input("Det du vil legge til:"))
    if val == "2":
        li.remove(input("Velg hva du vil fjerne her"))
    if val == "3":
        print(li)
    if val == "x":
        print( )
        print("Er du sikker på at du vil stopp programmet og slette listen?")
        print( )
        gg=input("Skriv x igjen hvis du fortsatt vil avslutte:")
        if gg == "x":
            x=2

#2
for i in range(9,110):
    if i % 2 ==1:
        print(i)
#bruker modulus til å finne ut om tallet i for-løkkken er heltall eller ikke
#Deretter printer løkken i som blir traversjert, hvis i er et oddetall

#3
tolkien_bokliste = ["The Hobbit",
                    "Farmer Giles of Ham",
                    "The Fellowship of the Ring",
                    "The Two Towers",
                    "The Return of the King",
                    "The Adventures of Tom Bombadil",
                    "Tree and Leaf"]

#Lager en index liste for å legge til index tallene i de øsnkede


index = []
index.append(0)
index.append(1)
index.append(5)
index.append(6)

print("--------------------------------")
print("╎ De to første og siste bøkene ╎")
print("--------------------------------")
print("                                ")

for i in range(4):
    y = index[i]
    print(tolkien_bokliste[y])
    print("               ")


tolkien_bokliste.append("The Silmarillion")
tolkien_bokliste.append("Unfinished Tales")


tolkien_bokliste[2:4] = ["Lord of the Rings: The Fellowship of the Ring",
                           "Lord of the Rings: The Two Towers",
                           "Lord of the Rings: The Return of the King"]


print("------------------")
print("╎ Usortert liste ╎")
print("------------------")
print("              ")
print(tolkien_bokliste)
print("              ")


print("-----------------")
print("╎ Sortert liste ╎")
print("-----------------")
print("                 ")

#Brukte sorter fuksjon på listen, oppgaen spesifiserte ikke måte listen skole sorteres på
tolkien_bokliste.sort()

for n in range(len(tolkien_bokliste)):
    x = 1+n
    print(x, tolkien_bokliste[n])

#4

tolkien_bokliste = ["The Hobbit",
                    "Farmer Giles of Ham",
                    "Lord of the Rings: The Fellowship of the Ring",
                    "Lord of the Rings: The Two Towers",
                    "Lord of the Rings: The Return of the King",
                    "The Adventures of Tom Bombadil",
                    "Tree and Leaf",
                    "The Silmarillion",
                    "Unfinished Tales"]


ny = []
vy = []
ty = []

for i in range(len(tolkien_bokliste)):
    if "Lord of the Rings" in tolkien_bokliste[i]:
        ny.append(tolkien_bokliste[i])

for n in range(len(tolkien_bokliste)):
    if "Lord" and "of" and "the" and "Rings" in tolkien_bokliste[n]:
        vy.append(tolkien_bokliste[n])

for g in range(len(tolkien_bokliste)):
    setning = tolkien_bokliste[g]
    if setning.find("Lord of the Rings") == True:
        ty.append(tolkien_bokliste[g])
print(setning)

#5
import random

kast = 3
score = 0
resutat = 0

inp = input("Hvor mange spillere?")

spillere = int(inp) #La til denne  for å gjøre inforoamsjonen fra input til en integer fordi jeg fikk feilmelding

for n in range(spillere): #Den første løkken repeterer seg selv for andtall spillere
    spiller_tall = n+1
    resultat = 0
    for i in range(kast): #Denne løkken reppeterer seg selv for antall kast som er 3
        score = random.randrange(0,61)
        resultat += score
        kast_num = i+1
        print("Kast", kast_num , "poeng:", score) #skriver ut hvert kast til den enkelte spiller

    print("Spiller", spiller_tall, "Resultat:", resultat,) # skriver ut resultatet for hver spiller
    print("          ")

#6
print("--------------")
print("╎ Pakkeliste ╎")
print("--------------")
print("                 ")

print("1 legg til noe til lista")
print("2 fjern noe fra lista")
print("3 skriv ut hele lista")
print("x for å stoppe program")
li = []
x = 1
while x == 1 == True:
    val = input("Velg hva du vil gjøre her:")
    if val == "1":
        li.append(input("Det du vil legge til:"))
    if val == "2":
        li.remove(input("Velg hva du vil fjerne her"))
    if val == "3":
        print(li)
    if val == "x":
        print( )
        print("Er du sikker på at du vil stopp programmet og slette listen?")
        print( )
        gg=input("Skriv x igjen hvis du fortsatt vil avslutte:")
        if gg == "x":
            x=2




