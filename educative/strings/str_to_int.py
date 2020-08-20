"""
ord('1') - ord('0') == 1
123

"""
def str_to_int(input_str):

  if len(input_str) == 0:
    return 0

  rtn = 0
  place = 1

  for c in reversed(input_str):
    if c.isalnum():
      rtn += place * (ord(c)- ord('0'))
      place *= 10
    elif c == '-':
      rtn *= -1

  return rtn