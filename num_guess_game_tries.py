import random
win=0
while True:
    diff=input("Enter 'e', 'm', 'h' or 'ex 'for easy medium hard and extreme:")
    if diff.lower()=="e":
        rand=random.randint(1,25)
        higher=25
        tries=8
        break
    elif diff.lower()=="m":
        rand=random.randint(1,100)
        higher=100
        tries=9
        break
    elif diff.lower()=="h":
        rand=random.randint(1,1000)
        higher=1000
        tries=11
        break
    elif diff.lower()=="ex":
        rand=random.randint(1,100)
        higher=100
        tries=1
        break
    else:
        print("invalid")
        continue
while tries>0:
    while True:
        guess=input("Guess number here:")
        if guess.isnumeric():
            guess=int(guess)
            break
        else:
            print("invalid")
            continue
    if guess<1 or guess>higher:
        print("out of bounds")
        continue
    elif guess>rand:
        print("try lower")
        tries=tries-1
        print(f"u have {tries} tries left")
    elif guess<rand:
        print("try higher")
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

    
