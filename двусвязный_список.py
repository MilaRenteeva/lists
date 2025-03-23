class Node():
    def __init__(self,value):
        self.next = None
        self.previous = None
        self.value = value

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

class DoubleLinkedList():
    def __init__(self, cycle=False):
        self.head = None
        self.tail = None
        self.length = 0
        self.cycle = cycle

    def conclusion(self):
        index = 0
        node = self.head
        while index != self.length:
            print(node.value, end = " ")
            print("<->", end = " ")
            index += 1
            node = node.next

    def add_back(self, value):
        new_node = Node(value)
        if self.head != None:
            new_node.next = self.head
            self.head.previous = new_node
        else:
            self.tail = new_node
        self.head = new_node
        self.length += 1

    def add_end(self, value):
        new_node = Node(value)
        if self.tail != None:
            new_node.previous = self.tail
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node
        self.length += 1
    
    def add(self, value, index):
        new_node = Node(value)
        i = 0
        node = self.head
        while i != index + 1:  
            if i == index:
                if index == 0:
                    self.add_back(value)
                elif index == self.length:
                    self.add_end(value)
                else:
                    new_node.previous = node
                    new_node.next = node.next
                    node.next = new_node
                    new_node.next.previous = new_node
            i += 1
            node = node.next
    
    def remove_back(self):
        self.head.next.previous = None
        self.head = self.head.next
    
    def remove_end(self):
        self.tail.previous.next = None
        self.tail = self.tail.previous

    def remove(self,index):
        i = 0
        node = self.head
        while i != index+1:
            if i == index:
                if i == 0:
                    self.remove_back()
                elif i == self.length:
                    self.remove_end()
                else:
                    node.previous.next = node.next
                    node.next.previous = node.previous
            i += 1
            node = node.next



    def remove_value(self, value):
        if self.length > 0:
            node = self.head
            while node.next != None:
                    if node.value == value:
                        if node.previous != None:
                            node.previous.next = node.next
                            node.next.previous = node.previous
                        else:
                            self.head = node.next
                            node.next.previous = None
                        self.length-=1
                    node = node.next
            if node.value == value:
                self.tail = node.previous  
                node.previous.next = None
                self.length -= 1
    
    def __iter__(self):
        return Iterator(self.head)

    def index(self, index):
        node = self.head  
        if index > self.length or index < 0:
            print("нет элемента с таким индексом")
        else:
            for i in range(self.length):  
                if i == index:
                    return node.value
                    break
                node = node.next
    
    def revers(self):
        new_DoubleLinkedList = DoubleLinkedList(self.cycle)
        node = self.tail.previous
        new_DoubleLinkedList.head = self.tail
        lenght = self.length
        for i in range(lenght-1):
            new_DoubleLinkedList.add_end(node)
            if node.previous == None:
                new_DoubleLinkedList.tail = node
            node = node.previous  
        return new_DoubleLinkedList


new_list = DoubleLinkedList()
new_list.add_end(1) 
new_list.add_end(2)
new_list.add_end(3)
       


