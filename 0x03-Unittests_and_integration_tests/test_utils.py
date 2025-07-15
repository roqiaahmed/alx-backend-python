#!/usr/bin/env python3

"""
module test
"""

import unittest
from unittest.mock import patch


from parameterized import parameterized
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """
    test a access_nested_map function
    """

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected):
        """
        assert_equal(access_nested_map(nested_map, path), expected)
        """

        res = access_nested_map(nested_map, path)
        self.assertEqual(res, expected)

    @parameterized.expand(
        [
            ({}, ("a",), "a"),
            ({"a": 1}, ("a", "b"), "b"),
        ]
    )
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """
        except a KeyError is raised
        """

        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(error.exception.args[0], expected)


class TestGetJson(unittest.TestCase):
    """
    test class for get_json func

    """

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    def test_get_json(self, url, expected):
        """
        mock requests.get and return expected result
        """

        with patch("requests.get") as req_patch:
            req_patch.return_value.json.return_value = expected
            self.assertEqual(get_json(url), expected)

        req_patch.assert_called_once_with(url)
