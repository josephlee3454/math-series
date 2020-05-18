def fibonacci(n):
  if n==1:
    return 1
  elif n == 0:
    return 0
  # elif n > 2:
  else: 
      return fibonacci(n -1) + fibonacci(n-2)
# for n in range (1,11):
#   print(n, ":", fibonacci(n))
# fibonacci(n)

def lucas(n):
  if n==0:
    return 2
  if n == 1:
    return 1
  return lucas(n-1) + lucas(n-2)
# for n in range (2,11):
#   print(n, ":", lucas(n))
# lucas(n)
def sum series(n ,thing1, thing2):
  return 5