#citire date de la tastatura1
produs_dorit = str(input("Care este produsul pentru care verificati stocul? "))
bonuri = int(input("Cate cititi?: "))
stok = {}
stok["produs"]
stok["cantitate"]
#definire matrice
date = {}
date["bonuri"] = {}
date["produse_bon"] = {}
date["data"] = {}

for bon in range(bonuri):
    bon += 1
    date["bonuri"][bon] = {}
    produse = int(input("Cate produse doriti sa adaugati pe bonul "+str(bon)+": "))
    for produs in range(produse):
        produs += 1
        nume = str(input("Ce nume are produsul cu numarul "+str(produs) + ": "))
        contitate = int(input("Ce cantitate s-a cumparat "+str(produs) + ": "))
        stok["cantitate"]-cantitate
        date["bonuri"][bon][produs] = { "nume": nume, "cantitate": cantitate }
        if (stok["cantitate"])==0:
            print("Produsul " + produs_dorit + " nu mai este in stok. Ultimul produs vandut la ora: " + date["data"]+ ".")