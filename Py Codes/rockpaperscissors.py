import random

def play():
 user=input("WHATS YOUR CHOICE\n(r) for Rock\n(p) for Paper\n(s) for scissors\n")
 comp=random.choice(['r','p','s']).lower()
 
 if user==comp:
   return "tie"
 if is_win(user,comp):
   return ("YOU WON")
   
 return "YOU LOST"  
 
def is_win(player,opponent):
   if player=='r' and opponent=='s' or player=='p' and opponent=='r' or player=='s' and opponent=='p':
     return True
   
print(play())   
   
  