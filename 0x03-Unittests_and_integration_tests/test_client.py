#!/usr/bin/env python3

"""
Parameterize a unit test
"""
import unittest
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch


class TestGithubOrgClient(unittest.TestCase):
    """
    TestGithubOrgClient class
    """

    @parameterized.expand(
        [
            ("google"),
            ("abc"),
        ]
    )
    @patch("client.get_json")
    def test_org(self, url, mock_get):
        """
        test_org
        """
        res = GithubOrgClient(url)
        res.org
        mock_get.assert_called_once()
