#crude implementation of a queue
#10/17/2019 - Hunter Anderson

class Queue:
    def __init__(self):
        self._array = []
        self._len = 0

    def enqueue(self, element):
        """
        Inserts element at the end of the queue
        """
        self._array.append(element)
        self._len += 1
        return

    def dequeue(self):
        """
        Removes an element from the start of the queue
        """
        if self._len != 0:
            t = self._array[0]
            self._array = self._array[1:]
            self._len -= 1
            return t

    def isEmpty(self):
        """
        Returns true if queue is empty
        """
        return True if self._len is 0 else False

    def top(self):
        """
        Returns the top of queue without removing it
        """
        if self._len != 0:
            return self._array[0]

    def __len__(self):
        """
        Returns length of queue
        """
        return self._len
