import unittest
from implement_queue import Queue

class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()
    
    def test_is_empty(self):
        self.assertEqual(self.queue.is_empty(), True)
        self.queue.enqueue(1)
        self.assertEqual(self.queue.is_empty(), False)
    
    def test_enqueue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(4)
        self.queue.enqueue(7)
        self.assertEqual(self.queue.length(), 3)
     
    def test_dequeue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(4)
        self.queue.enqueue(7)
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.dequeue(), 4)
        self.assertEqual(self.queue.dequeue(), 7)
    
    def test_length(self):
        self.queue.enqueue(1)
        self.queue.enqueue(4)
        self.queue.enqueue(7)
        self.assertEqual(self.queue.length(), 3)

    
if __name__ == '__main__':
    unittest.main()
