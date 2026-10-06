class CircularQueue:
    def __init__(self,size):
        self.size=size
        self.queue=[None]*size
        self.front=-1
        self.rear=-1
    def enqueue(self,data):
        if (self.rear+1)%self.size==self.front:
            print("Queue overflow")
            return
        if self.front==-1:
            self.front=0
            self.rear=0
            self.queue[self.rear]=data
        else:
            self.rear=(self.rear+1)%self.size
            self.queue[self.rear]=data
        print(data," inserted into queue.")
    def dequeue(self):
        if self.front==-1:
            print("Queue underflow")
            return
        if self.front==self.rear:
            item=self.queue[self.front]
            self.queue[self.front]=None
            self.front=-1
            self.rear=-1
        else:
            item=self.queue[self.front]
            self.queue[self.front]=None
            self.front=(self.front+1)%self.size
        print(item," deleted from the queue")
    def display(self):
        if self.front==-1:
            print("No elements in the queue")
        else:
            print("Elements in the queue are:")
            i=self.front
            while True:
                print(self.queue[i])
                if i==self.rear:
                    break
                i=(i+1)%self.size
size=int(input("Enter the size of the queue: "))
queue=CircularQueue(size)
while True:
    print("--------------------Circular Queue Menu--------------------")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        data=int(input("Enter element: "))
        queue.enqueue(data)
    elif choice==2:
        queue.dequeue()
    elif choice==3:
        queue.display()
    elif choice==4:
        break
    else:
        print("Invalid choice")
