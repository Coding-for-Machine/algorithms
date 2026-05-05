from typing import Any, Optional

class Node:
    def __init__(self, value: Any):
        self.data: Any = value
        self.next: Optional['Node'] = None