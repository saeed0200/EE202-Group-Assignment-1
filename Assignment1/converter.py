# Constants for coloring output
COLORS = {
    "green": "\033[92m",    # Green: results
    "yellow": "\033[93m",   # Yellow: titles 
    "red": "\033[91m",      # Red: errors
    "reset": "\033[0m"      # Reset: back to normal
}

''' '''
def cprint(text, kind): # take the text here and print it in a specific colour
    """Prints text in a specific color."""
    if kind in COLORS:
        color_code = COLORS[kind]
    else:
        color_code = COLORS["reset"]      # if the color is unknown

        
    print(f"{color_code}{text}{COLORS['reset']}")

history = []
''' this is the main function for the temperature when called it ask the user for the unit he want to convert from
and the unit he want to convert to and the value of the unit he want convert from, after that send the input to 
(tocelius) function to do the calculation'''
def temperature(): # Here is the main function for temperature catagory

    temperatureUnits=["F","C","K"]
    cprint(f"Temperature units: {temperatureUnits}", "yellow") # Coloring unit list
    fromUnit = input("choose unit to convert from: ").upper() # The unit to convert from
    fromUnit = unitcheck(temperatureUnits,fromUnit,"from") # to make sure that the user intered a valid unit
    toUnit= input("choose unit to convert to: ").upper() # The unit to convert to
    toUnit= unitcheck(temperatureUnits,toUnit,"to")
    value=checkValue()
    
    result_val = toCelius(fromUnit,toUnit,value)
    
    history.append(f"Temperature: {value} {fromUnit} {result_val} {toUnit}") # add the result to the history
    
    cprint(f"Result: {result_val} {toUnit}", "green") # Coloring result

def toCelius(fromUnit,toUnit,value): # here we convert the enterd value of tempreature to celcius
    # Conversion Factors to celsius
    FtoC=(value-32)*5/9
    KtoC=value-273.15
    if fromUnit=="C":
        return fromCelsius(toUnit,value)
    elif fromUnit=="F":

        return fromCelsius(toUnit,FtoC)
    elif fromUnit=="K":
        return fromCelsius(toUnit,KtoC)

def fromCelsius(toUnit,c): # here we recive the value of tempreature in cilsius and convert it to the wanted unit
    # Conversion Factors from celsius
    CtoF=c*9/5+32
    CtoK=c + 273.15
    if toUnit=="F":
        result =CtoF
    elif toUnit=="K":
        result=CtoK
    elif toUnit=="C":
        result=c
    return result


# ======================================================================
# opitional category (Volume)
# ======================================================================

def fromLiter(toUnit, liters):
    # Conversion Factors from Liters
    ML = 1000
    GALLON = 0.264172       
    OZ_FLUID = 33.814     

    if toUnit == "ml":
        result = ML * liters
    elif toUnit == "gal":
        result = GALLON * liters
    elif toUnit == "oz":
        result = OZ_FLUID * liters
    else:  # if toUnit == "l"
        result = liters
        
    return result

def toLiter(fromUnit, toUnit, value):
    # This is a function to convert to base Volume unit (Liter)
    # Conversion Factors to Liters
    ML_FACTOR = 0.001
    GALLON_FACTOR = 3.78541 
    OZ_FACTOR = 0.0295735 

    # converting to liters
    if fromUnit == "ml":
        liters = ML_FACTOR * value
    elif fromUnit == "gal":
        liters = GALLON_FACTOR * value
    elif fromUnit == "oz":
        liters = OZ_FACTOR * value
    else:  # if fromUnit == "l"
        liters = value

    return fromLiter(toUnit, liters)

def volume():
    # Here is the main function for Volume catagory
    volumeUnits = ["l", "ml", "gal", "oz"]
    cprint(f"Volume units: {volumeUnits}", "yellow") 
    fromUnit = input("choose unit to convert from: ").lower()
    fromUnit = unitcheck(volumeUnits, fromUnit, "from")
    toUnit = input("choose unit to convert to: ").lower()
    toUnit = unitcheck(volumeUnits, toUnit, "to")
    value = checkValue()
    result = toLiter(fromUnit, toUnit, value)
    
    history.append(f"Volume: {value} {fromUnit} = {result} {toUnit}") # add the result to the history
    
    cprint(f"Result: {result} {toUnit}", "green") 


def toKg(fromUnit,toUnit,value): # This is a function to convert to base weight unit
    # Conversion Factors to Kg
    G=0.001
    Lb=0.4536
    Oz=0.0283
    Mg=0.000001 
    if fromUnit =="g":
        kg=G*value
    elif fromUnit=="lb":
        kg=Lb*value
    elif fromUnit=="oz":
        kg=Oz*value
    elif fromUnit=="mg": 
        kg=Mg*value
    else:
        kg=value
    return fromKg(toUnit,kg)


def fromKg(toUnit,kg): # This function to caculte the final result for the lenght catagory
    # Conversion Factors from kg
    G=1000
    Lb=2.2
    Oz=35.374
    Mg=1000000 
    if toUnit=="g":
        result=G*kg
    elif toUnit=="lb":
        result=Lb*kg
    elif toUnit=="oz":
        result=Oz*kg
    elif toUnit=="mg":
        result=Mg*kg
    else:
        result=kg
    
    return result

