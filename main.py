import random
'''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([-1, 0, 1])
you_str = input("Enter your choice: ")
you_dict = {"s": 1, "w": -1, "g": 0}
reverse_dict = {1: "Snake", -1: "Water", 0: "Gun"}
you = you_dict[you_str]

# By now we have 2 numbers (variables), you and computer

print(f"You chose {reverse_dict[you]} \nComputer chose {reverse_dict[computer]}")

if(computer == you):
    print("Its a draw!")

else:
    #  if((computer - you) == -1 or (computer - you) == 2):
    #    print("YOU LOSE!")
    #  else:
    #    print("YOU WIN!")

    if(computer == -1 and you == 0):
        print("YOU LOSE!")

    elif(computer == -1 and you == 1):
        print("YOU WIN!")

    elif(computer == 1 and you == 0):
        print("YOU WIN!")

    elif(computer == 1 and you == -1):
        print("YOU LOSE!")

    elif(computer == 0 and you == 1):
        print("YOU LOSE!")

    elif(computer == 0 and you == -1):
        print("YOU WIN!")

    else:
        print("Something went wrong!")