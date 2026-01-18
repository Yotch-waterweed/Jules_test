import unittest
import sys
import os

<<<<<<< HEAD
# Add the 'src' directory to the Python path to allow for package-less imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.main import add
=======
# Add the 'src' directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.main import add, multiply
>>>>>>> feat/initial-project-structure-797294041455331580

class TestMain(unittest.TestCase):

    def test_add(self):
<<<<<<< HEAD
        """Test the add function with various inputs."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(100, 200), 300)
        self.assertEqual(add(-5, -10), -15)
=======
        """Test the add function."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_multiply(self):
        """Test the multiply function."""
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(0, 100), 0)
        self.assertEqual(multiply(3, -4), -12)
>>>>>>> feat/initial-project-structure-797294041455331580

if __name__ == '__main__':
    unittest.main()
