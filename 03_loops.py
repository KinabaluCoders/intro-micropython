# Loops - repeating code blocks

# Example 1: Using a for loop with range
print("Example 1: For loop with range")
for i in range(5):
  print(i)
print("-" * 20)

# Example 2: Using a for loop to iterate over a list
print("Example 2: For loop over a list")
colors = ["red", "green", "blue"]
for color in colors:
  print(color)
print("-" * 20)

# Example 3: Using a while loop
print("Example 3: While loop")
count = 0
while count < 3:
  print("Count:", count)
  count += 1
print("-" * 20)

# Example 4: Nested loops
print("Example 4: Nested loops")
for i in range(2):
  for j in range(3):
    print(f"i={i}, j={j}")
print("-" * 20)

# Example 5: Using break in a loop
print("Example 5: Using break")
for i in range(10):
  if i == 5:
    break
  print(i)
print("-" * 20)
