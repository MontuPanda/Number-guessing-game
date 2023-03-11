import random
print("Hello Folks - This is Number guessing game:")
print("_________________")
print("easy is between 1 and 25")
e=25
print("medium is between 1 and 100")
m=100
print("hard is between 1 and 200")
h=200
inputdict={'e':25, 'm':100, 'h':200}
while True:
    dif=input("Choose your difficulty by typing 'e' for easy 'm' for medium and 'h' for hard:-")
    break
while True:
    if dif!="e" and "m" and "h":
        print("Please type again as you have typed an invalid text")
        dif=input("Choose your difficulty by typing 'e' for easy 'm' for medium and 'h' for hard:-")
    if dif =="e" or "m" or "h":
        if dif=="e":
            num=random.randint(1,25)
            print("So you have chosen easy difficulty")
            break
        if dif=="m":
            num=random.randint(1,100)
            print("So you have chosen medium difficulty")
            break
        if dif=="h":
            num=random.randint(1,200)
            print("So you have chosen hard difficulty")
            break
loopCounter=0
print("The game has begun")
while True:
    inputValue=(input("Guess the number here->  "))
    loopCounter=loopCounter+1
    if (inputValue.isnumeric()):
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