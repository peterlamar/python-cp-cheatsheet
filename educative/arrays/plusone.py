A1 = [1, 4, 9]
A2 = [9, 9, 9]

# s = ''.join(map(str, A))
# print(int(s) + 1)
1 , 4 , 9

def plus_one(A):

    carry, total = 1, 0

    if len(A) == 0 or len(A) == 1:
        return 

    for i in reversed(range(0, len(A))):
        total = (A[i] + carry) 
        carry =  total // 10
        A[i] = total % 10

    if carry == 1:
        A.insert(0, 1)

    return A

print(plus_one(A1))
print(plus_one(A2))