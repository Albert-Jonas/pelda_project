import random

number = random.randint(1, 10)

print("Gondoltam egy számra 1 és 10 között. Találd ki melyik az!")

guess = int(input("Add meg a tipped: "))

while guess != number:
    if guess < number:
        print("Nagyobb számra gondoltam!")
    else:
        print("Kisebb számra gondoltam!")
    guess = int(input("Add meg a tipped: "))

print("Gratulálok, eltaláltad a számot!")