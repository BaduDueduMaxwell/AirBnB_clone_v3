#!/usr/bin/python3
""" Test .get() and .count() methods
"""
import unittest
from models import storage
from models.state import State

class TestStorageMethods(unittest.TestCase):
    def test_get(self):
        """Test the get method"""
        first_state = State(name="California")
        storage.new(first_state)
        storage.save()
        self.assertEqual(storage.get(State, first_state.id), first_state)

    def test_count(self):
        """Test the count method"""
        initial_count = storage.count()
        initial_count_state = storage.count(State)
        
        new_state = State(name="New York")
        storage.new(new_state)
        storage.save()
        
        self.assertEqual(storage.count(), initial_count + 1)
        self.assertEqual(storage.count(State), initial_count_state + 1)

if __name__ == "__main__":
    unittest.main()
