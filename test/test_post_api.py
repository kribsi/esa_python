# coding: utf-8

"""
    Secure Email Gateway API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.post_api import PostApi  # noqa: E501
from swagger_client.rest import ApiException


class TestPostApi(unittest.TestCase):
    """PostApi unit test stubs"""

    def setUp(self):
        self.api = PostApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_esa_api_v20_config_local_quarantines_post(self):
        """Test case for esa_api_v20_config_local_quarantines_post

        add pvo quarantine  # noqa: E501
        """
        pass

    def test_esa_api_v20_quarantine_blocklist_post(self):
        """Test case for esa_api_v20_quarantine_blocklist_post

        Add, edit and append Blocklist entries  # noqa: E501
        """
        pass

    def test_esa_api_v20_quarantine_messages_post(self):
        """Test case for esa_api_v20_quarantine_messages_post

        Release messages that match various attribute  # noqa: E501
        """
        pass

    def test_esa_api_v20_quarantine_messages_rules_post(self):
        """Test case for esa_api_v20_quarantine_messages_rules_post

        Release messages from the rule summary that match multiple attributes  # noqa: E501
        """
        pass

    def test_esa_api_v20_quarantine_safelist_post(self):
        """Test case for esa_api_v20_quarantine_safelist_post

        Add, edit and append Safelist entries  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
