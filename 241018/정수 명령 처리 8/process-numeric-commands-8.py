class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.node_num = 0

    def push_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head

        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            self.head = new_node
            
        new_node.prev = None
        self.node_num += 1


    def push_back(self, new_data):
        new_node = Node(new_data)
        new_node.prev = self.tail

        if self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        new_node.next = None
        self.node_num += 1

    def pop_front(self):
        if self.head == None:
            return print("List is empty")
    
        elif self.head.next == None:
            pop_node = self.head
            self.head = None
            self.tail = None
            self.node_num = 0

            print(pop_node.data)

        else:
            pop_node = self.head
            pop_node.next.prev = None
            self.head = pop_node.next
            pop_node.next = None
            self.node_num -= 1

            print(pop_node.data)

    def pop_back(self):
        if self.tail == None:
            return print("List is empty")
    
        elif self.tail.prev == None:
            pop_node = self.tail
            self.head = None
            self.tail = None
            self.node_num = 0

            print(pop_node.data)

        else:
            pop_node = self.tail
            pop_node.prev.next = None
            self.tail = pop_node.prev
            pop_node.prev = None
            self.node_num -= 1

            print(pop_node.data)

    def size(self):
        print(self.node_num)
        return self.node_num

    def empty(self):
        if self.node_num == 0:
            print(1)
        else:
            print(0)

    def front(self):
        if self.head == None:
            print("List is empty")
        else:
            print(self.head.data)

    def back(self):
        if self.tail == None:
            print("List is empty")
        else:
            print(self.tail.data)

n = int(input())
dll = DoublyLinkedList()
for i in range(n):
    s = input()
    if s == 'pop_front':
        dll.pop_front()
    elif s == 'pop_back':
        dll.pop_back()
    elif s == 'size':
        dll.size()
    elif s == 'empty':
        dll.empty()
    elif s == 'front':
        dll.front()
    elif s == 'back':
        dll.back()
    else:
        s, num = s.split()
        if s == 'push_front':
            dll.push_front(int(num))
        else:
            dll.push_back(int(num))

    # print(f'size : {dll.size()}')