class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        stack=[]
        

    def push(self, val: int) -> None:
        stack.append(val)

    def pop(self) -> None:
        stack.pop()

    def top(self) -> int:
        return stack[-1]

    def getMin(self) -> int:
        return min(stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
