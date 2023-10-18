def fibonacci(n):
  a = 0
  b = 1

  if n == 0:
    return a

  for _ in range(n-1):
    [a, b] = [b, a+b]
  return b
