# Temperature Converter
# A small program for practising Git and GitHub.
# It converts a temperature from Celsius to Fahrenheit and Kelvin.
#
# How to run it:  python temperature_converter.py

# Ask the user for a temperature in Celsius
celsius = float(input("Temperature in Celsius: "))

# Convert to Fahrenheit
fahrenheit = celsius * 9 / 5 + 32

# Convert to Kelvin
kelvin = celsius + 273.15

# Show the result
print("Fahrenheit:", fahrenheit)
print("Kelvin:", kelvin)
