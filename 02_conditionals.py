# Conditionals - when you need to decide on something


# Example 1: Simple if statement
temperature = 25

if temperature > 20:
  print("It's a warm day!")

# Example 2: if-else statement
humidity = 60

if humidity > 70:
  print("The air is humid.")
else:
  print("The air is not too humid.")

# Example 3: if-elif-else statement
light_level = 500

if light_level < 100:
  print("It's dark.")
elif light_level < 600:
  print("It's a bit dim.")
else:
  print("It's bright.")

# Example 4: Using logical operators (and)
temperature = 30
humidity = 80

if temperature > 25 and humidity > 75:
  print("It's hot and humid.")

# Example 5: Using logical operators (or)
battery_voltage = 3.0

if battery_voltage < 3.3 or battery_voltage > 4.2:
  print("Battery voltage is out of optimal range.")
