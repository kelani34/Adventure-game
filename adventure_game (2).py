
import time  # Imports a module to add a pause of  sec
import random
import string
# Grabbing objects
weapon = ["sword",  "spear", "dagger"]
armour = 0
flower = 0
arm = random.choice(weapon)


def typewriter_simulator(message):
    for char in message:
        print(char, end='')
        if char in string.punctuation:
            time.sleep(.5)
        time.sleep(.03)
    print('')


def print_pause(message, delay=1):
    typewriter_simulator(message)
    time.sleep(delay)


def valid_input(prompt, options):
    while True:
        response = input(prompt)
        for option in options:
            if option in response:
                return response
        print_pause("Please write a valid number.")


def end_game():
    print_pause("Looks like you died....")
    response = valid_input("Would you like to play again\n"
                           "1 - Yes\n"
                           "2 - No\n", ["1", "2"])
    if response == "1":
        intro()
    else:
        print_pause("It was fun having you around. "
                    "Try again later.")
        exit(0)


def intro():
    print_pause("After a drunken night out with friends,\
 you awaken the ")
    print_pause("next morning in a thick, dank forest.\
 Head spinning and ")
    print_pause("fighting the urge to vomit, you stand\
 and marvel at your new, ")
    print_pause("unfamiliar setting. The peace quickly\
 fades when you hear a ")
    print_pause("grotesque sound emitting behind you.\
 A slobbering orc is running towards you ")
    print("""
  1. Grab a nearby rock and throw it at the orc
  2. Lie down and wait to be mauled
  3. Run
  """)
    choice = valid_input(">>> ", ["1", "2", "3"])
    if choice == "1":
        option_rock()
    elif choice == "2":
        print("\nWelp, that was quick. "
              "\n\nYou died!")
        end_game()
    elif choice == "3":
        option_run()


def option_rock():
    print_pause("\nThe orc is stunned, but regains\
 control. He begins "
                "running towards you again. Will you:")
    print("""
  1. Run
  2. Throw another rock
  3. Run towards a nearby cave
  """)
    choice = valid_input(">>> ", ["1", "2", "3"])
    if choice == "1":
        option_run()
    elif choice == "2":
        print("\nYou decided to throw another rock,\
 as if the first "
              "rock thrown did much damage. The rock\
 flew well over the "
              "orcs head. You missed. \n\nYou died!")
        end_game()
    elif choice == "3":
        option_cave()


def option_cave():
    print_pause("\nYou were hesitant, since the cave was dark\
 and ")
    print_pause(
        "As you walk inside, a text on the wall of the cave")
    print_pause(
        "'This is a treasure cave with a good heart comes good treasure.'")
    print_pause(
        "Inside the box is exists a death wish or a useful item.")
    print_pause(
        "If you open it, you will either get a useful item "
        "or you will die.")
    print_pause(
        "'I would turn back if I was in your place. You know just saying. '")
    print_pause("What will you do?\n"
                "1 - Open the chest.\n"
                "2 - Turn back.\n")
    choice = valid_input(">>> ", ["1", "2"])
    if choice == "1":
        armour = 1  # adds a armour
        print_pause("Despite the warnings, you try to open "
                    "the chest and...")
        choices = ["good heart", "bad heart"]
        if random.choice(choices) == "good heart":
            print_pause("Looks like you have a really good heart.")
            print_pause("Thankfully you are not dead.")
            print_pause(f"Inside there was a {arm}")
            print_pause(f"You return outside of the cave with your new {arm}")

        else:
            end_game()
    else:
        armour = 0
    print("\nWhat do you do next?")
    time.sleep(1)
    print("""
  1. Hide in silence
  2. Fight
  3. Run""")
    choice = valid_input(">>> ", ["1", "2", "3"])
    if choice == "1":
        print("\nReally? You're going to hide in the dark?\
 I think "
              "orcs can see very well in the dark, right?\
 sure, but "
              "I'm going with YES, so...\n\nYou died!")
        end_game()
    elif choice == "2":
        if armour > 0:
            print(f"\nYou laid in wait. The shimmering {arm}\
 attracted "
                  "the orc, which thought you were no match.\
 As he walked "
                  "closer and closer, your heart beat rapidly.\
 As the orc "
                  f"reached out to grab the {arm}, you pierced\
 the blade into "
                  "its chest. \n\nYou survived!")
        else:  # If the user didn't grab the weapon
            print(f"\nYou should have opened up the\
 chest. You're "
                  "defenseless."
                  "There is no hope Maybe you should have opened the chest")
            end_game()
    elif choice == "3":
        print("As the orc enters the dark cave,\
 you sliently "
              "sneak out. You're several feet \
 away, but the orc turns "
              "around and sees you running.")
        option_run()


def option_run():
    print("\nYou run as quickly as possible,\
 but the orc's "
          "speed is too great. You will:")
    time.sleep(1)
    print("""
  1. Hide behind boulder
  2. Trapped, so you fight
  3. Run towards an abandoned town
  """)
    choice = valid_input(">>> ", ["1", "2", "3"])
    if choice == "1":
        choices = ["invisible", "visible"]
        if random.choice(choices) == "Invisible":
            print_pause("Thankfully you are not spotted by the orc.")
            print_pause("You spot a nearby town")
            option_town()
        else:
            print_pause("You were easily spotted by the orc")
            end_game()
    elif choice == "2":
        print("\nYou're no match for an orc. ")
        end_game()
    elif choice == "3":
        option_town()


def option_town():
    print("\nWhile frantically running, you \
 notice a rusted "
          f"{arm} lying in the mud. You quickly\
 reach down and grab it, "
          "but miss. You try to calm your heavy\
 breathing as you hide "
          "behind a delapitated building, waiting\
 for the orc to come "
          "charging around the corner. You notice\
 a purple flower "
          "near your foot. Do you pick it up? "
          "1 - Yes\n"
          "2 - No\n")
    choice = valid_input(">>> ", ["1", "2"])
    if choice == "1":
        flower = 1
    else:
        flower = 0
    print_pause("You hear its heavy footsteps and ready yourself for "
                "the impending orc.")
    if flower > 0:
        print("\nYou quickly hold out the purple \
 flower, somehow "
              "hoping it will stop the orc. It does!\
 The orc was looking "
              "for love. "
              "\n\nThis got weird, but \
 you survived!")
    else:
        print("\nMaybe you should have picked up\
 the flower. ")
        end_game()


if __name__ == '__main__':
    intro()
