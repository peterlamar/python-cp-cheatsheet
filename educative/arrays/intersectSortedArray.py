def intersect_sorted_array(A, B):
    intersection = []
    seenNum = {}

    for a in A:
        if a not in seenNum:
            seenNum[a] = 0
    
    for b in B:
        if b in seenNum:
            if seenNum[b] == 0:
                seenNum[b] = 1
                intersection.append(b)
    
    return intersection

A = [2, 3, 3, 5, 7, 11]
B = [3, 3, 7, 15, 31]

print(intersect_sorted_array(A, B))