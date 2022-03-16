import unittest
import copy

from src.problems import ArrayProblems


class ArrayProblemsTests(unittest.TestCase):

    def test_is_unique(self):
        sol_1 = ArrayProblems._is_unique_hash_table
        sol_2 = ArrayProblems._is_unique_no_data_structure

        self.assertTrue(ArrayProblems.is_unique("qwerty", sol_1))
        self.assertTrue(ArrayProblems.is_unique("qwerty", sol_2))

        self.assertTrue(ArrayProblems.is_unique("", sol_1))
        self.assertTrue(ArrayProblems.is_unique("", sol_2))

        self.assertFalse(ArrayProblems.is_unique("similar", sol_1))
        self.assertFalse(ArrayProblems.is_unique("similar", sol_2))

    def test_check_permutations(self):
        sol_1 = ArrayProblems._check_permutation_hash_table
        sol_2 = ArrayProblems._check_permutation_sorting

        self.assertTrue(ArrayProblems.check_permutation("qwerty", "ytrewq", sol_1))
        self.assertTrue(ArrayProblems.check_permutation("qwerty", "ytrewq", sol_2))

        self.assertFalse(ArrayProblems.check_permutation("qwerty", "ytewq", sol_1))
        self.assertFalse(ArrayProblems.check_permutation("qwerty", "ytewq", sol_2))

        self.assertFalse(ArrayProblems.check_permutation("qwerty", "asdfgh", sol_1))
        self.assertFalse(ArrayProblems.check_permutation("qwerty", "asdfgh", sol_2))

    def test_urlify(self):
        sol_1 = ArrayProblems._urlify

        self.assertEqual(ArrayProblems.urilify("Mr John Smith   ", sol_1), "Mr%20John%20Smith")
        self.assertEqual(ArrayProblems.urilify("  ", sol_1), "")
        self.assertEqual(ArrayProblems.urilify("", sol_1), "")

    def test_is_palindrone_permutation(self):
        sol_1 = ArrayProblems._is_palindrome_permutation

        self.assertTrue(ArrayProblems.is_palindrome_permutation("", sol_1))
        self.assertTrue(ArrayProblems.is_palindrome_permutation("a", sol_1))
        self.assertTrue(ArrayProblems.is_palindrome_permutation("abab", sol_1))
        self.assertTrue(ArrayProblems.is_palindrome_permutation("abcab", sol_1))
        self.assertFalse(ArrayProblems.is_palindrome_permutation("abcdab", sol_1))
        self.assertFalse(ArrayProblems.is_palindrome_permutation("abcdadeb", sol_1))

    def test_one_away(self):
        sol_1 = ArrayProblems._one_away

        self.assertTrue(ArrayProblems.one_away("pale", "ale", sol_1))
        self.assertTrue(ArrayProblems.one_away("pales", "pales", sol_1))
        self.assertTrue(ArrayProblems.one_away("pale", "bale", sol_1))
        self.assertFalse(ArrayProblems.one_away("pale", "bake", sol_1))

    def test_string_compress(self):
        sol_1 = ArrayProblems._string_compress

        self.assertEqual(ArrayProblems.string_compress("", sol_1), "")
        self.assertEqual(ArrayProblems.string_compress("a", sol_1), "a1")
        self.assertEqual(ArrayProblems.string_compress("aabccccaaa", sol_1), "a2b1c4a3")

    def test_rotate_matrix(self):
        sol_1 = ArrayProblems._rotate_matrix_not_inplace

        input_1 = [
            [1, 2],
            [4, 3]
        ]

        expected_output_1 = [
            [4, 1],
            [3, 2]
        ]

        input_2 = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]

        expected_output_2 = [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3],
        ]

        self.assertEqual(ArrayProblems.rotate_matrix(copy.deepcopy(input_1), sol_1,),
                         expected_output_1)
        self.assertEqual(ArrayProblems.rotate_matrix(copy.deepcopy(input_2), sol_1,),
                         expected_output_2)


if "__main__" == __name__:
    unittest.main()
