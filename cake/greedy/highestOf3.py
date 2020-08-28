import unittest
"""
time: 18min+
errors: first pass was ugly algo, used 3char array
Didn't fully test algo with enough test cases resulting in silly errors

"""

def highest_product_of_3(list_of_ints):

    if len(list_of_ints) < 3:
        return

    highest = max(list_of_ints[0], list_of_ints[1])
    lowest = min(list_of_ints[0], list_of_ints[1])
    highestOfTwo = list_of_ints[0] * list_of_ints[1]
    lowestOfTwo = list_of_ints[0] * list_of_ints[1]
    highestOfThree = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]
    
    for i in range(2, len(list_of_ints)):
        current = list_of_ints[i]
        
        highestOfThree = max(highestOfThree, current * highestOfTwo, current * lowestOfTwo)
        highestOfTwo = max(highestOfTwo, highest * current, lowest * current)
        lowestOfTwo = min(lowestOfTwo, highest * current, lowest * current)
        lowest = min(lowest, current)
        highest = max(highest, current)

    return highestOfThree












# Tests

class Test(unittest.TestCase):

    def test_short_list(self):
        actual = highest_product_of_3([1, 2, 3, 4])
        expected = 24
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = highest_product_of_3([6, 1, 3, 5, 7, 8, 2])
        expected = 336
        self.assertEqual(actual, expected)

    def test_list_has_one_negative(self):
        actual = highest_product_of_3([-5, 4, 8, 2, 3])
        expected = 96
        self.assertEqual(actual, expected)

    def test_list_has_two_negatives(self):
        actual = highest_product_of_3([-10, 1, 3, 2, -10])
        expected = 300
        self.assertEqual(actual, expected)

    def test_list_is_all_negatives(self):
        actual = highest_product_of_3([-5, -1, -3, -2])
        expected = -6
        self.assertEqual(actual, expected)



unittest.main(verbosity=2)