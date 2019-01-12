import glob
import os
import unittest
import typing

from parameterized import parameterized

from oqp.parsers.openqasm.openqasm import parser as openqasm_parser


def _get_test_files() -> typing.Iterable[typing.Tuple[str, ...]]:
    here = os.path.dirname(os.path.abspath(__file__))
    files = glob.glob(os.path.join(here, "examples/**.qasm"), recursive=True)
    return files


def _custom_name_func(testcase_func, param_num, param):

    here = os.path.dirname(os.path.abspath(__file__))
    example_directory = os.path.join(here, "examples")
    test_filepath = param.args[0]
    relative_filepath = test_filepath[len(example_directory) + 1 :]

    return "{}_{}".format(
        testcase_func.__name__,
        parameterized.to_safe_name(relative_filepath.replace("/", "_")),
    )


class OpenQASMParserTestCase(unittest.TestCase):
    @parameterized.expand(_get_test_files(), name_func=_custom_name_func)
    def test_parsing(self, test_file: str):
        with open(test_file, "r") as f:
            _ = openqasm_parser.parse(f.read() + "\n")


if __name__ == "__main__":
    unittest.main()
