# Day 1 of 100 Days of Code
# This program will ask user for birth place and their pet name, and generate a band name based on input
# Topics covered: print, input, basic string manipulation
def generate_band_name():
    # Ask the user for the city they grew up in
    city_name = input("What's the name of the city you grew up in?\n")
    # Ask the user for the name of their pet
    pet_name = input("What's your pet's name?\n")
    # Generates the band name (city name + pet name)
    print(f"Your band name could be: {city_name} {pet_name}")


generate_band_name()
