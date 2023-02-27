import sys

print("\n\nWelcome to the tip calculator!")
total_bill = float(input("What was the total bill? \n"))
split = float(input("\nHow many people split the bill?\n"))
tip_percent = float(input("\nWhat percentage tip would you like to give? 10, 12, or 15?\n"))*.01
total_bill_with_tip = (total_bill + total_bill*tip_percent) / split
print(f"\nYour total bill with tip is ${total_bill_with_tip: .2f}.")




