promt = "\n Tell me something, and I will repeat it back to you: "
promt += "\nEnter 'quit' to end the program. "

while True:
    city = input(promt)

    if city == 'quit':
        break

    else:
        print("I'd love to go to " + city.title() + "!")

