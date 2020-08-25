"""
time: 13 min
errors: 
maxLetter was unitialized and checked incorrectly in hash
"""
def length_of_longest_substring(str, k):
  lgSub, j, maxLetter = 0, 0, ''
  ht = {}

  for i, c in enumerate(str):

    if maxLetter == '':
      maxLetter = c

    if c in ht:
      ht[c] += 1
    else:
      ht[c] = 1

    if ht[c] >= ht[maxLetter]:
      maxLetter = c    

    curSub = 0
    for sc in ht:
      if sc != maxLetter:
        curSub += ht[sc]
    
    if curSub <= k:
      lgSub = max(lgSub, i-j+1)
    else:
      rmchar = str[j]
      ht[rmchar] -= 1
      if ht[rmchar] <= 0:
        del ht[rmchar]
      j += 1
    
  return lgSub


def main():
  print(length_of_longest_substring("aabccbb", 2))
  print(length_of_longest_substring("abbcb", 1))
  print(length_of_longest_substring("abccde", 1))


main()
