# Write a program that prints numbers from 1 to 100.
# But for multiples of three, print 'Fizz' instead of the number.
# For the multiples of five, print 'Buzz'.
# For numbers which are multiples of both three and five, print 'FizzBuzz'.

# Define a function to perform the FizzBuzz logic
def fizzbuzz(limit):
    for number in range(1, limit + 1):  # Loop from 1 up to the limit
        output = ""
        # Check for multiples of both 3 and 5 first
        if number % 3 == 0 and number % 5 == 0:
            output = "FizzBuzz"
        # Then check for multiples of 3
        elif number % 3 == 0:
            output = "Fizz"
        # Then check for multiples of 5
        elif number % 5 == 0:
            output = "Buzz"
        # If none of the above, print the number itself
        else:
            output = str(number)
        print(output)

# Call the function to run FizzBuzz up to 100
fizzbuzz(100)
