from typing import Any, Optional

class Node:
    def __init__(self, value: Any, /)->None:
        self.value: Any = value
        self.next: Optional['Node'] = None

class CircularLinkedList:
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None  # ← tail
        self.size: int = 0

    # append method
    def append(self, value: Any, /)->None:
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
            self.tail.next = self.head
            self.size += 1
            return
        new_node.next = self.head
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1
    # prepend method - O(1)
    def prepend(self, value: Any, /)->None:
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
            self.tail.next = self.head
            self.size += 1
            return
        new_node.next = self.head
        self.head = new_node
        self.tail.next = self.head
        self.size += 1
    # insert method - O(n)
    def insert(self, value: Any, index: int)->None:
        if self.size < index or index<0:
            raise IndexError("Index error!")
        if index==0:
            self.prepend(value)
            return
        new_node = Node(value)
        last = self.head
        for _ in range(index-1):
            last = last.next
        new_node.next = last.next
        last.next = new_node
        self.size+=1
    
    def left_pop(self):
        if self.head is None:
            return None
        delete_value = self.head.value
        if self.head == self.tail:      # ← 1 ta element
            self.head = self.tail = None
            self.size -= 1
            return delete_value
        
        self.head = self.head.next
        self.tail.next = self.head
        self.size -= 1
        return delete_value
    
    # pop method - O(n)
    def pop(self):
        if self.head is None:
            return None
        if self.head == self.tail:
            delete_value = self.head.value
            self.head = self.tail = None
            self.size -= 1
            return delete_value
        last = self.head
        while last.next.next:
            last = last.next
        delete_value = last.next.value
        self.tail = last
        self.tail.next = self.head
        self.size -= 1
        return delete_value
    
    # delete value method - O(n)
    def delete(self, value: Any)->None:
        if self.head is None:
            return None
        if self.head.value==value:
            return self.left_pop()
        last = self.head
        while last.next != self.head:
            if last.next.value==value:
                delete_value = last.next.value
                last.next = last.next.next
                return delete_value
            last = last.next
        return None