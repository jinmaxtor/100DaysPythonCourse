print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

left_or_right_message = "You're at a cross road. Where do you want to go? Type 'left' or 'right' "
swim_or_wait_message = "You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a " \
                       "boat. Type 'swim' to swim across."
red_yellow_blue_message = "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and " \
                          "one blue. Which colour do you choose?"

if input(left_or_right_message) == "left":
    if input(swim_or_wait_message) == "wait":
        if input(red_yellow_blue_message) == "yellow":
            print("You found the treasure! You win!")
        else:
            print("Game Over.")
    else:
        print("Game Over.")
else:
    print("Game Over.")
