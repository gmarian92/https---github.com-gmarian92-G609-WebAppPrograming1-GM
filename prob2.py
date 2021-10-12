#citire date de la tastatura1
produs_dorit = str(input("Care este produsul pentru care verificati stocul? "))
bonuri = int(input("Cate cititi?: "))

#definire matrice
date = {}
date["bonuri"] = {}
date["produse_bon"] = {}
date["stoc"] = {}

for bon in range(bonuri):
    bon += 1
    date["bonuri"][bon] = {}
    produse = int(input("Cate produse doriti sa adaugati pe bonul "+str(bon)+": "))
    for produs in range(produse):
        produs += 1
        nume = str(input("Ce nume are produsul cu numarul "+str(produs) + ": "))
        valoare = int(input("Ce valoare are produsul cu numarul "+str(produs) + ": "))
        date["bonuri"][bon][produs] = { "nume": nume, "valoare": valoare }

for bon in date["bonuri"].keys():
    date["produse_bon"][bon] = []
    for produs in date["bonuri"][bon].keys():
        date["produse_bon"][bon].append(date["bonuri"][bon][produs]["nume"])

for bon in date["produse_bon"].keys():
    if produs_dorit in date["produse_bon"][bon]:
        print("Produsul " + produs_dorit + " a fost gasit pe bonul cu numarul " + str(bon) + ".")
        total_bon = 0
        for produs in date["bonuri"][bon]:
            produs_curent = date["bonuri"][bon][produs]
            total_bon += produs_curent["valoare"]
        print("Valoarea totala a produselor de pe bonul cu numarul " + str(bon) + " care include si produsul" + produs_dorit + " este de " + str(total_bon) + ".")