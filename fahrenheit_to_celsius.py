def fahrenheit_to_celcius(temperature):
    temp_in_celsius = (temperature -32)*5/9
    print(str(temperature) + " degrees in Fahrenheit is equal to " + str(temp_in_celsius) + " degree(s) in Celsius")

print(fahrenheit_to_celcius(32))