g=int(input('Numarul de gaini='))
p=int(input('numarul de boabe de proumb ='))
if (p//(g+1)) and (p%(g+1)==0):
    print('Numarul de boabe primit este' , int(p/(g+1)) , 'egalitate' )
elif p/g :
    print('Curcanul Copan a primit mai mult cu  ' , p%(g+1) , 'boabe' )