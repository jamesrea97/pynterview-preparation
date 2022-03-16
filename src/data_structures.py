from typing import Optional
####################################################################################################
"""
Linked List Implementation
"""


class Node:
    def __init__(self, id: str, data: int) -> None:
        self.id = id
        self.data = data

    def __hash__(self) -> int:
        return hash(self.id)

    def __eq__(self, o: "Node") -> bool:
        return o.id == self.id


class LinkedList:
    def __init__(self, value: Node, next=None) -> None:
        self.value = value
        self.next = next

    def add_element(self, value: Node):
        current_node = self
        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = LinkedList(value=value)

    def find_element(self, node_id: str) -> Optional[Node]:
        current_node = self
        while current_node is not None:
            if current_node.value.id == node_id:
                return current_node.value
            current_node = current_node.next

        return None

    def delete_element(self, node_id: str) -> None:
        current_node = self
        previous_node = self
        has_node = False
        while current_node is not None:
            if current_node.value.id == node_id:
                has_node = True
                break
            previous_node = current_node
            current_node = current_node.next

        if has_node:
            if previous_node is not None and current_node is not None:
                previous_node.next = current_node.next


####################################################################################################
"""
HashTable Implementation
"""


class HashTable:

    def __init__(self, array_size: int = 10) -> None:
        self.array = [None] * array_size

    def _get_index(self, hashed_element: int) -> int:
        return hashed_element % len(self.array)

    def _hash_element_id(self, element_id: str) -> int:
        return hash(element_id)

    def _hash_element(self, element: Node) -> int:
        return hash(element)

    def _add_element_at(self, element: Node, index: int):
        if self.array[index] is None:
            self.array[index] = LinkedList(element)
        else:
            self.array[index].add_element(element)

    def _get_element_at(self, element_id: str, index: int) -> Optional[Node]:
        linked_list = self.array[index]

        if linked_list is None:
            return None

        return linked_list.find_element(element_id)

    def add_element(self, element: Node):
        # 1. Hash element
        hashed_element = self._hash_element(element=element)
        # 2. Get index
        index = self._get_index(hashed_element=hashed_element)
        # 3. Add to LinkedList
        self._add_element_at(element=element, index=index)

    def lookup_element(self, element_id: str):
        hashed_element = self._hash_element_id(element_id=element_id)

        index = self._get_index(hashed_element=hashed_element)

        return self._get_element_at(element_id=element_id, index=index)


####################################################################################################
