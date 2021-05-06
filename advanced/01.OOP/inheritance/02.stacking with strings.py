from typing import List


class Stack:
    data: List

    def __init__(self):
        self.data = []

    def push(self,item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def is_empty(self):
        if len(self.data) == 0:
            return True
        return False

    def __str__(self):
        return f"[{', '.join(reversed(self.data))}]"

mystack = Stack()
mystack.push("dqdo")
mystack.push("baba")


print(mystack)