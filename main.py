# Input
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# Logic
t = name1.lower().count("t") + name2.lower().count("t")
r = name1.lower().count("r") + name2.lower().count("r")
u = name1.lower().count("u") + name2.lower().count("u")
e = name1.lower().count("e") + name2.lower().count("e")

true = str(t+r+u+e)

l = name1.lower().count("l") + name2.lower().count("l")
o = name1.lower().count("o") + name2.lower().count("o")
v = name1.lower().count("v") + name2.lower().count("v")
e = name1.lower().count("e") + name2.lower().count("e")

love = str(l+o+v+e)

loveScore = true + love

if int(loveScore) < 10 or int(loveScore) > 90:
    print(f"Your score is {loveScore}, you go together like coke and mentos.")
elif int(loveScore) >= 40 and int(loveScore) <= 50:
    print(f"Your score is {loveScore}, you are alright together.")
else:
    print(f"Your score is {loveScore}.")