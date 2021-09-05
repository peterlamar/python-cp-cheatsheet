"""
For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].
Read instructions and realize problem is easier, just
have to sort and reinsert
"""
def sortByHeight(a):
    b = sorted(i for i in a if i != -1)

    j = 0
    for i in range(len(a)):
        if a[i] != -1:
            a[i] = b[j]
            j += 1
    return a