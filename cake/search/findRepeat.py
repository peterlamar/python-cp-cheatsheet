import unittest

def find_repeat(numbers):

    # Find a number that appears more than once
    l, r = 1, len(numbers) - 1
    
    while l < r:
        mid = l + (r-l)//2
        
        count = 0
        for n in numbers:
            if l <= n <= mid:
                count += 1
        
        dist = mid - l + 1
        
        if count > dist:
            r = mid
        else:
            l = mid + 1

    return l







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

    def test_just_the_repeated_number(self):
        actual = find_repeat([1, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_short_list(self):
        actual = find_repeat([1, 2, 3, 2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_repeat([1, 2, 5, 5, 5, 5])
        expected = 5
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_repeat([4, 1, 4, 8, 3, 2, 7, 6, 5])
        expected = 4
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)