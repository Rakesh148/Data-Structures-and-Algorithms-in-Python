from ArrayStacks import ArrayStack

def reverse_file(file):
    ''' Reversing the data stored in a file using stack'''
    S = ArrayStack()
    original = open(file)
    for line in file:
        S.push(line.rstrip('\n'))
    original.close()
    
    # overwriting with reversed data
    new = open(file, 'w')
    while not S.is_empty():
        new.write(S.pop() + '\n')
    new.close()
    

reverse_file('C:/Users/user/Desktop/Github/PDS/Stack/file.txt')