from ArrayStacks import ArrayStack

def is_matched(expression):
    lefty = '({['
    righty = ')}]'
    S = ArrayStack()
    
    for c in expression:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if righty.index(c) != lefty.index(S.pop()):
                return False
    return S.is_empty()


# Test
print(is_matched('[(5x+1)+{34x+y}]'))