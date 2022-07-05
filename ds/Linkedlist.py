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

    def get(self,index):
        temp = self.head
        if self.length == 0:
            return self.head.value
        elif index < 0 or index >= self.length :
            return None
        elif temp.next == None:
            return self.tail.value
        else:
          for i in range(index):
              temp = temp.next
          return temp

    def set_value(self, index, value):

        if index < 0 or index >= self.length:
            return None
        else:
            temp = self.get(index)
            temp.value = value
            return True
        return False

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

    def prepend_pop(self):
        if self.length == 0:
            return None
        else:
          temp = self.head
          new = temp.next
          self.head = new
          self.length -= 1
          return temp.value

    def prepend_add(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
          temp = self.head
          new_node.next = temp
          self.head = new_node
          self.length += 1

    def insert_at_point(self,index,value):
        if index < 0 or index >= self.length:
            return True
        if index == 0:
            return self.prepend_add(value)
        elif index == self.length:
            return self.append_new_node(value)
        else:
            new_node = Node(value)
            temp = self.get(index-1)
            next_value = self.get(index)
            temp.next = new_node
            new_node.next = next_value
            self.length += 1
            return False

    def delete_at_point(self,index):
        if index < 0 or index > self.length:
            return False
        elif index == 0:
            self.prepend_pop()
        elif index == self.length:
            self.pop()
        else:
            new_node = self.get(index-1)
            next_value = self.get(index)
            new_node.next = next_value.next
            self.length -= 1


my_linked_list = Linkedlist(15)
my_linked_list.append_new_node(5)
my_linked_list.append_new_node(6)
my_linked_list.print_list()
print('-----------')
my_linked_list.insert_at_point(1,44)
my_linked_list.print_list()
print('--------')
my_linked_list.delete_at_point(1)
my_linked_list.print_list()


#print(my_linked_list.pop())
# print(my_linked_list.prepend_pop())
# print(my_linked_list.prepend_pop())
# print(my_linked_list.prepend_pop())
#my_linked_list.prepend_add(10)
#my_linked_list.print_list()
#print(my_linked_list.get(2))
#my_linked_list.set_value(0,20)
#my_linked_list.print_list()
#print(my_linked_list.tail.value)
