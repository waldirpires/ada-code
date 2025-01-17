# entry class to store customer ticket info
class Entry:
    id = 0
    tickets = 0
    def __init__(self, id, tickets):  # constructor
        self.id = id
        self.tickets = tickets

# node class to store elements from queue
class Node:
    def __init__(self, data=None): # constructor
        self.data = data
        self.next = None

# queue class
class Queue:
    def __init__(self): # constructor
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front == None

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        return temp.data

    def front(self):
        if self.is_empty():
            return None
        return self.front.data

class Solution:
    def timeToBuyTickets(self, tickets, k):
        t = 0

        queue = Queue()
        for i in range(len(tickets)):
            entry = Entry(i, tickets[i])
            queue.enqueue(entry)

        done = False
        while done == False:
            t += 1
            entry = queue.dequeue() # dequeue entry for processing
            entry.tickets -=1 # ticket bought
            # if there are no more tickets to buy and entry belongs to k
            if entry.tickets == 0 and entry.id == k:
                done = True # we are done!
                continue
            if entry.tickets > 0: #re-queue entry that still has tickets to buy
                queue.enqueue(entry)

        return t # return total elapsed time (sec)

tickets = [2, 3, 2]
k = 2
s = Solution()
r = s.timeToBuyTickets(tickets, k)
print(r)