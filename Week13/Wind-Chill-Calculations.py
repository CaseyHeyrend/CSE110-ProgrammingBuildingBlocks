# Wind Chill(F)  = 35.74 + 0.6215T - 35.75(V^0.16) + 0.4275T(V^0.16)
# 35.74 + 0.6215 * temperature - 35.75 * (speed_c ** 0.16) + 0.4275 * temperature * (speed_c ** 0.16), 2
# Where, T = Air Temperature(F) V = Wind Speed (mph)

def windchill_formula(temperature, speed_c):
    return round(35.74 + 0.6215 * temperature - 35.75 * (speed_c ** 0.16) +0.4275 * temperature * (speed_c ** 0.16), 2)#Fahrenheit
def windchill_formula_c(temp_cel, speed_a):
    return round(35.74 + 0.6215 * ((temp_cel * (9 / 5)) + 32) - 35.75 * (speed_a **0.16) + 0.4275 * ((temp_cel * (9 / 5)) + 32) * (speed_a ** 0.16), 2)#Celsius

temperature = float(input('What is the temperature? '))
degree = input("Fahrenheit or Celsius (F/C)? ")
for speed_w in range(5, 65, 5):
    speed_c = speed_w
    if degree == 'F':#Fahrenheit
            print(f'At temperature {temperature}F, and wind speed {speed_w} mph, the windchill is: {windchill_formula(temperature, speed_c)}F.')
    elif degree == 'C':#Celsius
        temp_cel = temperature
        speed_a = speed_w
        print(f'At temperature {temperature}F, and wind speed {speed_w} mph, the windchill is: {windchill_formula_c(temp_cel, speed_a)}F.')