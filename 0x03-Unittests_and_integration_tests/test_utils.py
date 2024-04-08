#!/usr/bin/env python3
""" Module that test utils file
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ Representation of class TestAccessNestedMap
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_output):
        """ Tests for access nested map
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_output)
