### Problem 2 - FizzBuzz

# Given a list of ordered numbers from 1 to 100, perform the following actions
# - For every number divisible by 3, print 'Fizz'
# - For every number divisible by 5, print 'Buzz'
# - For every number divisible by both 3 and 5, print 'FizzBuzz'

# Input: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ..., 100

# Expected output: 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16, ..., 100

def fizzbuzz(list):
  new_list = []
  for num in list:
    if num % 15 == 0:
      new_list.append("FizzBuzz")
    elif num % 3 == 0:
      new_list.append("Fizz")
    elif num % 5 == 0:
      new_list.append("Buzz")
    else:
      new_list.append(num)
  return new_list

input = list(range(1,101))

print(fizzbuzz(input))