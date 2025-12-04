class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        if self.empty():
            raise IndexError("pop from empty stack")
        return self.queue.popleft()

    def top(self) -> int:
        if self.empty():
            raise IndexError("top from empty stack")
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0
