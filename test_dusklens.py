# test_dusklens.py
"""
Tests for DuskLens module.
"""

import unittest
from dusklens import DuskLens

class TestDuskLens(unittest.TestCase):
    """Test cases for DuskLens class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DuskLens()
        self.assertIsInstance(instance, DuskLens)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DuskLens()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
