class stack:
    def __init__(self):
        self._data=[]
    
    def push(self,item):
        self._data.append(item)
    
    def pop(self):
        if self.is_empty():
           raise empty('Stack is empty')
        return self._data.pop()
    
    def is_empty(self):
        return len(self._data) == 0

s = stack()
s.push(1)
s.push(2)
s.push(3)
print(s.pop())  
print(s.pop())
print(s.is_empty())