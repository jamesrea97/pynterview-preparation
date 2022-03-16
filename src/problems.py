from typing import Callable
import logging
import data_structures as DataStructures

"""
Problems to revist:
ArraysProblems.Problem5

"""


class ArrayProblems:

    # Problem 1: IsUnique
    @staticmethod
    def is_unique(string: str, fn: Callable) -> bool:
        """
        Returns True if string has all unique characters.
        """
        logging.info(f"Starting is_unique with arguments: {string}.")
        return fn(string)

    @staticmethod
    def _is_unique_hash_table(string: str) -> bool:
        # Time Complexity: O(N)
        # Space Complexity: O(N)

        count = {}

        for e in string:
            if count.get(e) is None:
                count[e] = 1
            else:
                return False

        return True

    @staticmethod
    def _is_unique_no_data_structure(string: str) -> bool:
        # Time Complexity: O(Nlog(N))
        # Space Complexity: O(1)

        sorted_string = sorted(string)

        for i in range(len(sorted_string)-1):
            if sorted_string[i] == sorted_string[i-1]:
                return False

        return True

    # Problem 2: Permutation Checker
    @staticmethod
    def check_permutation(string_a: str, string_b: str, fn: Callable) -> bool:
        """
        Returns True if string_a is a permutation of string_b.
        """
        logging.info(f"Starting check_permutation with arguments: {string_a}, {string_b}.")
        return fn(string_a, string_b)

    @staticmethod
    def _check_permutation_sorting(string_a: str, string_b: str) -> bool:
        # Time Complexity: O(Nlog(N))
        # Space Complexity: O(1)

        if len(string_a) != len(string_b):
            return False

        sorted_string_a = sorted(string_a)
        sorted_string_b = sorted(string_b)

        for a, b in zip(sorted_string_a, sorted_string_b):
            if a != b:
                return False
        return True

    @staticmethod
    def _check_permutation_hash_table(string_a: str, string_b: str) -> bool:
        # Time Complexity: O(N)
        # Space Complexity: O(N)
        count_a = {}
        count_b = {}

        for a in string_a:
            if count_a.get(a) is None:
                count_a[a] = 1
            else:
                count_a[a] += 1

        for b in string_b:
            if count_b.get(b) is None:
                count_b[b] = 1
            else:
                count_b[b] += 1

        if set(count_a).difference(set(count_b)):
            return False

        for k, count in count_a.items():
            if count_b[k] != count:
                return False

        return True

    # Problem 3: URLify
    @staticmethod
    def urilify(string: str, fn: Callable) -> str:
        logging.info("Starting urilify with arguments: {string}.")
        return fn(string)

    @staticmethod
    def _urlify(string: str) -> str:
        # Time Complexity: O(N)
        # Space Complexity: O(N) - #TODO this can be improved if element-wise operations
        res = ""
        has_none_space_character = False
        for i in range(len(string)-1, -1, -1):
            if string[i] == " ":
                if has_none_space_character:
                    res = "%20" + res
            else:
                has_none_space_character = True
                res = string[i] + res

        return res

    # Problem 4: Permutation Palindrome Check
    @staticmethod
    def is_palindrome_permutation(string: str, fn: Callable) -> bool:
        """
        Returns True if string is a permutation of a palindrome.
        """
        logging.info(f"Starting is_palindrome_permutation with arguments: {string}.")
        return fn(string)

    @staticmethod
    def _is_palindrome_permutation(string: str) -> bool:
        # Time Complexity: O(N)
        # Space Complexity: O(N)
        counts = {}

        for e in string:
            if counts.get(e):
                counts[e] += 1
            else:
                counts[e] = 1

        count_ones = 0

        for values in counts.values():
            if values == 1:
                count_ones += 1
            elif values % 2 != 0:
                return False

        count_ones != 1
        if len(string) % 2 != 0:
            if count_ones != 1:
                return False
            return True

        if len(string) % 2 == 0:
            if count_ones == 0:
                return True
            return False

    # Problem 5: One Away
    @staticmethod
    def one_away(string_a: str, string_b: str, fn: Callable) -> bool:
        """
        Returns True if string_a is at most one of the following operations away from string_b:
        - Delete character
        - Add character
        - Swap character
        """
        logging.info(f"Starting one_away with arguments: {string_a}, {string_b}.")
        return fn(string_a, string_b)

    @staticmethod
    def _one_away(string_a: str, string_b: str) -> bool:
        # Time Complexity: O(N)
        # Space Complexity: O(1)

        operations = 0

        smallest = min(string_a, string_b)
        largest = max(string_a, string_b)
        size_difference = len(largest) - len(smallest)

        # helper
        def _add_character(string, character, index):
            return string[:index] + character + string[index:]

        def _swap_character(string, new_character, index):
            if index < len(string) - 1:
                return string[:index] + new_character + string[index+1:]
            else:
                return string[:index] + new_character

        # hedge case - empty smallest
        if not smallest:
            return size_difference

        i = 0
        while i < len(largest):
            if smallest[i] != largest[i]:
                # add element
                if size_difference:
                    size_difference -= 1
                    smallest = _add_character(smallest, largest[i], i)
                    operations += 1
                # swap
                else:
                    operations += 1
                    smallest = _swap_character(smallest, largest[i], i)

            i += 1

        return True if operations < 2 else False

    # Problem 6: String Compression
    @staticmethod
    def string_compress(string: str, fn: Callable) -> str:
        """
        Returns a compressed string - e.g. `abbaa` -> 'a2b2a'
        """
        logging.info(f"Starting string_compress with arguments: {string}.")
        return fn(string)

    @staticmethod
    def _string_compress(string: str) -> str:
        # Time Complexity: O(N)
        # Space Complexity: O(1)
        res = ""

        i = 0

        while i < len(string):
            j = i
            current_character = string[j]
            count = 0
            while j < len(string) and string[j] == current_character:
                if string[j] == current_character:
                    count += 1
                j += 1

            res += f"{current_character}{count}"
            i = j

        return res

    @staticmethod
    def rotate_matrix(matrix: list[list[int]], fn: Callable) -> None:
        """
        Rotates a 2-D NxN matrix 90 clockwise.
        Input:
        [
            [1,2],
            [4,3]
        ]
        Output:
        [
            [4,1],
            [3,2]
        ]
        """
        logging.info(f"Starting rotate_matrix with arguments: {matrix}.")
        return fn(matrix)

    def _rotate_matrix_not_inplace(matrix: list[list[int]]) -> list[list[int]]:
        # Time Complexity: O(N*N)
        # Space Complexity: O(N*N)

        matrix_side_length = len(matrix)
        res = [[0 for _ in range(matrix_side_length)] for _ in range(matrix_side_length)]

        for i in range(matrix_side_length):
            for j in range(matrix_side_length):
                res[i][j] = matrix[matrix_side_length-1-j][i]

        return res

    # TODO complete faster matrix_rotate
    # TODO complete zero_matrix and string_rotation

    def zero_matrix(matrix: list[list[int]], fn: Callable) -> list[list[int]]:
        """
        If an element in an MxN matrix is 0, its entire row and column are set to 0
        """

    def string_rotation(sl: str, s2: str, fn: Callable) -> list[list[int]]:
        """
        Assume you have a method isSubstringwhich checks if one word is a substring
        of another. Given two strings, sl and s2, write code to check if s2 is a rotation of 
        sl using only one call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat").
        """


class LinkListProblems:

    def remove_duplicates(linked_list: DataStructures.LinkedList, fn: Callable) -> None:
        pass
    