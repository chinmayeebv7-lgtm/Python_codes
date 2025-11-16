# class Node:
#   def __init__(self,data):
#     self.data=data
#     self.next=None
#     self.prev=None


# node1=Node(3)
# node2=Node(6)
# node3=Node(9)
# node4=Node(12)

# node1.next=node2
# node2.next=node3
# node3.next=node4
# node4.next=node2

# print(node1.next.data)

# node2.prev=node1
# node3.prev=node2
# node4.prev=node3

# print("Traversing forward:\n")
# currentnode=node1
# while currentnode:
#   print(currentnode.data,end="->")
#   currentnode=currentnode.next
# print("null")

# print("Traversing backward:\n")
# currentnode=node4
# while currentnode:
#   print(currentnode.data,end="->")
#   currentnode=currentnode.prev
# print("null")


# CIRCULAR LINKED LISTS:
# class Node:
#   def __init__(self,data):
#     self.data=data
#     self.next=None
#     self.prev=None

# node1=Node(3)
# node2=Node(6)
# node3=Node(9)
# node4=Node(12)

# node1.next=node2
# node2.next=node3
# node3.next=node4
# node4.next=node1
# node4.next=node1

# node4.prev=node3
# node3.prev=node2
# node2.prev=node1
# node4.prev=node1

# print("Traversing forward:\n")
# currentnode=node1
# startnode=node1
# print(currentnode.data,end="->")
# currentnode=currentnode.next

# while currentnode!=startnode:
#    print(currentnode.data,end="->")
#    currentnode=currentnode.next
# print("null")

# print("\nTraversing backward:")
# currentnode = node4
# startnode = node4
# print(currentnode.data, end=" -> ")
# currentNode = currentnode.prev

# while currentnode != startnode:
#     print(currentnode.data, end=" -> ")
#     currentnode = currentnode.prev

# print("...")

# print((node4.next).data)

#lowest:
# class Node:
#   def __init__(self,data):
#     self.data=data
#     self.next=None

# def FindLowest(head):
#   minval=head.data
#   currentnode=head.next
#   while currentnode:
#     if minval>currentnode.data:
#       minval=currentnode.data
#   currentnode=currentnode.next
#   return minval

# node1=Node(10)
# node2=Node(13)
# node3=Node(5)
# node4=Node(12)

# node1.next=node2
# node2.next=node3
# node3.next=node4

# res=FindLowest(node1)
# print(res)

#delete
# class Node:
#   def __init__(self,data):
#     self.data=data
#     self.next=None

# def traverseAndPrint(head):
#     currentNode = head
#     while currentNode:
#         print(currentNode.data, end=" -> ")
#         currentNode = currentNode.next
#     print("null")

# def insert(head,newnode,position):
#     if position==1:
#         newnode.next=head
#     currentnode=head
#     for i in range(position-2):
#      if currentnode is None:
#         break
#      currentnode=currentnode.next
#      currentnode

   



# node1=Node(10)
# node2=Node(13)
# node3=Node(5)
# node4=Node(12)

# node1.next=node2
# node2.next=node3
# node3.next=node4

# node1=deleteNode(node1,node3)
# print()


# class hash_set():
#     def __init__(self,size):
#         self.size=size
#         self.buckets=[[] for i in range(size)]

#     def hash_func(self,word):
#         return sum(ord(char) for char in word)%self.size
    

#     def add(self,value):
#         index=self.hash_func(value)
#         bucket=self.buckets[index]
#         if value not in bucket:
#           bucket.append(value)

#     def contains(self,value):
#         index=self.hash_func(value)
#         bucket=self.buckets[index]
#         return value in bucket
    
#     def remove(self,value):
#         index=self.hash_func(value)
#         bucket=self.buckets[index]
#         if value in bucket:
#             bucket.remove(value)

#     def printset(self):
#         print("Hash set elements:\n")
#         for index,bucket in enumerate(self.buckets):
#             print(f'Bucket {index}:{bucket}')

# hash_set = hash_set(size=10)

# hash_set.add("Charlotte")
# hash_set.add("Thomas")
# hash_set.add("Jens")
# hash_set.add("Peter")
# hash_set.add("Lisa")
# hash_set.add("Adele")
# hash_set.add("Michaela")
# hash_set.add("Bob")

# hash_set.remove("Thomas")
# hash_set.add("genevive")
# print(hash_set.contains("hello"))
# print(hash_set.hash_func("Chinmayee"))
# hash_set.printset()



