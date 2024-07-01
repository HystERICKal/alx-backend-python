#!/usr/bin/env python3
"""Implement unittests and Integration Tests"""

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
import json
import unittest
from unittest.mock import patch, PropertyMock, Mock


class TestGithubOrgClient(unittest.TestCase):
    """Implement unittests and Integration Tests"""
    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, input, mock):
        """Implement unittests and Integration Tests"""
        temp_5 = GithubOrgClient(input)
        temp_5.org()
        mock.assert_called_once_with(f'https://api.github.com/orgs/{input}')

    def test_public_repos_url(self):
        """Implement unittests and Integration Tests"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            temp_7 = {"repos_url": "World"}
            mock.return_value = temp_7
            temp_5 = GithubOrgClient('test')
            temp_6 = temp_5._public_repos_url
            self.assertEqual(temp_6, temp_7["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """Implement unittests and Integration Tests"""
        temp_8 = [{"name": "Google"}, {"name": "Twitter"}]
        mock_json.return_value = temp_8

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public:

            mock_public.return_value = "hello/world"
            temp_5 = GithubOrgClient('test')
            temp_6 = temp_5.public_repos()

            temp_9 = [i["name"] for i in temp_8]
            self.assertEqual(temp_6, temp_9)

            mock_public.assert_called_once()
            mock_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Implement unittests and Integration Tests"""
        temp_6 = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(temp_6, expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Implement unittests and Integration Tests"""
    @classmethod
    def setUpClass(temp_11):
        """Implement unittests and Integration Tests"""
        temp_10 = {'return_value.json.side_effect':
                   [
                      temp_11.org_payload, temp_11.repos_payload,
                      temp_11.org_payload, temp_11.repos_payload
                   ]
                   }
        temp_11.get_patcher = patch('requests.get', **temp_10)

        temp_11.mock = temp_11.get_patcher.start()

    def test_public_repos(self):
        """Implement unittests and Integration Tests"""
        temp_5 = GithubOrgClient("google")
        self.assertEqual(temp_5.org, self.org_payload)
        self.assertEqual(temp_5.repos_payload, self.repos_payload)
        self.assertEqual(temp_5.public_repos(), self.expected_repos)
        self.assertEqual(temp_5.public_repos("XLICENSE"), [])
        self.mock.assert_called()

    def test_public_repos_with_license(self):
        """Implement unittests and Integration Tests"""
        temp_5 = GithubOrgClient("google")
        self.assertEqual(temp_5.public_repos(), self.expected_repos)
        self.assertEqual(temp_5.public_repos("XLICENSE"), [])
        self.assertEqual(temp_5.public_repos(
            "apache-2.0"), self.apache2_repos)
        self.mock.assert_called()

    @classmethod
    def tearDownClass(temp_11):
        """Implement unittests and Integration Tests"""
        temp_11.get_patcher.stop()
