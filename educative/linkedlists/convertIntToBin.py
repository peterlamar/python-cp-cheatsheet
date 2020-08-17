from stack import Stack

# Return string of binary
def convert_int_to_bin(dec_num):
  sk = []
  rtn = ""

  if dec_num == 0:
    return 0

  while dec_num > 0:
    bn = dec_num % 2
    sk.append(bn)
    dec_num = dec_num // 2
 
  while sk:
    rtn = rtn + str(sk.pop()) 
  return rtn