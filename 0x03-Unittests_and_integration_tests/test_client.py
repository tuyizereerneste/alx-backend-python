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

    def test_public_repos_url(self):
        """Function that Tests the `_public_repos_url` property.
        """
        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock,
                ) as mock_org:
            mock_org.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )

    @parameterized.expand([
        ({'license': {'key': "bsd-3-clause"}}, "bsd-3-clause", True),
        ({'license': {'key': "bsl-1.0"}}, "bsd-3-clause", False),
    ])
    def test_has_license(self, repo: Dict, key: str, expected: bool) -> None:
        """Function that Tests the has_license method.
        """
        github_org_client = GithubOrgClient("google")
        client_has_licence = github_org_client.has_license(repo, key)
        self.assertEqual(client_has_licence, expected)
