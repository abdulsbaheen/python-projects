# Number guessing game
print("This  is a number guessing game.")
import random

comp_guess=random.randint(1,100)

attempt = 0
max_attempt=7

while attempt < max_attempt:
    user_guess=float(input("\nEnter a number between 1 and 100 :"))
    attempt=attempt+1

    if comp_guess==user_guess:
        print("\ncongratulations! You won the game.")
        break
    elif(comp_guess<user_guess):
        print("\nyour guess is Too high.")
    elif(comp_guess>user_guess):
        print("\nyour guess is Too low.")

    print(f"\nyour remaining attempts are {max_attempt-attempt}") 

if attempt==max_attempt and comp_guess!=user_guess:
    print("\nsorry you reach your maximum attempts and you lost!")    
    print(f"The computer guess is {comp_guess}")   



