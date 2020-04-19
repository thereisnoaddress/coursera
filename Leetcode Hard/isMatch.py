"""
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
"""
import re
import unittest


def isMatch(s: str, p: str) -> bool:
        interpreter = re.compile(s)
        return True if interpreter.match(p) is not None else False


class TestReg(unittest.TestCase):
    def test_given_examples(self):
        self.assertEqual(isMatch("aa", "a"), False)
        self.assertEqual(isMatch("ab",".*"), True)
        self.assertEqual(isMatch("aab", "c*a*b"), True)
        self.assertEqual(isMatch("mississippi", "mis*is*p*"), False)

if __name__ == "__main__":
    unittest.main()
