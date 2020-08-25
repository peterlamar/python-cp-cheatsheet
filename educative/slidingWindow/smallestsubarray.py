"""
time: 13 min

error: missed edge case

  if rtn == float('inf'):
    rtn = 0
"""
def smallest_subarray_with_given_sum(s, arr):
  rtn, minTotal, total, j = float('inf'), 0, 0, 0

  for i, n in enumerate(arr):
    total += n
    while total >= s:
      rtn = min(i - j + 1, rtn)
      total -= arr[j]
      j += 1

  if rtn == float('inf'):
    rtn = 0
  return rtn
