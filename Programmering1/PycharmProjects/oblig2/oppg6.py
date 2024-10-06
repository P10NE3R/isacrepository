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

