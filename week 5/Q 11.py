# This is my code for question 11.
# A linked list is linear so we have to traverse the list,comparing data at each node.
class Node(object):                       #a double linked list NodeN has three attributes
      def __init__(self, value):
          self.value=value                #data item stored by the node
          self.next=None                  #pointer to the next node
          self.prev=None                  #pointer to the previous node

class List(object):
      def __init__(self):                 #a list contains two attributes
          self.head=None                  #the first node in the list
          self.tail=None                  #the last node in the list
      def insert(self,n,x):
         
          if n!=None:                     #if there is something in n then run the following code
              x.next=n.next               
              n.next=x                    #N will point to x 
              x.prev=n                    #x will point to n
              if x.next!=None:            #If statement check if n already points to a node         
                  x.next.prev=x              
          if self.head==None:             #if there is no head Node then set the head and tail to variable x
              self.head=self.tail=x
              x.prev=x.next=None
          elif self.tail==n:
              self.tail=x
      def display(self):
          values=[]
          n=self.head
          while n!=None:
              values.append(str(n.value))
              n=n.next
          print ("List: ",",".join(values))

      def delete(self,n):                 
            if n.prev != None:           
                  n.prev.next=n.next
            else:
                  self.head=n.next
            if n.next != None:
                  n.next.prev =n.prev
            else:
                 self.tail=n.prev
                
         
          
if __name__ == '__main__':
      
      a=Node(8)
      
      l=List()
      l.insert(None, Node(4))
      l.insert(l.head,Node(6))
      l.insert(l.head,a)
      l.insert(l.head,Node(10))
      l.insert(l.head,Node(12))
      l.display()
      l.delete(a)
      l.display()
