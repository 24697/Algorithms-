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

    def pop(self,remove_item):
        self.items.pop(remove_item)

    def peek(self):
        print(self.items[0])

    def size(self):
        pass
    
def main():
    max_stacks = int(input('please enter the max stacks: '))
    while each != -1:
        each = str(input('Please enter the next entery of the stack enter -1 to end: '))
        items_list.append(each)
    


if __name__ == '__main__':
    main()
    
