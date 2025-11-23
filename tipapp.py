# --- Welcome Message ---
print("----Restaurant Tip Calculator----")

# --- Ask for Input ---
bill = input("Enter the total bill amount: ")
tip_percent = input("Enter the total tip amount: ")

# --- Error Handling and Converting Input
try:
    bill = float(bill)
    tip_percent = float(tip_percent)
except ValueError:
    print("Please enter valid numbers for the bill and tip percantage")
    exit()

# --- Calculate Bill and Tip Amount ---
tip_amount = bill * (tip_percent / 100)
total_bill = bill + tip_amount

# --- Display Results ---
print(f"\nTip amount: ${tip_amount:.2f}")
print(f"Total bill including tip: ${total_bill:.2f}")

# --- Comments ---
# program calculates the tip amount and the total bill at a restaurant
# user enters bill and tip amount
# program computes tip and final bill