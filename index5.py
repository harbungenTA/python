krotka = (1,2,3,4)
print(type(krotka))
print(krotka)
# krotka[0]=3 Statyczna

# zbior = {"a", "b", "c"}
# print(type(zbior))
# print(zbior)
# zbior.add("d")
# print(zbior)

# slownik = {
#     "imie":"Aldona",
#     "nazwisko":"Bialkowa",
#     "wiek":"80"
# }
# print(slownik)
# print(slownik["nazwisko"])
  
taba = []
  
for i in range(0,3): 
    print("Podaj imie: ")
    imie = input()
    print("Podaj nazwisko: ")
    nazwisko = input()
    print("Podaj wiek: ")
    wiek = input()

    tablica ={
        "imie":imie,
        "nazwisko":nazwisko,
        "wiek":wiek
    }
    taba.append(tablica)
                
    print(taba)
    

