class Stack:
    '''An Example Stack Class'''

    def __init__(self,max_stack,items_list):
        self.max_stack = max_stack
        self.stack_pointer = 0

        self.items = []
        for each in items_list:
            self.items.append(each)

    def is_empty(self):
        if len(self.items) == 0:
            self.empty == True
        else:
            self.empty == False

    def push(self):
        self.items.append(str(input('Please enter the next entry for the stack: ')))

    def pop(self):
        self.items.pop(0)

    def peek(self):
        print(self.items[0])

    def size(self):
        pass



if __name__ == '__main__':
    items_list=['Hello world','My name is Peter']
    test_stack = Stack(6,items_list)
    
