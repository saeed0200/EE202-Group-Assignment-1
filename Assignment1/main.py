# constants for coloring output
COLORS = {
    "green": "\033[92m",    # Green: results
    "yellow": "\033[93m",   # Yellow: titles, warnings
    "red": "\033[91m",      # Red: erors
    "reset": "\033[0m"      # Reset: back to normal
}


def cprint(text, kind):
    """Prints text in a specific color."""
    if kind in COLORS:
        color_code = COLORS[kind]
    else:
        color_code = COLORS["reset"]
        
    print(f"{color_code}{text}{COLORS['reset']}")



import standard
import programmer
import scientific
import converter

def main():
    while True:
        cprint("\n=== Welcome to Multi-Mode Calculator ===","yellow")
        print("1. Standard Mode")
        print("2. Programmer Mode")
        print("3. Scientific Mode")
        print("4. Converter Mode")
        cprint("5. Exit","red")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            standard.main_menu()
        elif choice == "2":
            programmer.main_menu()
        elif choice == "3":
            scientific.main_menu()
        elif choice == "4":
            converter.main_menu()
        elif choice == "5":
            cprint("Exiting... Goodbye!","green")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 5.","red")

if __name__ == "__main__":
    main()
