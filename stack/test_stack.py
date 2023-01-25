import unittest
from implement_stack import Stack

class TestStack(unittest.TestCase):
    
    def setUp(self):
        self.stack = Stack()
    
    def test_is_empty(self):
        # self.assertTrue(self.stack.is_empty())
        self.assertEqual(self.stack.is_empty(), True)
        self.stack.push(1)
        # self.assertFalse(self.stack.is_empty())
        self.assertEqual(self.stack.is_empty(), False)

    def test_push(self):
        self.stack.push(31)
        self.stack.push("31")
        self.stack.push("python")
        self.assertEqual(self.stack.peek(), "python")
        self.assertEqual(self.stack.size(), 3)
    
    def test_pop(self):
        self.stack.push(31)
        self.stack.push("31")
        self.stack.push("python")
        self.assertEqual(self.stack.pop(), "python")
        self.assertEqual(self.stack.pop(), "31")
        self.assertEqual(self.stack.pop(), 31)

    def test_peek(self):
        self.stack.push(10)
        self.stack.push(20)
        self.stack.push(30)
        self.assertEqual(self.stack.peek(), 30)
        self.stack.pop()
        self.assertEqual(self.stack.peek(), 20)

    def test_size(self):
        self.stack.push(10)
        self.stack.push(20)
        self.stack.push(30)
        self.assertEqual(self.stack.size(), 3)
        self.stack.pop()
        self.assertEqual(self.stack.size(), 2)


if __name__ == '__main__':
    unittest.main()
