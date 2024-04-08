#!/usr/bin/env python3
""" Module that test utils file
"""

import unittest
import requests
from parameterized import parameterized
from utils import access_nested_map
from utils import get_json
from utils import memoize
from unittest.mock import patch, Mock


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

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
        ])
    def test_access_nested_map_exception(
                                         self,
                                         nested_map,
                                         path,
                                         expected_output
                                         ):
        """ Tests if the function raises exception
        """
        with self.assertRaises(expected_output):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ Representation of the TestGetJson class
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """ Function that tests get_json output
        """
        att = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**att)) as request_get:
            self.assertEqual(get_json(test_url), test_payload)
            request_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Representation of TestMemoize class
    """
    def test_memoize(self) -> None:
        """Tests `memoize`'s output."""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        test_instance = TestClass()
        with patch.object(
                test_instance,
                "a_method",
                return_value=lambda: 42,
                ) as memoize_fun:
            self.assertEqual(test_instance.a_property(), 42)
            self.assertEqual(test_instance.a_property(), 42)
            memoize_fun.assert_called_once()
