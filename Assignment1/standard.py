# constants for coloring output
COLORS = {
    "green": "\033[92m",    # Green: results
    "yellow": "\033[93m",   # Yellow: titles, warnings
    "red": "\033[91m",      # Red: erors
    "reset": "\033[0m"      # Reset: back to normal
}


def cprint(text, kind):  # take the text here and print it in a specific colour
    if kind in COLORS:
        color_code = COLORS[kind]
    else:
        color_code = COLORS["reset"]          # if the color is unknown

        
    print(f"{color_code}{text}{COLORS['reset']}")
  


history = []

# function for add
'''This function adds two numbers n1 and n2, stores the operation in a history list, and returns the result.
It helps keep track of all addition operations performed.'''

def add(n1,n2):
    result = n1 + n2
    history.append(f"{n1} + {n2} = {result}")
    return result

# function for subtract
def subtract(n1,n2):
    if n1 > n2:
        result = n1 - n2
        history.append(f"{n1} - {n2} = {result}")
        return result
    else:
        result = - n2 + n1
        history.append(f"{n1} - {n2} = {result}")
        return result
    
# function for multiply
def multiply(n1,n2):
    if type(n1) == str or type(n2) == str:
        cprint("Please enter integer or float number", "red")
    else:
        result = n1 * n2
        history.append(f"{n1} * {n2} = {result}")
        return result

# function for divide
def divide(n1,n2):
    try:
        result = n1 / n2
        history.append(f"{n1} / {n2} = {result}")
        return result
    except ZeroDivisionError:
        return COLORS["red"] + "Please Dont divide by 0 " + COLORS["reset"]
    
    
# function for sqrt
import math
def sqrt(n):
    while True:
      try:
        result = math.sqrt(n)
        history.append(f"sqrt({n}) = {result}")
        return result
      except ValueError:
        return COLORS["red"] + "negative number will creat imaginary number" + COLORS["reset"]
      
# Function for power
def power(n1,n2):
    result = n1 ** n2
    history.append(f"{n1} ** {n2} = {result}")
    return result

# functon for reciprocal
def reciprocal(n):
    try:
        result = 1 / n
        history.append(f"1 / {n} = {result}")
        return result
    except ZeroDivisionError:
        return COLORS["red"] + "Please Dont divide by 0 " + COLORS["reset"]

    
# function for precentage
def percentage(n1,total):
    try:
        result = (n1 / total) * 100
        history.append(f"({n1} / {total}) * 100 = {result}%")
        return result
    except ValueError:
        return COLORS["red"] + "The total should greater than zero" + COLORS["reset"]
    

def evaluate_exepression():
    a_input = input(COLORS["yellow"] + "Enter the equation: " + COLORS["reset"])
    a = eval(a_input)
    cprint(f"Result = {a}", "green")
    history.append(f"Expression result: {a}")

# main function
def main_menu():
    while True:
        cprint("----- Standard Mode  -----", "yellow")
        print("Enter number 1 for add:")
        print("Enter number 2 for subtract:")
        print("Enter number 3 for  multiply:")
        print("Enter number 4 for divide")
        print("Enter number 5 for sqrt:")
        print("Enter number 6 for Power:")
        print("Enter number 7 for reciprocal:")
        print("Enter number 8 for precentage:")
        print("Enter number 9 for evaluate exepression:")
        print("Enter number 10 for History:")
        print("Enter number 0 to Exit:")
          
        Choose = checChoose()
          
        if Choose == 1:
            
            n1,n2 =checknumber()
            cprint(f"{n1} + {n2} = {add(n1,n2)}", "green")
            
        elif  Choose == 2:
            n1,n2 = eval(input(COLORS["yellow"] + "Enter the numbers eg. 2,3: " + COLORS["reset"]))
            cprint(f"{n1} - {n2} = {subtract(n1,n2)}", "green")
            
        elif Choose == 3:
            n1,n2 = checknumber()
            cprint(f"{n1} * {n2} = {multiply(n1,n2)}", "green")
            
        elif Choose == 4:
            n1,n2 =checknumber()
            cprint(f"{n1} / {n2} = {divide(n1,n2)}", "green")
            
        elif Choose == 5:
            n1 = checknumberr()
            cprint(f"{n1} ** 0.5 = {sqrt(n1)}", "green")
            
        elif Choose == 6:
            n1,n2 = checknumber()
            cprint(f"{n1} ** {n2} = {power(n1,n2)}", "green")
            
        elif Choose == 7:
            n1 = eval(input(COLORS["yellow"] + "Enter the number: " + COLORS["reset"]))
            cprint(f" Reciprocal {n1} = {reciprocal(n1)}", "green")
            
        elif Choose == 8:
            n1,total = checknumber()
            cprint(f"{n1} of {total} = {percentage(n1,total)}%", "green")
            
        elif Choose == 9:
            evaluate_exepression()
        
        elif Choose == 10:
            cprint("History", "yellow")
            if len(history) == 0:
                print("The History is empty")
            else:
                cprint('\n'.join(history), 'green') 
            print("------------------------------") 
        elif Choose == 0:
            cprint("THANK YOU", "green")
            break
            
        else:
            cprint("Error input try again please", "red")
            Choose = eval(input(COLORS["yellow"] + "Enter your Choose" + COLORS["reset"]))



def checChoose(): # a function to check if the value is postive or not
    while True:
        try:
            value = eval(input(COLORS["yellow"] + "Enter your Choose: " + COLORS["reset"]))
        except NameError:
            cprint("Please Enter numbers only", "red")
            continue

        return value

def checknumber(): # a function to check if the value is postive or not
    while True:
        try:
           n1,n2 = eval(input(COLORS["yellow"] + "Enter the numbers eg. 2,3: " + COLORS["reset"]))
        except NameError:
            cprint("Please Enter numbers only", "red")
            continue

        return n1,n2
def checknumberr(): # a function to check if the value is postive or not
    while True:
        try:
           n1 = eval(input(COLORS["yellow"] + "Enter the number" + COLORS["reset"]))
        except NameError:
            cprint("Please Enter numbers only", "red")
            continue

        return n1

