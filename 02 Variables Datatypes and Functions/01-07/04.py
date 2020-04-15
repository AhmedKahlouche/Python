def celsiusToFahrenheit(C):
    return (C * (9/5) + 32)

def fahrenheitToCelsius(F):
    return ((F - 32)*(5/9))

tempC = input("enter the temperature in C : ")
print("the temperature in F is ", celsiusToFahrenheit(int(tempC)))
