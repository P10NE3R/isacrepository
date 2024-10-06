#oppgave 1
print("Hello, world!")


#oppgave 2
x ='Isac'
y ='Høie'
z =24
print("Hei. Jeg heter",x, y, "og jeg er",z,"år gammel" )

#oppgave 3
print("________________")
print("kalkulator")
print("________________")
print("1.addisjon")
print("2.subtrasksjon")
print("3.gange")
print("5.modulo")
print("6.opphøye")
print("7.dele med nedrunding")

print("_____________________________________________________________")
#Valgte å bruke flere input linjer for å gjøre kalkulatoren mer brukervennlig
#Kunne også brukt input().split() for å få legge inn alle verdiene til variablene med en gang
valg = input("skriv inn tallet på det du ønsker kalkulatoren skal gjøre her:")

a = input("skriv inn første tallet her:")
b = input("skriv inn andre tallet her:")

#Brukte flere if statements men satte print funksjonen på utsiden for å korte ned lengden på koden
if valg == "1":
   ans = float(a) + float(b)

if valg == "2":
   ans = float(a) - float(b)

if valg == "3":
   ans = float(a) * float(b)

if valg == "4":
   ans = float(a) / float(b)

if valg == "5":
   ans = float(a) % float(b)

if valg == "6":
   ans = float(a) ** float(b)

if valg == "7":
   ans = float(a) // float(b)

print("                ")
print("________________")
print("                ")
print("Resultat =", ans)
print("                ")
print("________________")




#oppgave 4
a = 6
b = 3
c = 2

oppga = a+(b*c)
oppgb = (a+b)/c
oppgc = a/b/c
oppgd = a/(b/c)

#satte print funksjonene under hverandre slik at svaret og koden ble lettere å lese
print("Oppgave a =",oppga)
print("Oppgave b =",oppgb)
print("Oppgave c =",oppgc)
print("Oppgave d =",oppgd)

#oppgave 5
p1 = 5
p2 = 9
p3 = 2.5
p4 = 21
p5 = 0

antall = 5

sum = (p1+p2+p3+p4+p5)

gjennomsnitt = sum/antall

#funksjonen int gjør svaret gjennomsnitt til en integer altså et heltall
print("Gjennomsnittet av antall småkaker spist er", int(gjennomsnitt))