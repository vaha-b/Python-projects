# https://hyperskill.org/projects/68/stages/370/implement


water = 400
milk = 540
beans = 120
cups = 9
money = 550


def coffe_machine():
    machine_runs = True

    while machine_runs:
        user_input = input("Write action (buy, fill, take, remaining, exit:\n")
        print()

        if user_input == "buy":
            buy()
        elif user_input == "fill":
            fill()
        elif user_input == "take":
            take()
        elif user_input == "remaining":
            remaining()
        elif user_input == "exit":
            machine_runs = False


def buy():
    coffe_type = input(
        "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
    print()

    global water, milk, beans, cups

    if coffe_type == "1":
        if water >= 250 and beans >= 16 and cups >= 1:
            print("I have enough resources, making you a coffee!")

            water -= 250
            beans -= 16
            cups -= 1

            # print(f"{milk} of milk")
            # print(f"{beans - 16} of coffe beans")
            # print(f"{cups - 1} of disposable cups")
            # print(f"${money + 4} of money")
    elif coffe_type == "2":
        if water >= 350 and milk >= 75 and beans >= 20 and cups >= 1:
            print("I have enough resources, making you a coffee!")

            water -= 350
            milk -= 75
            beans -= 20
            cups -= 1

            # print(f"{water - 250} of water")
            # print("The coffe machine has:")
            # print(f"{water - 350} of water")
            # print(f"{milk - 75} of milk")
            # print(f"{beans - 20} of coffe beans")
            # print(f"{cups - 1} of disposable cups")
            # print(f"${money + 7} of money")
    elif coffe_type == "3":
        if water >= 200 and milk >= 100 and beans >= 12 and cups >= 1:
            print("I have enough resources, making you a coffee!")

            water -= 200
            milk -= 100
            beans -= 100
            cups -= 1

            # print(f"{water -= 200} of water")
            # print(f"{milk -= 100} of milk")
            # print(f"{beans -= 12} of coffe beans")
            # print(f"{cups -= 1} of disposable cups")
            # print(f"${money += 6} of money")
        # else:
        # 	print("I don't have enough resources!")

    elif coffe_type == "back":
        coffe_machine()

    print()


def fill():
    added_water = int(input("Write how many ml of water do you want to add: "))
    added_milk = int(input("Write how many ml of milk do you want to add: "))
    added_beans = int(
        input("Write how many grams of coffee beans do you want to add: "))
    added_cups = int(
        input("Write how many disposable cups of coffee do you want to add: "))

    global water, milk, beans, cups

    water += added_water
    milk += added_milk
    beans += added_beans
    cups += added_cups

    print()


def take():
    print(f"I gave you ${money}")
    print()


def remaining():
    print(f"{water} of water")
    print(f"{milk} of milk")
    print(f"{beans} of coffe beans")
    print(f"{cups} of disposable cups")
    print(f"${money} of money")
    print()


def state():
    print("")
    print("The coffe machine has:")
    print(f"{water} of milk")
    print(f"{beans} of coffe beans")
    print(f"{cups} of disposable cups")
    print(f"{money} of money")
    print()
