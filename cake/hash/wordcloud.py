import unittest


class WordCloudData(object):

    def __init__(self, input_string):
        
        def splitWords(input_string) -> list:
            words = []
            start = length = 0
            for i, c in enumerate(input_string):
                if c.isalpha():
                    if length == 0:
                        start = i                    
                    length += 1
                else:
                     words.append(input_string[start:start+length])
                     length = 0
            if length > 0:
                words.append(input_string[start:start+length])
            return words
            
        self.words_to_counts = {}

        split = splitWords(input_string)
        
        print(split)

        for word in split:
            if len(word) > 0 and word != "s":
                self.words_to_counts[word] = self.words_to_counts.get(word, 0) + 1
        
        print(self.words_to_counts)
            
        # Count the frequency of each word
    
 


















# Tests

# There are lots of valid solutions for this one. You
# might have to edit some of these tests if you made
# different design decisions in your solution.

class Test(unittest.TestCase):

    def test_simple_sentence(self):
        input = 'I like cake'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'I': 1, 'like': 1, 'cake': 1}
        self.assertEqual(actual, expected)

    def test_longer_sentence(self):
        input = 'Chocolate cake for dinner and pound cake for dessert'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {
            'and': 1,
            'pound': 1,
            'for': 2,
            'dessert': 1,
            'Chocolate': 1,
            'dinner': 1,
            'cake': 2,
        }
        self.assertEqual(actual, expected)

    def test_punctuation(self):
        input = 'Strawberry short cake? Yum!'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'cake': 1, 'Strawberry': 1, 'short': 1, 'Yum': 1}
        self.assertEqual(actual, expected)

    def test_hyphenated_words(self):
        input = 'Dessert - mille-feuille cake'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'cake': 1, 'Dessert': 1, 'mille-feuille': 1}
        self.assertEqual(actual, expected)

    def test_ellipses_between_words(self):
        input = 'Mmm...mmm...decisions...decisions'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'mmm': 2, 'decisions': 2}
        self.assertEqual(actual, expected)

    def test_apostrophes(self):
        input = "Allie's Bakery: Sasha's Cakes"

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {"Bakery": 1, "Cakes": 1, "Allie's": 1, "Sasha's": 1}
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)