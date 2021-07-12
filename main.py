import random
i = 0
gameCheck = True 

while gameCheck:
    print("how many games do you want to play")
    try:
        games = int(input())
        if games < 0:
            print("choose a positive intiger")
        else: gameCheck = False
    except:
        print("please choose an intiger")



while i < games:
    point = 0

    x = random.randint(1, 10)
    try:
        print("guess the number between 1-10: ")
        y = int(input())
        if 0 < y < 11:
            if x == y:
                print("right guess!")
                point = point + 1
                i = i + 1
                print(f"{games}-{i} games remaining")
                continue
            else:
                print(f"the right guess is {x}")
                i = i + 1
                print(f"{games-i} games remaining")
                continue
        else:
            print("choose an intiger between 1-10") 

    except:
        print("choose an intiger between 1-10") 
        continue
print(f"Game over you have won {point} games out of {games}")


