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

    def add_new_node_at_the_end(self, node):
        if self.head is None:
            self.head = node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = node

    def print_linked_list(self):
        current_node = self.head
        output_str = ""
        while current_node is not None:
            output_str += str(current_node.data) + "->"
            current_node = current_node.next
        print(output_str[0:len(output_str)-2])

    def reverse_linked_list_iteratively(self, node):
        previous_node = None
        current_node = node
        next_node = current_node.next

        while current_node is not None:
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
            if next_node is not None:
                next_node = next_node.next

    def reverse_linked_list_recursively(self, node):
        if node.next is None:
            self.head = node
            return
        self.reverse_linked_list_recursively(node.next)
        temp_node = node.next
        temp_node.next = node
        node.next = None


linked_list_1 = LinkedList()
node_0 = Node(4)
node_1 = Node(3)
node_2 = Node(2)
node_3 = Node(1)
node_4 = Node(0)
linked_list_1.add_new_node_at_the_end(node_0)
linked_list_1.add_new_node_at_the_end(node_1)
linked_list_1.add_new_node_at_the_end(node_2)
linked_list_1.add_new_node_at_the_end(node_3)
linked_list_1.add_new_node_at_the_end(node_4)

print("Initial linked list 1: ")
linked_list_1.print_linked_list()
linked_list_1.reverse_linked_list_iteratively(node_0)
linked_list_1.head = node_4
print("After reversal linked list 1: ")
linked_list_1.print_linked_list()

linked_list_2 = LinkedList()
node_0 = Node("A")
node_1 = Node("B")
node_2 = Node("C")
node_3 = Node("D")
node_4 = Node("E")
linked_list_2.add_new_node_at_the_end(node_0)
linked_list_2.add_new_node_at_the_end(node_1)
linked_list_2.add_new_node_at_the_end(node_2)
linked_list_2.add_new_node_at_the_end(node_3)
linked_list_2.add_new_node_at_the_end(node_4)

print("Initial linked list 2: ")
linked_list_2.print_linked_list()

linked_list_2.reverse_linked_list_recursively(node_0)
linked_list_2.head = node_4
print("After reversal linked list 2: ")
linked_list_2.print_linked_list()
