class Osoba:
    imie="Bartosz"
    nazwisko="Bucha"
    wiek=45
    
    def __init__(nlf, newImie, newNazwisko, newWiek):
        nlf.imie=newImie
        nlf.nazwisko=newNazwisko
        nlf.wiek=newWiek
    
    def getImie(nlf):
        return nlf.imie
    
    def setImie(nlf, newImie):
        nlf.imie=newImie
        
    def thirdImie(nlf):
        return nlf.imie, nlf.nazwisko, nlf.wiek

    def toString(nlf):
        return nlf.imie+" "+nlf.nazwisko+" "

class bazaOsob:
    osoby = []
    
    def dodajOsobe(nlf, newOsoba):
        nlf.osoby.append(newOsoba)
        
    def thirdImie(nlf):
        return nlf.osoby[0].imie, nlf.osoby[0].nazwisko, nlf.osoby[0].wiek

    def getCount(nlf):
        return len(nlf.osoby)
    
    def findByImie(nlf,nimie):
        for i in nlf.osoby:
            if i.imie==nimie:
                return True
            else: 
                return False
            
os1=Osoba("Krystian", "Łakomy", 18)
os2=Osoba("Mikołaj", "Kempa", 18)
os3=bazaOsob()

# print(os1)
# print(type(os1))
# print(os1.imie)
# os1.setImie("Ja")
# print(os1.getImie())
# print(os1.thirdImie())
# print(os2.thirdImie())
os3.dodajOsobe(Osoba("Krystian","Miller", 19))
print(os3.thirdImie())
print(os3.getCount())
print(os3.findByImie("Krystian"))
