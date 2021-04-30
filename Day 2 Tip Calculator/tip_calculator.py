# Day 2 of 100 Days of Code
# This program will calculate the tip each person should pay based on user input of how
# many people are paying and the desired tip percentage
def calculate_tip():
    # User input
    print("Welcome to the tip calculator")
    bill = float(input("What was the total bill? $"))
    people = float(input("How many people will split the bill? "))
    percentage = float(input("What percentage tip would you like to give? eg. 15, 20, etc. "))

    # Math calculations to get the tip
    percent_convert = percentage / 100 + 1
    tip = round((bill / people) * percent_convert, 2)
    print(f"Each person should pay: ${tip}")


calculate_tip()
