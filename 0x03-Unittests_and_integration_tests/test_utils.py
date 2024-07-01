#!/usr/bin/env python3
"""Implement unittests and Integration Tests"""
from parameterized import parameterized
import unittest
from utils import (access_nested_map, get_json, memoize)
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """Implement unittests and Integration Tests"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Implement unittests and Integration Tests"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """Implement unittests and Integration Tests"""
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError('{expected}')", repr(e.exception))


class TestGetJson(unittest.TestCase):
    """Implement unittests and Integration Tests"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """Implement unittests and Integration Tests"""
        temp_1 = {'return_value.json.return_value': test_payload}
        temp_2 = patch('requests.get', **temp_1)
        mock = temp_2.start()
        self.assertEqual(get_json(test_url), test_payload)
        mock.assert_called_once()
        temp_2.stop()


class TestMemoize(unittest.TestCase):
    """Implement unittests and Integration Tests"""
    def test_memoize(self):
        """Implement unittests and Integration Tests"""
        class TestClass:
            """Implement unittests and Integration Tests"""

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock:
            temp_4 = TestClass()
            temp_4.a_property()
            temp_4.a_property()
            mock.assert_called_once()
