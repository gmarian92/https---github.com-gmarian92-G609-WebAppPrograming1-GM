
#Problema1

n=int(input("Cate numere introduceti? "))
numere=[]

for i in range(n):
    nr=int(input("Introduceti numere"))
    numere.append(nr)

max=numere[0]
count=1

for n in numere:
    if n>max:
        max=n
        count=1
    if n==max:
        count=count+1

print("cel mai mare numar este"+str(max))
print("Numarul de aparitii este"+str(count))



#Problema 2

n=int(input("Introduceti n= "))
nrImpar=1

if n==1:
    print("Numarul n impar este"+str(nrImpar))
else:
    for i in range(1, n):
          nrImpar=nrImpar+2


print("Numarul n impar este"+str(nrImpar))


#Problema 3

n=int(input("Introduceti n!= "))
factorial = 1

for i in range(1, n):
    factorial=factorial*i

print("n! este"+str(nrImpar))

#Problema 4

n=int(input("Introduceti n natural "))
numere=[]

for i in range(n):
    nr=int(input("Introduceti numere"))
    numere.append(nr)

max=numere[0]
min=numere[0]

for i in numere:
    if max<i:
        max=i
    if min>i:
        min=i

dif=max-min
count=0
for i in numere:
    if i==dif:
        count=count+1


print("Numare egale cu diferenta sunt="+str(dif))

#Problema 5

n=int(input("Introduceti n natural "))
numere=[]

for i in range(n):
    nr=int(input("Introduceti numere"))
    numere.append(nr)

lungime=0
cont=0

for i in numere:
    if i==0:
        cont=cont+1
        if lungime<cont:
            lungime=cont
    else:
        cont=0

print("Lungimea secventei maxime de zerouri este="+str(lungime))

