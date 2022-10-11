

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
