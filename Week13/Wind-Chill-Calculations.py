#Wind Chill(ºF) = 35.74 + 0.6215T - 35.75(V0.16) + 0.4275T(V0.16)
print('=' * 65, 'WIND CHILL ☁ ☁ ☁ ' , '=' * 18)
vaule = float(input("What is the temperature? "))
wind = -1
conversion = formula = 9 * vaule / 5 + 32
degree = input("Fahrenheit or Celsius (F/C)? ")
print()
def C_to_F():
    formula = 9 * vaule / 5 + 32
    temperature = formula
    windchillformula = 35.74 + 0.6215 * temperature - 35.75 * (wind ** 0.16) + 0.4275 * temperature * (wind ** 0.16)
    return windchillformula
def wind_chill():
    formulawc = 35.74 + 0.6215 * vaule - 35.75 * (wind ** 0.16) + 0.4275 * vaule * (wind ** 0.16)

#def wind_chill_formula(temperature, speed_c):
    #return round(35.74 + 0.6215 * temperature - 35.75 * (wind ** 0.16) + 0.4275 * temperature * (wind ** 0.16), 2)
#def wind_chill_formula(temperature_c, speed_a):
    #return round(35.74 + 0.6215 * temperature_c - 35.75 * (speed_a ** 0.16) + 0.4275 * temperature_c * (speed_a ** 0.16), 2)

# 35.74 + 0.6215 * temperature - 35.75 * (speed_c ** 0.16) + 0.4275 * temperature * (speed_c ** 0.16), 2
# Where, T = Air Temperature(F) V = Wind Speed (mph)