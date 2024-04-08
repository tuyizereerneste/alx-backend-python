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
    """ Representation of TestMonize class
    """
    def test_memoize(self):
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        test_instance = TestClass()
        with patch.object(
                TestClass,
                'a_method',
                return_value=lambda: 42) as mock_a_method:
            test_instance = TestClass()
            result1 = test_instance.a_property()
            result2 = test_instance.a_property()
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_a_method.assert_called_once()
