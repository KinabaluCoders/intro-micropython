# Write a program that prints numbers from 1 to 100.
# But for multiples of five, blink the onboard LED 3 times,
# print the number, and then print 'Buzz' to the console.
# For numbers not divisible by five, ensure the onboard LED is off and print the number to the console.


from machine import Pin  # Import the Pin class for GPIO control
import time              # Import the time module for delays

# Configure the onboard LED pin as an output
led = Pin("LED", Pin.OUT) 

# Loop through numbers from 1 to 100
for number in range(1, 101): # 'range(1, 101)' generates numbers from 1 up to, but not including, 101
    # Check if the number is a multiple of 5 using the modulo operator
    # The modulo operator (%) returns the remainder of a division. If the remainder is 0, the number is a multiple
    if number % 5 == 0:
        # If it's a multiple of 5, blink the LED 3 times
        for _ in range(3): # Nested loop to control the blinks
            led.value(1)       # Turn LED on (set pin to "on" or high level)
            time.sleep(0.1)    # Wait for 0.1 seconds
            led.value(0)       # Turn LED off (set pin to "off" or low level)
            time.sleep(0.1)    # Wait for 0.1 seconds between blinks
        print(number)      # Print the number to the console
        print("Buzz")      # Print "Buzz" to the console
    else:
        # If not a multiple of 5, ensure the LED is off
        led.value(0)       # Turn LED off
        print(number)      # Print the number to the console

    # Add a 1-second delay after processing each number
    time.sleep(1) # Pause for 1 second

# After the loop finishes, ensure the LED remains off
led.value(0) # Ensures the LED is off at the end of the program

