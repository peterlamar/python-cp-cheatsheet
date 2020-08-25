"""
time: 19min

errors:
misread directions, didn't go into big example
permcount = 0
Mis leveled if statement
"""

def find_permutation(str, pattern):

  return False


def main():
  print('Permutation exist: ' + str(find_permutation("oidbcaf", "abc")))
  print('Permutation exist: ' + str(find_permutation("odicf", "dc")))
  print('Permutation exist: ' + str(find_permutation("bcdxabcdy", "bcdyabcdx")))
  print('Permutation exist: ' + str(find_permutation("aaacb", "abc")))


main()
