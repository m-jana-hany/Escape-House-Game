import time
import random


def print_pause(text):
    print(text)
    time.sleep(2)


# Random door colors to ensure changes in the game each time
door1 = random.choice(["red", "black"])
door2 = random.choice(["green", "grey"])
door3 = random.choice(["blue", "white"])


def score_update(score):
    print(f"Your current score is {score}")  # let user know his score


def game():
    score = 0
    wrong_choices = 0  # if wrong choices exceed 3, you'll only lose.
    # ensure user gets all items req
    items = {"chair": False, "gas mask": False, "key": False}
    rooms_visited = {
        "red/black": False,
        "green/grey": False,
        "blue/white": False,
    }  # prevent re-entry

    # Description of the player's state so he can play
    print_pause(
        "You are in a scary, dimly lit house. You wander "
        "around and find three closed "
        f"doors: {door1}, {door2}, and {door3}."
    )
    print_pause(
        "You have 3 keys for the rooms, a flashlight,"
        " a match, a rope, and a stick."
    )
    print_pause(
        "You have only 2 hours to escape the house."
        " You have two ways, the closed door "
        "and the high locked window."
    )
    print("Will you wander again? (1)\nWill you "
          "open rooms? (2)\nEnter 'q' to quit.\n")

    while not all(rooms_visited.values()):
        print(
            "Will you wander again? (1)\nWill you open "
            "rooms? (2)\nEnter 'q' to quit.\n"
        )
        choice = input("Your choice 1/2/q: ")
        match choice:
            case "1":
                print_pause(
                    "\nYou are now wandering again in the "
                    "house, you found nothing.\n"
                )
                print_pause(
                    "The game decides you choose a room to open."
                    " You stand in front of the "
                    "doors now.\n"
                )
                print(
                    f"Choose {door1} (1) or {door2} (2) "
                    f"or {door3} (3) or q to quit\n"
                )
                room_choice = input("Your choice 1/2/3/q: ")
                score -= 10
                wrong_choices += 1
                score, wrong_choices, items, rooms_visited = enter_room(
                    room_choice, score, wrong_choices, items, rooms_visited
                )
                # the above code updates the parameters to avoid using global
                # var
                score_update(score)
            case "2":
                print_pause("\nYou stand in front of the three doors.\n")
                print(
                    f"Choose {door1} (1) or {door2} (2) or"
                    f" {door3} (3) or q to quit\n"
                )
                room_choice = input("Your choice 1/2/3/q: ")
                score += 10
                score, wrong_choices, items, rooms_visited = enter_room(
                    room_choice, score, wrong_choices, items, rooms_visited
                )
                score_update(score)
            case "q":
                exit_game(score)
                return
            case _:
                print("Invalid input!! Please enter 1, 2 or q.")

    final_escape(score, wrong_choices, items)


def enter_room(choice, score, wrong_choices, items, rooms_visited):
    if choice == "1" and not rooms_visited["red/black"]:
        return enter_red_black(score, wrong_choices, items, rooms_visited)
    elif choice == "2" and not rooms_visited["green/grey"]:
        return enter_green_grey(score, wrong_choices, items, rooms_visited)
    elif choice == "3" and not rooms_visited["blue/white"]:
        return enter_blue_white(score, wrong_choices, items, rooms_visited)
    elif choice == "q":
        exit_game(score)
        return score, wrong_choices, items, rooms_visited
    else:
        print("Invalid input or room already visited! "
              "Please enter 1, 2, 3 or q.")
        return score, wrong_choices, items, rooms_visited


def enter_red_black(score, wrong_choices, items, rooms_visited):
    animal = random.choice(["wolf", "crocodile", "bear"])
    print_pause(f"You opened the {door1} door. In front"
                f" of you lies a {animal}.")
    print_pause(
        "Will you fight him with the stick? (1)\nOr scare him"
        " using the match? (2)\nq "
        "for Quit"
    )
    reaction_door1 = input("Enter 1/2/q: ")
    match reaction_door1:
        case "1":
            score -= 10
            wrong_choices += 1
            print_pause(
                f"The {animal} attacks you until you get out of the "
                "room. You are not Tarzan or Tsukasa."
            )
            print_pause(
                "Game made you enter, use the match and scare him,"
                " then you earned a CHAIR."
            )
        case "2":
            print_pause("You scared it away, you earned a CHAIR.")
            print_pause("Good you thought well or you'd be injured.")
            score += 10
        case "q":
            exit_game(score)
            return score, wrong_choices, items, rooms_visited
        case _:
            print("Invalid input!! Please enter 1, 2 or q.")
    items["chair"] = True
    rooms_visited["red/black"] = True
    return score, wrong_choices, items, rooms_visited


