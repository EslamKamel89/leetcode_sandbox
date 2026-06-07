import random

n = 6 
max = 90

if n > max:
    raise ValueError("n cannot be greater than max when numbers must be unique.")

numbers = random.sample(range(1,max+1) , n)
numbers.sort()
print(numbers)