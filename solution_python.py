class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.arr = []
        self.arr.append(0)
        self.current = 0
        self.revert = []

    def add(self, num: int):
        self.value += num
        self.arr.append(self.value)
        self.current += 1
        

    def subtract(self, num: int):
        self.value -= num
        self.arr.append(self.value)
        self.current += 1

    def undo(self):
        if self.current != 0:
            self.current -= 1
            self.value = self.arr[self.current]
            val = self.arr[self.current + 1] - self.arr[self.current]
            self.revert.insert(0, val)
            del self.arr[self.current + 1]
            
    def redo(self):
        if len(self.revert) != 0:
            self.add(self.revert[0])
            del self.revert[0]

    def bulk_undo(self, steps: int):
        if steps > len(self.arr):
            steps = len(self.arr)
        for i in range(0, steps):
            self.undo()
            

    def bulk_redo(self, steps: int):
        if steps > len(self.revert):
            steps = len(self.revert)
        for i in range(0, steps):
            self.redo()
