def TempConvert(fah):
    cel = 5/9*(fah-32)
    kel = cel + 273.15
    return cel,kel

temp = float(input("input temperature in fahrenheit = "))
cel1, kel1 = TempConvert(temp)
print("temp in Fahrenheit = ", temp)
print("temp in Celsius = ", cel1)
print("temp in Kelvin = ", kel1)