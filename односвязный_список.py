class Node():
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class Iterator():
    def __init__(self, head, length):
        self.node = head
        self.index = 0
        self.length = length

    def __iter__(self):
        return self
    
    def __next__(self):
        while self.index!= self.length:
            result = self.node.value
            self.index += 1
            self.node = self.node.next
            return result
        

class LinkedList():
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def add_back(self, value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.length +=1

    def add_end(self, value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.length += 1

    def remove_value(self, value):
        if self.length > 0:
            node = self.head
            node_last = None
            while node.next != None:
                    if node.value == value:
                        if node_last != None:
                            node_last.next = node.next
                        else:
                            self.head = node.next
                        self.length-=1
                    else:
                        node_last = node
                        node = node.next
            if node.value == value:
                self.tail = node_last
                self.length -= 1


    def remove_dublicate(self):
        new_list = set()
        new_list.add(self.head.value)
        node = self.head.next.value
        node_last = self.head

        while node.next != None:
            if node.value not in new_list:
                new_list.add(node.value)
                node = node.next

            else:
                node_last.next = node.next
                self.length -= 1

    def __iter__(self):
        return Iterator(self.head)
    
    def sort(self):
        node = self.head

    
def merge(linked_list_1, linked_list_2):
    index = 0
    list_3 = LinkedList()
    node_1 = linked_list_1.head
    node_2 = linked_list_2.head
    while index != linked_list_1.length+linked_list_2.length:
        if node_1.value> node_2.value:
            list_3.add_end(node_1.value)
            node_1 = node_1.next
        else:
            list_3.add_end(node_2.value)
            node_2 = node_2.next
            
        
        index += 1
    return list_3


def compression(linked_list):
        
        
        linked_list.remove_dublicate()
