class Stack:
    '''An Example Stack Class'''

    def __init__(self,max_stack,items_to_add):
        self.max_stack = max_stack
        self.stack_pointer = None

        self.items_list = []
        for each in items_to_add:
            self.items_list.append(each)

    def is_empty(self):
        if len(self.items_list) == 0:
            self.empty = True
        else:
            self.empty = False
        return self.empty

    def push(self,new_item):
        self.items_list.append(new_item)

    def pop(self,remove_item):
        self.poped_item = self.items_list[remove_item]
        self.items_list.pop(remove_item)
        return self.poped_item

    def peek(self):
        self.peeked_item = self.items_list[0]
        return self.peeked_item

    def size(self):
        self.size = len(self.items_list)
        return self.size

def menu():
    print()
    print('1. Is Empty')
    print('2. Push')
    print('3. Pop')
    print('4. Peek')
    print('5. Size')
    print('6. End')
    print()
    end = False
    while end != True:
        try:
            choice = int(input('Please enter you choice: '))
            for count in range(1,6):
                if end == True:
                    pass
                else:
                    if choice == count:
                        end = True
                    else:
                        pass
            if end == False:
                print('Please enter a valid value')
        except ValueError:
            print('Please enter a valid value')
    return choice

def main():
    max_stacks = int(input('please enter the maxaum about of items in the stack: '))
    items_to_add = []
    each = 0
    while each != '-1':
        each = str(input('Please enter the next entery of the stack enter -1 to end: '))
        if each == '-1':
            pass
        else:
            items_to_add.append(each)
    end = False
    new_stack = Stack(max_stacks,items_to_add)
    while end != True:
        choice = menu()
        if choice == 1:
            empty = new_stack.is_empty()
            if empty == True:
                print('The stack is empty')
            else:
                print('The stack is not empty')
        elif choice == 2:
            new_item = str(input('Please enter the new entry to the stack: '))
            new_stack.push(new_item)
        elif choice == 3:
            pass
        elif choice == 4:
            peek = new_stack.peek()
            print(peek)
        elif choice == 5:
            size = new_stack.size()
            print(size)
        else:
            end = True

if __name__ == '__main__':
    main()
    
