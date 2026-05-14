from typing import Any, Optional

class Node:
    def __init__(self, value: Any, /)->None:
        self.value: Any = value
        self.next: Optional['Node'] = None
        


class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None
        self.size: int = 0

    # append method - O(n)
    def append(self, value: Any, /)->None:
        if self.head is None:
            self.head = Node(value)
            self.size+=1
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = Node(value)
        self.size += 1

    # prepend method - O(1)
    def prepend(self, value: Any, /)->None:
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.size+=1

    # insert method - ~O(n)
    def insert(self, value: Any, index: int, /)->IndexError | None:
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
        # size add
        self.size += 1
    
    # left delete method - O(1)
    def left_pop(self)->int | None:
        if self.head is None:
            return None
        delete_value = self.head.value
        self.head = self.head.next
        # size 
        self.size -=1
        return delete_value

    # right delete method - O(n)
    def pop(self)->int | None:
        if self.head is None:
            return None
        last = self.head
        while last.next.next:
            last = last.next
        last.next = None
        self.size -= 1

    # delete (value) method - O(n)
    def delete(self, value: Any)->None:
        if self.head is None:
            return None
        if self.head.value == value:
            self.head = self.head.next
            self.size -= 1
            return value

        last = self.head
        while last.next:
            if last.next.value==value:
                delete_value = last.next.value
                last.next = last.next.next
                return delete_value
            last = last.next
    # Reverse method - O(n)
    def Reverse(self)->None:
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow.value
    
    def max_value(self)->Any:
        max_value = self.head.value
        last = self.head
        while last.next:
            if last.next.value>max_value:
                max_value = last.next.value
            last = last.next
        return max_value
    
    def min_value(self):
        min_value = self.head.value
        last = self.head
        while last.next:
            if last.next.value<min_value:
                min_value = last.next.value
            last = last.next
        return min_value
    
    def search(self, value: Any)->bool:
        current = self.head
        while current:
            if current.value==value:
                return True
            current = current.next
        return False
    def remove_fublicates(self)->None:
        current = self.head
        seen = set()
        prev = None
        while current:
            if current.value in seen:
                prev.next = current.next
            else:
                seen.add(current.value)
                prev = current
            current = current.next

    def clear(self):
        self.head = None
        self.size = 0

    # __str__ dunder method - O(n)
    def __str__(self) -> str:
        result = []
        last = self.head
        while last:
            result.append(str(last.value))
            last = last.next
        return " -> ".join(result)
    # for 
    def __iter__(self):
        last = self.head
        while last:
            yield last.value
            last = last.next
    def to_list(self) -> list:
        return [item for item in self]
if __name__ == "__main__":
    ll = LinkedList()

    # 1. Qo'shishni test qilamiz
    ll.append(10)
    ll.append(20)
    ll.prepend(5)
    ll.insert(15, 2)  # 5 -> 10 -> 15 -> 20
    print(f"Ro'yxat: {ll}") 
    print(f"O'lchami: {ll.size}") # 4 bo'lishi kerak

    # 2. Middle, Max, Min testlari
    print(f"O'rtadagi element: {ll.middle()}") # 15
    print(f"Eng katta: {ll.max_value()}")      # 20
    print(f"Eng kichik: {ll.min_value()}")      # 5

    # 3. Search test
    print(f"15 bormi?: {ll.search(15)}")  # True
    print(f"100 bormi?: {ll.search(100)}") # False

    # 4. Reverse test
    ll.Reverse()
    print(f"Teskari tartib: {ll}") # 20 -> 15 -> 10 -> 5

    # 5. Duplicates (takrorlanishlar) testi
    ll.append(15)
    ll.append(20)
    print(f"Takrorlanganlar bilan: {ll}")
    ll.remove_fublicates() # Metod ismidagi xatoni (fublicates) tekshiring
    print(f"Tozalangandan keyin: {ll}")

    # 6. O'chirish (Pop/Delete) testlari
    ll.left_pop()
    print(f"Chapdan o'chirilgach: {ll}")
    
    # Eslatma: Sizning delete metodingizda xato bor, 
    # u o'chirish o'rniga prepend qilmoqda. Testda shuni kuzating:
    ll.delete(10) 
    print(f"10 o'chirilgach (tekshiring!): {ll}")

    # 7. To'liq tozalash
    ll.clear()
    print(f"Tozalangandan keyin: '{ll}' (bo'sh bo'lishi kerak)")
