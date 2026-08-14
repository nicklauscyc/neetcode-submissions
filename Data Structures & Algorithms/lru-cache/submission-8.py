from collections import namedtuple

class LRUCache:
    Value = namedtuple('Value', ['link', 'data'])
    class Link:
        # Linked list helps us figure out what to remove in the cache
        def __init__(self, key):
            self.key = key
            self.prev = None
            self.next = None

    def debug(self, msg):
        p = self.head
        s = ""
        while p:
            s += str(p.key)
            s += " -> "
            p = p.next
        
        p = self.tail
        t = ""
        while p:
            t += str(p.key)
            t += " -> "
            p = p.prev
        
            
        
        print(msg, "head", s)
        print("tail", t)
        print("---")

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0

        # Stores key -> Value = ('link', 'data') where data can be of any type and
        # link is a pointer to the link list node
        self.store = {} 
        self.head = None
        self.tail = None 

    def get(self, key: int) -> int:
        self.debug("get "+ str(key))
        res = self.store.get(key, -1)
        
        # Update the key
        if res != -1:
            self.updateLRU(res)
            return res.data

        self.debug("get end " + str(key))
        return res

    # Accesses the link in value and updates the cache
    def updateLRU(self, value):
        link = value.link

        # Nothing to do if link is head
        if link == self.head:
            return
            
        # If link is tail, update tail
        if link == self.tail:
            self.tail = link.prev
            assert self.tail

        # Fix link connections
        if link.prev:
            link.prev.next = link.next
        if link.next:
            link.next.prev = link.prev

        # Move link to head
        link.next = self.head
        self.head.prev = link
        self.head = link
        link.prev = None
        self.debug("updateLru")
        
    def put(self, key: int, value: int) -> None:
        self.debug("put " + str(key))

        storedValue = self.store.get(key, -1)

        # Key is stored
        if storedValue != -1:
            # Update cache position
            self.updateLRU(storedValue)

            # Update data
            newStoredValue = self.Value(storedValue.link, value)
            self.store[key] = newStoredValue
            self.debug("put end " + str(key))
            return
        
        # Key is not stored

        # Evict if capacity is too high
        self.size += 1
        if self.size > self.capacity:
            # Delete from LRU linked list
            if self.tail and self.tail.prev:
                    self.tail.prev.next = None

            # Delete from store
            self.store.pop(self.tail.key)

            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            self.size -= 1

        # Add to LRU and store dict
        newLink = self.Link(key)
        self.store[key] = self.Value(newLink, value)
        
        # Update LRU head
        if self.head:
            self.head.prev = newLink
            newLink.next = self.head
            self.head = newLink
        else:
            self.head = newLink
            self.tail = newLink
            assert self.tail

        self.debug("put end " + str(key))

        
    
       






        
