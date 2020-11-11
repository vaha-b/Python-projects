import random


class Account:
    def __init__(self, num=None, pin=None):
        self.number = num
        self.pin = pin

    def new_account(self):
        number = "400000" + str(random.randint(000000000, 99999999999))
        self.number = number
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
