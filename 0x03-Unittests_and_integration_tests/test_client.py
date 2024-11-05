#!/usr/bin/env python3
"""Unit tests for GithubOrgClient in client.py"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient class"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""
        # Setup expected return value
        test_payload = {"login": org_name}
        mock_get_json.return_value = test_payload

        # Instantiate client and call the org property
        client = GithubOrgClient(org_name)
        result = client.org

        # Assert get_json was called once with the correct URL
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )
        self.assertEqual(result, test_payload)

    def test_public_repos_url(self):
        """Test that _public_repos_url returns the expected
        URL from mocked payload"""
        test_payload = {"repos_url": "https://api.github.com/orgs/google/repos"}

        # Patch 'org' to return the test_payload dictionary directly
        with patch.object(GithubOrgClient, "org", return_value=test_payload):
            client = GithubOrgClient("google")
            result = client._public_repos_url

            # Assert that _public_repos_url matches the 'repos_url' in test_payload
            self.assertEqual(result, test_payload["repos_url"])

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """Test that public_repos returns the
        expected list of repositories"""
        # Mock response payload from get_json
        test_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"},
        ]
        mock_get_json.return_value = test_payload

        # Mock the _public_repos_url to avoid any real HTTP calls
        with patch.object(
            GithubOrgClient,
            "_public_repos_url",
            new="https://api.github.com/orgs/google/repos"
        ):
            client = GithubOrgClient("google")
            result = client.public_repos

            # Verify the returned list of repository names
            expected_repos = ["repo1", "repo2", "repo3"]
            self.assertEqual(result, expected_repos)

            # Check that _public_repos_url and get_json were each called once
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/google/repos"
            )


if __name__ == "__main__":
    unittest.main()
