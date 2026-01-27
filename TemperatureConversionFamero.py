#MARC RODEN D. FAMERO BSIT 1-3
#PYTHON PRACTICE: TEMPERATURE CONVERSION
#C = (F - 32) x 5/9
#F = (Cx9/5) + 32
#K= (F-32) x 5/9 + 273.15
#F = (K - 273.15) x 9/5 + 32

while True:
    name = input("Enter your name: ")
    print ("Hello," +name+"!")

    age = int (input("Enter Your Age: "))
    print ("You are" ,age, "years old")

    #FAHRENHEIT  TO CELCIUS
    print ("CONVERT FAHRENHEIT  TO CELCIUS")
    F = float (input ("ENTER TEMPERATURE IN FAHRENHEIT: "))
    C = (F - 32) * 5/9
    print (F, "Fahrenheit is equal to: ", C , "Celcius") 
                 
    #CELCIUS TO FAHRENHEIT
    print ("CONVERT CELCIUS TO FAHRENHEIT")
    C = float (input ("ENTER TEMPERATURE IN CELCIUS: "))
    F = (C * 9/5) + 32
    print (C, "Celcius is equal to: ", F , "Fahrenheit")

    #FAHRENHEIT TO KELVIN
    print ("CONVERT  FAHRENHEIT TO KELVIN")
    F = float (input ("ENTER TEMPERATURE IN FAHRENHEIT: "))
    K= (F-32) * 5/9 + 273.15
    print (F, "Fahrenheit is equal to: ", K , "Kelvin")

    #KELVIN TO FAHRENHEIT
    print ("CONVERT KELVIN TO FAHRENHEIT")
    K = float (input ("ENTER TEMPERATURE IN KELVIN: "))
    F = (K - 273.15) * 9/5 + 32
    print (K, "Kelvin is equal to: ", F , "Fahrenheit")

    print ("====END OF PROGRAM====")
