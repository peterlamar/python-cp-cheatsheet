"""
time: 13 min
errors: none!

"""

def non_repeat_substring(str):
  maxLen, i = 0, 0
  ht = {}

  for i, c in enumerate(str):
    if c in ht:
      maxLen = max(maxLen, len(ht))
      ht.clear()
    ht[c] = True
  
  maxLen = max(len(ht), maxLen) 

  return maxLen

def main():
  print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
  print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
  print("Length of the longest substring: " + str(non_repeat_substring("abccde")))


main()