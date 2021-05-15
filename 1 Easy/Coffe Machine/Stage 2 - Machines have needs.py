# About the project:
# https://hyperskill.org/projects/68?track=2

# Stage description
# https://hyperskill.org/projects/68/stages/367/implement

water = int(input("Write how many ml of water the coffe machine has: "))
milk = int(input("Write how many ml of milk the coffe machine has: "))
beans = int(input("Write how many grams of coffe beans you will need: "))
cups = int(input("Write how many cups of coffee you will need: "))

cups_available = min([water/200, milk/50, beans/15])

if cups == cups_available:
    print("Yes, I can make that amount of coffee")
elif cups < cups_available:
    print(
        f"Yes, I can make that amount of coffee (and even {int(cups-cups_available)} more than that)")
else:
    print(f"No, I can make only {int(cups_available)} cups of coffee")

amount = int(input("Write how many cups of coffee you will need: "))
print(f"For {amount} cups of coffee you will need:")
print(200 * amount, "ml of water")
print(50 * amount, "ml of milk")
print(15 * amount, "g of coffee beans")
