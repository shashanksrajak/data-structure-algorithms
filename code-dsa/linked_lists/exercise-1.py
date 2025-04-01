# https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/3_LinkedList/3_linked_list_exercise.md#exercise-linked-list

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next
        # print(self)

class LinkedList:
    def __init__(self):
        self.head = None

    # prints linked list
    def print_list(self):
        itr = self.head

        if(itr == None):
            print("The list is empty")
            return
        
        while(itr):
            print(itr.value)
            itr = itr.next

    # len of list
    def length(self):
        len = 0
        itr = self.head

        if(itr == None):
            print("The list is empty")
        
        while(itr):
            len = len +1
            itr = itr.next

        return len
        

    # insert in list at head
    def insert_at_start(self, value):
        node = Node(value, self.head)
        self.head = node #head will point to the new node, and the newly created node points to node which was head earlier

    #insert at end of the list
    def insert_at_end(self, value):
        node = Node(value, None)

        # if list is empty and this function gets called
        # safety check - edge case
        if self.head is None:
            self.head = node
            return
        
        itr = self.head
        
        # traverse to the last node
        while(itr.next):
            itr = itr.next

        # last node points to this new node which will become tail
        itr.next = node
        return
    
    def insert_at(self, index, value):
        itr = self.head
        count = 0

        while (itr):
            if(count == index-1):
                # do this
                node = Node(value, itr.next)
                itr.next = node
                break
          
            count = count+1
            itr = itr.next

    def remove_at(self, index):
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1
    def insert_after_value(self, data_after, data_to_insert):
    # Search for first occurance of data_after value in linked list
    # Now insert data_to_insert after data_after node
        itr = self.head
        len = self.length()
        count = 0
        while(count<len):
            if(itr.value == data_after):
                # create a node
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break

            itr = itr.next

    def remove_by_value(self, data):
    # Remove first node that contains data
        if self.head is None:
            print("List is empty")
            return
        
        # if its the head node 
        # this case is handled seprately
        if self.head.value == data:
            self.head = self.head.next
            return
        

        prev = self.head
        itr = self.head.next
       
        while(itr):
            if(itr.value == data):
                prev.next = itr.next 
                return

            prev = itr
            itr = itr.next

        print("Value not found in the list")

if __name__ == "__main__":
    my_list = LinkedList()
    # print("My linked list is->", my_list)
    my_list.insert_at_start(56)
    my_list.insert_at_start(98)


    print("Length of list is =>", my_list.length())

    my_list.insert_at_end(1200)

    my_list.insert_at(1, 102)


    my_list.insert_after_value(1200, 77777)
    print("Final linked list looks like this")

    my_list.print_list()

    my_list.remove_by_value(7777)
    my_list.print_list()
    
