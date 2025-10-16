# programmer.py


def main_menu():
    while True:
        print("1 Base Conversions")
        print("2 Bitwise Operations")
        print("3 Back to Main Menu")

        choice = input("Enter choice 1-3: ")

        if choice == '1':
            base_conversion_menu()
        elif choice == '2':
            bitwise_menu()
        elif choice == '3':
            print("Returning to the Main Menu")
            break
        else:
            print("Invalid choice Please try again")

def base_conversion_menu():
    while True:
        print(" The Base Conversion")
        print("1 from Decimal to Binary")
        print("2 from Decimal to Octal")
        print("3 from  Decimal to Hexadecimal")
        print("4 from Binary to Decimal")
        print("5 from Octal to Decimal")
        print("6 from Hexadecimal to Decimal")
        print("7 go Back")

        choice = input("Enter your choice from 1-7 : ")

        try:
            if choice == '1':
                dec = int(input("Enter decimal number: "))
                print("Binary:", bin(dec)[2:])
            elif choice == '2':
                dec = int(input("Enter decimal number: "))
                print("Octal:", oct(dec)[2:])
            elif choice == '3':
                dec = int(input("Enter decimal number: "))
                print("Hexadecimal:", hex(dec)[2:].upper())
            elif choice == '4':
                b = input("Enter binary number: ")
                if all(ch in '01' for ch in b):
                    print("Decimal:", int(b, 2))
                else:
                    print("Error: Binary number must contain only 0 and 1")
            elif choice == '5':
                o = input("Enter octal number: ")
                if all(ch in '01234567' for ch in o):
                    print("Decimal:", int(o, 8))
                else:
                    print("Error: Octal number must contain digits 0–7 only")
            elif choice == '6':
                h = input("Enter hexadecimal number: ")
                try:
                    print("Decimal:", int(h, 16))
                except ValueError:
                    print("Error: Invalid hexadecimal format")
            elif choice == '7':
                break
            else:
                print("Invalid choice")
        except ValueError:
            print("Error: Please enter a valid integer")
#part 2
#The Bitwise menu
def bitwise_menu():
    while True:
        print("The Bitwise Operations")
        print("1. AND (&)")
        print("2. OR (|)")
        print("3. XOR (^)")
        print("4. NOT (~)")
        print("5. Left Shift (<<)")
        print("6. Right Shift (>>)")
        print("7. Back")

        choice = input("Enter choice 1-7: ")

        try:
            if choice in ['1', '2', '3']:
                a = int(input("Enter first integer: "))
                b = int(input("Enter second integer: "))
                if choice == '1':
                    print("Result:", a & b)
                elif choice == '2':
                    print("Result:", a | b)
                elif choice == '3':
                    print("Result:", a ^ b)

            elif choice == '4':
                a = int(input("Enter integer: "))
                print("Result:", ~a)

            elif choice == '5':
                a = int(input("Enter integer: "))
                shift = int(input("Enter shift amount: "))
                print("Result:", a << shift)

            elif choice == '6':
                a = int(input("Enter integer: "))
                shift = int(input("Enter shift amount: "))
                print("Result:", a >> shift)
            elif choice == '7':
                break

            else:
                print("Invalid choice.")

        except ValueError:
            print("Error: enter valid integers only")
