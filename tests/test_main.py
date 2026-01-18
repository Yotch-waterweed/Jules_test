import unittest
import sys
import os

# Add the 'src' directory to the Python path to allow for package-less imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.main import add

class TestMain(unittest.TestCase):

    def test_add(self):
        """Test the add function with various inputs."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(100, 200), 300)
        self.assertEqual(add(-5, -10), -15)

if __name__ == '__main__':
    unittest.main()
