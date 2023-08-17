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

class ReportingMailIncomingDomainDetailBlockedSdrDataResultSet(object):
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
        'blocked_sdr': 'list[dict(str, object)]'
    }

    attribute_map = {
        'blocked_sdr': 'blocked_sdr'
    }

    def __init__(self, blocked_sdr=None):  # noqa: E501
        """ReportingMailIncomingDomainDetailBlockedSdrDataResultSet - a model defined in Swagger"""  # noqa: E501
        self._blocked_sdr = None
        self.discriminator = None
        if blocked_sdr is not None:
            self.blocked_sdr = blocked_sdr

    @property
    def blocked_sdr(self):
        """Gets the blocked_sdr of this ReportingMailIncomingDomainDetailBlockedSdrDataResultSet.  # noqa: E501


        :return: The blocked_sdr of this ReportingMailIncomingDomainDetailBlockedSdrDataResultSet.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._blocked_sdr

    @blocked_sdr.setter
    def blocked_sdr(self, blocked_sdr):
        """Sets the blocked_sdr of this ReportingMailIncomingDomainDetailBlockedSdrDataResultSet.


        :param blocked_sdr: The blocked_sdr of this ReportingMailIncomingDomainDetailBlockedSdrDataResultSet.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._blocked_sdr = blocked_sdr

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
        if issubclass(ReportingMailIncomingDomainDetailBlockedSdrDataResultSet, dict):
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
        if not isinstance(other, ReportingMailIncomingDomainDetailBlockedSdrDataResultSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
