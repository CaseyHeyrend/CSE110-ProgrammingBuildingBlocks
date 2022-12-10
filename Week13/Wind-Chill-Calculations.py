# Wind Chill(F)  = 35.74 + 0.6215T - 35.75(V^0.16) + 0.4275T(V^0.16)
# 35.74 + 0.6215 * temperature - 35.75 * (power ** 0.16) + 0.4275 * temperature * (power ** 0.16), 2
# Where, T = Air Temperature(F) V = Wind Speed (mph) or power

def windchill_formula(temperature, power):#Fahrenheit
    return round(35.74 + 0.6215 * temperature - 35.75 * (power ** 0.16) +0.4275 * temperature * (power ** 0.16), 2)#Fahrenheit
def windchill_formula_cel(temperature_cel, power_cel):#Celsius
    return round(35.74 + 0.6215 * ((temperature_cel * (9 / 5)) + 32) - 35.75 * (power_cel **0.16) + 0.4275 * ((temperature_cel * (9 / 5)) + 32) * (power_cel ** 0.16), 2)#Celsius

temperature = float(input("What is the temperature? "))
degree = input("Fahrenheit or Celsius (F/C)? ")
for windspeed in range(5, 65, 5):
    power = windspeed
    if degree == "F":#Fahrenheit
            print(f"At temperature {temperature}F, and wind speed {windspeed} mph, the windchill is: {windchill_formula(temperature, power)}F.")
    elif degree == "C":#Celsius
        temperature_cel = temperature
        power_cel = windspeed
        print(f"At temperature {temperature}F, and wind speed {windspeed} mph, the windchill is: {windchill_formula_cel(temperature_cel, power_cel)}F.")
