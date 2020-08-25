"""
time : 17 min
error:
used pop instead of del ht[jc]
"""

def longest_substring_with_k_distinct(str, k):
  j, lgSub = 0, 0
  ht = {}
  
  for i, c in enumerate(str):
    if c in ht:
      ht[c] += 1
    else:
      ht[c] = 1

    if len(ht) <= k:
      lgSub = max(lgSub, i-j + 1)
    else:
      jc = str[j]

      ht[jc] -= 1
      if ht[jc] <= 0:
        del ht[jc]
      j += 1

  return lgSub


def main():
  print("Length of the longest substr1ing: " + str(longest_substring_with_k_distinct("araaci", 2)))
  print("Length of the longest substr1ing: " + str(longest_substring_with_k_distinct("araaci", 1)))
  print("Length of the longest substr1ing: " + str(longest_substring_with_k_distinct("cbbebi", 3)))


main()
