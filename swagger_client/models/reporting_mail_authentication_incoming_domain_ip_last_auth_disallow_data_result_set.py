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

class ReportingMailAuthenticationIncomingDomainIpLastAuthDisallowDataResultSet(object):
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
        'last_auth_disallow': 'list[dict(str, object)]'
    }

    attribute_map = {
        'last_auth_disallow': 'last_auth_disallow'
    }

    def __init__(self, last_auth_disallow=None):  # noqa: E501
        """ReportingMailAuthenticationIncomingDomainIpLastAuthDisallowDataResultSet - a model defined in Swagger"""  # noqa: E501
        self._last_auth_disallow = None
        self.discriminator = None
        if last_auth_disallow is not None:
            self.last_auth_disallow = last_auth_disallow

    @property
    def last_auth_disallow(self):
        """Gets the last_auth_disallow of this ReportingMailAuthenticationIncomingDomainIpLastAuthDisallowDataResultSet.  # noqa: E501


        :return: The last_auth_disallow of this ReportingMailAuthenticationIncomingDomainIpLastAuthDisallowDataResultSet.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._last_auth_disallow

    @last_auth_disallow.setter
    def last_auth_disallow(self, last_auth_disallow):
        """Sets the last_auth_disallow of this ReportingMailAuthenticationIncomingDomainIpLastAuthDisallowDataResultSet.


        :param last_auth_disallow: The last_auth_disallow of this ReportingMailAuthenticationIncomingDomainIpLastAuthDisallowDataResultSet.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._last_auth_disallow = last_auth_disallow

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
        if issubclass(ReportingMailAuthenticationIncomingDomainIpLastAuthDisallowDataResultSet, dict):
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
        if not isinstance(other, ReportingMailAuthenticationIncomingDomainIpLastAuthDisallowDataResultSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
