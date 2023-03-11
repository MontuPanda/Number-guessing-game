import random
print("Hello Folks - This is Number guessing game VERSION 2:")
print("__________________________________________________________")
print("The difference between Version 1 and Version 2 is that you can choose any range for infinite difficulties!")
print("You will have to enter both numbers in your range, the starting one and the ending")
print("Make sure that the second number has to be larger than the first!")
while True:
    dif=(input("Choose the first number in your range:-"))
    if not dif.isnumeric():
        print("Now you will do everything once again because you don't cooperate with the code")
        continue
    dif2=(input("Choose the second number in your range:-"))
    if not dif2.isnumeric():
        print("Now you will do everything once again because you don't cooperate with the code")
        continue
    if int(dif)>int(dif2):
        print("You have made the first number smaller than the second\nNow restart your journey")
        continue
    if int(dif)==int(dif2):
        print("You have made the first number equal to the second\nNow restart your journey")
        continue
    else:
        if (dif.isnumeric()) and (dif2.isnumeric()):
            num=random.randint(int(dif),int(dif2))
            if (int(dif2)-int(dif))>500:
                confirm=input("Are you sure you want to play with such a high number?\nType 'yes' or 'no':- ")                
                if confirm=="yes":
                    print("So you have chosen a custom difficulty of",int(dif),"to",int(dif2))
                    break
                if confirm=="no":
                    continue
                else:
                    print("Now you will do everything once again because you don't cooperate with the code")
            else:
                break
        else:
            print("Now you will do everything once again because you don't cooperate with the code")
loopCounter=0
print("The game has begun")
while True:
    inputValue=(input("Guess the number here->  "))
    loopCounter=loopCounter+1
    if (inputValue.isnumeric()):
        if int(inputValue)>int(dif2) or int(inputValue)<int(dif) :
            print("It's out of your range so try again")
        else:
            if num<int(inputValue):
                print("Try lower")
            if num>int(inputValue):
                print("Try higher")
            if num==int(inputValue):
                print("Congratulations, you got it")
                break
    else:
        print("Invalid")
        continue
print("Your tries: ",loopCounter)