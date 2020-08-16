class Empty(Exception):
    pass

class ArrayDeque:
    '''Array based Dequeue'''
    DEFAULT_SIZE = 10
    
    def __init__(self):
        '''Generates an empty dequeue'''
        self._data = [None]*self.DEFAULT_SIZE
        self._size = 0
        self._front = 0
        
    def __len__(self):
        '''Returns the length of the dequeue'''
        return self._size
    
    def is_empty(self):
        '''check if the dequeue is empty'''
        return self._size == 0
    
    def first(self):
        '''Return the first element (but don't remove it)'''
        if self.is_empty():
            raise Exception('DeQueue is empty')
        return self._data[self._front]
    
    def last(self):
        '''Return the last element(but don't remove it)'''
        if self.is_empty():
            raise Exception('DeQueue is empty')
        return self._data[(self._front + self._size - 1) % len(self._data)]
    
    def add_first(self, item):
        if self._size == len(self._data):
            self._resize(2*self._size)
        self._data[(self._front - 1) % len(self._data)] = item
        self._front = (self._front - 1) % len(self._data)
        self._size += 1
    
    def remove_first(self):
        if self.is_empty():
            raise Empty('DeQueue is empty')
        ans = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front+1)%len(self._data)
        self._size -= 1 
        return ans
    
    def add_last(self, value):
        if self._size == len(self._data): self._resize(self._size*2)
        self._data[(self._front+self._size)%len(self._data)] = value
        self._size += 1
        
    def remove_last(self):
        if self.is_empty(): raise Empty('DeQueue is empty')
        ans = self._data[(self._front+ self._size-1)%len(self._data)]
        self._data[(self._front+ self._size)%len(self._data)] = None
        self._size -= 1
        return ans
        
    def _resize(self, capacity):
        old = self._data
        self._data = [None]*capacity
        for i in range(len(old)):
            self._data[i] = old[(self._front+i)%len(old)]
        self._front = 0
    
# Instantiation
if __name__ == '__main__':
    Q = ArrayDeque()
    for i in range(3):
        Q.add_last(1)
        
    print(Q.first())
    
    for i in range(3):
        Q.add_last(0)
        
    print(Q.last())
    print(len(Q))
        
    for i in range(3):
        Q.add_first(9)
    
    print(Q.remove_last())
    print(len(Q))
    