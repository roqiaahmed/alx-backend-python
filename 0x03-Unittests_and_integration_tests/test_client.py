#!/usr/bin/env python3

"""
Parameterize a unit test
"""
import unittest
from client import GithubOrgClient
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from unittest.mock import patch


class TestGithubOrgClient(unittest.TestCase):
    """
    TestGithubOrgClient class
    """

    @parameterized.expand(
        [
            ("http://google.com", {"payload": True}),
            ("http://abc.com", {"payload": False}),
        ]
    )
    @patch("test_client.get_json")
    def test_org(self, url, pay_load, mock_get):
        """
        test_org
        """
        mock_get.return_value = pay_load
        get_json(url)
        mock_get.assert_called_once()
