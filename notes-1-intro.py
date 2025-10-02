# Notes - Introduction
# Sept 16
# Eric Gao

greeting = "Hello! I am a chatbot."

print(greeting)
name = input("What is your name? ")

how_day = input("Hi " + name + " ! How's your day? ")
if (how_day == "good" or how_day == "great" or how_day == "awesome"):
    print("That's nice!")
else:
    print("Well, I hope your day get better!")

food = input("What is your favourite food? ")
print("Wow ok! I love " + food + " as well.")

drink = input("What is your favourite drink? ")
print(drink + " is a good choice.")

print("That's all I can say for now. Bye " + name + " !")
