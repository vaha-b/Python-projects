# https://hyperskill.org/projects/69/stages/375/implement

print("The coffe machine has:")
print("400 of water")
print("540 of milk")
print("120 of coffe beans")
print("9 of disposable cups")
print("550 of money")
print()

water = 400
milk = 540
beans = 120
cups = 9
money = 550

action = input("Write action (buy, fill or take): ")

if action == "buy":
    coffe_type = int(
        input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: "))
    print()

    if coffe_type == 1:
        print("The coffe machine has:")
        print(f"{water - 250} of water")
        print(f"{milk} of milk")
        print(f"{beans - 16} of coffe beans")
        print(f"{cups - 1} of disposable cups")
        print(f"${money + 4} of money")
    elif coffe_type == 2:
        print("The coffe machine has:")
        print(f"{water - 350} of water")
        print(f"{milk - 75} of milk")
        print(f"{beans - 20} of coffe beans")
        print(f"{cups - 1} of disposable cups")
        print(f"${money + 7} of money")
    elif coffe_type == 3:
        print("The coffe machine has:")
        print(f"{water - 200} of water")
        print(f"{milk - 100} of milk")
        print(f"{beans - 12} of coffe beans")
        print(f"{cups - 1} of disposable cups")
        print(f"${money + 6} of money")

elif action == "fill":
    added_water = int(input("Write how many ml of water do you want to add: "))
    added_milk = int(input("Write how many ml of milk do you want to add: "))
    added_beans = int(
        input("Write how many grams of coffee beans do you want to add: "))
    added_cups = int(
        input("Write how many disposable cups of coffee do you want to add: "))

    print("The coffe machine has:")
    print(f"{water + added_water} of water")
    print(f"{milk + added_milk} of milk")
    print(f"{beans + added_beans} of coffe beans")
    print(f"{cups + added_cups} of disposable cups")
    print(f"${money} of money")

else:
    print("I gave you $550")
    print()
    print("The coffe machine has:")
    print("400 of water")
    print("540 of milk")
    print("120 of coffe beans")
    print("9 of disposable cups")
    print("0 of money")
