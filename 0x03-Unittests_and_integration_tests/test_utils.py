#!/usr/bin/env python3

"""
module test
"""

import unittest

from parameterized import parameterized
from utils import access_nested_map


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
