import random
target=random.randint(0,101)
while True:
    userchoice=input("Enter your guess or press Q/q to quit")
    if(userchoice=="Q" or userchoice=="q" ):
        print("BAHAHAHAHAHHAHHAHAHAHAHA your number was", target)
        break
    userchoice=int(userchoice)
    if(userchoice==target):
        print("CONGRATS YOU GOT 10/10 INTUITION ON GUESSING")
        break
    elif(target<userchoice):
        print("The target is smaller than the number you just entered")
    else:
        print("The target is greater than the number you just entered")

