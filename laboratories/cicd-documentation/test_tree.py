import unittest
from tree import Tree

class TestTree(unittest.TestCase):

    def setUp(self):
        # Runs before each test
        self.tree = Tree()
        for value in [3, 4, 0, 8, 2]:
            self.tree.add(value)

    def test_find_existing(self):
        self.assertIsNotNone(self.tree.find(3))
        self.assertIsNotNone(self.tree.find(4))
        self.assertIsNotNone(self.tree.find(0))

    def test_find_missing(self):
        self.assertIsNone(self.tree.find(5))
        self.assertIsNone(self.tree.find(10))

    def test_print_tree(self):
        import io
        import sys

        captured = io.StringIO()
        sys_stdout = sys.stdout
        sys.stdout = captured

        try:
            self.tree.printTree()
        finally:
            sys.stdout = sys_stdout

        output = captured.getvalue().strip()

        self.assertTrue(len(output) > 0)  # placeholder test

if __name__ == '__main__':
    unittest.main()
