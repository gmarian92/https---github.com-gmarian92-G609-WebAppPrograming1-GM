# Se citeste n natural, apoi n numere intregi. Sa se introduca elementele pare intr-o lista 
# si cele impare in alta lista, apoi sa se afiseze cea mai mare valoare para introdusa si 
# cea mai mica valoare impara introdusa

n=int(input("Cate numere doriti sa introduceti? "))

nrPare=[]
nrImpare=[]

for i in range(n):
    nr=int(input("Introduceti urmatorul numar: "))
    if nr%2==0:
        nrPare.append(nr)
    else:
        nrImpare.append(nr)

max=nrPare[0]

for n in nrPare:
    if n>max:
        max=n

print("cel mai mare numar par este "+str(max))

min=nrImpare[0]

for n in nrImpare:
    if n<min:
        min=n

print("cel mai mic numar impar este "+str(min))