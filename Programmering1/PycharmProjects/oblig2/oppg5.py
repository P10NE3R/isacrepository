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