x=int(input("Introduceti primul numar: "))
y=int(input("Introduceti al doilea numar: "))
z=int(input("Introduceti al treilea numar: "))

#1
#if (x>=y and x>=z):
#print(x)
#elif (y>=x and y>=z):
#print (y)
#else:
#    print(z)


#2 max
max=x

if y>max:
    max=y
if z>max:
    max=z
if w>max:
    max=w

print("Cel mai mare numar introdus este "+str(max))


#3
if x>y:
    if x>z:
        print (x)
    else:
        print (z)  
else:
    if y>z:
        print (y)
    else:
        print (z)    


#min 

min=x

if y<min:
    min=y
if z<min:
    min=z
if w<min:
    min=w

print("Cel mai mic numar introdus este "+str(min))
