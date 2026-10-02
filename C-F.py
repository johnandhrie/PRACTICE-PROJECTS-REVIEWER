def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

print(f"25°C is {celsius_to_fahrenheit(25):.2f}°F")