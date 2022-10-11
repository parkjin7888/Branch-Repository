class Queue:
  def __init__(self,display=False):
      self.queue = []
      self.display=display
  def enqueue(self,data):
      self.queue.insert(0,data)
      if self.display:
          print("after enqueue",data,end=" ")
          print(self.queue)
  def dequeue(self):
      if len(self.queue)>0:
          data = self.queue.pop()
          if self.display:
              print("after dequeue",data,end=" ")
              print(self.queue)
      else:
          print("Queue Empty!")

def main():
    myQueue = Queue(display=True)
    myQueue.enqueue(5) 
    myQueue.enqueue(6) 
    myQueue.enqueue(9) 
    myQueue.enqueue(9) 
    myQueue.dequeue()  
    myQueue.dequeue()  
    myQueue.dequeue()  
    myQueue.dequeue()
    myQueue.dequeue()
main()
