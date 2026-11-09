def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
while True:
    choice=input("Enter 1 for addition,2 for subtraction, 3 for multiplication,4 for divison and 5 to exit")
    if(choice==1 or choice==2 or choice==3 or choice==4 or choice==5):
        try:
            num1=float(input("Enter a number"))
            num2=float(input("Enter a number"))
        except ValueError:
            print("Enter a valid number")
            continue
        if(choice==1):
            print(add(num1,num2))
        elif(choice==2):
            print(sub(num1,num2))
        elif(choice==3):
            print(mul(num1,num2))
        elif(choice==4):
            print(div(num1,num2))
        elif(choice==5):
            break
    else:
        print("Enter either 1,2,3,4 or 5 according toi the given menu")

