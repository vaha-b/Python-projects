# About the project
# https://hyperskill.org/projects/109

# Stage description
# https://hyperskill.org/projects/109/stages/592/implement

import random
import math


class ATM:
    card_number = None
    pin_code = None
    balance = None

    @staticmethod
    def menu():
        print('1. Create an account \n2. Log into account \n0. Exit')
        user_input = input('> ')
        if user_input == '1':
            ATM.generator()
        elif user_input == '2':
            ATM.login()
        elif user_input == '0':
            ATM.exit()

    @staticmethod
    def generator():
        base_card = list(
            str('400000' + str(random.randrange(100000000, 999999999))))
        numbers = dict(zip(list(range(1, 16)), base_card))
        multipliers = dict(zip(list(range(1, 16)), '212121212121212'))
        for values in numbers:
            numbers[values] = int(numbers[values])
        for values in multipliers:
            multipliers[values] = int(multipliers[values])
        new_numbers = {key: value * multipliers[key]
                       for key, value in numbers.items() if key in multipliers}
        for value in new_numbers:
            if new_numbers[value] > 9:
                new_numbers[value] -= 9
        luhn_total = sum(new_numbers.values())

        def round_up(n, decimals=-1):
            multiplier = 10 ** decimals
            return int(math.ceil(n * multiplier) / multiplier)

        check_digit = round_up(luhn_total) - luhn_total
        final_card_number = ''.join(base_card) + str(check_digit)
        ATM.card_number = final_card_number
        ATM.pin_code = str(random.randrange(1000, 9999))
        ATM.balance = round(0, 2)
        print(
            f'Your card has been created \nYour card number: \n{ATM.card_number}\nYour card PIN: \n{ATM.pin_code}')
        ATM.menu()

    @staticmethod
    def login():
        print('Enter your card number:')
        user_card_number = input('> ')
        print('Enter your PIN:')
        user_pin_code = input('> ')
        if user_card_number == ATM.card_number and user_pin_code == ATM.pin_code:
            print('You have successfully logged in!')
            ATM.nav()
        elif user_card_number != ATM.card_number or user_pin_code != ATM.pin_code:
            print('Wrong card number or PIN!')
            ATM.menu()

    @staticmethod
    def nav():
        print('1. Balance \n2. Log out \n0. Exit')
        user_input = input('> ')
        if user_input == '1':
            print(f'Balance: 0')
            ATM.nav()
        elif user_input == '2':
            print('You have successfully logged out!')
            ATM.menu()
        elif user_input == '0':
            ATM.exit()

    @staticmethod
    def exit():
        print('Bye!')


ATM.menu()

#################################################################


class Account:
    IIN = 400000

    def __init__(self):

        self.pin = str(random.sample([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4)).strip(
            "[]").replace(',', '').replace(' ', '')
        self.card_number = str(Account.luhn_algorithm(self)).strip(
            "[]").replace(',', '').replace(' ', '')
        self.Balance = 0

    def luhn_algorithm(self):
        card = [4, 0, 0, 0, 0, 0] + \
            random.sample([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 9)
        temp = card.copy()
        index = 0
        for digit in temp:
            if (index + 1) % 2 != 0:
                temp[index] = digit * 2
            index += 1
        index = 0
        for digit in temp:
            if digit > 9:
                temp[index] = digit - 9
            index += 1
        total = sum(temp)
        card.append((total * 9) % 10)
        return card

    def get_card_number(self):
        return self.card_number

    def get_balance(self):
        return self.Balance

    def get_pin(self):
        return self.pin


class Bank:
    def __init__(self):
        self.Accounts = []
        self.Accounts_details = {}

    def run(self):
        while True:
            choice = input(
                '1. Create an account \n2. Log into account\n0. Exit\n')
            if choice == '1':
                Bank.create_account(self)
            elif choice == '2':
                card = input('Enter your card number:\n')
                pin = input('Enter your PIN:\n')
                if Bank.check_account(self, card, pin):
                    print('You have successfully logged in!')
                    Bank.login(self, card)
                else:
                    print('Wrong card number or PIN!')
            else:
                print('Bye!')
                exit()

    def check_account(self, card_number, pin):
        for a in self.Accounts:
            if a.get_card_number() == card_number:
                if a.get_pin() == pin:
                    return True
                else:
                    return False

    def create_account(self):
        a = Account()
        self.Accounts.append(a)
        self.Accounts_details[a.get_card_number()] = a
        print('Your card number:')
        print(a.get_card_number() + '\n')
        print('Your card PIN:')
        print(a.get_pin() + '\n')

    def login(self, card):
        while True:
            choice = input('1. Balance \n2. Log out\n0. Exit\n')
            if choice == '1':
                print('Balance:', self.Accounts_details[card].get_balance())
            elif choice == '2':
                print('You have successfully logged out!')
                break
            else:
                print('Bye!')
                exit()


B = Bank()
B.run()
