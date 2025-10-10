# function for add
def add(n1,n2):
        return n1 + n2

# function for subtract
def subtract(n1,n2):
    if n1 > n2:
        return n1 - n2
    else:
        return  - n2 + n1
    
# function for multiply
def multiply(n1,n2):
    if type(n1) == str or type(n2) == str:
        print ("Please enter integer or float number")
    else:
        return n1 * n2
# n1 = float(input())
# n2 = float(input())

# function for divide
def divide(n1,n2):
    try:
        return n1 / n2
    except ZeroDivisionError:
        return "Please Dont divide by 0 " 
    
    
# function for sqrt
import math
def sqrt(n):
    while True:
     try:
        return math.sqrt(n)
     except ValueError:
        return "negative number will creat imaginary number"
     
# Function for power
def power(n1,n2):
    return n1 ** n2

# functon for reciprocal
def reciprocal(n):
    try:
        return 1 / n
    except ZeroDivisionError:
        return "Please Dont divide by 0 "

    
# function for precentage
def percentage(n,total):
    try:
        return(n / total) * 100
    except ValueError:
        return "The total should greater than zero"
    

def evaluate_exepression():
    a = eval(input("Enter the equation: "))
    print("Result = ",a)

# main function
def StandardMode_Main():
    while True:
        print("----- Standard Mode  -----")
        print("Enter number 1 for add:")
        print("Enter number 2 for subtract:")
        print("Enter number 3 for  multiply:")
        print("Enter number 4 for divide")
        print("Enter number 5 for sqrt:")
        print("Enter number 6 for Power:")
        print("Enter number 7 for reciprocal:")
        print("Enter number 8 for precentage:")
        print("Enter number 9 for evaluate exepression:")
        print("Enter number 0 to Exit:")

        Choose = eval(input("Enter your Choose: "))

        if Choose == 1:
            n1,n2 = eval(input("Enter the numbers eg. 2,3: "))
            print(n1 , "+", n2 ,"= ",add(n1,n2))
        elif  Choose == 2:
            n1,n2 = eval(input("Enter the numbers eg. 2,3: "))
            print(n1 , "-", n2 ," = ",subtract(n1,n2))
        elif Choose == 3:
            n1,n2 = eval(input("Enter the numbers eg. 2,3: "))
            print(n1 , "*", n2 ," = ",multiply(n1,n2))
        elif Choose == 4:
            n1,n2 = eval(input("Enter the numbers eg. 2,3: "))
            print(n1 , "/", n2 ," = ",divide(n1,n2))
        elif Choose == 5:
            n1 = eval(input("Enter the number"))
            print(n1 , "** 0.5" ," = ",sqrt(n1))
        elif Choose == 6:
            n1,n2 = eval(input("Enter the numbers eg. 2,3: "))
            print(n1 , "**", n2 ," = ",power(n1,n2))
        elif Choose == 7:
            n1 = eval(input("Enter the number: "))
            print(" Reciprocal" , n1 ,"=", reciprocal(n1))
        elif Choose == 8:
            n1,total = eval(input("Enter the: number, Total eg. 2,3: "))
            print(n1 ,"of",total ,"=" , power(n1,total),"%")
        elif Choose == 9:
            evaluate_exepression()
        elif Choose == 0:
            break
        else:
            print("Error input try again please")
            Choose = eval(input("Enter your Choose"))


StandardMode_Main():

