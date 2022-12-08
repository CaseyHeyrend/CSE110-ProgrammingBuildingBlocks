def wind_chill_formula(temperature, speed_c):
    return round(35.74 + 0.6215 * temperature - 35.75 * (speed_c ** 0.16) + 0.4275 * temperature * (speed_c ** 0.16), 2)
def wind_chill_formula(temperature_c, speed_a):
    return round(35.74 + 0.6215 * temperature_c - 35.75 * (speed_a ** 0.16) + 0.4275 * temperature_c * (speed_a ** 0.16), 2)
temperature = float(input("What is the temperature? "))
far_or_cel = input("Fahrenheit or Celsius (F/C)? ")

# Wind Chill(F)  = 35.74 + 0.6215T - 35.75(V^0.16) + 0.4275T(V^0.16)
# 35.74 + 0.6215 * temperature - 35.75 * (speed_c ** 0.16) + 0.4275 * temperature * (speed_c ** 0.16), 2
# Where, T = Air Temperature(F) V = Wind Speed (mph)