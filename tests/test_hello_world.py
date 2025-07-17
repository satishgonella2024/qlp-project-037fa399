import unittest
from io import StringIO
import sys
from src.hello_world import hello_world

class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        # Capture the output
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the hello_world function
        hello_world()

        # Reset the stdout
        sys.stdout = sys.__stdout__

        # Assert the output is correct
        self.assertEqual(captured_output.getvalue().strip(), "Hello, World!")

if __name__ == '__main__':
    unittest.main()