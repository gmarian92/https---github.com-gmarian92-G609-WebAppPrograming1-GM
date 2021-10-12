#se citeste n natural apaoi n numere intregi. sa se afiseze cea mai mare si cea mai mica valoare

n=int(input("Cate mumere se introduc?"))

numere=[]

for i in range(n):
    nr=int(input("Introduceti numere"))
    numere.append(nr)

suma=0

for n in numere:
    suma=suma+n

print("Suma este"+str(suma))

max=numere[0]

for n in numere:
    if n>max:
        max=n

print("cel mai mare numar este"+str(max))

min=numere[0]

for n in numere:
    if n<min:
        min=n

print("cel mai mic numar este"+str(min))