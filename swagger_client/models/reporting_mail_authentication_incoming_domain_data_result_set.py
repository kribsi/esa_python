# coding: utf-8

"""
    Secure Email Gateway API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ReportingMailAuthenticationIncomingDomainDataResultSet(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'auth_disallow': 'list[dict(str, object)]',
        'auth_fail': 'list[dict(str, object)]',
        'auth_success': 'list[dict(str, object)]',
        'cert_fail': 'list[dict(str, object)]',
        'cert_fallback_fail': 'list[dict(str, object)]',
        'cert_fallback_success': 'list[dict(str, object)]',
        'cert_success': 'list[dict(str, object)]',
        'noauth': 'list[dict(str, object)]',
        'total': 'list[dict(str, object)]'
    }

    attribute_map = {
        'auth_disallow': 'auth_disallow',
        'auth_fail': 'auth_fail',
        'auth_success': 'auth_success',
        'cert_fail': 'cert_fail',
        'cert_fallback_fail': 'cert_fallback_fail',
        'cert_fallback_success': 'cert_fallback_success',
        'cert_success': 'cert_success',
        'noauth': 'noauth',
        'total': 'total'
    }

    def __init__(self, auth_disallow=None, auth_fail=None, auth_success=None, cert_fail=None, cert_fallback_fail=None, cert_fallback_success=None, cert_success=None, noauth=None, total=None):  # noqa: E501
        """ReportingMailAuthenticationIncomingDomainDataResultSet - a model defined in Swagger"""  # noqa: E501
        self._auth_disallow = None
        self._auth_fail = None
        self._auth_success = None
        self._cert_fail = None
        self._cert_fallback_fail = None
        self._cert_fallback_success = None
        self._cert_success = None
        self._noauth = None
        self._total = None
        self.discriminator = None
        if auth_disallow is not None:
            self.auth_disallow = auth_disallow
        if auth_fail is not None:
            self.auth_fail = auth_fail
        if auth_success is not None:
            self.auth_success = auth_success
        if cert_fail is not None:
            self.cert_fail = cert_fail
        if cert_fallback_fail is not None:
            self.cert_fallback_fail = cert_fallback_fail
        if cert_fallback_success is not None:
            self.cert_fallback_success = cert_fallback_success
        if cert_success is not None:
            self.cert_success = cert_success
        if noauth is not None:
            self.noauth = noauth
        if total is not None:
            self.total = total

    @property
    def auth_disallow(self):
        """Gets the auth_disallow of this ReportingMailAuthenticationIncomingDomainDataResultSet.  # noqa: E501


        :return: The auth_disallow of this ReportingMailAuthenticationIncomingDomainDataResultSet.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._auth_disallow

    @auth_disallow.setter
    def auth_disallow(self, auth_disallow):
        """Sets the auth_disallow of this ReportingMailAuthenticationIncomingDomainDataResultSet.


        :param auth_disallow: The auth_disallow of this ReportingMailAuthenticationIncomingDomainDataResultSet.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._auth_disallow = auth_disallow

    @property
    def auth_fail(self):
        """Gets the auth_fail of this ReportingMailAuthenticationIncomingDomainDataResultSet.  # noqa: E501


        :return: The auth_fail of this ReportingMailAuthenticationIncomingDomainDataResultSet.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._auth_fail

    @auth_fail.setter
    def auth_fail(self, auth_fail):
        """Sets the auth_fail of this ReportingMailAuthenticationIncomingDomainDataResultSet.


        :param auth_fail: The auth_fail of this ReportingMailAuthenticationIncomingDomainDataResultSet.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._auth_fail = auth_fail

    @property
    def auth_success(self):
        """Gets the auth_success of this ReportingMailAuthenticationIncomingDomainDataResultSet.  # noqa: E501


        :return: The auth_success of this ReportingMailAuthenticationIncomingDomainDataResultSet.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._auth_success

    @auth_success.setter
    def auth_success(self, auth_success):
        """Sets the auth_success of this ReportingMailAuthenticationIncomingDomainDataResultSet.


        :param auth_success: The auth_success of this ReportingMailAuthenticationIncomingDomainDataResultSet.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._auth_success = auth_success

    @property
    def cert_fail(self):
        """Gets the cert_fail of this ReportingMailAuthenticationIncomingDomainDataResultSet.  # noqa: E501


        :return: The cert_fail of this ReportingMailAuthenticationIncomingDomainDataResultSet.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._cert_fail

    @cert_fail.setter
    def cert_fail(self, cert_fail):
        """Sets the cert_fail of this ReportingMailAuthenticationIncomingDomainDataResultSet.


        :param cert_fail: The cert_fail of this ReportingMailAuthenticationIncomingDomainDataResultSet.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._cert_fail = cert_fail

    @property
    def cert_fallback_fail(self):
        """Gets the cert_fallback_fail of this ReportingMailAuthenticationIncomingDomainDataResultSet.  # noqa: E501


        :return: The cert_fallback_fail of this ReportingMailAuthenticationIncomingDomainDataResultSet.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._cert_fallback_fail

    @cert_fallback_fail.setter
    def cert_fallback_fail(self, cert_fallback_fail):
        """Sets the cert_fallback_fail of this ReportingMailAuthenticationIncomingDomainDataResultSet.


        :param cert_fallback_fail: The cert_fallback_fail of this ReportingMailAuthenticationIncomingDomainDataResultSet.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._cert_fallback_fail = cert_fallback_fail

    @property
    def cert_fallback_success(self):
        """Gets the cert_fallback_success of this ReportingMailAuthenticationIncomingDomainDataResultSet.  # noqa: E501


        :return: The cert_fallback_success of this ReportingMailAuthenticationIncomingDomainDataResultSet.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._cert_fallback_success

    @cert_fallback_success.setter
    def cert_fallback_success(self, cert_fallback_success):
        """Sets the cert_fallback_success of this ReportingMailAuthenticationIncomingDomainDataResultSet.


        :param cert_fallback_success: The cert_fallback_success of this ReportingMailAuthenticationIncomingDomainDataResultSet.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._cert_fallback_success = cert_fallback_success

    @property
    def cert_success(self):
        """Gets the cert_success of this ReportingMailAuthenticationIncomingDomainDataResultSet.  # noqa: E501


        :return: The cert_success of this ReportingMailAuthenticationIncomingDomainDataResultSet.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._cert_success

    @cert_success.setter
    def cert_success(self, cert_success):
        """Sets the cert_success of this ReportingMailAuthenticationIncomingDomainDataResultSet.


        :param cert_success: The cert_success of this ReportingMailAuthenticationIncomingDomainDataResultSet.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._cert_success = cert_success

    @property
    def noauth(self):
        """Gets the noauth of this ReportingMailAuthenticationIncomingDomainDataResultSet.  # noqa: E501


        :return: The noauth of this ReportingMailAuthenticationIncomingDomainDataResultSet.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._noauth

    @noauth.setter
    def noauth(self, noauth):
        """Sets the noauth of this ReportingMailAuthenticationIncomingDomainDataResultSet.


        :param noauth: The noauth of this ReportingMailAuthenticationIncomingDomainDataResultSet.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._noauth = noauth

    @property
    def total(self):
        """Gets the total of this ReportingMailAuthenticationIncomingDomainDataResultSet.  # noqa: E501


        :return: The total of this ReportingMailAuthenticationIncomingDomainDataResultSet.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ReportingMailAuthenticationIncomingDomainDataResultSet.


        :param total: The total of this ReportingMailAuthenticationIncomingDomainDataResultSet.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._total = total

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ReportingMailAuthenticationIncomingDomainDataResultSet, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ReportingMailAuthenticationIncomingDomainDataResultSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other