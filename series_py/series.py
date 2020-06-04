
def fibo_nth(n):
  """fibonacci function that takes in number and returns the nth value in the fibonacci sequence """
  if n == 1:
    return 1
  elif n == 2 :
    return 1
  else:
    return ( fibo_nth(n-1) + fibo_nth(n-2) )
print(fibo_nth(7))

def lucas_nth(n):
  """lucas function that takes in number and returns the nth value in the lucas number seqeunce"""
  if n == 0:
    return 2
  if n == 1:
    return 1
  if n == 2:
    return 3
  else: 
    return (lucas_nth(n-1) + lucas_nth(n-2))
print(lucas_nth(2))

def sum_series(n, a=0, b=1):
  """    This sum_series function takes in a required parameter(n) which indicates which nth value to return in the series. There are two optional parameters to indicate the series. If no a and b arguments provided it will default to standard fibonacci series: 0, 1. """
  if n == 0:
    return a
  elif n == 1:
    return b
  else: 
    return(sum_series(n-1, a, b) + sum_series(n-2, a, b))
print(sum_series(5,3,3))
  