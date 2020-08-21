def recursive_multiply(x, y):
  if x == 1:
    return y
  
  return recursive_multiply(x - 1, y) + y