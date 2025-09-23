class MinStack:

    def __init__(self):
        self.min = []
        self.main = []
        
    def push(self, val: int) -> None:
        if len(self.main) == 0:
            self.min.append(val)
        elif val <= self.min[-1]:
            self.min.append(val)
        else:
            self.min.append(self.min[-1])
        self.main.append(val)
        
    def pop(self) -> None:
        self.min.pop()
        self.main.pop()

    def top(self) -> int:
        return self.main[len(self.main) - 1]
        

    def getMin(self) -> int:
        return self.min[-1]
