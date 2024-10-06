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
