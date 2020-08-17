def array_advance(A):
    furthest_reached = 0
    i=0
    lastIndex = len(A)-1

    # If furthest reach still has range and we have not reached goal
    while i <= furthest_reached and furthest_reached < lastIndex:
        furthest_reached = max(furthest_reached, A[i]+i)
        i += 1

    return furthest_reached >= lastIndex


# True: Possible to navigate to last index in A:
# Moves: 1,3,2
A = [3, 3, 1, 0, 2, 0, 1]
print(array_advance(A))

# False: Not possible to navigate to last index in A:

A = [2, 4, 1, 1, 0, 2, 3, 0, 0, 3,0,0,3,0,0,2,0]
print(array_advance(A))