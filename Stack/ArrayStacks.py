''' We are modifying the list class to bahave like a stack class.'''

class Empty(Exception):
    '''Error attempting to access an element from empty stack'''
    pass

#===============  Stack class  ==================

class ArrayStack:
    '''Array based implementation of stack'''
    def __init__(self):
        '''Create an empty stack'''
        self._data = []
        
    def __len__(self):
        '''Return the number of elements in the stack'''
        return len(self._data)
    
    def is_empty(self):
        '''check if the stack is empty'''
        return len(self._data) == 0
    
    def top(self):
        '''Return the top element
        Raise Empty exception if the stack is empty.'''
        if self.is_empty():
            raise Empty('The stack is empty')
        return self._data[-1]
        
    def push(self, data):
        '''Add element to the top of the stack'''
        self._data.append(data)
        
    def pop(self):
        '''Remove and retrun the top element in the stack
        Raise Empty exception if the stack is empty.'''
        if self.is_empty():
            raise Empty('The stack is empty')
        return self._data.pop()
    
    
# Instatiating
if __name__ == '__main__':
    S = ArrayStack( )
    S.push(5)
    S.push(3)
    print(len(S))
    print(S.pop( ))
    print(S.is_empty( ))
    print(S.pop( ))
    print(S.is_empty( ))
    S.push(7)
    S.push(9)
    print(S.top( ))
    S.push(4)
    print(len(S))
    print(S.pop( ))
    S.push(6)
    print(S.top( ))
    
    