# class SimpleHashMap():
#   def __init__(self,size=100):
#     self.size=size
#     self.buckets=[[] fori in range size]

#   def hash_function(self):
#     numeric_sum= sum(int(char) for char in key if char.isdigit())
#     return numeric_sum%10
  
#   def put(self,key,value):
#     index=self.hash_function(key)
#     bucket=self.buckets[index]
#     for i, (k,v) in enumerate(bucket):
#       if k==key:
#         bucket[i]=(key,value)
#         return
#     bucket.append((key,value))

#   def get(self,key):
#     index=self.hash_function(key)
#     bucket=self.buckets[index]
#     for k,v in bucket:
#       if k==key:
#         return v
#     return None
  
#   def remove(self):
#     index=self.hash_function(key)
#     bucket=self.buckets[index]
#     for i,(k,v) in enumerate(bucket):
#       if k==key:
#         del bucket[i]
#         return 


# IMPLEMENTATION OF TREES
# class TreeNode():
#   def __init__(self,data):
#     self.data=data
#     self.left=None
#     self.right=None
  

# Root=TreeNode("R")
# NodeA=TreeNode("A")
# NodeB=TreeNode("B")
# NodeC=TreeNode("C")
# NodeD=TreeNode("D")
# NodeE=TreeNode("E")
# NodeF=TreeNode("F")
# NodeG=TreeNode("G")

# Root.left=NodeA
# Root.right=NodeB

# NodeA.left=NodeC
# NodeA.right=NodeD
# NodeB.left=NodeE
# NodeB.right=NodeF
# NodeF.left=NodeG

# print(Root.right.left.data)

# def PreOrderTraversal(node):
#   if node is None:
#     return
#   print(node.data,end=",")
#   PreOrderTraversal(node.left)
#   PreOrderTraversal(node.right)


# def InOrderTreversal(node):
#   if node is None:
#     return
#   PreOrderTraversal(node.left)
#   print(node.data,end=' ')
#   PreOrderTraversal(node.right)

# def PostOredrTrverasal(node):
#   if node is None:
#     return
#   PostOredrTrverasal(node.left)
#   PostOredrTrverasal(node.right)
#   print(node.data,end=" ")


  # BINARY SEARCH ALGORITHM:
  
# def binary_Search(arr,val):
#     left=0
#     right=len(arr)-1
#     while left<=right:
#       mid=(left+right)//2
#       if arr[mid]==val:
#         return mid
#       elif arr[mid]<val:
#         left=mid+1
#       else:
#         right=mid-1
#     return None
  
# array= [2,3,7,7,11,15,25 ]
# value=int(input("Enter the element to search:\n"))
# res=binary_Search(array,value)
# if res!=None:
#   print("The value is found at index:",res)
# else:
#   print("Value not found")

# LINEAR SEARCH ALGORITHM
# def linearSearch(arr,val):
#   for i in range(len(arr)):
#     if arr[i]==val:
#       return i
#   return None

# array=[21,3,4,50,6,0,9,0,1]
# value=int(input("Enter the element to search:\n"))
# res=linearSearch(array,value)
# if res!=None:
#   print("Value found at index:",res)
# else:
#   print("Value not found")

# STACK IMPLEMENTATION USING LINKED LISTS:
# class Node:
#   def __init__(self,value):
#     self.value=value
#     self.next=None

# class Stack:
#   def __init__(self):
#     self.head=None        
#     self.size=0
#     # THESE ARE THE POINTERS=HEAD AND SIZE

#   def push(self,value):
#       new_node=Node(value)
#       if self.head:
#         new_node.next=self.head
#       self.head=new_node
#       self.size+=1
    
#   def pop(self):
#       if self.isEmpty():
#         return "Stack is empty"
#       popped_node=self.head
#       self.head=self.head.next
#       self.size=-1
#       return popped_node.value
    
#   def peek(self):
#       if self.isEmpty():
#         return "Stack is empty"
#       return self.head.value
    
#   def isEmpty(self):
#       return self.size==0
    
#   def stackSize(self):
#       return self.size
    

# myStack = Stack()
# myStack.push('A')
# myStack.push('B')
# myStack.push('C')

# print("Pop: ", myStack.pop())
# print("Peek: ", myStack.peek())
# print("isEmpty: ", myStack.isEmpty())
# print("Size: ", myStack.stackSize())

arr=[2,7,11,15]
arr.append("_")


  







      
    




       
            


 

 

  