"""
time: 14

errors: none!
"""
def length_of_longest_substring(arr, k):
  j, lgSub, seenZ = 0, 0, 0

  for i, n in enumerate(arr):
    if n == 0:
      seenZ += 1

    while seenZ > k:
      if arr[j] == 0:
        seenZ -= 1
      j += 1
    
    lgSub = max(lgSub, i-j+1)

  return lgSub



def main():
  print(length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
  print(length_of_longest_substring(
    [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))


main()
