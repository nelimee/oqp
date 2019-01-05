import os
import re
import typing

from lark import Lark, Tree

here = os.path.dirname(os.path.abspath(__file__))


class QuilParser(Lark):

    DEFAULT_INCLUDE_PATH = [
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "includes")
    ]

    INCLUDE_REGEX = re.compile(r"^include\s+\"([^\"]+)\"(?:\s*//.*)?$")

    def __init__(self, grammar, include_paths: typing.Iterable[str] = None, **options):
        super().__init__(grammar, **options)
        self._include_paths = (
            list(include_paths or []) + QuilParser.DEFAULT_INCLUDE_PATH
        )

    @classmethod
    def open(cls, grammar_filename, rel_to=None, **options) -> "QuilParser":
        if rel_to:
            basepath = os.path.dirname(rel_to)
            grammar_filename = os.path.join(basepath, grammar_filename)
        with open(grammar_filename, encoding="utf8") as f:
            return cls(f, **options)

    def parse(self, text: str) -> Tree:
        # text = self._replace_includes(text)
        return super().parse(text)

    def _replace_includes(self, text: str) -> str:

        match = re.search(QuilParser.INCLUDE_REGEX, text)
        while match:
            include_filename = match.group(1)
            include_replaced = False
            for include_path in self._include_paths:
                include_file_candidate = os.path.join(include_path, include_filename)
                if os.path.exists(include_file_candidate):
                    with open(include_file_candidate, "r") as include_file:
                        text = (
                            text[: match.start()]
                            + (
                                "// From included file '{}'\n".format(include_filename)
                                + include_file.read()
                                + "\n"
                                + "// End of included file '{}'\n".format(
                                    include_filename
                                )
                            )
                            + text[match.end() + 1 :]
                        )
                    include_replaced = True
                    break
            if not include_replaced:
                raise RuntimeError(
                    "Included file {} was not found.".format(include_filename)
                )
            match = re.search(QuilParser.INCLUDE_REGEX, text)
        return text


parser = QuilParser.open(
    os.path.join(here, "grammars", "quil.lark"), parser="earley", debug=True
)
