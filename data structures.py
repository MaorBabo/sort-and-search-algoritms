"""
This file implements basic data structures algorithms and its purpose
is to use as a tool for other projects.
"""


class LNode:

    def __init__(self, data=None, nextNode=None):
        self.next = nextNode
        self.data = data

    def __repr__(self):
        """
        This method responsible on how the object appear on the screen.
        :return: the data in the Node.
        """

        return repr(self.data)

    def next(self, node):
        self.next = node

    def set(self, data):
        self.data = data


class LinkedList:

    def __init__(self, head=None):
        self.__head = head

    def __repr__(self):
        """
        This method responsible on how the object appear on the screen.
        :return: the data in the linked list.

        complexity:

        run time complexity = O(1)
        """

        if self.__head is None:
            return '[]'

        s = '['
        current = self.__head

        while current:
            s += repr(current) + ', '
            current = current.next

        return s[:-2] + ']'

    def __len__(self):
        """
        This method counting the length of the linked list.
        :return: int number.

        complexity:

        n = len(linked list)
        run time complexity = O(n)
        """
        counter = 0
        current = self.__head

        while current:
            counter += 1
            current = current.next

        return counter

    def __getitem__(self, index):
        """
        This method gets an index and returns the value in that index.
        :param index: int number.
        :return: the value in the place index.

        Complexity:

        n = index
        run time complexity = O(n)
        """

        # Checks if the given index is valid.
        if index < 0 or index > len(self) - 1:
            raise IndexError("List index out of range!")

        current = self.__head

        for _ in range(0, index):
            current = current.next

        return current.data

    def addFirst(self, value):
        """
        This method add node to the start of the linked list.
        :param value: the value the user want to add (can be from any type).
        :return: None

        run time complexity = O(1)
        """

        # Creating LNode object to store the value.
        node = LNode(value)

        node.next = self.__head
        self.__head = node

    def sum(self):
        """
        This method calculates the sum of the data in the linked list.
        :return: Optional(str, int, float).

        complexity:

        n = len(linked list)
        run time complexity = O(n)
        """
        if self.__head is None:
            return 0

        current = self.__head
        total = current.data

        while current.next:
            total += current.next.data
            current = current.next

        return total

    def find(self, value):
        """
        This method find the value in the linked list
        and return the Node that contain this value.
            :param value: Some value.
        :return: Node if the value was found else None.

        Complexity:

        n = len(linked list)
        run time complexity = O(n)
        """

        current = self.__head
        while current:
            if current.data == value:
                return current
            current = current.next

        # In case that there is no such value in the linked list.
        return None


l1 = LinkedList()
l1.addFirst('1')
l1.addFirst('2')
l1.addFirst('3')
l1.addFirst('4')
print(l1)
print(len(l1))
print(l1.sum())
n = l1.find('2')
print(n.next)

print(l1[1])
print(type(l1[1]))
