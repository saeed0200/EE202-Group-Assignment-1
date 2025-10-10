
print("Converter Mode")
print("Categorys: \n1.Length \n2.Weight \n3.Temperature")
category = input("Category: ").lower()

def toKg(fromUnit,toUnit,value): # This is a function to convert to base weight unit
    # Conversion Factors to Kg
    G=0.001
    Lb=0.4536
    Oz=0.0283

    
    if fromUnit =="g":
        kg=G*value
    elif fromUnit=="lb":
        kg=Lb*value
    elif fromUnit=="oz":
        kg=Oz*value
    else:
        kg=value
    return fromKg(toUnit,kg)


def fromKg(toUnit,kg): # This function to caculte the final result for the lenght catagory
   # Conversion Factors from kg
   G=1000
   Lb=2.2
   Oz=35.374

   if toUnit=="g":
       result=G*kg
   elif toUnit=="lb":
       result=Lb*kg
   elif toUnit=="oz":
       result=Oz*kg
   else:
       result=kg
    
   return result






def checkValue(value): # a function to check if the value is postive or not
    while True:
        if value <0:
            print("Invalid value, please inter a postive number")
            value=eval(input("value: "))
        else:
            return value

    


def ToMeter(fromUnit,toUnit,value): # This is a function to convert to base length unit
   # Conversion Factors
   M=1
   Cm=0.01 
   In=0.0254
   Ft=0.3058
   # converting to meters
   if fromUnit =="cm":
       meters=Cm*value
       
   elif fromUnit=="in":
       meters=In*value

   elif fromUnit=="ft":
       meters=Ft*value
   elif fromUnit =="m":
       meters=value
   return fromMeter(toUnit,meters) #sending the value in meters to calculte it in the wanted unit

def fromMeter(toUnit,meters): # This function to caculte the final result for the lenght catagory
   # Conversion Factors
   Cm=100
   In=39,37
   Ft=3.28
   
   #converting to the wanted lenght unit
   if toUnit=="cm":
      result = Cm*meters
   elif toUnit =="in":
       result=In*meters
   elif toUnit =="ft":
       result =Ft*meters
   elif toUnit =="m":
       result=meters


   return result


def unitcheck(list,choice,type): #This is a function to check if the user chose a correct unit
    while True:
        if choice in list:
            return choice
        else:
            print("invalid choise")
            choice = input(f"please chose one of these units to convert {type} {list}: ").lower()


def length():
    lengthUnits =["m","cm","ft","in"] # A list of all lenght units
    print(f"Lenght units: {lengthUnits}")
    fromUnit = input("choose unit to convert from: ").lower() # The unit to convert from
    fromUnit = unitcheck(lengthUnits,fromUnit,"from") # to make sure that the user intered a valid unit
    toUnit= input("choose unit to convert to: ").lower() # The unit to convert to
    toUnit= unitcheck(lengthUnits,toUnit,"to")
    value=eval(input("Value: "))
    value= checkValue(value) #To check if the value of the lenght is postive
    result=ToMeter(fromUnit,toUnit,value)
    print(result,toUnit)
    

def weight():
    weightUnits=["kg","g","lb","oz"]
    print(f"Weigh units: {weightUnits}")
    fromUnit = input("choose unit to convert from: ").lower() # The unit to convert from
    fromUnit = unitcheck(weightUnits,fromUnit,"from") # to make sure that the user intered a valid unit
    toUnit= input("choose unit to convert to: ").lower() # The unit to convert to
    toUnit= unitcheck(weightUnits,toUnit,"to")
    value=eval(input("Value: "))
    value= checkValue(value) #To check if the value of the lenght is postive
    result=toKg(fromUnit,toUnit,value)
    print(result,toUnit)



def main(category):
    if category=="length" or category =="1":
        length()
    elif category=="weight" or category =="2":
        weight()


main(category)







