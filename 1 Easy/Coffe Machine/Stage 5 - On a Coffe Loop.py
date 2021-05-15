# About the project:
# https://hyperskill.org/projects/68?track=2

# Stage description
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


# better


money = 550
water = 400
milk = 540
beans = 120
cups = 9


class ResourceError(Exception):
    pass


def print_state():
    print()
    print('The coffee machine has:')
    print(f'{water} of water')
    print(f'{milk} of milk')
    print(f'{beans} of coffee beans')
    print(f'{cups} of disposable cups')
    print(f'{money} of money')
    print()


def select_action() -> str:
    return input('Write action (buy, fill, take, remaining, exit): ')


def select_flavor() -> int:
    print()
    response = input('What do you want to buy?'
                     ' 1 - espresso,'
                     ' 2 - latte,'
                     ' 3 - cappuccino,'
                     ' back - to main menu: ')
    if response == 'back':
        return 0
    return int(response)


def is_enough(need_water=0, need_milk=0, need_beans=0):
    if water < need_water:
        print('Sorry, not enough water!\n')
        raise ResourceError
    if milk < need_milk:
        print('Sorry, not enough milk!\n')
        raise ResourceError
    if beans < need_beans:
        print('Sorry, not enough beans!\n')
        raise ResourceError
    if cups < 1:
        print('Sorry, not enough cups\n')
        raise ResourceError
    print('I have enough resources, making you a coffee!\n')


def buy():
    global money, water, milk, beans, cups

    flavor = select_flavor()

    try:
        if flavor == 0:
            pass
        elif flavor == 1:  # espresso
            is_enough(need_water=250, need_beans=16)

            money += 4
            water -= 250
            beans -= 16
            cups -= 1
        elif flavor == 2:  # latte
            is_enough(need_water=350, need_milk=75, need_beans=20)

            money += 7
            water -= 350
            milk -= 75
            beans -= 20
            cups -= 1
        elif flavor == 3:  # cappuccino
            is_enough(need_water=200, need_milk=100, need_beans=12)

            money += 6
            water -= 200
            milk -= 100
            beans -= 12
            cups -= 1
        else:
            raise ValueError(f'Unknown flavor {flavor}')
    except ResourceError:
        pass


def fill():
    global water, milk, beans, cups

    print()
    water += int(input('Write how many ml of water do you want to add: '))
    milk += int(input('Write how many ml of milk do you want to add: '))
    beans += int(input('Write how many grams of coffee beans'
                       ' do you want to add: '))
    cups += int(input('Write how many disposable cups of coffee'
                      ' do you want to add: '))
    print()


def take():
    global money

    print()
    print(f'I gave you ${money}')
    print()

    money = 0


def main():
    while True:
        action = select_action()

        if action == 'buy':
            buy()
        elif action == 'fill':
            fill()
        elif action == 'take':
            take()
        elif action == 'exit':
            break
        elif action == 'remaining':
            print_state()
        else:
            raise ValueError(f'Unknown command {action}')


if __name__ == '__main__':
    main()
