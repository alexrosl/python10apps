def weather_condition(temperature):
    if temperature > 7:
        return "Warn"
    else:
        return "Cold"


temp = float(input("Enter temperature: "))
print(weather_condition(temp))
