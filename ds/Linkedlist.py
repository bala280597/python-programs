class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Linkedlist:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append_new_node(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        previous = self.head
        while temp.next is not None:
            previous = temp
            temp = temp.next
        self.tail = previous
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value



my_linked_list = Linkedlist(4)
my_linked_list.append_new_node(5)
my_linked_list.append_new_node(6)
print(my_linked_list.pop())
my_linked_list.print_list()

#print(my_linked_list.tail.value)
