# ============================================================
# Case Study 3: ATM Simulation System
# Student Roll: 26000985
# Name: Yarlagadda Divya Sita Maha Lakshmi | Section: CSM2
# ============================================================
# Problem Statement:
# ATM options (Balance, Deposit, Withdraw, History)
# Objectives: loops, lists, nested lists, tuples
# Algorithm:
# 1. Start
# 2. Initialize balance=10000 and empty history list
# 3. Display ATM menu
# 4. Get user choice
# 5. if choice is 1,display balance
# 6. If choice is 2,deposit amount and update history
# 7. If choice is 3,check balance and withdraw if sufficient
# 8. If choice is 4,display transaction history using loop
# 9. If choice is 5,exit system
#10.stop
# ============================================================

def main():
    # Initial data using list and tuple concepts
    balance = 10000
    transaction_history = []  # Nested list: [type, amount, balance]
    atm_cards = ("26000985", "1234")  # Tuple unpacking example
    user_id, pin = atm_cards

    print("===== ATM Simulation - Roll 26000985 =====")
    print(f"Welcome User: {user_id}")
    print(f"Initial Balance: {balance}")

    # Simulated user inputs (No input() needed for auto-run)
    operations = [
        (1, 0),      # Check Balance
        (2, 5000),   # Deposit 5000
        (3, 2000),   # Withdraw 2000
        (3, 20000),  # Withdraw fail - insufficient
        (4, 0),      # History
        (5, 0)       # Exit
    ]

    for choice, amount in operations:  # Unpacking
        print(f"\n--- Option Selected: {choice} ---")

        if choice == 1:
            print(f"Current Balance: Rs. {balance}")

        elif choice == 2:
            # Deposit
            if amount <= 0:
                print("Invalid Deposit Amount")
            else:
                balance += amount
                transaction_history.append(["DEPOSIT", amount, balance])
                print(f"Deposited: {amount} | New Balance: {balance}")

        elif choice == 3:
            # Withdraw
            if amount > balance:
                print(f"FAILED: Insufficient Balance. You have {balance}, tried {amount}")
                transaction_history.append(["FAILED-WITHDRAW", amount, balance])
            elif amount <= 0:
                print("Invalid Withdraw Amount")
            else:
                balance -= amount
                transaction_history.append(["WITHDRAW", amount, balance])
                print(f"Withdrawn: {amount} | New Balance: {balance}")

        elif choice == 4:
            # History - Nested list loop
            print("Transaction History:")
            if len(transaction_history) == 0:
                print("  No transactions yet")
            else:
                for i in range(len(transaction_history)):
                    record = transaction_history[i]
                    print(f"  {i+1}. Type:{record[0]} Amount:{record[1]} Balance:{record[2]}")

        elif choice == 5:
            print("Thank you! Visit Again")
            break

        else:
            print("Invalid Choice")

    print("\n===== Final Report =====")
    print(f"Final Balance: {balance}")
    print(f"Total Transactions: {len(transaction_history)}")

if __name__ == "__main__":
    main() 
  
   
 
