tolkien_bokliste = ["The Hobbit",
                    "Farmer Giles of Ham",
                    "The Fellowship of the Ring",
                    "The Two Towers",
                    "The Return of the King",
                    "The Adventures of Tom Bombadil",
                    "Tree and Leaf"]

#Lager en index liste for å legge til index tallene i de øsnkede

#1
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

#2
tolkien_bokliste.append("The Silmarillion")
tolkien_bokliste.append("Unfinished Tales")

#3
tolkien_bokliste[2:4] = ["Lord of the Rings: The Fellowship of the Ring",
                           "Lord of the Rings: The Two Towers",
                           "Lord of the Rings: The Return of the King"]

#4
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

