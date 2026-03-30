# This program generate the password
import random,string

print("Welcome to password generator")
#we are going to create a pool of words for password generation
letters=''.join(random.choices(string.ascii_letters,k=5))
digits=''.join(random.choices(string.digits,k=3))
symbols="!@#*&"
#we are going to combine all the pool of words
pool_words=letters+symbols+digits
password=""
#we are going to ask the user for the length of password
user_input=int(input("\nEnter the length of password: "))
#we are going to generate the password by randomly selecting characters from the pool of words
for i in range (user_input):
    comp_choice=random.choice(pool_words)
    password+=comp_choice
print("\nYour strong password is :",password)    
print("\nThank you for using password generator")