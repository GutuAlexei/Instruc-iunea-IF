n1=int(input('Numarul primului elev ='))
n2=int(input('Numarul la al doilea elev='))
n3=int(input('Numarul la al treilea elev ='))
p1=int(input('Punctajul primului ='))
p2=int(input('Punctajul la al doilea='))
p3=int(input('Punctajul la al treilea ='))
if  (p1>p2) and (p1>p3):
    print('Punctajul maxim are elevul ' , n1)
if (p2 >p1) and (p2>p3):
    print ('Punctajul maxim are elevul ' , n2)
if (p3 >p1) and (p3>p2):
    print ('Punctajul maxim are elevul ' , n3)
if (p1== p2) and (p1>p3) and (p2> p3):
    print ('Punctajul maxim au elevii ' , n1 , n2)
if (p1== p3) and (p1>p2) and (p3>p2):
    print('Punctajul maxim au elevii ' , n1 , n3)
if (p2==p3) and (p2>p1) and (p3>p1):
    print ('Punctajul maxim au elevii ' ,n2 , n3)