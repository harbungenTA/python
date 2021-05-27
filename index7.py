class Rodzic:
    def __init__(nlf, newImie, newNazwisko):
        nlf.imie = newImie
        nlf.nazwisko = newNazwisko
    
    def toString(nlf):
        return nlf.imie+" "+nlf.nazwisko

class Dziecko(Rodzic):
    def __init__(nlf, newImie, newNazwisko):
        nlf.imie = newImie
        nlf.nazwisko = newNazwisko
        
r=Rodzic("Aldon", "Praktyczny")
d=Dziecko("Elicza","Blada")
print(r.toString())
print(d.toString())