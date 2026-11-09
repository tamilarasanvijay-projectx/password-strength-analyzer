"""Basic unit tests for password_checker.py."""

import unittest

from password_checker import analyze_password


class PasswordAnalyzerTests(unittest.TestCase):
    def test_very_strong_password(self):
        score, strength, suggestions = analyze_password("A-LongExample!9284")
        self.assertEqual(score, 6)
        self.assertEqual(strength, "VERY STRONG")
        self.assertEqual(suggestions, [])

    def test_short_password_is_weak(self):
        _, strength, suggestions = analyze_password("abc")
        self.assertEqual(strength, "WEAK")
        self.assertTrue(suggestions)

    def test_password_with_some_requirements_is_medium(self):
        _, strength, _ = analyze_password("Hello123")
        self.assertEqual(strength, "MEDIUM")


if __name__ == "__main__":
    unittest.main()
