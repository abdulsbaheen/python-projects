# this program is used to encrypt or decrypt a message
print("""Greetings User,
      This is a simpe text encription and decription program.""")
# import pyhton libraries like random and string
import random ,string
# take input from user and split it 

message = input("Enter your message: ")
words =message.split(" ")

# ask user for encrypt or decrypt a message 
choice=input("Enter 1 for Encryption or 0 for Decryption: ")
coding = True if (choice=="1") else False
# check condition 
if (coding):
    new_words = []
    for word in words:
        if (len(word) >= 3):
          # take the random string 
          r1=''.join(random.choices(string.ascii_letters + string.digits, k=4))
          r2=''.join(random.choices(string.ascii_letters + string.digits, k=4))
          # make a new word string
          stnew = r1 + word[1:] +word[0] +r2
          # add new word to a new list at end 
          new_words.append(stnew)
        else:
            new_words.append(word[::-1])
    print(" ".join(new_words))
else:
  new_words = []
  for word in words:
    if (len(word) >= 3):
      # access the items of the word from index 3 to last 3 index
      stnew =word[3:-3]
      stnew =stnew[-1] + stnew[:-1]
      # Add the new word to list 
      new_words.append(stnew)
    else:
         new_words.append(word[::-1])
  print(" ".join(new_words))

print("Thank you for using the program. Goodbye!")
print("This program is written by {Abdul-Rehman Azam}")