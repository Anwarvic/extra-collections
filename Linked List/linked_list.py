class Node():
    def __init__(self, value=None):
        self.data = value
        self.next = None

    def __repr__(self):
        if self.next:
            return "Node: (value: {}, next: {})".format(self.data, self.next.data)
        else:
            return "Node: (value: {}, next: {})".format(self.data, self.next)
    


class LinkedList():
    def __init__(self, value=None):
        self.__root = Node(value)
        self.length = 1 if value else 0


    def __repr__(self):
        pointer = self.__root
        # handle edge case
        if pointer.data == None:
            return "[]"
        # general case
        output = "["
        while(pointer.next != None):
            output += str(pointer.data) + ", "
            pointer = pointer.next
        output += str(pointer.data)
        return output+"]"


    def __len__(self):
        return self.length


    def __getitem__(self, idx):
        # caliberate idx if -ve
        if idx <= -1:
            idx += self.length
        # sanity check over given index
        if idx >= self.length:
            raise IndexError("max index for this list is "+str(self.length-1))
        pointer = self.__root
        # handle edge case
        if idx == 0: return pointer.data
        # iterate over the linked list
        counter = 0
        while(pointer.next != None):
            counter += 1
            pointer = pointer.next
            if counter == idx:
                return pointer.data


    def is_empty(self):
        return self.length == 0


    def add_front(self, value):
        self.length += 1
        if self.__root.data == None:
            self.__root = Node(value)
        else:
            new_node = Node(self.__root.data)
            new_node.next = self.__root.next
            self.__root = Node(value)
            self.__root.next = new_node


    def add_end(self, value):
        self.length += 1
        if self.__root.data == None:
            self.__root = Node(value)
        else:
            pointer = self.__root
            while(pointer.next != None):
                pointer = pointer.next
            # now pointer is the last node
            pointer.next = Node(value)


    def remove_front(self):
        if self.length>0:
            tmp = self.__root.next
            self.__root = tmp
            self.length -= 1


    def remove_end(self):
        if self.length > 0:
            tmp = self.__root
            while(tmp.next.next != None):
                tmp = tmp.next
            tmp.next = None
            self.length -= 1



    def clear(self):
        self.__root = Node()
        self.length = 0


    def reverse(self):
        output = LinkedList()
        tmp = self.__root
        while(tmp.next != None):
            output.add_front(tmp.data)
            tmp = tmp.next
        output.add_front(tmp.data)
        return output




if __name__ == "__main__":
    l = LinkedList()
    rev = l.reverse()
    l.add_end(1) #1
    l.add_end(0) #1 0
    l.add_end(7) #1 0 7
    print(l[2])
    print(l)
    l.add_front(0) #0 1 0 7
    l.add_front(2) #2 0 1 0 7
    l.add_front(9) #9 2 0 1 0 7
    rev = l.reverse()
    print(l)
    print(rev)
    l.remove_end() #9 2 0 1 0
    l.remove_front() #2 0 1 0
    print(l.is_empty())
    print(l)
    l.clear()
    print(l.is_empty())
    print(len(l))




