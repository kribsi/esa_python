# coding: utf-8

"""
    Secure Email Gateway API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class PostApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def esa_api_v20_config_local_quarantines_post(self, body, **kwargs):  # noqa: E501
        """add pvo quarantine  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.esa_api_v20_config_local_quarantines_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConfigLocalQuarantinesBody body: Add pvo quarantine request body (required)
        :param str device_type:
        :return: ConfigLocalQuarantinesAddMessage
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.esa_api_v20_config_local_quarantines_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.esa_api_v20_config_local_quarantines_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def esa_api_v20_config_local_quarantines_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """add pvo quarantine  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.esa_api_v20_config_local_quarantines_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConfigLocalQuarantinesBody body: Add pvo quarantine request body (required)
        :param str device_type:
        :return: ConfigLocalQuarantinesAddMessage
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'device_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method esa_api_v20_config_local_quarantines_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `esa_api_v20_config_local_quarantines_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'device_type' in params:
            query_params.append(('device_type', params['device_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json, text/plain, */*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth', 'UserSecurity']  # noqa: E501

        return self.api_client.call_api(
            '/esa/api/v2.0/config/local_quarantines', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConfigLocalQuarantinesAddMessage',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def esa_api_v20_quarantine_blocklist_post(self, body, **kwargs):  # noqa: E501
        """Add, edit and append Blocklist entries  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.esa_api_v20_quarantine_blocklist_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param QuarantineBlocklistPostRequestBody body: Add, edit and append Blocklist entries request body (required)
        :return: QuarantineBlocklistPost
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.esa_api_v20_quarantine_blocklist_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.esa_api_v20_quarantine_blocklist_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def esa_api_v20_quarantine_blocklist_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Add, edit and append Blocklist entries  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.esa_api_v20_quarantine_blocklist_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param QuarantineBlocklistPostRequestBody body: Add, edit and append Blocklist entries request body (required)
        :return: QuarantineBlocklistPost
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method esa_api_v20_quarantine_blocklist_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `esa_api_v20_quarantine_blocklist_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json, text/plain, */*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth', 'UserSecurity']  # noqa: E501

        return self.api_client.call_api(
            '/esa/api/v2.0/quarantine/blocklist', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='QuarantineBlocklistPost',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def esa_api_v20_quarantine_messages_post(self, body, **kwargs):  # noqa: E501
        """Release messages that match various attribute  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.esa_api_v20_quarantine_messages_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param QuarantineMessagesBody body: Quarantine message release request body (required)
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.esa_api_v20_quarantine_messages_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.esa_api_v20_quarantine_messages_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def esa_api_v20_quarantine_messages_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Release messages that match various attribute  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.esa_api_v20_quarantine_messages_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param QuarantineMessagesBody body: Quarantine message release request body (required)
        :return: InlineResponse2002
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method esa_api_v20_quarantine_messages_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `esa_api_v20_quarantine_messages_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json, text/plain, */*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth', 'UserSecurity']  # noqa: E501

        return self.api_client.call_api(
            '/esa/api/v2.0/quarantine/messages', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2002',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def esa_api_v20_quarantine_messages_rules_post(self, body, **kwargs):  # noqa: E501
        """Release messages from the rule summary that match multiple attributes  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.esa_api_v20_quarantine_messages_rules_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param QuarantinePvoRulesReleaseRequestBody body: Release messages from the rule summary that match multiple attributes (required)
        :return: QuarantineMessagesRelease
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.esa_api_v20_quarantine_messages_rules_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.esa_api_v20_quarantine_messages_rules_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def esa_api_v20_quarantine_messages_rules_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Release messages from the rule summary that match multiple attributes  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.esa_api_v20_quarantine_messages_rules_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param QuarantinePvoRulesReleaseRequestBody body: Release messages from the rule summary that match multiple attributes (required)
        :return: QuarantineMessagesRelease
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method esa_api_v20_quarantine_messages_rules_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `esa_api_v20_quarantine_messages_rules_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json, text/plain, */*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth', 'UserSecurity']  # noqa: E501

        return self.api_client.call_api(
            '/esa/api/v2.0/quarantine/messages/rules', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='QuarantineMessagesRelease',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def esa_api_v20_quarantine_safelist_post(self, body, **kwargs):  # noqa: E501
        """Add, edit and append Safelist entries  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.esa_api_v20_quarantine_safelist_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param QuarantineSafelistPostRequestBody body: Add, edit and append Safelist entries request body (required)
        :return: QuarantineSafelistPost
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.esa_api_v20_quarantine_safelist_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.esa_api_v20_quarantine_safelist_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def esa_api_v20_quarantine_safelist_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Add, edit and append Safelist entries  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.esa_api_v20_quarantine_safelist_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param QuarantineSafelistPostRequestBody body: Add, edit and append Safelist entries request body (required)
        :return: QuarantineSafelistPost
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method esa_api_v20_quarantine_safelist_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `esa_api_v20_quarantine_safelist_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json, text/plain, */*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth', 'UserSecurity']  # noqa: E501

        return self.api_client.call_api(
            '/esa/api/v2.0/quarantine/safelist', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='QuarantineSafelistPost',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
