import unittest


"""
Condition 
"""
def find_rotation_point(words):
    # Find the rotation point in the list
    if len(words) <= 1:
        return

    left, right = 0, len(words) - 1
    while left < right:
        mid = left + (right - left) // 2
        if words[len(words)-1] > words[mid]:
            right = mid
        else:
            left = mid + 1
    return left
    


















# Tests

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = find_rotation_point(['cape', 'cake'])
        expected = 1
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_rotation_point(['grape', 'orange', 'plum',
                                      'radish', 'apple'])
        expected = 4
        self.assertEqual(actual, expected)

    def test_large_list(self):
        actual = find_rotation_point(['ptolemaic', 'retrograde', 'supplant',
                                      'undulate', 'xenoepist', 'asymptote',
                                      'babka', 'banoffee', 'engender',
                                      'karpatka', 'othellolagkage'])
        expected = 5
        self.assertEqual(actual, expected)

    # Are we missing any edge cases?


unittest.main(verbosity=2)