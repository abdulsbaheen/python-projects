#This code is about email slicer
print("Welcome to email slicer")
email=input("\nEnter your email:")
if "@"and"." in email:
    username=email[0:email.index("@")]
    domain=email[email.index("@")+1::]

    print("\nusername:",username)
    print("\nDomain:",domain)
    print("Program has Ended.Thanks for interacting.")
else:
    print('ERROR, Invalid email format!')
    print("you forgot @ symbol!")    
