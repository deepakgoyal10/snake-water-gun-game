import random
i = 10
my_list = {"1": "Snake", "2": "Water", "3": "Gun"}
me = 0
comp = 0
while i > 0:
    try:
        i = i - 1
        game_elements = ("Snake", "Water", "Gun")
        d1 = random.choice(game_elements)
        d2 = input("\tChoose  1: Snake  2: Water  3: Gun\n")

        if d2 == "1" and d1 == "Snake" or d2 == "2" and d1 == "Water" or d2 == "3" and d1 == "Gun":
            print("tie! play again")
        elif d2 == "1" and d1 == "Water" or d2 == "2" and d1 == "Gun" or d2 == "3" and d1 == "Snake":
            print("you won")
            me = me + 1
        elif d2 == "1" and d1 == "Gun" or d2 == "2" and d1 == "Snake" or d2 == "3" and d1 == "Water":
            print("computer won!")
            comp = comp + 1
        else:
            print("invalid input")
        print("Computer chose:",d1, "|You chose:",my_list[d2], "|Round left",i,"\n" )
        if i == 0:
            print("Your score: ",me, "Computer score: ", comp)
            if comp > me:
                print("Computer Won this game")
            elif comp < me:
                print("You Won this game")
            else:
                print("its a tie")
    except Exception as error:
        print(error)
        print("Invalid input Try again\n")
