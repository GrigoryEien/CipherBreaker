import unittest
from random import shuffle

from Modules.textsAnalyzer import TextsAnalyzer


class TextsAnalyzerTest(unittest.TestCase):
    def test_register_top_100(self):
        analyzer = TextsAnalyzer("stub")
        for word in self.generate_words(1, 201):
            analyzer.register_100_longest(word)
        actual = analyzer.temp_longest
        expected = self.generate_words(101, 201)
        self.assertEqual(len(actual), 100)
        self.assertSetEqual(set(actual), set(expected))
    
    def test_contains_letter_for_four_times(self):
        self.assertTrue(TextsAnalyzer.has_frequent_letter("degenerate"))
        self.assertFalse(TextsAnalyzer.has_frequent_letter("revenge"))
    
    def test_register_ngrams(self):
        analyzer = TextsAnalyzer("stub")
        analyzer.register_ngrams("python")
        self.assertEqual(analyzer.letters,
                         {'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1})
        self.assertEqual(analyzer.bigrams,
                         {'py': 1, 'yt': 1, 'th': 1, 'ho': 1, 'on': 1})
        self.assertEqual(analyzer.trigrams,
                         {'pyt': 1, 'yth': 1, 'tho': 1, 'hon': 1})
    
    def test_register_one_letter_word(self):
        analyzer = TextsAnalyzer("stub")
        analyzer.register_word('i')
        self.assertTrue('i' in analyzer.letters)
    
    def test_register_two_letter_word(self):
        analyzer = TextsAnalyzer("stub", )
        analyzer.register_word('if')
        self.assertTrue('if' in analyzer.two_letter_words)
    
    def test_register_word_with_four_occurrences_of_same_letter(self):
        analyzer = TextsAnalyzer("stub", )
        analyzer.register_word('degenerate')
        self.assertTrue(
            'degenerate' in analyzer.with_frequent_letter)
    
    @staticmethod
    def generate_words(shortest, longest):
        words = []
        for i in range(longest, shortest, -1):
            words.append('a' * i)
        shuffle(words)
        return words
