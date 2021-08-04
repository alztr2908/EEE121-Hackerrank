class Queue:
  def __init__(self):
    self.__q = [0] * 1000
    self.__start = 0
    self.__end = 0
    return
    
  def size(self):
    return self.__end - self.__start
  
  def enqueue(self, i):
    self.__q[self.__end % 1000] = i
    self.__end += 1
    
  def dequeue(self):
    if self.size() > 0:
      self.__start += 1
    else:
      print("Empty Queue")
  
  def front(self):
    return self.__q[self.__start % 1000]

  def __str__(self):
    # Print the contents of the queue from front to back
    return str(self.__q[self.__start % 1000:self.__end % 1000])
  
# Do not modify anything above this line!


# Define the following stack operations below
class Stack:
  def __init__(self):
    self.q1 = Queue()
    self.q2 = Queue()
    return
   
  def push(self, i):
    # Push x first in empty q2 
    self.q2.enqueue(i)

    # Push all the remaining elements in q1 to q2. 
    while(self.q1.size() != 0):
      self.q2.enqueue(self.q1.front())
      self.q1.dequeue()

    # swap the names of two queues 
    self.q = self.q1
    self.q1 = self.q2
    self.q2 = self.q
    return
    
  def pop(self):
    self.q1.dequeue()
    return
  
  def peek(self):
    return self.q1.front()


# You shouldn't need to modify anything below this line
n = int(input())
s = Stack()
for i in range(n):
    call = input().split()
    if call[0] == "push":
      s.push(int(call[1]))
    elif call[0] == "pop":
      print(s.peek())
      s.pop()
    else:
      print("Invalid Command")