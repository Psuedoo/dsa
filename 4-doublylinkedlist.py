class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + " --> " if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def get_length(self):
        length = 0

        itr = self.head

        while itr:
            length += 1
            itr = itr.next

        return length

    def insert_at_beginning(self, data):
        if self.head is None:
            node = Node(data, None, None)
            self.head = node
            self.tail = node
            return

        itr = self.head

        while itr:
            if not itr.prev:
                node = Node(data, itr, None)
                itr.prev = node
                self.head = itr.prev
                return

            itr = itr.prev

    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data, None, None)
            self.head = node
            self.tail = node
            return

        itr = self.head

        while itr:
            if not itr.next:
                node = Node(data, None, itr)
                itr.next = node
                self.tail = node
                break

            itr = itr.next

    def insert_at(self, index, data):
        count = 0

        itr = self.head

        while itr:
            count += 1
            if count == index:
                node = Node(data, itr.next, itr)
                itr.next = node
                break

            itr = itr.next

    def remove_at(self, index):
        count = 0

        itr = self.head

        while itr:
            count += 1

            if count == index:
                if not itr.next.next:
                    return
                itr.next = itr.next.next

            itr = itr.next

    def insert_values(self, data_list):
        for value in data_list:
            self.insert_at_end(value)

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head

        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next, itr)
                itr.next = node
                break
            itr = itr.next

    def remove_by_value(self, data):
        pass

    def print_forward(self):
        self.print()

    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.tail

        llstr = ""
        while itr:
            llstr += str(itr.data) + " --> " if itr.prev else str(itr.data)
            itr = itr.prev
        print(llstr)


if __name__ == "__main__":
    dll = DoubleLinkedList()
    dll.insert_at_end(10)
    dll.print()
    dll.insert_values(["banana", "mango", "grapes", "orange"])
    dll.insert_at_beginning("pineapple")
    dll.print()
    dll.insert_at(1, "blueberry")
    dll.print()
    dll.remove_at(2)
    dll.print()
    dll.insert_after_value("banana", "watermelon")
    print("forwards")
    dll.print()
    print("backwards")
    dll.print_backward()

    # dll.insert_values([45, 7, 12, 567, 99])
    # dll.insert_at_end(67)
    # dll.print()
