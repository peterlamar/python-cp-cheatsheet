import math
# Add any extra import statements you may need here
"""
https://www.quora.com/What-is-the-formula-of-the-sequence-1-3-6-10-15-21

n*(n-1)/2
"""
# Add any helper functions you may need here


def numberOfWays(arr, k):
 	# Write your code here
  ht = {}
  numTimes = 0
  
  for n in arr:
    if n in ht:
      num = ht[n]
      num += 1
      ht[n] = num
    else:
      ht[n] = 1
  
  for n in arr:
    if k - n in ht:
      
      if n != k-n:
        numTimes += 1

        if ht[n] > 1:
          ht[n] -= 1
        else:
          ht.pop(n, None)
      else:
        mynum = ht[n]
        numTimes += (mynum*(mynum-1))//2
        ht.pop(n, None)
      

  return numTimes
      












# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printInteger(n):
  print('[', n, ']', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  k_1 = 6
  arr_1 = [1, 2, 3, 4, 3]
  expected_1 = 2
  output_1 = numberOfWays(arr_1, k_1)
  check(expected_1, output_1)

  k_2 = 6
  arr_2 = [1, 5, 3, 3, 3]
  expected_2 = 4
  output_2 = numberOfWays(arr_2, k_2)
  check(expected_2, output_2)

  # Add your own test cases here
  k_3 = 6
  arr_3 = [1, 5, 3, 3, 3, 3]
  expected_3 = 7
  output_3 = numberOfWays(arr_3, k_3)
  check(expected_3, output_3)  