def buy_apples():
    buy_choice = input("\n\033[1;34;40mWelcome to our store! We're selling apples for 20 pesos each. Would you like to buy some? ")

    if buy_choice == "yes":
        while True:
            try:
                money = float(input("\033[1;32;40mEnter the amount of money you have: "))
                if money < 0:
                    print("\033[1;31;40m Please enter a positive amount.")
                    continue
                else:
                    break
            except ValueError:
                print("\033[1;31;40m Invalid input. Please enter a valid number.")
        
        apple_price = 20
        max_apples = money // apple_price
        remaining_money = money % apple_price
        print(f"\n\033[1;37;40mYou can buy {int(max_apples)} apples with that amount and you will have {remaining_money}")
        print("\033[1;34;40mThank you for purchasing from our store. Have a great day!\n")
    else:
        print("\033[1;34;40mThank you for considering our store. Have a great day!\n")
buy_apples()