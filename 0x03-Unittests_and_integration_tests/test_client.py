from unittest.mock import patch
from parameterized import parameterized
import unittest
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient class"""

    @parameterized.expand([
    ({"license": {"key": "my_license"}}, "my_license", True),
    ({"license": {"key": "other_license"}}, "my_license", False),
])
    def test_has_license(self, repo, license_key, expected):
        """Test that has_license returns the expected value."""
        client = GithubOrgClient("google")
    
    # Mock the public_repos method to return the provided repo
        with patch.object(client, "public_repos", return_value=[repo]):
            # Call the has_license method
            result = client.has_license(license_key)

            # Assert the result is as expected
            self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
