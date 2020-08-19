def find_highest_number(A):

    if len(A) < 3:
        return None

    def condition(value) -> bool:  
        leftNeighbor = value - 1
        rightNeighbor = value + 1

        # TODO: Add conditions for leftmost and rightmost values

        if A[leftNeighbor] < A[value] < A[rightNeighbor]:
            return False
        elif A[leftNeighbor] > A[value] > A[rightNeighbor]:
            return True
        elif A[leftNeighbor] < A[value] and A[value] > A[rightNeighbor]:
            return True

    left, right = 0, len(A) -1
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid 
        else:
            left = mid + 1

    return A[left]

# Peak element is "5".
A = [1, 2, 3, 4, 5, 4, 3, 2, 1]
print(find_highest_number(A))
A = [1, 6, 5, 4, 3, 2, 1]
print(find_highest_number(A))
A = [1, 2, 3, 4, 5]
print(find_highest_number(A))
A = [5, 4, 3, 2, 1]
print(find_highest_number(A))