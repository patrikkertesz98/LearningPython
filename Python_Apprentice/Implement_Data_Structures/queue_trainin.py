from queue import Queue

olympics = Queue(5)

print(olympics)

olympics.put('United States(USA)')
olympics.put('Great Britain(GBR)')

print("Is empty?: ", olympics.empty())
print("Is full?: ", olympics.full())

print("Size of?: ", olympics.qsize())

olympics.put('China(CHN)')
olympics.put('Russia(RUS)')
olympics.put('Germany(GER)')

print("Is empty?: ", olympics.empty())
print("Is full?: ", olympics.full())

print("Size of?: ", olympics.qsize())

print("Element on top: ", olympics.get())

print("Size of?: ", olympics.qsize())

print("Element on top: ", olympics.get())

print("Size of?: ", olympics.qsize())

print("Element on top: ", olympics.get())

print("Size of?: ", olympics.qsize())

print("Element on top: ", olympics.get())

print("Size of?: ", olympics.qsize())


###############################################################
######### implement a list as a queue
###############################################################

class MyQueue:

    def __init__(self, limit):
        '''Create a new queue.'''
        self.items = []
        self.limit = limit

    def is_empty(self):
        ''' Returns true if queue is empty. '''
        return len(self.items) == 0

    def enqueue(self, item):
        ''' Adds element to the end of the queue. '''
        if self.size() < self.limit:
            self.items.append(item)
        else:
            raise Exception("Reached current queue's limit.")

    def dequeue(self):
        ''' Returns element form the top of the queue. '''
        if self.size() == 0:
            raise Exception("Queue is empty.")
        else:    
            return self.items.pop(0)

    def size(self):
        ''' Returns the size of the queue. '''
        return len(self.items)
    
    def peek(self):
        ''' Have a look at the first element of the queue. '''
        if self.is_empty():
            raise Exception("No more elements in the queue.")
        else:
            return self.items[0]

    def is_full(self):
        ''' Returns True if the queue is full. '''
        return self.size() == self.limit


olympics = MyQueue(5)

print(olympics)

olympics.enqueue('United States(USA)')
olympics.enqueue('Great Britain(GBR)')

print("Is empty?: ", olympics.is_empty())
print("Is full?: ", olympics.is_full())

print("Size of?: ", olympics.size())

olympics.enqueue('China(CHN)')
olympics.enqueue('Russia(RUS)')
olympics.enqueue('Germany(GER)')

print("Is empty?: ", olympics.is_empty())
print("Is full?: ", olympics.is_full())


print("Take a peek: ", olympics.peek())
print("Size of?: ", olympics.size())

print("Element on top: ", olympics.dequeue())

print("Size of?: ", olympics.size())

print("Element on top: ", olympics.dequeue())

print("Size of?: ", olympics.size())

print("Element on top: ", olympics.dequeue())

print("Size of?: ", olympics.size())

print("Element on top: ", olympics.dequeue())

print("Size of?: ", olympics.size())

print("Element on top: ", olympics.dequeue())

print("Size of?: ", olympics.size())
