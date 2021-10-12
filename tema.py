# TEMA 1: Se citesc 5 numere naturale de la tastatura. 
# Sa se afiseze cel mai mare numar mai mic decat 10 si cel mai mic numar mai mare decat 10.
# TEMA 2: Incercati sa faceti schema logica pentru algoritmul de la TEMA 1

x=int(input("Introduceti primul numar: "))
y=int(input("Introduceti al doilea numar: "))
z=int(input("Introduceti al treilea numar: "))
v=int(input("Introduceti al patrulea numar: "))
w=int(input("Introduceti al cincilea numar: "))
max=int
min=int

if x<10:
    max=x
if x>10:
    min=x
if (y<10 and y>max):
    max=y
if (y>10 and y<min):
    min=y
if (z<10 and z>max):
    max=z
if (z>10 and z<min):
    min=z
if (v<10 and v>max):
    max=v
if (v>10 and v<min):
    min=v
if (w<10 and w>max):
    max=w
if (w>10 and w<min):
    min=w

print("Cel mai mare numar mai mic decat 10 este "+str(max))
print("Cel mai mic numar mai mare decat 10 este "+str(max))

