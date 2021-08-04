class LLNode:
  def __init__(self, data=0, next=None, prev=None):
    self.data = data
    self.next = next
    self.prev = prev

class LinkedList:
  def __init__(self):
    self.head = LLNode(0)
    self.tail = LLNode(0)
    
  def access(self, k):
    temp = self.head
    while k >= 0 and temp.next != None:
      temp = temp.next
      k -= 1
    return temp
  
  def insert(self, new_element, k=0):
    temp = self.access(k-1)

    # For first and only assignment of value @k=-1 -> A|0|A 
    if k == 0 and temp.next == None:
      new_node = LLNode(new_element, next=temp.next, prev=temp.prev)
      temp.next = new_node
      temp.prev = new_node
      self.tail = new_node

    # Update Last (k= last of the list)
    elif temp.next == None:
      new_node = LLNode(new_element, next=None, prev=temp)
      temp.next = new_node
      self.tail = self.access(-1)
      self.tail.prev = new_node

      # To get things back to normal pointer

    # Update First Element(k=0)
    elif temp.next.prev == None:
      new_node = LLNode(new_element, next=temp.next, prev=None)
      # For cases where insert at 1 then insert at 0
      if k == 0 and temp.next == new_node.next:
        temp.next.prev = new_node
      # Normal scenario
      else:
        self.tail.prev = new_node
      temp.next = new_node
            
    # Update any element
    else:
      new_node = LLNode(new_element, next=temp.next, prev=temp.next.prev)
      temp.next.prev = new_node
      temp.next = new_node

    # This acts as a "pointer" for the linked list
    self.tail = new_node
    return


  # This needs to be changed based on insert
  def delete(self, k=0):
    temp = self.access(k-1)
    to_delete = temp.next
    
    # Delete will diverge to 3 cases to avoid error when traversing the linked list
    if to_delete.prev == None:
      temp.next = to_delete.next
      to_delete.next.prev = to_delete.prev

      # For getting "back on track" when deleting a data and inserting on the next one
      self.tail = temp.next 

    elif to_delete.next == None:
      x = self.access(-1)
      x.prev = temp
      temp.next = to_delete.next

    else:
      temp.next.next.prev = temp
      temp.next = to_delete.next 
      
    del to_delete
    return 
  
  def print_forward(self):
    temp = self.head.next
    out = ""
    while temp != None:
      out = out + str(temp.data) + " -> "
      temp = temp.next
    print(out)
    return
  
  def print_backward(self):
    self.tail = self.head
    temp = self.tail.prev
    out = ""
    while temp != None:
      out = out + str(temp.data) + " <- "
      temp = temp.prev
    print(out)
    return

# You shouldn't need to modify anything below this line

n = int(input())
LL = LinkedList()
for i in range(n):
    call = input().split()
    if call[0] == "insert":
      LL.insert(int(call[2]), int(call[1]))
    elif call[0] == "delete":
      LL.delete(int(call[1]))
    else:
      print("Invalid Command")

LL.print_forward()
LL.print_backward()