class Node:
    def __init__(self,new_data):
        self.data = new_data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
        
    def append(self,new_data):
        current = self.head
        if current is not None:
            while current.next:
                current = current.next
            current.next = Node(new_data)
        else:
            self.head = Node(new_data)

    def travel_linked_list(self):
        current = self.head
        while current:
            print(current.data, end="-->")
            current = current.next
        print(None)
    
    def list_to_ll(self,my_list):
        if len(my_list) != 0:  
            if self.head is None:
                self.head = Node(my_list[0])
                current = self.head
                for each in my_list[1:]:
                    current.next = Node(each)
                    current = current.next
                
            else:
                current = self.head
                while current.next:
                    current = current.next
                for each in my_list:
                    current.next = Node(each)
                    current = current.next
       
    def count_nodes(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count


    def search_value(self,value):
        current = self.head
        index = 0
        index_list = []
        while current:
            if current.data == value:
                index_list.append(index)
                current = current.next
                index += 1
            else:
                current = current.next
                index += 1  
        if len(index_list) == 0:
            print("Value NOT found") 
        else:
            print("Value : ",value,",found at index:", index_list)

    def delete_node_by_value(self,value):
        index = 0
        index_list = []
        while self.head is not None and self.head.data == value :

            if self.head.next is not None:
                self.head = self.head.next
                index_list.append(index)
                index += 1
            else:
                self.head = None
                index_list.append(index)
                index += 1

        current = self.head
        prev = None
        print(index,self.head)

        while current is not None:
            if current.data == value:
                prev.next = current.next
                current = current.next
                index_list.append(index)
                index += 1
            else:
                prev = current
                current = current.next
                index += 1
        if len(index_list) == 0:
            print("No Value found to Delete")
        else:
            print(value ,"Deleted from index : ",index_list)

    def insert_value_at_position(self,pos,val):

        current = self.head
        

    
                    


            
my_list = [1,2,3,5]

ll = Linkedlist()
try:
    ll.list_to_ll(my_list)
    print(my_list)

    
except Exception as e:
    print(type(e))
    print(e)
    
