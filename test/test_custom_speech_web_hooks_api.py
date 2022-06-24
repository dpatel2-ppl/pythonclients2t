# coding: utf-8

"""
    Speech Services API v3.0

    Speech Services API v3.0.  # noqa: E501

    OpenAPI spec version: v3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.custom_speech_web_hooks_api import CustomSpeechWebHooksApi  # noqa: E501
from swagger_client.rest import ApiException


class TestCustomSpeechWebHooksApi(unittest.TestCase):
    """CustomSpeechWebHooksApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.custom_speech_web_hooks_api.CustomSpeechWebHooksApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_hook(self):
        """Test case for create_hook

        Creates a new web hook.  # noqa: E501
        """
        pass

    def test_delete_hook(self):
        """Test case for delete_hook

        Deletes the web hook identified by the given ID.  # noqa: E501
        """
        pass

    def test_get_hook(self):
        """Test case for get_hook

        Gets the web hook identified by the given ID.  # noqa: E501
        """
        pass

    def test_get_hooks(self):
        """Test case for get_hooks

        Gets the list of web hooks for the authenticated subscription.  # noqa: E501
        """
        pass

    def test_ping_hook(self):
        """Test case for ping_hook

        Sends a ping event to the registered URL.  # noqa: E501
        """
        pass

    def test_test_hook(self):
        """Test case for test_hook

        Sends a request for each registered event type to the registered URL.  # noqa: E501
        """
        pass

    def test_update_hook(self):
        """Test case for update_hook

        Updates the web hook identified by the given ID.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
