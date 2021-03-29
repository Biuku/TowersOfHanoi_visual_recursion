""" March 29, 2021 """

class Stack:
    def __init__(self):
        self.stack = []


    def add_ring(self, ring):
        self.stack.insert(0, ring)


    def pop_ring(self):
        ring = self.stack.pop(0)
        return ring


    def get_top_ring_size(self):
        if self.stack:
            return self.stack[0].getsize()

        return self.set.ring_max_w

    def get_num_rings(self):
        return len(self.stack)
