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
from swagger_client.api.delete_api import DeleteApi  # noqa: E501
from swagger_client.rest import ApiException


class TestDeleteApi(unittest.TestCase):
    """DeleteApi unit test stubs"""

    def setUp(self):
        self.api = DeleteApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_esa_api_v20_config_local_quarantines_quarantine_name_delete(self):
        """Test case for esa_api_v20_config_local_quarantines_quarantine_name_delete

        delete pvo quarantine  # noqa: E501
        """
        pass

    def test_esa_api_v20_quarantine_blocklist_delete(self):
        """Test case for esa_api_v20_quarantine_blocklist_delete

        Delete blocklist entries  # noqa: E501
        """
        pass

    def test_esa_api_v20_quarantine_messages_delete(self):
        """Test case for esa_api_v20_quarantine_messages_delete

        Delete messages that match various attribute  # noqa: E501
        """
        pass

    def test_esa_api_v20_quarantine_messages_rules_delete(self):
        """Test case for esa_api_v20_quarantine_messages_rules_delete

        Delete messages from the rule summary that match multiple attributes  # noqa: E501
        """
        pass

    def test_esa_api_v20_quarantine_safelist_delete(self):
        """Test case for esa_api_v20_quarantine_safelist_delete

        Delete safelist entries  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
