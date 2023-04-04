ans1 = input("Hello, this is a test. Type ENTER to continue.\n")

while ans1.lower() != ("enter"):
    print("?")
    ans1 = input()

ans2 = input("It worked? Nice. Now type A or B.\n")
options = ["a","b"]

while ans2.lower() not in options:
    print("?")
    ans2 = input()

if ans2.lower() == ("a"):
    print("You chose path A.")
elif ans2.lower() == ("b"):
    print("You chose path B.")

print("This is the end of the test. Hopefully it worked.")