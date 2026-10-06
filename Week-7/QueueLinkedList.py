class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class QueueLinkedList:
    def __init__(self):
        self.front=None
        self.rear=None
    def enqueue(self,data):
        new=Node(data)
        if self.rear is None:
            self.rear=self.front=new
        else:
            self.rear.next=new
            self.rear=new
    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
        
        else:
            if self.front==self.rear:
                self.front=self.rear=None
            else:
                self.front=self.front.next
                if self.front is None:
                    self.rear=None
    def peek(self):
        if self.front is None:
            print("Queue is empty")
        else:
            print(f"Peek: {self.front.data}")
    def display(self):
        if self.front is None:
            print("Queue is empty")
        else:
            temp=self.front
            while temp is not None:
                print(temp.data)
                temp=temp.next
Queue=QueueLinkedList()
while True:
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    choice=int(input("Enter your choice"))
    if choice==1:
        data=int(input("Enter a value"))
        Queue.enqueue(data)
    elif choice==2:
        Queue.dequeue()
    elif choice==3:
        Queue.peek()
    elif choice==4:
        Queue.display()
    elif choice==5:
        break
    else:
        print("Invalid choice")
