#!/usr/bin/env python3
# Created by Maximiliano Fairman
# Created on Dec 12th, 2025
# This program lets the user choose between:
# 1. Calculating the tax percentage
# 2. Converting seconds into hours, minutes, and seconds

# Constants
HOUR_IN_SECONDS = 3600
MINUTE_IN_SECONDS = 60


# FUNCTION 1 (TAX)
def calculate_tax(subtotal=0.0, total=0.0):
    tax = total - subtotal
    tax_percent = (tax / subtotal) * 100
    return tax, tax_percent


# FUNCTION 2 (TIME)
def convert_seconds(time_seconds=0):
    hours = time_seconds // HOUR_IN_SECONDS
    minutes = (time_seconds % HOUR_IN_SECONDS) // MINUTE_IN_SECONDS
    seconds = time_seconds % MINUTE_IN_SECONDS
    return hours, minutes, seconds


# FUNCTION 3 (RESTART PROMPT)
def ask_restart():
    choice = input("Would you like to restart and choose a different option? (y/n): ")
    print("")
    if choice.lower() == "y" or choice.lower() == "yes":
        return True
    elif choice.lower() == "n" or choice.lower() == "no":
        return False
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        return ask_restart()


# MAIN PROGRAM
def main():
    restart = True

    while restart:
        print("")
        print("Welcome to Max's Price Checker & Time Converter.")
        print("Enter the number 1 → Price Checker")
        print("Enter the number 2 → Time Converter")
        print("")

        try:
            user_choice = int(input("Enter your choice (1 or 2): "))
            print("")

            if user_choice == 1 or user_choice == 2:

                if user_choice == 1:
                    print("PRICE CHECKER SELECTED")
                    print("")
                    print("aka the best tax calculator ever made")
                    print("")
                    try:
                        subtotal = float(input("Enter the subtotal amount: $"))
                        total = float(input("Enter the total amount: $"))
                        print("")

                        if subtotal <= 0:
                            print("Subtotal must be greater than 0.")
                        else:
                            tax, percent = calculate_tax(subtotal, total)
                            print(f"Tax amount: ${tax:.2f}")
                            print(f"Tax percentage: {percent:.2f}%")
                            print("")

                    except ValueError:
                        print("Invalid number entered.")

                else:  # user_choice == 2
                    print("TIME CONVERTER SELECTED")
                    print("")

                    try:
                        sec = int(input("Enter time in seconds: "))
                        print("")

                        if sec < 0:
                            print("Time cannot be negative.")
                        else:
                            h, m, s = convert_seconds(sec)
                            print(f"Hours: {h}")
                            print(f"Minutes: {m}")
                            print(f"Seconds: {s}")
                            print("")

                        # ask to restart
                        restart = ask_restart()

                    except ValueError:
                        print("Invalid number entered.")

            else:
                print("Invalid choice. Please select 1 or 2.")

        except ValueError:
            print("Your input was not a number.")

    print("Thank you for using the program. Goodbye!")


if __name__ == "__main__":
    main()
