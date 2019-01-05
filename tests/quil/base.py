import glob
import os
import unittest

from oqp.parsers.quil.quil import parser as quil_parser


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.here = os.path.dirname(os.path.abspath(__file__))

    def test_parsing(self):
        examples = glob.glob(
            os.path.join(self.here, "examples/**/*.quil"), recursive=True
        )
        for test_file in examples:
            with open(test_file, "r") as f:
                print("Parsing {}.".format(test_file))
                tree = quil_parser.parse(f.read() + "\n")


if __name__ == "__main__":
    unittest.main()
