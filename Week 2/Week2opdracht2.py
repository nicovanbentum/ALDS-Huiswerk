class mystack():
    def __init__(self):
        self.stack_list = []
        self.it_index = -1

    def isEmpty(self):
        if self.stack_list == []:
            return True
        else:
            return False

    def push(self, item):
        self.stack_list.append(item)
        self.it_index += 1

    def pop(self):
        if self.isEmpty():
            return

        return_item = self.stack_list[self.it_index]
        self.stack_list.pop()
        self.it_index -= 1
        return return_item

    def peek(self):
        if self.isEmpty():
            return
        return self.stack_list[self.it_index]

    def print(self):
        print(self.stack_list)


        
