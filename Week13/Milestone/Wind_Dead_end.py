import math

temperature = float(input("What is the temperature? "))
far_or_cel = input("Fahrenheit or Celsius (F/C)? ")

if far_or_cel == "F":
    temperature_num_f = float(temperature) * 1
    print()
    for v in range(5, 65, 5):
        wind_chill_f = 35.74 + 0.6215 * temperature_num_f - 35.75 * v ** 0.16 + 0.4215 * temperature_num_f * v ** 0.16
        print(f"At temperature {temperature_num_f:.2f} F, and wind speed is {v:.2f} mph,")