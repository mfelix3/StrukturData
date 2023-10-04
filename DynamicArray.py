import ctypes  # provides low-level arrays

class DynamicArray:
    def __init__(self):
        self.n = 0  # count actual elements
        self.capacity = 1  # default array capacity
        self.A = self.make_array(self.capacity)  # low-level array

    def __len__(self):
        return self.n

    def __getitem__(self, k):
        if not 0 <= k < self.n:
            raise IndexError('invalid index')
        return self.A[k]  # retrieve from array

    def append(self, obj):
        if self.n == self.capacity:  # not enough room
            self.resize(2 * self.capacity)  # so double capacity
        self.A[self.n] = obj
        self.n += 1

    def resize(self, c):  # nonpublic utility
        B = self.make_array(c)  # new (bigger) array
        for k in range(self.n):  # for each existing value
            B[k] = self.A[k]
        self.A = B  # use the bigger array
        self.capacity = c

    def make_array(self, c):  # nonpublic utility
        return (c * ctypes.py_object)()

A = DynamicArray()
A.append(1)
A.append(2)
A.append(7)
A.append(8)
A.append(9)
print(A[0], A[1], A[2])
print(A[4])