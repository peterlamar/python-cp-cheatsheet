import unittest

"""
time: 5 min
errors: peeked at algo and got set idea
"""

def has_palindrome_permutation(the_string):

    # Check if any permutation of the input is a palindrome
    st = set()
    
    if len(the_string) <= 1:
        return True
    
    for c in the_string:
        if c in st:
            st.remove(c)
        else:
            st.add(c)
    
    if len(the_string) % 2 == 1:
        if len(st) == 1: return True
    else:
        if len(st) == 0: return True

    return False


















# Tests

class Test(unittest.TestCase):

    def test_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcbcd')
        self.assertTrue(result)

    def test_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabccbdd')
        self.assertTrue(result)

    def test_no_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcd')
        self.assertFalse(result)

    def test_no_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabbcd')
        self.assertFalse(result)

    def test_empty_string(self):
        result = has_palindrome_permutation('')
        self.assertTrue(result)

    def test_one_character_string(self):
        result = has_palindrome_permutation('a')
        self.assertTrue(result)


unittest.main(verbosity=2)