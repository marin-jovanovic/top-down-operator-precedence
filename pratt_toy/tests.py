"""test suite"""
from ast import literal_eval
import os
import subprocess
import unittest


class TestMain(unittest.TestCase):
    """test class"""

    @staticmethod
    def execute(arguments=""):
        """function copied from https://github.com/zoranmedic/autograder"""

        max_time = 10  # seconds
        ex_cmd = "py main.py"
        command = ex_cmd + " " + arguments

        try:

            result = subprocess.check_output(
                command,
                stderr=subprocess.STDOUT,
                timeout=max_time,
                env={**os.environ.copy(), "PYTHONUTF8": "1"},
            )

        except subprocess.CalledProcessError as e_cp:
            error_message = e_cp.output.decode("utf-8")
            return "ERR_EXECUTE", error_message, command

        except subprocess.TimeoutExpired:
            return "ERR_TIMEOUT", None, command

        result = result.decode("utf-8").strip()

        return result

    def test_00(self):
        """test 00"""

        output = self.execute('"1 + 2"')
        output = literal_eval(output)

        self.assertEqual(output, ["+", "1", "2"])

    def test_01(self):
        """test 01"""

        output = self.execute('"2 + 3 + 4"')
        output = literal_eval(output)

        self.assertEqual(output, ["+", ["+", "2", "3"], "4"])

    def test_02(self):
        """test 02"""

        output = self.execute('"2 + 3 * 5"')
        output = literal_eval(output)

        self.assertEqual(output, ["+", "2", ["*", "3", "5"]])

    def test_03(self):
        """test 03"""

        output = self.execute('"2 + 3 * 4 * 5"')
        output = literal_eval(output)

        self.assertEqual(output, ["+", "2", ["*", ["*", "3", "4"], "5"]])

    def test_04(self):
        """test 04"""

        output = self.execute('"2 * 3 + 4 * 5"')
        output = literal_eval(output)

        self.assertEqual(output, ["+", ["*", "2", "3"], ["*", "4", "5"]])

    def test_05(self):
        """test 05"""

        output = self.execute('"1 / 2"')
        output = literal_eval(output)

        self.assertEqual(output, ["/", "1", "2"])

    def test_06(self):
        """test 06"""

        output = self.execute('"1 / 2 / 3 * 4"')
        output = literal_eval(output)

        self.assertEqual(output, ["*", ["/", ["/", "1", "2"], "3"], "4"])

    def test_07(self):
        """test 07"""

        output = self.execute('"1 + 2 / 2 * 4 + 5 / 3 + 6 * 4"')
        output = literal_eval(output)

        self.assertEqual(
            output,
            [
                "+",
                ["+", ["+", "1", ["*", ["/", "2", "2"], "4"]], ["/", "5", "3"]],
                ["*", "6", "4"],
            ],
        )

    def test_08(self):
        """test 08"""

        output = self.execute('"1 - 2"')
        output = literal_eval(output)

        self.assertEqual(output, ["-", "1", "2"])

    def test_09(self):
        """test 09"""

        output = self.execute('"1 - 2 - 3"')
        output = literal_eval(output)

        self.assertEqual(output, ["-", ["-", "1", "2"], "3"])

    def test_10(self):
        """test 10"""

        output = self.execute('"3 * ( 2 + - 4 ) ^ 4"')
        output = literal_eval(output)

        self.assertEqual(
            output, ["*", "3", ["**", ["(", ["+", "2", ["-", "4"]], ")"], "4"]]
        )

    def test_11(self):
        """test 11"""

        output = self.execute('"2 + ( ( 3 ) + ( ( 2 - 4 ) + 3 ) ) + 1"')
        output = literal_eval(output)

        self.assertEqual(
            output,
            [
                "+",
                [
                    "+",
                    "2",
                    [
                        "(",
                        [
                            "+",
                            ["(", "3", ")"],
                            ["(", ["+", ["(", ["-", "2", "4"], ")"], "3"], ")"],
                        ],
                        ")",
                    ],
                ],
                "1",
            ],
        )

    def test_12(self):
        """test 12"""

        output = self.execute('"sin ( 1 ) + 2"')
        output = literal_eval(output)

        self.assertEqual(output, ["+", ["sin", "(", "1", ")"], "2"])

    def test_13(self):
        """test 13"""

        output = self.execute('"1 - cos ( 3 + 1 )"')
        output = literal_eval(output)

        self.assertEqual(output, ["-", "1", ["cos", "(", ["+", "3", "1"], ")"]])

    def test_14(self):
        """test 14"""

        output = self.execute('"1 - cos ( alpha + beta + 2 )"')
        output = literal_eval(output)

        self.assertEqual(
            output, ["-", "1", ["cos", "(", ["+", ["+", "alpha", "beta"], "2"], ")"]]
        )

    def test_15(self):
        """test 15"""

        output = self.execute('"1 - x != 5 + p"')
        output = literal_eval(output)

        self.assertEqual(output, ["!=", ["-", "1", "x"], ["+", "5", "p"]])

    def test_16(self):
        """test 16"""

        output = self.execute('"( 2 )"')
        output = literal_eval(output)

        self.assertEqual(output, ["(", "2", ")"])

    def test_17(self):
        """test 17"""

        output = self.execute('"[ j * ( 7 + l ) + f ]"')
        output = literal_eval(output)

        self.assertEqual(
            output, ["[", ["+", ["*", "j", ["(", ["+", "7", "l"], ")"]], "f"], "]"]
        )

    def test_18(self):
        """test 18"""

        output = self.execute(
            '"1 - x + 2 * cos ( 2 ) != 5 + { m - [ j * ( 7 + l ) + f ] / h } + p"'
        )
        output = literal_eval(output)

        self.assertEqual(
            output,
            [
                "!=",
                ["+", ["-", "1", "x"], ["*", "2", ["cos", "(", "2", ")"]]],
                [
                    "+",
                    [
                        "+",
                        "5",
                        [
                            "{",
                            [
                                "-",
                                "m",
                                [
                                    "/",
                                    [
                                        "[",
                                        [
                                            "+",
                                            ["*", "j", ["(", ["+", "7", "l"], ")"]],
                                            "f",
                                        ],
                                        "]",
                                    ],
                                    "h",
                                ],
                            ],
                            "}",
                        ],
                    ],
                    "p",
                ],
            ],
        )

    def test_19(self):
        """test 19"""

        output = self.execute('"true != false"')
        output = literal_eval(output)

        self.assertEqual(output, ["!=", "true", "false"])

    def test_20(self):
        """test 20"""

        output = self.execute('"2 == 2 ? x : y"')
        output = literal_eval(output)

        self.assertEqual(output, ["?", ["==", "2", "2"], "x", ":", "y"])

    def test_21(self):
        """test 21"""

        output = self.execute('"2 == 1 + 1 ? x + 1 : y + 7"')
        output = literal_eval(output)

        self.assertEqual(
            output,
            ["?", ["==", "2", ["+", "1", "1"]], ["+", "x", "1"], ":", ["+", "y", "7"]],
        )

    def test_22(self):
        """test 22"""

        output = self.execute('"4 != 2 + x ? a : b"')
        output = literal_eval(output)

        self.assertEqual(output, ["?", ["!=", "4", ["+", "2", "x"]], "a", ":", "b"])

    def test_23(self):
        """test 23"""

        output = self.execute('"a ? b : c ? d : e"')
        output = literal_eval(output)

        self.assertEqual(output, ["?", "a", "b", ":", ["?", "c", "d", ":", "e"]])

    def test_24(self):
        """test 24"""

        output = self.execute('"if a then b"')
        output = literal_eval(output)

        self.assertEqual(output, ["if", "a", "then", "b"])

    def test_25(self):
        """test 25"""

        output = self.execute('"if a then b else c"')
        output = literal_eval(output)

        self.assertEqual(output, ["if", "a", "then", "b", "else", "c"])

    def test_26(self):
        """test 26"""

        output = self.execute('"if a then if b then c"')
        output = literal_eval(output)

        self.assertEqual(output, ["if", "a", "then", ["if", "b", "then", "c"]])

    def test_27(self):
        """test 27"""

        output = self.execute('"if a then if b then c else d"')
        output = literal_eval(output)

        self.assertEqual(
            output, ["if", "a", "then", ["if", "b", "then", "c", "else", "d"]]
        )

    def test_28(self):
        """test 28"""

        output = self.execute('"if a then if b then c else d else f"')
        output = literal_eval(output)

        self.assertEqual(
            output,
            ["if", "a", "then", ["if", "b", "then", "c", "else", "d"], "else", "f"],
        )

    def test_29(self):
        """test 29"""

        output = self.execute('"if a then if b then c else d else if e then f else g"')
        output = literal_eval(output)

        self.assertEqual(
            output,
            [
                "if",
                "a",
                "then",
                ["if", "b", "then", "c", "else", "d"],
                "else",
                ["if", "e", "then", "f", "else", "g"],
            ],
        )

    def test_30(self):
        """test 30"""

        output = self.execute('"if x + 1 == a + b then a else c"')
        output = literal_eval(output)

        self.assertEqual(
            output,
            ["if", ["==", ["+", "x", "1"], ["+", "a", "b"]], "then", "a", "else", "c"],
        )

    def test_31(self):
        """test 31"""

        output = self.execute('"if x + 1 == a + b then a + m + sin ( x ) else c + d"')
        output = literal_eval(output)

        self.assertEqual(
            output,
            [
                "if",
                ["==", ["+", "x", "1"], ["+", "a", "b"]],
                "then",
                ["+", ["+", "a", "m"], ["sin", "(", "x", ")"]],
                "else",
                ["+", "c", "d"],
            ],
        )

    def test_32(self):
        """test 32"""

        output = self.execute(
            '"if x + 1 == a + b then if a == m then sin ( x ) else c else if x then a else b"'
        )
        output = literal_eval(output)

        self.assertEqual(
            output,
            [
                "if",
                ["==", ["+", "x", "1"], ["+", "a", "b"]],
                "then",
                ["if", ["==", "a", "m"], "then", ["sin", "(", "x", ")"], "else", "c"],
                "else",
                ["if", "x", "then", "a", "else", "b"],
            ],
        )

    def test_33(self):
        """test 33"""

        output = self.execute('"if x + 1 == a + b then a"')
        output = literal_eval(output)

        self.assertEqual(
            output, ["if", ["==", ["+", "x", "1"], ["+", "a", "b"]], "then", "a"]
        )

    def test_34(self):
        """test 34"""

        output = self.execute('"if x + 1 == a + b + sin ( x ) then a + b + ( a + d )"')
        output = literal_eval(output)

        self.assertEqual(
            output,
            [
                "if",
                ["==", ["+", "x", "1"], ["+", ["+", "a", "b"], ["sin", "(", "x", ")"]]],
                "then",
                ["+", ["+", "a", "b"], ["(", ["+", "a", "d"], ")"]],
            ],
        )

    def test_35(self):
        """test 35"""

        output = self.execute('"3 * ( 2 + - 4 ) ^ 4 ^ 5 ^ 6"')
        output = literal_eval(output)

        self.assertEqual(
            output,
            [
                "*",
                "3",
                [
                    "**",
                    ["(", ["+", "2", ["-", "4"]], ")"],
                    ["**", "4", ["**", "5", "6"]],
                ],
            ],
        )

    def test_36(self):
        """test 36"""

        output = self.execute('"( 1 - ( - 2 * 3 )"')
        output = literal_eval(output)

        self.assertEqual(
            output, ["(", ["-", "1", ["(", ["*", ["-", "2"], "3"], ")"]], "err )"]
        )

    def test_37(self):
        """test 37"""

        output = self.execute('"sin x + 1 )"')
        output = literal_eval(output)

        self.assertEqual(output, ["sin", "err (", ["+", "x", "1"], ")"])


if __name__ == "__main__":
    unittest.main()
