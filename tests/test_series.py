from series_py.series import fibonacci
from series_py.series import lucas
from series_py.series import sum series
# fibonacci tests 
def test_fibonacci_zero():
  expected = 0 
  actual = fibonacci(0)
  assert actual == expected
def test_fibonacci_one():
  expected = 1
  actual = fibonacci(1)
  assert actual == expected
def test_fibonacci_two():
  expected = 1
  actual = fibonacci(2)
  assert actual == expected
def test_fibonacci_five():
  actual = fibonacci(5)
  expected = 5 
  assert actual == expected
# test lucas 
def test_lucas_zero():
  actual = lucas(0)
  expected = 2
  assert actual == expected
def test_lucas_one():
  actual = lucas(1)
  expected = 1
  assert actual == expected
def test_lucas_two():
  actual = lucas(2)
  expected = 3
  assert actual == expected
def test_lucas_five():
  actual = lucas(5)
  expected = 11
  assert actual == expected
# sum series
def test_sumof():
  actual = sum_series(0,0,1)
  expected = 0 
  assert actual == expected 
