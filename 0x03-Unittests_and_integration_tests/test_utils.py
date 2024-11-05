#!/usr/bin/env python3
"""Unit tests for memoize decorator in utils.py"""

import unittest
from unittest.mock import patch
from utils import memoize


class TestMemoize(unittest.TestCase):
    """Test cases for the memoize decorator"""

    class TestClass:
        """Test class for memoize decorator"""

        def a_method(self):
            """Method that returns 42"""
            return 42

        @memoize
        def a_property(self):
            """Memoized property calling a_method"""
            return self.a_method()

    def test_memoize(self):
        """Test memoize only calls a_method once on
        repeated access to a_property"""
        test_instance = self.TestClass()

        with patch.object(
            test_instance, 'a_method', return_value=42
        ) as mock_method:
            # Call a_property twice
            result_first_call = test_instance.a_property
            result_second_call = test_instance.a_property

            # Check that a_method is called once and result is correct
            mock_method.assert_called_once()
            self.assertEqual(result_first_call, 42)
            self.assertEqual(result_second_call, 42)


if __name__ == "__main__":
    unittest.main()
