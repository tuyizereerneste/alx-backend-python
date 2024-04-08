#!/usr/bin/env python3
""" Module for GithubOrgClient.org
"""

import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, Mock, MagicMock, PropertyMock
from client import GithubOrgClient
from typing import Dict


class TestGithubOrgClient(unittest.TestCase):
    """ Representation of TestGithubOrgClient class
    """
    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
        ])
    @patch(
            "client.get_json",
            )
    def test_org(
            self,
            org: str,
            response: Dict,
            mocked_func: MagicMock) -> None:
        """Function that Tests the `org` method.
        """
        mocked_func.return_value = MagicMock(return_value=response)
        github_org_client = GithubOrgClient(org)
        self.assertEqual(github_org_client.org(), response)
        mocked_func.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org)
        )
