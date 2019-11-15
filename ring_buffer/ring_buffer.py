class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        for i in range(self.capacity):
            if self.storage[i] is None:
                self.storage[i] = item
                return

        self.storage[self.current] = item

        if self.current is not self.capacity - 1:
            self.current += 1
        else:
            self.current = 0

    def get(self):
        return [item for item in self.storage if item is not None]
