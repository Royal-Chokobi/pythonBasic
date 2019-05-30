import random

m = input("Enter your choice : ").upper()
x = ["R", "P", "S"]
# R : 바위, P : 보 , S:가위
z = random.choice(x)
msg = ""
if z == m:
    msg = "It`s a tie"
elif z == "R" and m == "P":
    msg = "choice is rock, You win"
elif z == "R" and m == "S":
    msg = "choice is rock, You lose"
elif z == "P" and m == "R":
    msg = "choice is rock, You lose"
elif z == "P" and m == "S":
    msg = "choice is rock, You win"
elif z == "S" and m == "R":
    msg = "choice is rock, You win"
elif z == "S" and m == "P":
    msg = "choice is rock, You lose"

print("Computer chooses : {}".format(z))
print(msg)