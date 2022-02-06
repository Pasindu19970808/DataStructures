#Linked list in dictionary form
# head = {
#             "value":11,
#             "next":{
#                     "value":3,
#                     "next":{
#                             "value":23,
#                             "next":{
#                                     "value":7,
#                                     "next":None
#                                     }

#                             }
#                     }

#         }
# linked_list = head
# while linked_list["next"] != None:
#     print(linked_list["value"])
#     linked_list = linked_list["next"]



from http.client import NETWORK_AUTHENTICATION_REQUIRED


class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self,value):
        #create new node
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    def append(self,value):
        #create new node
        #add node to the end
        next_node = Node(value)
        if self.head == None:
            self.head = next_node
            self.tail = next_node
        else:
            #setting the next_node as the next node of
            #the current last node
            #Note that setting self.tail.next will also
            #set self.head.next to next_node
            #IF self.tail and self.head are pointing to
            #same node
            self.tail.next = next_node
            #setting the next_node as the tail of the linked
            #list
            self.tail = next_node
        self.length += 1
        return True
    def prepend(self,value):
        #create new node
        #add to the start
        new_node = Node(value)
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            #set the next of new_node as current self.head
            new_node.next = self.head
            #set the new self.head as the new_node
            self.head = new_node
            self.length += 1
        return True
    def insert(self,index,value):
        #create new node
        #insert at index
        if index == 0 or index == self.length:
            return AssertionError("Use Append or Prepend to Insert node at beginning or end")
        else:
            x = self.head
            i = 0
            while i < index - 1:
                x = x.next
                i += 1
            new_node = Node(value)
            #get a pointer to the next node of the current x
            y = x.next
            #set the before node's next pointer to new node
            x.next = new_node
            #set the new node's next pointer to y
            new_node.next = y
            self.length += 1
    def print_list(self):
        x = self.head
        i = 0
        while i <= self.length - 1:  
            if x.next != None:
                print(x.value)
                x = x.next
            else:
                print(x.value)
            i += 1
    def pop_item(self):
        #pops the last item
        #There are 2 edge cases
        #1 with both self.head and self.tail equal to None 
        #2 with only one node where self.head = self.tail
        if self.head == None and self.tail == None:
            return Exception("Linked List doesnt exist")
        elif self.head == self.tail:
            y = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return y.value,y.next
        else:
            x = self.head
            while x.next.next != None: 
                x = x.next
            # while x.next != None:
            #     y = x
            #     x = x.next
            #collect the last node that is popped
            y = x.next
            self.tail = x
            self.tail.next = None
            self.length -= 1
            return y.value,y.next
    def pop_first(self):
        if self.head == None and self.tail == None:
            return Exception("Linked List doesnt exist")
        elif self.head == self.tail:
            y = self.head
            y.next = None
            self.head = None
            self.tail = None
            self.length -=1
            return y.value,y.next
        else:
            x = self.head.next
            y = self.head
            y.next = None
            self.head = x
            self.length -= 1
            return y.value,y.next
    def get(self,index):
        if self.head == None and self.tail == None:
            return Exception("Linked List doesnt exist")
        else:
            i = 0
            x = self.head
            if index <= self.length - 1 and index >= 0:
                while i < index:
                    x = x.next
                    i += 1
                return x
            else:
                return IndexError("Index greater than length of Linked List")


linked_list = LinkedList("A")
print('hi')