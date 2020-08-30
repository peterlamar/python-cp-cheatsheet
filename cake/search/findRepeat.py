import unittest

def find_repeat(numbers):
    floor = 1
    ceiling = len(numbers) - 1

    while floor < ceiling:
        # Divide our range 1..n into an upper range and lower range
        # (such that they don't overlap)
        # Lower range is floor..midpoint
        # Upper range is midpoint+1..ceiling
        midpoint = floor + ((ceiling - floor) // 2)
        lower_range_floor, lower_range_ceiling = floor, midpoint
        upper_range_floor, upper_range_ceiling = midpoint+1, ceiling

        # Count number of items in lower range
        items_in_lower_range = 0
        for item in numbers:
            # Is it in the lower range?
            if item >= lower_range_floor and item <= lower_range_ceiling:
                items_in_lower_range += 1

        distinct_possible_integers_in_lower_range = (
            lower_range_ceiling
            - lower_range_floor
            + 1
        )
        if items_in_lower_range > distinct_possible_integers_in_lower_range:
            # There must be a duplicate in the lower range
            # so use the same approach iteratively on that range
            floor, ceiling = lower_range_floor, lower_range_ceiling
        else:
            # There must be a duplicate in the upper range
            # so use the same approach iteratively on that range
            floor, ceiling = upper_range_floor, upper_range_ceiling

    # Floor and ceiling have converged
    # We found a number that repeats!
    return floor




"""
def find_repeat(numbers):

    # Find a number that appears more than once
    i = 0
    while i < len(numbers):
        j = numbers[i] - 1
        if numbers[i] != numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
        else:
            if j != i:
                return numbers[i]
            i += 1
            
    return -1

"""
















# Tests

class Test(unittest.TestCase):

    """
    def test_just_the_repeated_number(self):
        actual = find_repeat([1, 1])
        expected = 1
        self.assertEqual(actual, expected)
    """
    def test_short_list(self):
        actual = find_repeat([1, 2, 3, 2])
        expected = 2
        self.assertEqual(actual, expected)
    """
    def test_medium_list(self):
        actual = find_repeat([1, 2, 5, 5, 5, 5])
        expected = 5
        self.assertEqual(actual, expected)
    
    def test_long_list(self):
        actual = find_repeat([4, 1, 4, 8, 3, 2, 7, 6, 5])
        expected = 4
        self.assertEqual(actual, expected)
    """

unittest.main(verbosity=2)