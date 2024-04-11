#------------------------------
   #Random number guessing game
#------------------------------
import random

print("\nYou'll be given 3 tries to guess the number\n\nfor each correct guess you'll be rewarded 20pts\n\nand for each wrong guess 20pts will be deducted")

a=int(input("\nEnter starting number for range :"))
b=int(input("\nEnter ending number for range   :"))
x=0

c= random.randint(a,b)

d=int(input("\nEnter your first guess :"))
if d==c:
    x=x+20
    c=c+1
    print(f"congrats correct guess +20 pts\n total points:{x}")

else:
    x=x-20
    print(f"oops wrong guess -20 pts\n total points:{x}")

e=int(input("Enter your second guess :"))
if e==c:
    x=x+20
    c=c-2
    print(f"congrats correct guess +20 pts\n total points:{x}")

else:
    x=x-20
    print(f"oops wrong guess -20 pts\n total points:{x}")
    
f=int(input("Enter your Third guess :"))
if f==c:
    x=x+20
    c=c+1
    print(f"congrats correct guess +20 pts\n total points:{x}")

else:
    x=x-20
    print(f"oops wrong guess -20 pts\n total points:{x}\n\n   --------BETTER LUCK NEXT TIME-------- \n\n")
