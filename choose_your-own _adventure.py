name = input("Type your name; ")
print("Welcome", name, "to this adventure!")

answer = input(" You are on a dirt road, it has come to and end and you can go left or right. which way do you want to go? ")

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim. Type walk to walk or swim to swim.")

    if answer == "swim":
        print("You swam across and were eaten by an alligator.")

    elif answer == "walk":
        print("You walked for many miles, ran out of ewater and you lost the game")

    else:
        print("Not a valid option. you lose")

elif answer == "right":
    answer = input("You come to a bridge it looks wobbly, do you want to cross or go back?")
    if answer == "back":
        print("You go back andd lode")

    elif answer == "cross":
        print("You cross the bridge and meet a stranger. Do you talk to them? (Yes/No)")

        if answer == "Yes":
            print("You talk to the stranger and they give you gold . You Won!")

        elif  answer =="no":
            print("You ignore the stranger and they offended. You lose!")
        else:
            print('Not valid option. You Lose')

    else:
        print("Not a valid option. you lose")

else:
    print('Not a valid option, you lose ')

print('Thank you for trying', name)