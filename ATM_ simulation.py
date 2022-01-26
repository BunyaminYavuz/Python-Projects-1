# ATM simulation

# At the starting how much money that we have
wallet_balance = 2000     # This is just an example

# Transactions
transactions = int(input('''         Transactions
                            ---------------------
                            1 to withdraw money
                            2 to deposit money
                            3 to card information
                            4 to card return     
                            ---------------------
                            Please choose your transaction :
                            '''))

# Loop to keep going the system
while True:

    transactions = int(input('''     Transactions
                            ---------------------
                            1 to withdraw money
                            2 to deposit money
                            3 to card information
                            4 to card return     
                            ---------------------
                            Please choose your transaction :
                            '''))
    # If the user press 1, the loop enter this condition to withdraw money
    if transactions == 1 :

        withdrawed_money = float(input("Enter how much money you want to withdraw: "))

        wallet_balance = wallet_balance - withdrawed_money

        print("Your current wallet balance is : " + str(wallet_balance))

        continue

    # If the user press 2, the loop enter this condition to deposit money
    if transactions == 2 :

        deposited_money = float(input("Enter how much money you want to deposit: "))

        wallet_balance = wallet_balance + deposited_money

        print("Your current wallet balance is : " + str(wallet_balance))
    # If the user press 3, the loop enter this condition to have a look to the current wallet balance
    if transactions == 3 :

        print(''' Card informations :
                -------------------
                User Name = Benyamin Y****
                Card Number = 1234 5678 ****
                Wallet balance : {}'''.format(wallet_balance))


    # If the user press any wrong number, to alert
    if transactions not in [1,2,3,4]:

        print("You pressed a wrong button please try again : ")

        transactions = int(input('''     Transactions
                                    ---------------------
                                    1 to withdraw money
                                    2 to deposit money
                                    3 to card information
                                    4 to card return     
                                    ---------------------
                                    Please choose your transaction :
                                    '''))

    # If the user press 1, the loop enter this condition to quit
    if transactions == 4 :

        print("Take your card from the slot")

        break

