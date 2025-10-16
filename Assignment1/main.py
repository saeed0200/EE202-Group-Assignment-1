import standard
import programmer
import scientific_Module
import converter

def main():
    while True:
        print("\n=== Welcome to Multi-Mode Calculator ===")
        print("1. Standard Mode")
        print("2. Programmer Mode")
        print("3. Scientific Mode")
        print("4. Converter Mode")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            standard.main_menu()
        elif choice == "2":
            programmer.main_menu()
        elif choice == "3":
            scientific_Module.main_menu()
        elif choice == "4":
            converter.main_menu()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
