xa=int(input('Numar de bile albe mari = '))
ya=int(input('Numar de bilea albe mici = '))
xr=int(input('Numar de bile rosii mari = '))
yr=int(input('Numar de bile rosii mici = '))
xv=int(input('Numar de bile verzi mari = '))
yv=int(input('Numar de bile verzi mici = '))
tx=xa+xr+xv
ty=ya+yr+yv
print('totalul', tx+ty)
if (xa>=0) and (ya>=0) and (xr>=0) and (yr>=0) and (xv>=0) and (yv>=0):
    if (tx>ty):
        print (tx, 'bile mari')
    elif (tx<ty):
        print (ty , 'bile mici')
if (xa+ya>xr+yr) and (xa+ya>xv+yv):
    print (xa +ya, 'bile albe')
elif (xr+yr>xa+ya) and (xr+yr>xv+yv):
    print (xr+yr, 'bile rosii')
elif (xv+yv>xa+ya) and (xv+yv>xr+yr):
    print (xv+yv, 'bile verzi')
elif (xr+yr==xa+ya) and (xr+yr>xv+yv):
    print ('numarul maxim de bile rosii si albe= ',xr+yr)
elif (xv+yv==xa+ya) and (xv+yv>xr+yr):
    print ('numarul maxim de bile verzi si albe',xa+ya)
elif (xr+yr==xv+yv) and (xr+yr>xa+ya):
    print ('numarul maxim de bile rosii si verz= ',xv+yv)
else:
    print ('Eror')