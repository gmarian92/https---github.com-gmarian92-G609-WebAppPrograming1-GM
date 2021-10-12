#citim date
n = int(input("Introdu numarul de angajati: "))
angajati = []
for i in range(n):
    angajat = float(input("Introduceti salariul angajatului nr." + str(i) + ":"))
    angajati.append(angajat)

suma_pare = 0
suma_impare = 0
numere_pare = 0
numere_impare = 0

#numaram pozitiile pare si pozitiile impare pentru a calcula media

for i in range(n):
    if i%2 == 0:
        suma_pare = suma_pare + angajati[i]
        numere_pare = numere_pare + 1
    else i%2 == 1:
        suma_impare = suma_impare + angajati[i]
        numere_impare = numere_impare + 1

medImp = suma_impare/numere_impare
medPar = suma_pare/numere_pare

print("Media salariilor de pe locurile pare = " + str(medPar))
print("Media salariilor de pe locurile impare = " + str(medImp))