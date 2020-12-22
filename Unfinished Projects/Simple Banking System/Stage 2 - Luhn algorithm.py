# https://hyperskill.org/projects/109/stages/592/implement#solutions

import random


class Account:
    def __init__(self, num=None, pin=None):
        self.number = num
        self.pin = pin

    def new_account(self):
        number = "400000" + str(random.randint(0000000000, 9999999999))
        digits = [int(i) for i in number]
        num_list = digits
        check_digit = digits.pop()

        for index, a in enumerate(num_list):
            if index % 2 == 0:
                b = a * 2
                num_list[index] = b = b - 9 if b > 9 else b

        # calculates c
        c = 0
        for a in num_list:
            c = c + a
        ###########

        # our formula
        check_digit = 10 - (c % 10)

        # puts all nums together and in string
        num_list.append(check_digit)
        num_list = [str(i) for i in num_list]
        num_list = "".join(num_list)
        #num = int(num_list)

        self.number = num_list
        pin = str(random.randint(1000, 9999))
        self.pin = pin

    def profile(self, cardN_input, cardP_input):

        if self.number == cardN_input and self.pin == cardP_input:
            print("You have successfully logged in!")
            print()
            while True:
                print("1. Balance")
                print("2. Log out")
                print("0. Exit")
                acc_input = input()
                print()

                if acc_input == "1":
                    print("Balance: 0")
                    print()
                elif acc_input == "2":
                    print("You have successfully logged out!")
                    break
                    #  profile()
                elif acc_input == "0":
                    # break
                    print('Bye!')
                    exit()

        else:
            print("Wrong card number or PIN!")
            print()


def main():
    current_account = Account()
    while True:
        print("1. Create an account")
        print("2. Log into account")
        print("0. Exit")

        user_input = input()
        print()

        if user_input == "0":
            print("Bye")
            break
        elif user_input == "1":
            current_account.new_account()
            print("Your card has been created")
            print("Your card number:\n" + current_account.number)
            print("Your card PIN:\n" + current_account.pin)
            print()
        elif user_input == "2":
            print("Enter your card number:")
            cardN_input = input()
            print("Enter your card PIN:")
            cardP_input = input()
            print()

            current_account.profile(cardN_input, cardP_input)
        else:
            print("Choose a number between 0 and 2")


if __name__ == '__main__':
    main()
