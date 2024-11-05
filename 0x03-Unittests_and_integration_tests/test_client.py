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


if __name__ == "__main__":
    unittest.main()
