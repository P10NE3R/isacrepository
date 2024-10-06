

filmer = []



inception = {"name": "Inception",
             "year": "2010",
             "rating": 8.7
             }

insideout = {"name": "Inside Out",
             "year": "2015",
             "rating":  8.1
             }

conair = {"name": "Con Air",
             "year": "1997",
             "rating":  6.9
             }
listname = [inception,insideout,conair]
z = len(listname)

for i in range(z):
    filmer.append(listname[i])




#I denne funksjonen bruker jeg r(ating) som et betinget argument med alerede definert verdi, dette blir da "default verdi"
# hvis ikke rating blir gitt
def addfilm(liste,n,y,r = 5.0):
   d = dict(name = n, year = y, rating = r)
   if liste == "film":
        filmer.append(d)


addfilm("film", "Mad Max: Fury Road", 2015, 8.1)
addfilm("film", "Gone Girl", 2014, 8.1)
addfilm("film", "Femmern", 2024)


def printfilm():
    for f in range(len(filmer)):
        navn = filmer[f]["name"]
        year = filmer[f]["year"]
        rating = filmer[f]["rating"]
        print(navn, "-",year,"has a rating of",rating)


def avgrating():
    rating = 0
    add = 0
    for i in range(len(filmer)):
        rating = filmer[i]["rating"]
        add +=rating
    avg = add/len(filmer)
    avg = round(avg,1)
    print(avg)

avgrating()

def etter2010(list, year):
    for i in range(len(list)):
        if list[i]["year"] > 2009:
            print(list[i]["name"]["year"])