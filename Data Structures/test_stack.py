#Beginning of messing around with unit testing
#Hunter Anderson 10/17/2019

import unittest
from structures.stack import Stack

class TestStackMethods(unittest.TestCase):

    def test_push(self):
        a = Stack()
        self.assertTrue(a.push(4))
        self.assertTrue(a.push(6))
        self.assertTrue(a.push("foo"))

    def test_top(self):
        a = Stack()
        a.push(5)
        self.assertEqual(a.top(), 5)
        a.push(9)
        self.assertEqual(a.top(), 9)
        a.push("foo")
        self.assertEqual(a.top(), "foo")

    def test_pop(self):
        a = Stack()
        a.push(5)
        self.assertEqual(a.pop(), 5)
        a.push(4)
        a.push(8)
        self.assertEqual(a.pop(), 8)
        self.assertEqual(a.pop(), 4)

    def test_isEmpty(self):
        a = Stack()
        self.assertTrue(a.isEmpty())
        a.push(5)
        self.assertFalse(a.isEmpty())
        a.push(5)
        self.assertFalse(a.isEmpty())
        a.pop()
        a.pop()
        self.assertTrue(a.isEmpty())

if __name__ == "__main__":
    unittest.main()
