import unittest

"""
time: > 20 min
error: did not see that words seperated by one space

"""
def reverse_words(message):
    def reverse(l, r, msg):
        while l < r:
            msg[l], msg[r] = msg[r], msg[l]
            l += 1
            r -= 1
    
    reverse(0, len(message)-1, message)
    
    j = 0
    
    for i in range(len(message) + 1):
        if i == len(message) or message[i] == ' ':
            reverse(j, i-1, message)
            j = i + 1
        











# Tests

class Test(unittest.TestCase):

    def test_one_word(self):
        message = list('vault')
        reverse_words(message)
        expected = list('vault')
        self.assertEqual(message, expected)

    def test_two_words(self):
        message = list('thief cake')
        reverse_words(message)
        expected = list('cake thief')
        self.assertEqual(message, expected)

    def test_three_words(self):
        message = list('one another get')
        reverse_words(message)
        expected = list('get another one')
        self.assertEqual(message, expected)

    def test_multiple_words_same_length(self):
        message = list('rat the ate cat the')
        reverse_words(message)
        expected = list('the cat ate the rat')
        self.assertEqual(message, expected)

    def test_multiple_words_different_lengths(self):
        message = list('yummy is cake bundt chocolate')
        reverse_words(message)
        expected = list('chocolate bundt cake is yummy')
        self.assertEqual(message, expected)

    def test_empty_string(self):
        message = list('')
        reverse_words(message)
        expected = list('')
        self.assertEqual(message, expected)


unittest.main(verbosity=2)