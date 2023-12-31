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


class MailSenderDomainDetailApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def esa_api_v20_reporting_mail_sender_domain_detail_detected_amp_get(self, **kwargs):  # noqa: E501
        """mail sender domain detail detected amp  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.esa_api_v20_reporting_mail_sender_domain_detail_detected_amp_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str start_date:
        :param str end_date:
        :param str device_type:
        :param str top:
        :return: ReportingMailSenderDomainDetailDetectedAmp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.esa_api_v20_reporting_mail_sender_domain_detail_detected_amp_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.esa_api_v20_reporting_mail_sender_domain_detail_detected_amp_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def esa_api_v20_reporting_mail_sender_domain_detail_detected_amp_get_with_http_info(self, **kwargs):  # noqa: E501
        """mail sender domain detail detected amp  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.esa_api_v20_reporting_mail_sender_domain_detail_detected_amp_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str start_date:
        :param str end_date:
        :param str device_type:
        :param str top:
        :return: ReportingMailSenderDomainDetailDetectedAmp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['start_date', 'end_date', 'device_type', 'top']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method esa_api_v20_reporting_mail_sender_domain_detail_detected_amp_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_date' in params:
            query_params.append(('startDate', params['start_date']))  # noqa: E501
        if 'end_date' in params:
            query_params.append(('endDate', params['end_date']))  # noqa: E501
        if 'device_type' in params:
            query_params.append(('device_type', params['device_type']))  # noqa: E501
        if 'top' in params:
            query_params.append(('top', params['top']))  # noqa: E501

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
            '/esa/api/v2.0/reporting/mail_sender_domain_detail/detected_amp', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReportingMailSenderDomainDetailDetectedAmp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def esa_api_v20_reporting_mail_sender_domain_detail_detected_spam_get(self, **kwargs):  # noqa: E501
        """mail sender domain detail detected spam  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.esa_api_v20_reporting_mail_sender_domain_detail_detected_spam_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str start_date:
        :param str end_date:
        :param str device_type:
        :param str top:
        :return: ReportingMailSenderDomainDetailDetectedSpam
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.esa_api_v20_reporting_mail_sender_domain_detail_detected_spam_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.esa_api_v20_reporting_mail_sender_domain_detail_detected_spam_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def esa_api_v20_reporting_mail_sender_domain_detail_detected_spam_get_with_http_info(self, **kwargs):  # noqa: E501
        """mail sender domain detail detected spam  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.esa_api_v20_reporting_mail_sender_domain_detail_detected_spam_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str start_date:
        :param str end_date:
        :param str device_type:
        :param str top:
        :return: ReportingMailSenderDomainDetailDetectedSpam
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['start_date', 'end_date', 'device_type', 'top']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method esa_api_v20_reporting_mail_sender_domain_detail_detected_spam_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_date' in params:
            query_params.append(('startDate', params['start_date']))  # noqa: E501
        if 'end_date' in params:
            query_params.append(('endDate', params['end_date']))  # noqa: E501
        if 'device_type' in params:
            query_params.append(('device_type', params['device_type']))  # noqa: E501
        if 'top' in params:
            query_params.append(('top', params['top']))  # noqa: E501

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
            '/esa/api/v2.0/reporting/mail_sender_domain_detail/detected_spam', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReportingMailSenderDomainDetailDetectedSpam',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def esa_api_v20_reporting_mail_sender_domain_detail_detected_virus_get(self, **kwargs):  # noqa: E501
        """mail sender domain detail detected virus  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.esa_api_v20_reporting_mail_sender_domain_detail_detected_virus_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str start_date:
        :param str end_date:
        :param str device_type:
        :param str top:
        :return: ReportingMailSenderDomainDetailDetectedVirus
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.esa_api_v20_reporting_mail_sender_domain_detail_detected_virus_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.esa_api_v20_reporting_mail_sender_domain_detail_detected_virus_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def esa_api_v20_reporting_mail_sender_domain_detail_detected_virus_get_with_http_info(self, **kwargs):  # noqa: E501
        """mail sender domain detail detected virus  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.esa_api_v20_reporting_mail_sender_domain_detail_detected_virus_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str start_date:
        :param str end_date:
        :param str device_type:
        :param str top:
        :return: ReportingMailSenderDomainDetailDetectedVirus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['start_date', 'end_date', 'device_type', 'top']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method esa_api_v20_reporting_mail_sender_domain_detail_detected_virus_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_date' in params:
            query_params.append(('startDate', params['start_date']))  # noqa: E501
        if 'end_date' in params:
            query_params.append(('endDate', params['end_date']))  # noqa: E501
        if 'device_type' in params:
            query_params.append(('device_type', params['device_type']))  # noqa: E501
        if 'top' in params:
            query_params.append(('top', params['top']))  # noqa: E501

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
            '/esa/api/v2.0/reporting/mail_sender_domain_detail/detected_virus', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReportingMailSenderDomainDetailDetectedVirus',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def esa_api_v20_reporting_mail_sender_domain_detail_get(self, **kwargs):  # noqa: E501
        """mail sender domain detail detected amp  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.esa_api_v20_reporting_mail_sender_domain_detail_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str start_date:
        :param str end_date:
        :param str device_type:
        :param str top:
        :return: ReportingMailSenderDomainDetailDetectedAmp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.esa_api_v20_reporting_mail_sender_domain_detail_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.esa_api_v20_reporting_mail_sender_domain_detail_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def esa_api_v20_reporting_mail_sender_domain_detail_get_with_http_info(self, **kwargs):  # noqa: E501
        """mail sender domain detail detected amp  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.esa_api_v20_reporting_mail_sender_domain_detail_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str start_date:
        :param str end_date:
        :param str device_type:
        :param str top:
        :return: ReportingMailSenderDomainDetailDetectedAmp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['start_date', 'end_date', 'device_type', 'top']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method esa_api_v20_reporting_mail_sender_domain_detail_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_date' in params:
            query_params.append(('startDate', params['start_date']))  # noqa: E501
        if 'end_date' in params:
            query_params.append(('endDate', params['end_date']))  # noqa: E501
        if 'device_type' in params:
            query_params.append(('device_type', params['device_type']))  # noqa: E501
        if 'top' in params:
            query_params.append(('top', params['top']))  # noqa: E501

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
            '/esa/api/v2.0/reporting/mail_sender_domain_detail', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReportingMailSenderDomainDetailDetectedAmp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def esa_api_v20_reporting_mail_sender_domain_detail_threat_content_filter_get(self, **kwargs):  # noqa: E501
        """mail sender domain detail threat content filter  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.esa_api_v20_reporting_mail_sender_domain_detail_threat_content_filter_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str start_date:
        :param str end_date:
        :param str device_type:
        :param str top:
        :return: ReportingMailSenderDomainDetailThreatContentFilter
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.esa_api_v20_reporting_mail_sender_domain_detail_threat_content_filter_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.esa_api_v20_reporting_mail_sender_domain_detail_threat_content_filter_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def esa_api_v20_reporting_mail_sender_domain_detail_threat_content_filter_get_with_http_info(self, **kwargs):  # noqa: E501
        """mail sender domain detail threat content filter  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.esa_api_v20_reporting_mail_sender_domain_detail_threat_content_filter_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str start_date:
        :param str end_date:
        :param str device_type:
        :param str top:
        :return: ReportingMailSenderDomainDetailThreatContentFilter
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['start_date', 'end_date', 'device_type', 'top']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method esa_api_v20_reporting_mail_sender_domain_detail_threat_content_filter_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_date' in params:
            query_params.append(('startDate', params['start_date']))  # noqa: E501
        if 'end_date' in params:
            query_params.append(('endDate', params['end_date']))  # noqa: E501
        if 'device_type' in params:
            query_params.append(('device_type', params['device_type']))  # noqa: E501
        if 'top' in params:
            query_params.append(('top', params['top']))  # noqa: E501

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
            '/esa/api/v2.0/reporting/mail_sender_domain_detail/threat_content_filter', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReportingMailSenderDomainDetailThreatContentFilter',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def esa_api_v20_reporting_mail_sender_domain_detail_total_clean_recipients_get(self, **kwargs):  # noqa: E501
        """mail sender domain detail total clean recipients  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.esa_api_v20_reporting_mail_sender_domain_detail_total_clean_recipients_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str start_date:
        :param str end_date:
        :param str device_type:
        :param str top:
        :return: ReportingMailSenderDomainDetailTotalCleanRecipients
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.esa_api_v20_reporting_mail_sender_domain_detail_total_clean_recipients_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.esa_api_v20_reporting_mail_sender_domain_detail_total_clean_recipients_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def esa_api_v20_reporting_mail_sender_domain_detail_total_clean_recipients_get_with_http_info(self, **kwargs):  # noqa: E501
        """mail sender domain detail total clean recipients  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.esa_api_v20_reporting_mail_sender_domain_detail_total_clean_recipients_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str start_date:
        :param str end_date:
        :param str device_type:
        :param str top:
        :return: ReportingMailSenderDomainDetailTotalCleanRecipients
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['start_date', 'end_date', 'device_type', 'top']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method esa_api_v20_reporting_mail_sender_domain_detail_total_clean_recipients_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_date' in params:
            query_params.append(('startDate', params['start_date']))  # noqa: E501
        if 'end_date' in params:
            query_params.append(('endDate', params['end_date']))  # noqa: E501
        if 'device_type' in params:
            query_params.append(('device_type', params['device_type']))  # noqa: E501
        if 'top' in params:
            query_params.append(('top', params['top']))  # noqa: E501

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
            '/esa/api/v2.0/reporting/mail_sender_domain_detail/total_clean_recipients', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReportingMailSenderDomainDetailTotalCleanRecipients',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def esa_api_v20_reporting_mail_sender_domain_detail_total_dlp_incidents_get(self, **kwargs):  # noqa: E501
        """mail sender domain detail total dlp incidents  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.esa_api_v20_reporting_mail_sender_domain_detail_total_dlp_incidents_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str start_date:
        :param str end_date:
        :param str device_type:
        :param str top:
        :return: ReportingMailSenderDomainDetailTotalDlpIncidents
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.esa_api_v20_reporting_mail_sender_domain_detail_total_dlp_incidents_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.esa_api_v20_reporting_mail_sender_domain_detail_total_dlp_incidents_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def esa_api_v20_reporting_mail_sender_domain_detail_total_dlp_incidents_get_with_http_info(self, **kwargs):  # noqa: E501
        """mail sender domain detail total dlp incidents  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.esa_api_v20_reporting_mail_sender_domain_detail_total_dlp_incidents_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str start_date:
        :param str end_date:
        :param str device_type:
        :param str top:
        :return: ReportingMailSenderDomainDetailTotalDlpIncidents
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['start_date', 'end_date', 'device_type', 'top']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method esa_api_v20_reporting_mail_sender_domain_detail_total_dlp_incidents_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_date' in params:
            query_params.append(('startDate', params['start_date']))  # noqa: E501
        if 'end_date' in params:
            query_params.append(('endDate', params['end_date']))  # noqa: E501
        if 'device_type' in params:
            query_params.append(('device_type', params['device_type']))  # noqa: E501
        if 'top' in params:
            query_params.append(('top', params['top']))  # noqa: E501

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
            '/esa/api/v2.0/reporting/mail_sender_domain_detail/total_dlp_incidents', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReportingMailSenderDomainDetailTotalDlpIncidents',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def esa_api_v20_reporting_mail_sender_domain_detail_total_recipients_processed_get(self, **kwargs):  # noqa: E501
        """mail sender domain detail total recipients processed  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.esa_api_v20_reporting_mail_sender_domain_detail_total_recipients_processed_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str start_date:
        :param str end_date:
        :param str device_type:
        :param str top:
        :return: ReportingMailSenderDomainDetailTotalRecipientsProcessed
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.esa_api_v20_reporting_mail_sender_domain_detail_total_recipients_processed_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.esa_api_v20_reporting_mail_sender_domain_detail_total_recipients_processed_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def esa_api_v20_reporting_mail_sender_domain_detail_total_recipients_processed_get_with_http_info(self, **kwargs):  # noqa: E501
        """mail sender domain detail total recipients processed  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.esa_api_v20_reporting_mail_sender_domain_detail_total_recipients_processed_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str start_date:
        :param str end_date:
        :param str device_type:
        :param str top:
        :return: ReportingMailSenderDomainDetailTotalRecipientsProcessed
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['start_date', 'end_date', 'device_type', 'top']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method esa_api_v20_reporting_mail_sender_domain_detail_total_recipients_processed_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_date' in params:
            query_params.append(('startDate', params['start_date']))  # noqa: E501
        if 'end_date' in params:
            query_params.append(('endDate', params['end_date']))  # noqa: E501
        if 'device_type' in params:
            query_params.append(('device_type', params['device_type']))  # noqa: E501
        if 'top' in params:
            query_params.append(('top', params['top']))  # noqa: E501

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
            '/esa/api/v2.0/reporting/mail_sender_domain_detail/total_recipients_processed', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReportingMailSenderDomainDetailTotalRecipientsProcessed',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def esa_api_v20_reporting_mail_sender_domain_detail_total_threat_recipients_get(self, **kwargs):  # noqa: E501
        """mail sender domain detail total threat recipients  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.esa_api_v20_reporting_mail_sender_domain_detail_total_threat_recipients_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str start_date:
        :param str end_date:
        :param str device_type:
        :param str top:
        :return: ReportingMailSenderDomainDetailTotalThreatRecipients
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.esa_api_v20_reporting_mail_sender_domain_detail_total_threat_recipients_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.esa_api_v20_reporting_mail_sender_domain_detail_total_threat_recipients_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def esa_api_v20_reporting_mail_sender_domain_detail_total_threat_recipients_get_with_http_info(self, **kwargs):  # noqa: E501
        """mail sender domain detail total threat recipients  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.esa_api_v20_reporting_mail_sender_domain_detail_total_threat_recipients_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str start_date:
        :param str end_date:
        :param str device_type:
        :param str top:
        :return: ReportingMailSenderDomainDetailTotalThreatRecipients
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['start_date', 'end_date', 'device_type', 'top']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method esa_api_v20_reporting_mail_sender_domain_detail_total_threat_recipients_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_date' in params:
            query_params.append(('startDate', params['start_date']))  # noqa: E501
        if 'end_date' in params:
            query_params.append(('endDate', params['end_date']))  # noqa: E501
        if 'device_type' in params:
            query_params.append(('device_type', params['device_type']))  # noqa: E501
        if 'top' in params:
            query_params.append(('top', params['top']))  # noqa: E501

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
            '/esa/api/v2.0/reporting/mail_sender_domain_detail/total_threat_recipients', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReportingMailSenderDomainDetailTotalThreatRecipients',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
