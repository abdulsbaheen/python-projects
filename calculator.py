def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
        return "Error ! Division by zero"
    else:
        return x/y
    
print("simple calculatpr")    
print("1. Addition")    
print("2. Subtraction")    
print("3. Multiplication") 
print("4. Division")   

while True:
    choice =input("Enter your choice(1/2/3/4):")

    if choice in ('1','2','3','4'):
        num1 =float(input("enter first number:"))
        num2 =float(input("enter second number:"))

     
    if choice =='1':
          print(num1,"+",num2,"=",add(num1,num2))
    elif choice =='2':
          print(num1,"-",num2,"=",subtract(num1,num2))
    elif choice =='3':
          print(num1,"*",num2,"=",multiply(num1,num2))
    elif choice =='4':
          print(num1,"/",num2,"=",divide(num1,num2))
          
    next_calculation=input("let's do next calculation? (yes/no):")
    if next_calculation!='yes':
         break
    else:
         print("Ok let's start  next calculations")