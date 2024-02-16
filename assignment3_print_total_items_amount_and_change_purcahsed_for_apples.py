print("\033[1;34;40mHi! Welcome to our store, we sell apples and oranges here! I will now take your order")

def main():
    apple_price = 20
    orange_price = 25

    while True:
        apples = input("\n\033[1;31;40mHow many apples do you want to buy? ")
        try:
            apples = int(apples)
            if apples < 0:
                print("\033[1;30;40mOrder cannot be processed, please enter a valid number.")
            else:
                break
        except ValueError:
            print("\033[1;30;40mPlease enter a numerical value.")
    print("\033[1;31;40mYour order is", apples, "apple/s\n")

    while True:
        oranges = input("\033[1;33;40mHow many oranges do you want to buy? ")
        try:
            oranges = int(oranges)
            if oranges < 0:
                print("\033[1;30;40mOrder cannot be processed, please enter a valid number.")
            else:
                break
        except ValueError:
            print("\033[1;30;40mPlease enter a numerical value.")
    print("\033[1;33;40mYour order is", oranges, "orange/s")
    print()

    appleprice = apples*apple_price
    orangeprice = oranges*orange_price
    totalprice = appleprice*orangeprice

    while True:
        confirm = input("\033[1;34;40mDo you want to make this purchase? ")
        if confirm.lower() == "yes":
            print("\033[1;37;40mYour total price is: ", totalprice, "pesos")
            print()
            repeat = input("\033[1;34;40mWould you like to buy again? ")
            if repeat == "yes":
                main()
            elif repeat == "no":
                print("\033[1;34;40mThank you for shopping with us! Please come again!\n")
                break
            else:
                print('\033[1;30;40mPlease enter only "yes" or "no".')
        elif confirm.lower() == "no":
            print("\033[1;34;40mIf that's the case, ")
            repeat = input("Would you like to try again? ")
            if repeat == "yes":
                main()
            elif repeat == "no":
                print("\033[1;34;40mThank you for shopping with us! Have a nice day!\n")
                break
            else:
                print('\033[1;30;40mPlease enter a "yes" or "no"')
                break
        else:
            print('\033[1;30;40mPlease enter a "yes" or "no"')
    exit()
main()    