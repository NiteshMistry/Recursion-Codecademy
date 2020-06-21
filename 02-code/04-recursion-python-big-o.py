# Define factorial() below:
def factorial(n):
  if n == 1:
    return n
  return n * factorial(n-1)

print(factorial(12))
# print(factorial(1200)) # RecursionError: maximum recursion depth exceeded in comparison