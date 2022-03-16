import unittest
from unittest import mock
import src.data_structures as DataStructures


class MockHashTableElement:
    def __init__(self, id: str, value: int) -> None:
        self.id = id
        self.value = value

    def __eq__(self, other) -> bool:
        return other.id == self.id and other.value == self.value


class LinkedListTests(unittest.TestCase):

    def test_add(self):
        mock_element_one = DataStructures.Node(id="one", data=42)

        linked_list = DataStructures.LinkedList(mock_element_one)
        self.assertIsNone(linked_list.next)

        mock_element_two = DataStructures.Node(id="two", data=84)

        linked_list.add_element(mock_element_two)

        self.assertEqual(linked_list.next.value, mock_element_two)

    def test_find_element(self):
        mock_element_one = DataStructures.Node(id="one", data=42)
        linked_list = DataStructures.LinkedList(mock_element_one)
        mock_element_two = DataStructures.Node(id="two", data=84)
        linked_list.add_element(mock_element_two)

        self.assertIsNone(linked_list.find_element("three"))
        self.assertEqual(linked_list.find_element("two"), mock_element_two)

    def test_delete_element(self):
        mock_element_one = DataStructures.Node(id="one", data=42)
        mock_element_two = DataStructures.Node(id="two", data=84)
        mock_element_three = DataStructures.Node(id="three", data=-42)
        mock_element_four = DataStructures.Node(id="four", data=-84)

        linked_list = DataStructures.LinkedList(mock_element_one)
        linked_list = DataStructures.LinkedList(mock_element_two)
        linked_list = DataStructures.LinkedList(mock_element_three)
        linked_list = DataStructures.LinkedList(mock_element_four)

        linked_list.delete_element("third")

        self.assertIsNone(linked_list.find_element("third"))


class HashTableTests(unittest.TestCase):

    @mock.patch("src.data_structures.hash", side_effect=[0, 1, 0])
    def test_add_element(self, mock_hash):

        hash_table = DataStructures.HashTable(array_size=5)

        hash_table.add_element("one")
        hash_table.add_element("two")
        hash_table.add_element("three")

        self.assertEqual(hash_table.array[2:], [None, None, None])

        self.assertEqual(hash_table.array[0].value, "one")
        self.assertEqual(hash_table.array[0].next.value, "three")
        self.assertIsNone(hash_table.array[0].next.next)

        self.assertEqual(hash_table.array[1].value, "two")
        self.assertIsNone(hash_table.array[1].next)


if "__main__" == __name__:
    unittest.main()
