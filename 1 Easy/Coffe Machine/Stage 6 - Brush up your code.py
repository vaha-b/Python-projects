# About the project:
# https://hyperskill.org/projects/68?track=2

# Stage description
# https://hyperskill.org/projects/68/stages/371/implement

class CoffeeMachine:
    def __init__(self, water, milk, coffee_beans, cups, money):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.cups = cups
        self.money = money

    def remaining(self):
        print("The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.coffee_beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"${self.money} of money")

    def buy(self):
        coffee_choice = input(
            "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n")
        if coffee_choice == 'back':
            return
        coffee_choice = int(coffee_choice)
        if self.water < 200:
            print("Sorry, not enough water!")
            return
        elif self.milk <= 0:
            print("Sorry, not enough milk!")
            return
        elif self.coffee_beans < 12:
            print("Sorry, not enough coffee_beans!")
            return
        elif self.cups <= 0:
            print("Sorry, not enough disposable cups!")
            return

        if coffee_choice == 1:
            self.water -= 250
            self.coffee_beans -= 16
            self.money += 4
        elif coffee_choice == 2:
            self.water -= 350
            self.milk -= 75
            self.coffee_beans -= 20
            self.money += 7
        elif coffee_choice == 3:
            self.water -= 200
            self.milk -= 100
            self.coffee_beans -= 12
            self.money += 6
        self.cups -= 1
        print("I have enough resources, making you a coffee!")

    def fill(self):
        self.water += int(input("Write how many ml of water do you want to add:\n"))
        self.milk += int(input("Write how many ml of milk do you want to add:\n"))
        self.coffee_beans += int(
            input("Write how many grams of coffee beans do you want to add:\n"))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add:\n"))

    def take(self):
        print(f"I gave you ${self.money}")

    def run(self):
        while True:
            action = input(
                "Write action (buy, fill, take, remaining, exit):\n")
            print()
            if action == 'buy':
                self.buy()
            elif action == 'fill':
                self.fill()
            elif action == 'take':
                self.take()
                self.money = 0
            elif action == 'remaining':
                self.remaining()
            elif action == 'exit':
                exit()
            print()


cf = CoffeeMachine(400, 540, 120, 9, 550)
cf.run()
