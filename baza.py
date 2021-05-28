import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Osoby"]
mycol = mydb["Mieszkancy"]

class ModelOsoba:
    def __init__(nlf, inImie, inNazwisko, inWiek):
        nlf.imie = inImie
        nlf.nazwisko = inNazwisko
        nlf.wiek = inWiek
    def fillModelFromDB(nlf,osoba):
        nlf.imie = osoba["imie"]
        nlf.nazwisko = osoba["nazwisko"]
        nlf.wiek = osoba["wiek"]

class ViewConsole:
    def __init__(nlf, inModelOsoba):
        nlf.modelOsoba = inModelOsoba
    def showOsoba(nlf):
        print("Wyświetlona osoba:")
        print("------------------")
        print("IMIE: " + nlf.modelOsoba.imie)
        print("NAZWISKO: " + nlf.modelOsoba.nazwisko)
        print("WIEK: " + str(nlf.modelOsoba.wiek))
        print("------------------")
    def getOsoba(nlf):
        print("Podaj dane:\n")
        print("Imie: ")
        nlf.modelOsoba.imie=input()
        print("\nNazwisko: ")
        nlf.modelOsoba.nazwisko=input()
        print("\nWiek: ")
        nlf.modelOsoba.wiek=input()
        
class MainController:
    def __init__(nlf, inModel, inView):
        nlf.model = inModel
        nlf.view =inView
    def Init(nlf):
        nlf.model = ModelOsoba("Krzysztof","Kaczmarek",27)
        nlf.view.modelOsoba = nlf.model
        pass
    def Start(nlf):
        nlf.view.showOsoba()
        pass
    def Get(nlf, inView):
        nlf.view.getOsoba()
        inView.modelOsoba = nlf.view.modelOsoba
        inView.showOsoba()
        #print(nlf.view.modelOsoba.imie)
        pass
    def getFromKeyboard(nlf):
        nlf.view.getOsoba()
        inView.modelOsoba = nlf.view.modelOsoba
        inView.showOsoba()
    def Stop(nlf):
        pass

class ViewFile:

    def __init__(nlf, inModelOsoba):
        nlf.modelOsoba = inModelOsoba
                
    def showOsoba(nlf):
        hfile=open("plik.txt", mode="w")
        hfile.write("Wyswietlona osoba:\n")
        hfile.write("------------------\n")
        hfile.write("IMIE: " + nlf.modelOsoba.imie+"\n")
        hfile.write("NAZWISKO: " + nlf.modelOsoba.nazwisko+"\n")
        hfile.write("WIEK: " + str(nlf.modelOsoba.wiek)+"\n")
        hfile.write("------------------")
        hfile.close()

class ViewDB:
    def __init__(nlf,inModelOsoba):
        nlf.modelOsoba = inModelOsoba
        nlf.myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
        nlf.mydb = myclient["Osoby"]
        nlf.mycol = mydb["Mieszkancy"]
    def showOsoba(nlf):
        ins = {
            "imie":nlf.modelOsoba.imie,
            "nazwisko":nlf.modelOsoba.nazwisko,
            "wiek":nlf.modelOsoba.wiek
        }
        nlf.mycol.insert(ins)
    def getOsoba(nlf):
        query=nlf.mycol.find()
        if query.count()>0:
            nlf.modelOsoba.imie = query[0]["imie"]
            nlf.modelOsoba.nazwisko = query[0]["nazwisko"]
            nlf.modelOsoba.wiek = query[0]["wiek"]

cntrl = MainController(None,ViewDB(None))
cntrl.Init()
cntrl.Start()
cntrl.Get(ViewConsole(None))
cntrl.Get(ViewFile(None))
cntrl.Get(ViewDB(None))

# query1 = mycol.find({"imie":"Krystian"})
# if query1.count()>0:
#     for x in query1:
#         print(x)
# else:
#     print("Brak wyników")
# st = "{'wiek':45}"

# def extractWiek(param):
#     param=param+" "
#     t=param.split(sep=":")[1]
#     r=t.split(sep="}")[0]
#     return float(r)

# query2 = mycol.find({},{"_id":0,"wiek":1})
# if query2.count()>0:
#     s=0
#     for x in query2:
#         s=s+extractWiek(str(x))
# else:
#     print("Brak wyników")


# print(extractWiek(st))
# print("Srednia: " + str(s/query2.count()))