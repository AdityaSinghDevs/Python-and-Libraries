# -----------------------------
# YOU GUESS THE NUMBER
# -----------------------------
# import random

# def guess(x):
#   print(f"TRY GUESSING A NUMBER BETWEEN 1 AND {x}")
#   rndm_num= random.randint(1,x)
  
#   guess=0
  
#   while guess != rndm_num:
#     guess=int(input("ENTER YOUR GUESS :"))
    
#     if guess < rndm_num:
#       print("Sorry, Wrong guess, GUESS AGAIN!, TOO LOW")
      
#     elif guess > rndm_num:
#       print("Sorry, Wrong guess, GUESS AGAIN!, TOO HIGH")
      
#   print(f"WOOHOO! CONGRATS CORRECT GUESS!, i.e,{rndm_num}")
  
# guess(100)  

# # --------------------------------
# # Computer guesses the number
# # ---------------------------------

# import random
  
# def guess(x):
#   low_range =1
#   high_range=x
#   feedback= ''
 
#   print(f"Think about a no. between 1 and {high_range}")
  
#   while feedback!='c': 
#     if low_range!=high_range:
#      guess= random.randint(low_range,high_range)
#     else:
#      guess=low_range
#     feedback=input(f"Your Number is {guess},IS IT\nCORRECT?(C)\nIS IT TOO LOW(L)\nIS IT TOO HIGH(h)?").lower()
#     if feedback=='l':
#        low_range=guess+1
#     elif feedback=='h':
#        high_range=guess-1
       
#   print("Thanks for Playing")     
    
# guess(10000)  


  
      
  
  
    
  