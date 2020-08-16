class ArrayQueue:
    '''Queue implementation using list as underlying storage in python'''
    DEFAULT_SIZE = 10
    
    def __init__(self):
        '''Generate an empty Queue'''
        self._data = [None]*ArrayQueue.DEFAULT_SIZE
        self._size = 0
        self._front = 0
    
    def __len__(self):
        '''returns the length of the queue'''
        return self._size
    
    def is_empty(self):
        '''Check if empty'''
        return self._size == 0
    
    def first(self):
        '''Return the first element (but don't remove it)'''
        if self.is_empty():
            raise Exception('Queue is empty')
        return self._data[self._front]
    
    def dequeue(self):
        '''Return and remove the element as FIFO'''
        if self.is_empty():
            raise Exception('Queue is empty')
        val = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0 < self._size < len(self._data)//4:   #shrinking the underlying array
            self._resize(len(self._data)//2)
        return val
    
    def enqueue(self, element):
        '''Add element(data) to the queue at the end'''
        if self._size == len(self._data):
            self._resize(2*len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = element
        self._size += 1
        
    def _resize(self, capacity):
        ''' Resize the array'''
        old = self._data
        self._data = [None]*capacity
        front = self._front
        for k in range(self._size):
            self._data[k] = old[front]
            front = (front + 1) % len(old)
        self._front = 0
          
        
        
# Instantiation
if __name__ == '__main__':
    queue = ArrayQueue()
    queue.enqueue(2)
    queue.enqueue(9)
    queue.enqueue(0)
    queue.enqueue(7)
    queue.enqueue(5)
    print(queue.is_empty())
    queue.enqueue(3)
    print(len(queue))
    print(queue.first())
    queue.dequeue()
    print(queue.first())
    
    
