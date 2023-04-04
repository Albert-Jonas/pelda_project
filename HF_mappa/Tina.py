def osszead(szam1=input('Kérek egy számot:'), szam2=input('Kérek még egy számot:')):
    osszeg=float(szam1)+float(szam2)
    return 'A két szám összege', osszeg

print(osszead())