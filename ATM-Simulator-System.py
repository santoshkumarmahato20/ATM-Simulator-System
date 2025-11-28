import sys

# --- HARDCODED ACCOUNT DATA ---
# Since no database or file handling is required, we use a global dictionary
# to store the account details.
ACCOUNT_DATA = {
    "username": "user123",
    "pin": "1234",
    "balance": 5000.00,
    "transactions": [
        {"type": "Deposit", "amount": 5000.00, "note": "Initial Deposit"}
    ]
}

# --- CORE ATM FUNCTIONS ---

def sign_in():
    """Handles the user sign-in process."""
    max_attempts = 3
    
    # 1. Username Check
    for attempt in range(max_attempts):
        user_input = input("Enter Username: ").strip()
        if user_input == ACCOUNT_DATA["username"]:
            break
        elif attempt < max_attempts - 1:
            print("Invalid Username. Please try again.")
        else:
            print("Too many invalid attempts. Exiting.")
            sys.exit()

    # 2. PIN Check
    for attempt in range(max_attempts):
        pin_input = input("Enter PIN: ").strip()
        if pin_input == ACCOUNT_DATA["pin"]:
            print("\nSign In Successful! Welcome back.")
            return True
        elif attempt < max_attempts - 1:
            print("Invalid PIN. Please try again.")
        else:
            print("Too many invalid attempts. Access denied. Exiting.")
            sys.exit()
    
    return False

def display_statement():
    """Displays the current account balance and transaction history."""
    print("\n" + "="*40)
    print("           ACCOUNT STATEMENT")
    print("="*40)
    print(f"Current Balance: ${ACCOUNT_DATA['balance']:.2f}\n")
    print(f"{'Type':<10}{'Amount':<15}{'Note':<15}")
    print("-" * 40)
    
    # Display the last 5 transactions for brevity
    for t in ACCOUNT_DATA["transactions"][-5:]:
        amount_str = f"${t['amount']:.2f}"
        print(f"{t['type']:<10}{amount_str:<15}{t.get('note', ''):<15}")
    
    if len(ACCOUNT_DATA["transactions"]) > 5:
        print("\nShowing last 5 transactions.")
        
    print("="*40 + "\n")

def withdraw_amount():
    """Handles the withdrawal transaction."""
    try:
        amount = float(input("Enter amount to withdraw: $").strip())
        
        if amount <= 0:
            print("\nERROR: Withdrawal amount must be positive.")
            return
            
        if amount > ACCOUNT_DATA["balance"]:
            print("\nERROR: Insufficient funds.")
            return

        # Perform transaction
        ACCOUNT_DATA["balance"] -= amount
        ACCOUNT_DATA["transactions"].append({
            "type": "Withdraw", 
            "amount": amount, 
            "note": "ATM Withdrawal"
        })
        
        print(f"\nSUCCESS! Withdrew ${amount:.2f}.")
        print(f"New Balance: ${ACCOUNT_DATA['balance']:.2f}")

    except ValueError:
        print("\nERROR: Invalid amount entered. Please enter a number.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

def deposit_amount():
    """Handles the deposit (lodge) transaction."""
    try:
        amount = float(input("Enter amount to deposit (lodge): $").strip())
        
        if amount <= 0:
            print("\nERROR: Deposit amount must be positive.")
            return

        # Perform transaction
        ACCOUNT_DATA["balance"] += amount
        ACCOUNT_DATA["transactions"].append({
            "type": "Deposit", 
            "amount": amount, 
            "note": "ATM Deposit"
        })
        
        print(f"\nSUCCESS! Deposited ${amount:.2f}.")
        print(f"New Balance: ${ACCOUNT_DATA['balance']:.2f}")

    except ValueError:
        print("\nERROR: Invalid amount entered. Please enter a number.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

def change_pin():
    """Allows the user to change their PIN."""
    old_pin = input("Enter current PIN: ").strip()
    
    if old_pin != ACCOUNT_DATA["pin"]:
        print("\nERROR: Incorrect current PIN.")
        return

    new_pin = input("Enter new 4-digit PIN: ").strip()
    
    if not new_pin.isdigit() or len(new_pin) != 4:
        print("\nERROR: New PIN must be exactly 4 digits.")
        return

    confirm_pin = input("Confirm new PIN: ").strip()

    if new_pin != confirm_pin:
        print("\nERROR: New PINs do not match.")
        return

    # Update PIN
    ACCOUNT_DATA["pin"] = new_pin
    print("\nSUCCESS! Your PIN has been successfully changed.")

# --- MAIN PROGRAM EXECUTION ---

def main():
    """Main function to run the ATM console menu."""
    print("="*40)
    print("      WELCOME TO THE ATM SIMULATOR")
    print("="*40)

    # Start with the sign-in procedure
    if sign_in():
        while True:
            print("\n" + "#"*40)
            print("        MAIN MENU")
            print("#"*40)
            print("1. Account Statement")
            print("2. Withdraw Amount")
            print("3. Lodge Amount (Deposit)")
            print("4. Change Pin")
            print("5. Exit")
            print("#"*40)
            
            choice = input("Enter your command (1-5): ").strip()
            
            if choice == '1':
                display_statement()
            elif choice == '2':
                withdraw_amount()
            elif choice == '3':
                deposit_amount()
            elif choice == '4':
                change_pin()
            elif choice == '5':
                print("\nThank you for using the ATM Simulator. Goodbye!")
                sys.exit()
            else:
                print("\nInvalid choice. Please enter a number between 1 and 5.")

# Run the main function when the script starts
if __name__ == "__main__":
    main()
