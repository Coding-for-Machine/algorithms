from typing import Any, Optional

"""
Queue(navbot) - methods
    Enqueue() - O(1)
    Dequeue() - O(1)
    Size() - O(1)
    Peek() - O(1)

Enqueue -> [linked tail ] -> [data, ]
"""
class Node:
    def __init__(self, value: Any, /) -> None:
        self.value: Any = value
        self.next: Optional['Node'] = None

class Qeueu:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.size: int = 0

    # dequeue methid - O(1)
    def enqueue(self, value: Any)->None:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return
        self.tail.next = new_node # type: ignore
        self.tail = new_node
        self.size += 1
        

    # dequeue method - O(1)
    def dequeue(self)->Any:
        if self.head is None or self.tail is None:
            return None
        node = self.head
        self.head = self.head.next
        return node
    
    # size method - O(1)
    def __len__(self):
        return self.size

    # peek method - O(1)
    def peek(self)->None | Any:
        if self.head is None:
            return None
        value = self.head.value # type: ignore
        return value