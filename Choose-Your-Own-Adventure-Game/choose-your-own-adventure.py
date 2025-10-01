name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

q1 = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if q1 == "left":
    q2 = input("You come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim across: ").lower()

    if q2 == "walk":
        print("You walked for many miles, ran out of water, and lost the game.")
    elif q2 == "swim":
        print("You swam across and were eaten by an alligator.")
    else:
        print("Not a valid option. You lose.")

elif q1 == "right":
    q3 = input("You come to a bridge, it looks wobbly, do you want to cross it or head back? Type cross or back: ").lower()

    if q3 == "cross":
        q4 = input("You cross the bridge and meet a stranger. Do you talk to them? yes or no: ").lower()

        if q4 == "yes":
            print("You talk to the stranger and they give you gold!. You win!")
        elif q4 == "no":
            print("You ignore the stanger and they are offended and you lose.")
        else:
            print("Not a valid option. You lose.")
            
    elif q3 == "back":
        print("You go back and lose.")
    else:
        print("Not a valid option. You lose.")
else:
    print("Not a valid option. You lose.")