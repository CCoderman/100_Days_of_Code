# Day 2 of 100 Days of Code
# This program will calculate the tip each person should pay based on user input of how
# many people are paying and the desired tip percentage
def calculate_tip():
    # User input
    print("Welcome to the tip calculator")
    bill = float(input("What was the total bill? $"))
    people = float(input("How many people will split the bill? "))
    tip = float(input("What percentage tip would you like to give? eg. 15, 20, etc. "))

    # Math calculations to get the tip per person
    tip_as_percent = tip / 100
    total_tip_amount = bill * tip_as_percent
    total_bill = bill + total_tip_amount
    bill_per_person = total_bill / people
    final_amount = round(bill_per_person, 2)

    # display tip per person to console
    print(f"Each person should pay: ${final_amount}")


# Function call
calculate_tip()
