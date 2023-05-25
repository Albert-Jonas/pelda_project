import calendar

# felhasználó megadja az évet és a hónapot
yy=int(input("Válassz évet: "))
mm=int(input("Válassz hónapot: "))

print(calendar.month(yy,mm))
