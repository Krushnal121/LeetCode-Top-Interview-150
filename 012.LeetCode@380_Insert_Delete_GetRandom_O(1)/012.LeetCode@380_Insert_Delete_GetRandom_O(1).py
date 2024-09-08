class RandomizedSet:

    def __init__(self):
        self.lst = []
        self.idxmap = {}

    def search(self, val):
        return val in self.idxmap

    def insert(self, val: int) -> bool:
        if self.search(val):
            return False

        self.lst.append(val)
        self.idxmap[val]=len(self.lst) - 1
        return True

    def remove(self, val: int) -> bool:
        if not self.search(val):
            return False

        idx = self.idxmap[val]
        self.lst[idx] = self.lst[-1]
        self.idxmap[self.lst[-1]] = idx
        self.lst.pop()
        del self.idxmap[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.lst)