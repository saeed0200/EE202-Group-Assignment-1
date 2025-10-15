# Scientific Module

import math

def get_float(msg):
    "Keep asking until user enters a valid number"
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("Invalid number, try again.")

def get_int(msg):
    "Keep asking until user enters a valid integer"
    while True:
        try:
            n = int(input(msg))
            if n < 0:
                print("Please enter a non-negative number.")
                continue
            return n
        except ValueError:
            print("Invalid number, try again.")

def choose_units():
    "Ask if the user wants degrees or radians"
    while True:
        units = input("Degrees or radians? ").lower()
        if units in ["degrees", "degree", "d"]:
            return "deg"
        elif units in ["radians", "radian", "r"]:
            return "rad"
        else:
            print("Please type 'degrees' or 'radians'.")

def to_radians(x, units):
    if units == "deg":
        return math.radians(x)
    return x

def main_menu():
    while True:
        print("\n=== Scientific Mode ===")
        print("1. sin")
        print("2. cos")
        print("3. tan")
        print("4. asin")
        print("5. acos")
        print("6. atan")
        print("7. log10")
        print("8. ln")
        print("9. exp (e^x)")
        print("10. factorial")
        print("11. constants (pi, e)")
        print("12. convert degrees <-> radians")
        print("0. Back to main menu")

        choice = input("Enter your choice: ")

        if choice == "0":
            print("Returning to main menu...")
            break

        elif choice == "1":
            units = choose_units()
            x = get_float("Enter angle: ")
            print("Result:", round(math.sin(to_radians(x, units)), 4))

        elif choice == "2":
            units = choose_units()
            x = get_float("Enter angle: ")
            print("Result:", round(math.cos(to_radians(x, units)), 4))

        elif choice == "3":
            units = choose_units()
            x = get_float("Enter angle: ")
            rad = to_radians(x, units)
            if abs(math.cos(rad)) < 1e-12:
                print("Error: tan undefined for this angle.")
            else:
                print("Result:", round(math.tan(rad), 4))

        elif choice == "4":
            x = get_float("Enter value (-1 to 1): ")
            if -1 <= x <= 1:
                units = choose_units()
                ans = math.asin(x)
                if units == "deg":
                    ans = math.degrees(ans)
                print("Result:", round(ans, 4))
            else:
                print("Error: value out of range.")

        elif choice == "5":
            x = get_float("Enter value (-1 to 1): ")
            if -1 <= x <= 1:
                units = choose_units()
                ans = math.acos(x)
                if units == "deg":
                    ans = math.degrees(ans)
                print("Result:", round(ans, 4))
            else:
                print("Error: value out of range.")

        elif choice == "6":
            x = get_float("Enter value: ")
            units = choose_units()
            ans = math.atan(x)
            if units == "deg":
                ans = math.degrees(ans)
            print("Result:", round(ans, 4))

        elif choice == "7":
            x = get_float("Enter positive number: ")
            if x <= 0:
                print("Error: log10 undefined for non-positive numbers.")
            else:
                print("Result:", round(math.log10(x), 4))

        elif choice == "8":
            x = get_float("Enter positive number: ")
            if x <= 0:
                print("Error: ln undefined for non-positive numbers.")
            else:
                print("Result:", round(math.log(x), 4))

        elif choice == "9":
            x = get_float("Enter value: ")
            try:
                print("Result:", round(math.exp(x), 4))
            except OverflowError:
                print("Error: number too large!")

        elif choice == "10":
            n = get_int("Enter non-negative integer: ")
            try:
                print("Result:", math.factorial(n))
            except OverflowError:
                print("Error: factorial result too large.")

        elif choice == "11":
            print("pi =", math.pi)
            print("e  =", math.e)

        elif choice == "12":
            conv = input("Type 'to radians' or 'to degrees': ").lower()
            if "radian" in conv:
                deg = get_float("Enter degrees: ")
                print("Result:", round(math.radians(deg), 4))
            elif "degree" in conv:
                rad = get_float("Enter radians: ")
                print("Result:", round(math.degrees(rad), 4))
            else:
                print("Invalid choice.")

        else:
            print("Invalid option, try again.")
