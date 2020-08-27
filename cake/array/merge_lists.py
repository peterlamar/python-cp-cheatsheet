import unittest
"""
time: 5 min

errors: two typos
else
alices_list[m]


"""

def merge_lists(my_list, alices_list):
    # Combine the sorted lists into one large sorted list
    merged = []
    m = a = 0
    
    while m < len(my_list) and a < len(alices_list):
        if my_list[m] <= alices_list[a]:
            merged.append(my_list[m])
            m += 1
        else:
            merged.append(alices_list[a])
            a += 1
       
    while m < len(my_list):
        merged.append(my_list[m])
        m += 1
    
    while a < len(alices_list):
        merged.append(alices_list[a])
        a += 1  

    return merged




def merge_lists2(my_list, alices_list):
    return sorted(my_list + alices_list)













# Tests

class Test(unittest.TestCase):

    def test_both_lists_are_empty(self):
        actual = merge_lists([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_first_list_is_empty(self):
        actual = merge_lists([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_second_list_is_empty(self):
        actual = merge_lists([5, 6, 7], [])
        expected = [5, 6, 7]
        self.assertEqual(actual, expected)

    def test_both_lists_have_some_numbers(self):
        actual = merge_lists([2, 4, 6], [1, 3, 7])
        expected = [1, 2, 3, 4, 6, 7]
        self.assertEqual(actual, expected)

    def test_lists_are_different_lengths(self):
        actual = merge_lists([2, 4, 6, 8], [1, 7])
        expected = [1, 2, 4, 6, 7, 8]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)