def weight():
    weightUnits=["kg","g","lb","oz","mg"] # UPDATED: added 'mg'
    cprint(f"Weigh units: {weightUnits}", "yellow") # coloring unit list
    fromUnit = input("choose unit to convert from: ").lower() # The unit to convert from
    fromUnit = unitcheck(weightUnits,fromUnit,"from") # to make sure that the user intered a valid unit
    toUnit= input("choose unit to convert to: ").lower() # The unit to convert to
    toUnit= unitcheck(weightUnits,toUnit,"to")
    value= checkValue() #To check if the value of the lenght is postive
    
    result=toKg(fromUnit,toUnit,value)
    
    history.append(f"Weight: {value} {fromUnit} = {result} {toUnit}")  # add the result to the history
    
    cprint(f"Result: {result} {toUnit}", "green") # Coloring result


def checkValue(): # a function to check if the value is postive or not
    while True:
        try:
            value=eval(input("value:"))
        except NameError:
            print("Please inter numbers only", "red")
            continue
        if value <0:
            cprint("Invalid value, please inter a postive number", "red") # Coloring warning
        else:
            return value
        
def ToMeter(fromUnit,toUnit,value): # This is a function to convert to base length unit
    # Conversion Factors
    M=1
    Cm=0.01 
    In=0.0254
    Ft=0.3058
    Km=1000 
    Mile=1609.34 
    
    # converting to meters
    if fromUnit =="cm":
        meters=Cm*value
        
    elif fromUnit=="in":
        meters=In*value

    elif fromUnit=="ft":
        meters=Ft*value
    elif fromUnit=="km": # NEW
        meters=Km*value
    elif fromUnit=="mile": # NEW
        meters=Mile*value
    elif fromUnit =="m":
        meters=value
    return fromMeter(toUnit,meters) #sending the value in meters to calculte it in the wanted unit


def fromMeter(toUnit,meters): # This function to caculte the final result for the lenght catagory
    # Conversion Factors
    Cm=100
    In=39.37
    Ft=3.28
    Km=0.001 
    Mile=0.000621371 
    
    #converting to the wanted lenght unit
    if toUnit=="cm":
        result = Cm*meters
    elif toUnit =="in":
        result=In*meters
    elif toUnit =="ft":
        result =Ft*meters
    elif toUnit =="km": 
        result =Km*meters
    elif toUnit =="mile": 
        result =Mile*meters
    elif toUnit =="m":
        result=meters

    return result


def unitcheck(list,choice,type): #This is a function to check if the user chose a correct unit
    while True:
        if choice in list:
            return choice
        else:
            cprint("invalid choise", "red") # Coloring error
            choice = input(f"please chose one of these units to convert {type} {list}: ").lower()


def length():
    lengthUnits =["m","cm","ft","in","km","mile"] # A list of all lenght units (UPDATED)
    cprint(f"Lenght units: {lengthUnits}", "yellow") # Coloring unit list
    fromUnit = input("choose unit to convert from: ").lower() # The unit to convert from
    fromUnit = unitcheck(lengthUnits,fromUnit,"from") # to make sure that the user intered a valid unit
    toUnit= input("choose unit to convert to: ").lower() # The unit to convert to
    toUnit= unitcheck(lengthUnits,toUnit,"to")
    value= checkValue() #To check if the value of the lenght is postive and to handle NameEror
    
    result=ToMeter(fromUnit,toUnit,value)
    
    history.append(f"Length: {value} {fromUnit} = {result} {toUnit}") # add the result to the history
    
    cprint(f"Result: {result} {toUnit}", "green") # Coloring result


def main_menu():
    cprint("----- Converter Mode  -----", "yellow") # Coloring title
    cprint("Categorys:", "yellow") # Coloring label
    print("1.Length \n2.Weight \n3.Temperature \n4.Volume \n5.Exit \n6.History") 
    
    while True:

        
        category_input = input("Category: ").lower()
        
        if category_input == "history" or category_input == "6":
            cprint(" History", "yellow")
            if len(history)==0:
                print("The history is empty")
            else:
                cprint('\n'.join(history), 'green') 
            print("------------------------------")
            continue
        
        elif category_input == "exit" or category_input == "5": 
            return 
        
        elif category_input == "length" or category_input == "1":
            length()
        elif category_input == "weight" or category_input == "2":
            weight()
        elif category_input == "temperature" or category_input == "3":
            temperature()
        elif category_input == "volume" or category_input == "4": 
            volume()
        
        else:
            cprint("Invalid choise, please chose one of the folowing categorys:", "red") # Coloring error
            cprint("Categorys:", "yellow") # Coloring label
            print("1.Length \n2.Weight \n3.Temperature \n4.Volume \n5.Exit \n6.History")
            continue
        
        cprint("----- Converter Mode  -----", "yellow") # Coloring title
        cprint("Categorys:", "yellow")

        print("1.Length \n2.Weight \n3.Temperature \n4.Volume \n5.Exit \n6.History")
        if category_input=="exit" or category_input=="5": 
             return



