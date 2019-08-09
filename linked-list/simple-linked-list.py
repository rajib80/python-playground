class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_new_node_at_the_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_new_node_at_the_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def print_linked_list(self):
        current_node = self.head
        output_str = ""
        while current_node is not None:
            # print(current_node.data)
            output_str += str(current_node.data)
            current_node = current_node.next
        print(output_str)


def add_two_linked_lists(input_linked_list_1, input_linked_list_2):

    result_linked_list = LinkedList()
    carry = 0

    current_node_list_1 = input_linked_list_1.head
    current_node_list_2 = input_linked_list_2.head

    while current_node_list_1 is not None or current_node_list_2 is not None:
        if current_node_list_1 is not None:
            data_list_1 = current_node_list_1.data
        else:
            data_list_1 = 0

        if current_node_list_2 is not None:
            data_list_2 = current_node_list_2.data
        else:
            data_list_2 = 0

        added_data = carry + data_list_1 + data_list_2

        if added_data >= 10:
            carry = 1
        else:
            carry = 0

        if added_data < 10:
            added_data = added_data
        else:
            added_data = added_data % 10

        result_linked_list.add_new_node_at_the_beginning(added_data)

        current_node_list_1 = current_node_list_1.next
        current_node_list_2 = current_node_list_2.next

    result_linked_list.print_linked_list()


linked_list_1 = LinkedList()
linked_list_1.add_new_node_at_the_beginning(2)
linked_list_1.add_new_node_at_the_end(4)
linked_list_1.add_new_node_at_the_end(3)

linked_list_2 = LinkedList()
linked_list_2.add_new_node_at_the_beginning(5)
linked_list_2.add_new_node_at_the_end(6)
linked_list_2.add_new_node_at_the_end(4)

add_two_linked_lists(linked_list_1, linked_list_2)
