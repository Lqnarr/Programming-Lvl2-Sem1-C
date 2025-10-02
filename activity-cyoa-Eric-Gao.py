import time
import sys


def main():
    global name, mood, energy, money, social
    name = input("Hello friend! What is your name? ")
    mood = 10
    energy = 10
    money = 20
    social = 0
    time.sleep(0.5)
    print(f"Hello {name}, welcome to the skiing adventure!")
    time.sleep(0.5)
    game()


def game():
    global mood, energy, social
    time.sleep(0.5)
    print("You plan to go skiing at Whistler. Which day are you going? ")
    time.sleep(0.5)
    print("a. Monday (Sunny but icy)")
    time.sleep(0.5)
    print("b. Wednesday (Powder snow but low visibility)")
    time.sleep(0.5)
    print("c. Saturday (Windy & Crowded)")
    time.sleep(0.5)
    print("d. Not going skiing! ")
    time.sleep(0.5)
    dayOfWeek = input("You choose: ")
    if dayOfWeek.lower() == "a":
        time.sleep(0.5)
        print("Wow, you like ice huh?")
        time.sleep(0.5)
        askSkiType()
        if typeSki == "skinny":
            print("Good choice. You stayed stable on the icy terrain.")
            mood = 10
        else:
            print("Bad choice. You lost control on a patch of ice and fell! ")
            mood = 5
    elif dayOfWeek.lower() == "b":
        time.sleep(0.5)
        print("Powder day is a good choice.")
        time.sleep(0.5)
        askSkiType()
        if typeSki == "skinny":
            print(
                "Too skinny! You sank in powder often and got tired trying to get out."
            )
            mood = 5
            energy -= 5
        else:
            print("Good choice. You had a blast in powder!!")
            mood = 15
            energy -= 2
    elif dayOfWeek.lower() == "c":
        time.sleep(0.5)
        print("Ooof, so many people there. ")
        time.sleep(0.5)
        print(
            "You spent more time waiting in line than skiing. But at least you skied, right?"
        )
        mood = 5
        social += 3
    elif dayOfWeek.lower() == "d":
        time.sleep(0.5)
        print("Why would you not go skiing??? It is the best sport!")
        time.sleep(0.5)
        mood = 0
    else:
        print("Sorry I don't understand your input.")
        game()

    if mood > 0:
        lunch()
    else:
        ending()
        tryAgain()


def askSkiType():
    global typeSki
    print("Do you want to use: ")
    time.sleep(0.5)
    typeSki = input(
        "Skinny skis (good on hard snow) or Wide skis (good for powder snow)? (skinny/wide): "
    )
    typeSki = typeSki.lower()


def lunch():
    global mood, energy, money
    time.sleep(0.5)
    print("After skiing a bit, it's lunch time. What do you want to eat?")
    time.sleep(0.5)
    print("a. Expensive burger and fries in the chalet")
    time.sleep(0.5)
    print("b. Instant noodles you packed")
    time.sleep(0.5)
    print("c. Skip lunch and keep skiing")
    choice = input("You choose: ")
    if choice.lower() == "a":
        print("The burger was good, but your wallet is now empty.")
        mood += 5
        money -= 10
        energy += 5
    elif choice.lower() == "b":
        print("It wasn’t fancy, but you're full. You saved some money!")
        mood += 10
        money -= 2
        energy += 3
    elif choice.lower() == "c":
        print("You felt hungry all afternoon and was exhausted.")
        mood -= 5
        energy -= 5
    else:
        print("Sorry I don't understand your input.")
        lunch()

    friends()


def friends():
    global mood, social
    time.sleep(0.5)
    print("After lunch, do you ski alone or with friends?")
    time.sleep(0.5)
    print("a. Ski alone and go wherever you want")
    time.sleep(0.5)
    print("b. Ski with friends even if they are slower than you")
    choice = input("You choose: ")
    if choice.lower() == "a":
        print("You ended up skiing every run you wanted!")
        mood += 5
    elif choice.lower() == "b":
        print("You didn't get to ski much, but had good chairlift convos :)")
        social += 10
    else:
        print("Sorry I don't understand your input.")
        friends()

    night()


def night():
    global energy, mood
    time.sleep(0.5)
    print("The sun is setting. Do you want to go night skiing or call it a day?")
    time.sleep(0.5)
    print("a. Go night skiing, even though you're tired")
    time.sleep(0.5)
    print("b. End the day and rest")
    choice = input("You choose: ")
    if choice.lower() == "a":
        print(
            "You pushed yourself for a few more runs. It was worth it, just exhausted."
        )
        mood += 5
        energy -= 10
    elif choice.lower() == "b":
        print("You ended early, and had plenty of energy on the way back home.")
        mood += 10
        energy += 5
    else:
        print("Sorry I don't understand your input.")
        night()

    time.sleep(0.5)

    ending()
    tryAgain()


def tryAgain():
    goAgain = input("Do you want to go again? (y/n) ")
    if goAgain.lower() == "y":
        main()
    elif goAgain.lower() == "n":
        print(f"Have a good day {name} !")
        sys.exit()
    else:
        print("Sorry I don't understand.")
        tryAgain()


def ending():
    time.sleep(0.5)
    print(f"Game Over! Thank you for playing {name} !")
    global mood, energy, money, social

    print("Your ending:")

    if mood <= 0:
        print("You had a terrible day.")
    elif energy <= 0:
        print(
            "You skied until you could barely stand up. You’ll be sleeping until noon the next day."
        )
    elif money <= 0:
        print("You had fun but spent way too much. Your wallet is crying.")
    elif social >= 10:
        print("It wasn’t the best skiing, but hanging with friends made it special.")
    elif mood >= 20 and energy > 5:
        print("This was one of your best days on the mountain. Pure joy.")
    else:
        print("Overall, it was a pretty average ski trip. Not bad, not amazing.")


main()
