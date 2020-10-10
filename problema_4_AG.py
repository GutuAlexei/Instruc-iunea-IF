a=int(input('intr. primul numar='))
b=int(input('intr.al doilea numar='))
c=int(input('intr. al treilea numar='))
S=int(input('intr. suma numerilor='))
if ((a+b==S) or (a+c==S) or (b+c==S)):
   print('Numarul ramas in cutie este:' , (a+b+c)-S)
else:
   print('error')   