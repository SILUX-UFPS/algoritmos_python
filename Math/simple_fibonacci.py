# Algorithm that returns a list of Fibonacci numbers up to a given number

def fibonacci(n):
    prev_number = 0
    next_number = 0
    numbers = []

    while(next_number < n):
        numbers.append(next_number)
        next_number = next_number + prev_number
        prev_number = next_number - prev_number
        if(next_number == 0):
            next_number = next_number + 1
    return numbers


# In this example it will print a sequence of numbers up to 100
print(fibonacci(100))

# This code is contributed by Anderson Barbosa
