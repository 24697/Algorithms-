class node:
    def __init__(self,data):
        self.data = data
        self.next_pointer = None 

    def get_data(self,data):
        return self.data
    
    def set_data(self,new_data):
        self.data = new_data
        
    def get_next_pointer(self):
        return self.next_pointer
    
    def set_next_pointer(self,data):
        temp = node(data)
        self.next_pointer = temp
    
class Unorded_list:
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head == None
    
    def add(self,data):
        temp = node(data)
        self.head = temp
        
    def get_list(self):
        pass

    def length(self):
        pass

    def remove(self):
        pass

class Ordered_list(Unorded_list):
    def __init__(self):
        super().__init__()

    def add():
        pass

    def search():
        pass
