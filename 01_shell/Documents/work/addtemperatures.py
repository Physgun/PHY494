# Declare variables and get user input
initKelvin = float(input("Enter an initial Kelvin temperature (FLOAT VALUE): "))
deltaKelvin = 0.0
finalKelvin = 0.0

deltaF = float(input("Enter a change of temperature in Fahrenheit (FLOAT VALUE): "))

#Do the maff

deltaKelvin = (5/9)*deltaF
finalKelvin = initKelvin + deltaKelvin

print("The new temperature is ", finalKelvin, " Kelvin.")
