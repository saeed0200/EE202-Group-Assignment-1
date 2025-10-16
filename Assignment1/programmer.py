# programmer.py

COLORS = {
    "green": "\033[92m",    # Green: results
    "yellow": "\033[93m",   # Yellow: titles
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


def main_menu():
    while True:
        print("1 Base Conversions")
        print("2 Bitwise Operations")
        print("3 Back to Main Menu")
        cprint("4 View History", "yellow") 
        choice = input(f"{COLORS['yellow']}Enter choice 1-4: {COLORS['reset']}")

        if choice == '1':
            base_conversion_menu()
        elif choice == '2':
            bitwise_menu()
        elif choice == '3':
            cprint("Returning to the Main Menu", "yellow")
            break
        
        elif choice == '4':
            cprint(" History","yellow")
            if len(history)==0:
                print("The history is empty")
            else:
                cprint('\n'.join(history), 'green') 
            print("------------------------------")
            continue

        else:
            cprint("Invalid choice Please try again", "red")

def base_conversion_menu():
    while True:
        cprint(" The Base Conversion", "yellow")
        print("1 from Decimal to Binary")
        print("2 from Decimal to Octal")
        print("3 from  Decimal to Hexadecimal")
        print("4 from Binary to Decimal")
        print("5 from Octal to Decimal")
        print("6 from Hexadecimal to Decimal")
        print("7 go Back")

        choice = input(f"{COLORS['yellow']}Enter your choice from 1-7 : {COLORS['reset']}")

        try:
            if choice == '1':
                dec = int(input(f"{COLORS['yellow']}Enter decimal number: {COLORS['reset']}"))
                result = bin(dec)[2:]
                cprint(f"Binary: {result}", "green")
                history.append(f"Dec to Bin: {dec} = {result}")
            elif choice == '2':
                dec = int(input(f"{COLORS['yellow']}Enter decimal number: {COLORS['reset']}"))
                result = oct(dec)[2:]
                cprint(f"Octal: {result}", "green")
                history.append(f"Dec to Oct: {dec} = {result}")
            elif choice == '3':
                dec = int(input(f"{COLORS['yellow']}Enter decimal number: {COLORS['reset']}"))
                result = hex(dec)[2:].upper()
                cprint(f"Hexadecimal: {result}", "green")
                history.append(f"Dec to Hex: {dec} = {result}")
            elif choice == '4':
                b = input(f"{COLORS['yellow']}Enter binary number: {COLORS['reset']}")
                if all(ch in '01' for ch in b):
                    result = int(b, 2)
                    cprint(f"Decimal: {result}", "green")
                    history.append(f"Bin to Dec: {b} = {result}")
                else:
                    error_msg = "Error: Binary number must contain only 0 and 1"
                    cprint(error_msg, "red")
                    history.append(f"Bin to Dec: {b} = ERROR: {error_msg}")
            elif choice == '5':
                o = input(f"{COLORS['yellow']}Enter octal number: {COLORS['reset']}")
                if all(ch in '01234567' for ch in o):
                    result = int(o, 8)
                    cprint(f"Decimal: {result}", "green")
                    history.append(f"Oct to Dec: {o} = {result}")
                else:
                    error_msg = "Error: Octal number must contain digits 0–7 only"
                    cprint(error_msg, "red")
                    history.append(f"Oct to Dec: {o} = ERROR: {error_msg}")
            elif choice == '6':
                h = input(f"{COLORS['yellow']}Enter hexadecimal number: {COLORS['reset']}")
                try:
                    result = int(h, 16)
                    cprint(f"Decimal: {result}", "green")
                    history.append(f"Hex to Dec: {h} = {result}")
                except ValueError:
                    error_msg = "Error: Invalid hexadecimal format"
                    cprint(error_msg, "red")
                    history.append(f"Hex to Dec: {h} = ERROR: {error_msg}")
            elif choice == '7':
                break
            else:
                cprint("Invalid choice", "red")
        except ValueError:
            cprint("Error: Please enter a valid integer", "red")

#part 2
#The Bitwise menu
def bitwise_menu():
    while True:
        cprint("The Bitwise Operations", "yellow")
        print("1. AND (&)")
        print("2. OR (|)")
        print("3. XOR (^)")
        print("4. NOT (~)")
        print("5. Left Shift (<<)")
        print("6. Right Shift (>>)")
        print("7. Back")

        choice = input(f"{COLORS['yellow']}Enter choice 1-7: {COLORS['reset']}")

        try:
            if choice in ['1', '2', '3']:
                a = int(input(f"{COLORS['yellow']}Enter first integer: {COLORS['reset']}"))
                b = int(input(f"{COLORS['yellow']}Enter second integer: {COLORS['reset']}"))
                
                if choice == '1':
                    result = a & b
                    cprint(f"Result: {result}", "green")
                    history.append(f"{a} & {b} = {result}")
                elif choice == '2':
                    result = a | b
                    cprint(f"Result: {result}", "green")
                    history.append(f"{a} | {b} = {result}")
                elif choice == '3':
                    result = a ^ b
                    cprint(f"Result: {result}", "green")
                    history.append(f"{a} ^ {b} = {result}")

            elif choice == '4':
                a = int(input(f"{COLORS['yellow']}Enter integer: {COLORS['reset']}"))
                result = ~a
                cprint(f"Result: {result}", "green")
                history.append(f"~{a} = {result}")

            elif choice == '5':
                a = int(input(f"{COLORS['yellow']}Enter integer: {COLORS['reset']}"))
                shift = int(input(f"{COLORS['yellow']}Enter shift amount: {COLORS['reset']}"))
                result = a << shift
                cprint(f"Result: {result}", "green")
                history.append(f"{a} << {shift} = {result}")

            elif choice == '6':
                a = int(input(f"{COLORS['yellow']}Enter integer: {COLORS['reset']}"))
                shift = int(input(f"{COLORS['yellow']}Enter shift amount: {COLORS['reset']}"))
                result = a >> shift
                cprint(f"Result: {result}", "green")
                history.append(f"{a} >> {shift} = {result}")
            elif choice == '7':
                break

            else:
                cprint("Invalid choice.", "red")

        except ValueError:
            cprint("Error: enter valid integers only", "red")


