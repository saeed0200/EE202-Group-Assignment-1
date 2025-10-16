import math

COLORS = {
    "green": "\033[92m",    # Green: results
    "yellow": "\033[93m",   # Yellow: titles/prompts
    "red": "\033[91m",      # Red: errors
    "reset": "\033[0m"      # Reset: back to normal
}

def cprint(text, kind):
    """Prints text in a specific color."""
    if kind in COLORS:
        color_code = COLORS[kind]
    else:
        color_code = COLORS["reset"]
        
    print(f"{color_code}{text}{COLORS['reset']}")

history = []

def get_float(msg):
    "Keep asking until user enters a valid number"
    while True:
        try:
            return float(input(f"{COLORS['yellow']}{msg}{COLORS['reset']}"))
        except ValueError:
            cprint("Invalid number, try again.", "red")

def get_int(msg):
    "Keep asking until user enters a valid integer"
    while True:
        try:
            n = int(input(f"{COLORS['yellow']}{msg}{COLORS['reset']}"))
            if n < 0:
                cprint("Please enter a non-negative number.", "red")
                continue
            return n
        except ValueError:
            cprint("Invalid number, try again.", "red")

def choose_units():
    "Ask if the user wants degrees or radians"
    while True:
        units = input(f"{COLORS['yellow']}Degrees or radians? {COLORS['reset']}").lower()
        if units in ["degrees", "degree", "d"]:
            return "deg"
        elif units in ["radians", "radian", "r"]:
            return "rad"
        else:
            cprint("Please type 'degrees' or 'radians'.", "red")

def to_radians(x, units):
    if units == "deg":
        return math.radians(x)
    return x

def main_menu():
    while True:
        cprint("\n=== Scientific Mode ===", "yellow")
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
        print("13. View History") 
        print("0. Back to main menu")

        choice = input(f"{COLORS['yellow']}Enter your choice: {COLORS['reset']}")

        if choice == "0":
            print("Returning to main menu...")
            break
        
        elif choice == "13":
            cprint(" History", "yellow")
            if len(history)==0:
                print("The history is empty")
            else:
                cprint('\n'.join(history), 'green') 
            print("------------------------------")
            continue
        

        elif choice == "1":
            units = choose_units()
            x = get_float("Enter angle: ")
            result = round(math.sin(to_radians(x, units)), 4)
            cprint(f"Result: {result}", "green")
            history.append(f"sin({x} {units}) = {result}")

        elif choice == "2":
            units = choose_units()
            x = get_float("Enter angle: ")
            result = round(math.cos(to_radians(x, units)), 4)
            cprint(f"Result: {result}", "green")
            history.append(f"cos({x} {units}) = {result}")

        elif choice == "3":
            units = choose_units()
            x = get_float("Enter angle: ")
            rad = to_radians(x, units)
            if abs(math.cos(rad)) < 1e-12:
                error_msg = "Error: tan undefined for this angle."
                cprint(error_msg, "red")
                history.append(f"tan({x} {units}) = {error_msg}")
            else:
                result = round(math.tan(rad), 4)
                cprint(f"Result: {result}", "green")
                history.append(f"tan({x} {units}) = {result}")

        elif choice == "4":
            x = get_float("Enter value (-1 to 1): ")
            if -1 <= x <= 1:
                units = choose_units()
                ans = math.asin(x)
                if units == "deg":
                    ans = math.degrees(ans)
                result = round(ans, 4)
                cprint(f"Result: {result}", "green")
                history.append(f"asin({x}) = {result} {units}")
            else:
                error_msg = "Error: value out of range."
                cprint(error_msg, "red")
                history.append(f"asin({x}) = {error_msg}")

        elif choice == "5":
            x = get_float("Enter value (-1 to 1): ")
            if -1 <= x <= 1:
                units = choose_units()
                ans = math.acos(x)
                if units == "deg":
                    ans = math.degrees(ans)
                result = round(ans, 4)
                cprint(f"Result: {result}", "green")
                history.append(f"acos({x}) = {result} {units}")
            else:
                error_msg = "Error: value out of range."
                cprint(error_msg, "red")
                history.append(f"acos({x}) = {error_msg}")

        elif choice == "6":
            x = get_float("Enter value: ")
            units = choose_units()
            ans = math.atan(x)
            if units == "deg":
                ans = math.degrees(ans)
            result = round(ans, 4)
            cprint(f"Result: {result}", "green")
            history.append(f"atan({x}) = {result} {units}")

        elif choice == "7":
            x = get_float("Enter positive number: ")
            if x <= 0:
                error_msg = "Error: log10 undefined for non-positive numbers."
                cprint(error_msg, "red")
                history.append(f"log10({x}) = {error_msg}")
            else:
                result = round(math.log10(x), 4)
                cprint(f"Result: {result}", "green")
                history.append(f"log10({x}) = {result}")

        elif choice == "8":
            x = get_float("Enter positive number: ")
            if x <= 0:
                error_msg = "Error: ln undefined for non-positive numbers."
                cprint(error_msg, "red")
                history.append(f"ln({x}) = {error_msg}")
            else:
                result = round(math.log(x), 4)
                cprint(f"Result: {result}", "green")
                history.append(f"ln({x}) = {result}")

        elif choice == "9":
            x = get_float("Enter value: ")
            try:
                result = round(math.exp(x), 4)
                cprint(f"Result: {result}", "green")
                history.append(f"exp({x}) = {result}")
            except OverflowError:
                error_msg = "Error: number too large!"
                cprint(error_msg, "red")
                history.append(f"exp({x}) = {error_msg}")

        elif choice == "10":
            n = get_int("Enter non-negative integer: ")
            try:
                result = math.factorial(n)
                cprint(f"Result: {result}", "green")
                history.append(f"factorial({n}) = {result}")
            except OverflowError:
                error_msg = "Error: factorial result too large."
                cprint(error_msg, "red")
                history.append(f"factorial({n}) = {error_msg}")

        elif choice == "11":
            cprint(f"pi = {math.pi}", "green")
            cprint(f"e  = {math.e}", "green")

        elif choice == "12":
            conv = input(f"{COLORS['yellow']}Type 'to radians' or 'to degrees': {COLORS['reset']}").lower()
            if "radian" in conv:
                deg = get_float("Enter degrees: ")
                result = round(math.radians(deg), 4)
                cprint(f"Result: {result}", "green")
                history.append(f"{deg} deg to rad = {result}")
            elif "degree" in conv:
                rad = get_float("Enter radians: ")
                result = round(math.degrees(rad), 4)
                cprint(f"Result: {result}", "green")
                history.append(f"{rad} rad to deg = {result}")
            else:
                error_msg = "Invalid choice."
                cprint(error_msg, "red")
                history.append(f"Convert units = {error_msg}")

        else:
            cprint("Invalid option, try again.", "red")