def enter_green_grey(score, wrong_choices, items, rooms_visited):
    print_pause(f"You opened the {door2} door with your keys.")
    print_pause("You found out there's poisonous gas in it.")
    print_pause(
        "Will you use the rope to hold the door open? (1)\nOr"
        " enter fast and find clues? (2)\nOr q for quit."
    )
    reaction_door2 = input("Enter 1/2/q: ")
    match reaction_door2:
        case "1":
            print_pause(
                "You chose wisely. You entered and earned a gas mask"
                " to save you later!"
            )
            score += 10
        case "2":
            print_pause("Oops! You get slightly suffocated and escape "
                        "the room fast.")
            print_pause("Thank god your choices didn't kill you, bud.")
            print_pause("You use the rope and get a gas mask to save"
                        " you later.")
            score -= 10
            wrong_choices += 1
        case "q":
            exit_game(score)
            return score, wrong_choices, items, rooms_visited
        case _:
            print("Invalid input!! Please enter 1, 2 or q.")
    items["gas mask"] = True
    rooms_visited["green/grey"] = True
    return score, wrong_choices, items, rooms_visited


def enter_blue_white(score, wrong_choices, items, rooms_visited):
    print_pause(f"You opened the {door3} door with your keys.")
    print_pause(
        "You're hearing faint whispers. A ghost floats in the"
        " center of the room."
    )
    print_pause(
        "Will you ignore it? (1)\nOr try to use your flashlight so"
        " it goes away? (2)\nOr q for quit."
    )
    reaction_door3 = input("Enter 1/2/q: ")
    match reaction_door3:
        case "1":
            print_pause("Nope!!! The ghost gets FURIOUS and"
                        " screams at you ROUGH.")
            print_pause(
                "In reaction, you panic and wave the flashlight. It"
                " disappears and you find a KEY."
            )
            score -= 10
            wrong_choices += 1
        case "2":
            print_pause(
                "The ghost immediately disappears when you wave your"
                " flashlight. It appears that it hates light."
            )
            print_pause("You got a KEY as a reward!")
            score += 10
        case "q":
            exit_game(score)
            return score, wrong_choices, items, rooms_visited
        case _:
            print("Invalid input!! Please enter 1, 2 or q.")
    items["key"] = True
    rooms_visited["blue/white"] = True
    return score, wrong_choices, items, rooms_visited


def final_escape(score, wrong_choices, items):
    score_update(score)  # Show score before final escape message
    if all(items.values()):  # Check if all items have been collected
        print_pause("\nAfter finally collecting all items!")
        print_pause("You use the chair to reach the window.")
        print_pause(
            "You use the key to unlock the window and the stick"
            " to break the glass."
        )
        print_pause("You finally escape the house!")
        if wrong_choices >= 3:
            print_pause(
                "However, you needed a lot of help from the game host due to "
                "your poor choices, so you FAILED>"
            )
            print_pause("You need to practice depending on yourself more.")
        else:
            print_pause("Congrats! You escaped successfully on your "
                        "own and WON!")
    else:
        print_pause("You haven't collected all the necessary items.")
        print_pause(
            "You need to revisit some rooms to gather all the"
            " items before you can escape."
        )
    play_again()


def exit_game(score):
    score_update(score)  # Show score before ending the game
    print_pause("Thank you for playing! You ended this round.\n")
    play_again()


def play_again():
    choice = input("Do you want to play again? (y/n): ").lower()
    if choice == "y":
        game()
    elif choice == "n":
        print_pause("Goodbye! See you again soon.")
    else:
        print("Enter a valid input (y/n).")
        play_again()
