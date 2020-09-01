class Solution:
    def toHex(self, num: int) -> str:
    rtn = []
    index = "0123456789abcdef"
    if num == 0: return '0'
    if num < 0: num += 2 ** 32
    while num > 0:
        digit = num % 16
        num = num // 16
        rtn.append(index[digit])
    return "".join(rtn[::-1])