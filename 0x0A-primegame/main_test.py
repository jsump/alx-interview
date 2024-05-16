import unittest
isWinner = __import__('0-prime_game').isWinner

class TestPrimeGame(unittest.TestCase):
    def test_single_round_maria_wins(self):
        self.assertEqual(isWinner(1, [2]), "Maria")

    def test_single_round_ben_wins(self):
        self.assertEqual(isWinner(1, [4]), "Ben")

    def test_multiple_rounds_maria_wins(self):
        self.assertEqual(isWinner(3, [2, 3, 5]), "Maria")

    def test_multiple_rounds_ben_wins(self):
        self.assertEqual(isWinner(3, [4, 6, 8]), "Ben")

    def test_tie(self):
        self.assertEqual(isWinner(2, [4, 5]), "Ben")

    def test_empty_nums(self):
        self.assertEqual(isWinner(1, []), None)

    def test_large_numbers_maria_wins(self):
        self.assertEqual(isWinner(1, [9999]), "Maria")

    def test_large_numbers_ben_wins(self):
        self.assertEqual(isWinner(1, [10000]), "Ben")

if __name__ == "__main__":
    unittest.main()