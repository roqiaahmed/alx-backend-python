#!/usr/bin/env python3

"""
Parameterize a unit test
"""
import unittest
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch
from unittest.mock import PropertyMock


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

    def test_public_repos_url(self):
        """
        test_public_repos_url
        """
        with patch.object(
            GithubOrgClient,
            "org",
            new_callable=PropertyMock,
            return_value={"repos_url": "testURL"},
        ) as mock_get:
            client_json = {"repos_url": "testURL"}
            client_repos_url = GithubOrgClient(client_json.get("repos_url"))
            res = client_repos_url._public_repos_url
            self.assertEqual(res, mock_get.return_value.get("repos_url"))
            mock_get.assert_called_once
