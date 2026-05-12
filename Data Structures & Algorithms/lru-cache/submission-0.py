class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.ll = []
        self.head = 0
        self.time = 0
        self.n = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.ll.append([key, self.time])
            self.cache[key][1] = self.time
            self.time += 1
            return self.cache[key][0]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.ll.append([key, self.time])
            self.cache[key][0] = value
            self.cache[key][1] = self.time
            self.time += 1
        else:
            while self.n+1 > self.capacity:
                if self.ll[self.head][1] == self.cache[self.ll[self.head][0]][1]:
                    del self.cache[self.ll[self.head][0]]
                    self.head += 1
                    self.n -= 1
                else:
                    self.head += 1
            self.ll.append([key, self.time])
            self.cache[key] = [value, self.time]
            self.time += 1
            self.n += 1