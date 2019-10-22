#Beginning of messing around with unit testing
#Hunter Anderson 10/17/2019

import unittest
from structures.queue import Queue

class TestStackMethods(unittest.TestCase):

    def test_enqueue(self):
        """
        Test enqueue() and make sure item is put on queue
        """
        a = Queue()
        a.enqueue(4)
        self.assertEqual(len(a), 1)
        for i in range(1, 5):
            a.enqueue(str(i))
            self.assertEqual(len(a), i+1)

    def test_dequeue(self):
        """
        Test dequeue() and make sure item is removed from queue and returned
        """
        a = Queue()
        for i in range(1,4):
            a.enqueue(str(i))
        for j in range(1,4):
            self.assertEqual(a.dequeue(), str(j))
            self.assertEqual(len(a), 3-j)

    def test_isEmpty(self):
        a = Queue()
        self.assertTrue(a.isEmpty())
        a.enqueue(4)
        self.assertFalse(a.isEmpty())
        a.enqueue(5)
        self.assertFalse(a.isEmpty())
        a.dequeue()
        a.dequeue()
        self.assertTrue(a.isEmpty())

    def test_top(self):
        a = Queue()
        a.enqueue("abc")
        self.assertTrue(a.top(), "abc")
        a.enqueue("foo")
        self.assertTrue(a.top(), "foo")

    def test_len(self):
        a = Queue()
        self.assertEqual(len(a), 0)
        for i in range(10):
            a.enqueue(i)
            self.assertEqual(len(a), i+1)

if __name__ == "__main__":
    unittest.main()
