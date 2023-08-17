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


class ConfigApi(object):
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

    def esa_api_v20_config_local_quarantines_quarantine_name_delete(self, quarantine_name, **kwargs):  # noqa: E501
        """delete pvo quarantine  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.esa_api_v20_config_local_quarantines_quarantine_name_delete(quarantine_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str quarantine_name: (required)
        :param str device_type:
        :return: ConfigLocalQuarantinesDelete
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.esa_api_v20_config_local_quarantines_quarantine_name_delete_with_http_info(quarantine_name, **kwargs)  # noqa: E501
        else:
            (data) = self.esa_api_v20_config_local_quarantines_quarantine_name_delete_with_http_info(quarantine_name, **kwargs)  # noqa: E501
            return data

    def esa_api_v20_config_local_quarantines_quarantine_name_delete_with_http_info(self, quarantine_name, **kwargs):  # noqa: E501
        """delete pvo quarantine  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.esa_api_v20_config_local_quarantines_quarantine_name_delete_with_http_info(quarantine_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str quarantine_name: (required)
        :param str device_type:
        :return: ConfigLocalQuarantinesDelete
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['quarantine_name', 'device_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method esa_api_v20_config_local_quarantines_quarantine_name_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'quarantine_name' is set
        if ('quarantine_name' not in params or
                params['quarantine_name'] is None):
            raise ValueError("Missing the required parameter `quarantine_name` when calling `esa_api_v20_config_local_quarantines_quarantine_name_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'quarantine_name' in params:
            path_params['quarantine_name'] = params['quarantine_name']  # noqa: E501

        query_params = []
        if 'device_type' in params:
            query_params.append(('device_type', params['device_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json, text/plain, */*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth', 'UserSecurity']  # noqa: E501

        return self.api_client.call_api(
            '/esa/api/v2.0/config/local_quarantines/{quarantine_name}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConfigLocalQuarantinesDelete',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def esa_api_v20_config_local_quarantines_quarantine_name_get(self, quarantine_name, **kwargs):  # noqa: E501
        """get pvo quarantine details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.esa_api_v20_config_local_quarantines_quarantine_name_get(quarantine_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str quarantine_name: (required)
        :param str device_type:
        :return: ConfigLocalQuarantinesGet
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.esa_api_v20_config_local_quarantines_quarantine_name_get_with_http_info(quarantine_name, **kwargs)  # noqa: E501
        else:
            (data) = self.esa_api_v20_config_local_quarantines_quarantine_name_get_with_http_info(quarantine_name, **kwargs)  # noqa: E501
            return data

    def esa_api_v20_config_local_quarantines_quarantine_name_get_with_http_info(self, quarantine_name, **kwargs):  # noqa: E501
        """get pvo quarantine details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.esa_api_v20_config_local_quarantines_quarantine_name_get_with_http_info(quarantine_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str quarantine_name: (required)
        :param str device_type:
        :return: ConfigLocalQuarantinesGet
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['quarantine_name', 'device_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method esa_api_v20_config_local_quarantines_quarantine_name_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'quarantine_name' is set
        if ('quarantine_name' not in params or
                params['quarantine_name'] is None):
            raise ValueError("Missing the required parameter `quarantine_name` when calling `esa_api_v20_config_local_quarantines_quarantine_name_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'quarantine_name' in params:
            path_params['quarantine_name'] = params['quarantine_name']  # noqa: E501

        query_params = []
        if 'device_type' in params:
            query_params.append(('device_type', params['device_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json, text/plain, */*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth', 'UserSecurity']  # noqa: E501

        return self.api_client.call_api(
            '/esa/api/v2.0/config/local_quarantines/{quarantine_name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConfigLocalQuarantinesGet',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def esa_api_v20_config_local_quarantines_quarantine_name_put(self, body, quarantine_name, **kwargs):  # noqa: E501
        """edit pvo quarantine  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.esa_api_v20_config_local_quarantines_quarantine_name_put(body, quarantine_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LocalQuarantinesQuarantineNameBody body: Edit pvo quarantine request body (required)
        :param str quarantine_name: (required)
        :param str device_type:
        :return: ConfigLocalQuarantinesEditMessage
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.esa_api_v20_config_local_quarantines_quarantine_name_put_with_http_info(body, quarantine_name, **kwargs)  # noqa: E501
        else:
            (data) = self.esa_api_v20_config_local_quarantines_quarantine_name_put_with_http_info(body, quarantine_name, **kwargs)  # noqa: E501
            return data

    def esa_api_v20_config_local_quarantines_quarantine_name_put_with_http_info(self, body, quarantine_name, **kwargs):  # noqa: E501
        """edit pvo quarantine  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.esa_api_v20_config_local_quarantines_quarantine_name_put_with_http_info(body, quarantine_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LocalQuarantinesQuarantineNameBody body: Edit pvo quarantine request body (required)
        :param str quarantine_name: (required)
        :param str device_type:
        :return: ConfigLocalQuarantinesEditMessage
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'quarantine_name', 'device_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method esa_api_v20_config_local_quarantines_quarantine_name_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `esa_api_v20_config_local_quarantines_quarantine_name_put`")  # noqa: E501
        # verify the required parameter 'quarantine_name' is set
        if ('quarantine_name' not in params or
                params['quarantine_name'] is None):
            raise ValueError("Missing the required parameter `quarantine_name` when calling `esa_api_v20_config_local_quarantines_quarantine_name_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'quarantine_name' in params:
            path_params['quarantine_name'] = params['quarantine_name']  # noqa: E501

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
            '/esa/api/v2.0/config/local_quarantines/{quarantine_name}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConfigLocalQuarantinesEditMessage',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def esa_api_v20_config_logs_subscriptions_get(self, **kwargs):  # noqa: E501
        """Retrieve the details of all log subscriptions configured in your appliance  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.esa_api_v20_config_logs_subscriptions_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str retrieval_method:
        :return: ConfigLogSubscriptionsGet
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.esa_api_v20_config_logs_subscriptions_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.esa_api_v20_config_logs_subscriptions_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def esa_api_v20_config_logs_subscriptions_get_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve the details of all log subscriptions configured in your appliance  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.esa_api_v20_config_logs_subscriptions_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str retrieval_method:
        :return: ConfigLogSubscriptionsGet
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['retrieval_method']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method esa_api_v20_config_logs_subscriptions_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'retrieval_method' in params:
            query_params.append(('retrievalMethod', params['retrieval_method']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json, text/plain, */*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth', 'UserSecurity']  # noqa: E501

        return self.api_client.call_api(
            '/esa/api/v2.0/config/logs/subscriptions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConfigLogSubscriptionsGet',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def esa_api_v20_config_quarantine_filters_quarantine_name_get(self, quarantine_name, **kwargs):  # noqa: E501
        """get quarantine users  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.esa_api_v20_config_quarantine_filters_quarantine_name_get(quarantine_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str quarantine_name: (required)
        :param str device_type:
        :return: ConfigLocalQuarantinesFilters
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.esa_api_v20_config_quarantine_filters_quarantine_name_get_with_http_info(quarantine_name, **kwargs)  # noqa: E501
        else:
            (data) = self.esa_api_v20_config_quarantine_filters_quarantine_name_get_with_http_info(quarantine_name, **kwargs)  # noqa: E501
            return data

    def esa_api_v20_config_quarantine_filters_quarantine_name_get_with_http_info(self, quarantine_name, **kwargs):  # noqa: E501
        """get quarantine users  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.esa_api_v20_config_quarantine_filters_quarantine_name_get_with_http_info(quarantine_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str quarantine_name: (required)
        :param str device_type:
        :return: ConfigLocalQuarantinesFilters
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['quarantine_name', 'device_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method esa_api_v20_config_quarantine_filters_quarantine_name_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'quarantine_name' is set
        if ('quarantine_name' not in params or
                params['quarantine_name'] is None):
            raise ValueError("Missing the required parameter `quarantine_name` when calling `esa_api_v20_config_quarantine_filters_quarantine_name_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'quarantine_name' in params:
            path_params['quarantine_name'] = params['quarantine_name']  # noqa: E501

        query_params = []
        if 'device_type' in params:
            query_params.append(('device_type', params['device_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json, text/plain, */*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth', 'UserSecurity']  # noqa: E501

        return self.api_client.call_api(
            '/esa/api/v2.0/config/quarantine_filters/{quarantine_name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConfigLocalQuarantinesFilters',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def esa_api_v20_config_quarantine_users_get(self, **kwargs):  # noqa: E501
        """get quarantine users  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.esa_api_v20_config_quarantine_users_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_type:
        :return: ConfigLocalQuarantinesUsers
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.esa_api_v20_config_quarantine_users_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.esa_api_v20_config_quarantine_users_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def esa_api_v20_config_quarantine_users_get_with_http_info(self, **kwargs):  # noqa: E501
        """get quarantine users  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.esa_api_v20_config_quarantine_users_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_type:
        :return: ConfigLocalQuarantinesUsers
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method esa_api_v20_config_quarantine_users_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'device_type' in params:
            query_params.append(('device_type', params['device_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json, text/plain, */*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth', 'UserSecurity']  # noqa: E501

        return self.api_client.call_api(
            '/esa/api/v2.0/config/quarantine_users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConfigLocalQuarantinesUsers',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def esa_api_v20_config_sdr_categories_get(self, **kwargs):  # noqa: E501
        """get sdr categories  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.esa_api_v20_config_sdr_categories_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_type:
        :return: ConfigSdrCategories
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.esa_api_v20_config_sdr_categories_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.esa_api_v20_config_sdr_categories_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def esa_api_v20_config_sdr_categories_get_with_http_info(self, **kwargs):  # noqa: E501
        """get sdr categories  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.esa_api_v20_config_sdr_categories_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_type:
        :return: ConfigSdrCategories
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method esa_api_v20_config_sdr_categories_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'device_type' in params:
            query_params.append(('device_type', params['device_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json, text/plain, */*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth', 'UserSecurity']  # noqa: E501

        return self.api_client.call_api(
            '/esa/api/v2.0/config/sdr_categories', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConfigSdrCategories',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def esa_api_v20_config_sdr_threat_levels_get(self, **kwargs):  # noqa: E501
        """get sdr threat levels  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.esa_api_v20_config_sdr_threat_levels_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_type:
        :return: ConfigSdrThreatLevels
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.esa_api_v20_config_sdr_threat_levels_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.esa_api_v20_config_sdr_threat_levels_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def esa_api_v20_config_sdr_threat_levels_get_with_http_info(self, **kwargs):  # noqa: E501
        """get sdr threat levels  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.esa_api_v20_config_sdr_threat_levels_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_type:
        :return: ConfigSdrThreatLevels
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method esa_api_v20_config_sdr_threat_levels_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'device_type' in params:
            query_params.append(('device_type', params['device_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json, text/plain, */*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth', 'UserSecurity']  # noqa: E501

        return self.api_client.call_api(
            '/esa/api/v2.0/config/sdr_threat_levels', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConfigSdrThreatLevels',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)