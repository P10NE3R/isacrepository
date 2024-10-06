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