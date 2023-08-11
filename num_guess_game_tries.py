import random
import math
win=0
while True:
    diff=input("Enter 'e', 'm', 'h' or 'ex ' or 'custom' for easy medium hard and extreme and custom:")
    if diff.lower()=="e":
        rand=random.randint(1,25)
        higher=25
        lower=1
        tries=8
        break
    elif diff.lower()=="m":
        rand=random.randint(1,100)
        higher=100
        lower=1
        tries=9
        break
    elif diff.lower()=="h":
        rand=random.randint(1,1000)
        higher=1000
        lower=1
        tries=11
        break
    elif diff.lower()=="ex":
        rand=random.randint(1,100)
        higher=100
        lower=1
        tries=1
        break
    elif diff.lower()=="custom":
        while True:
            num1=input("Enter 1st number:")
            num2=input("Enter 2nd number:")
            if num1.isnumeric() and num2.isnumeric():
                num1, num2=int(num1), int(num2)
                if num2>num1:
                    rand=random.randint(num1,num2)
                    tries=round(math.log1p(num2-num1))
                    tries=tries*3
                    print(tries)
                    higher=num2
                    lower=num1
                    break
                else:
                    print("invalid range")
            else:
                print("Invalid, not integers")
        break
    else:
        print("invalid difficulty")
        continue
while tries>0:
    while True:
        guess=input(f"Guess number between {lower} and {higher} here:")
        if guess.isnumeric():
            guess=int(guess)
            break
        else:
            print("invalid")
            continue
    if guess<lower or guess>higher:
        print("out of bounds")
        continue
    elif guess>rand:
        print("try lower")
        higher=guess
        tries=tries-1
        print(f"u have {tries} tries left")
    elif guess<rand:
        print("try higher")
        lower=guess
        tries=tries-1
        print(f"u have {tries} tries left")
    elif guess==rand:
        tries=tries-1
        print("you won")
        win=win+1
        break
if win==0:
    print("u lost")
    print(f"also the number was {rand}")
if win==1:
    print(f"u won with {tries} tries left")

    
