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

class ReportingMailIncomingWebInteractionTrackUrlsAllowedDataResultSet(object):
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
        'allowed': 'list[dict(str, object)]'
    }

    attribute_map = {
        'allowed': 'allowed'
    }

    def __init__(self, allowed=None):  # noqa: E501
        """ReportingMailIncomingWebInteractionTrackUrlsAllowedDataResultSet - a model defined in Swagger"""  # noqa: E501
        self._allowed = None
        self.discriminator = None
        if allowed is not None:
            self.allowed = allowed

    @property
    def allowed(self):
        """Gets the allowed of this ReportingMailIncomingWebInteractionTrackUrlsAllowedDataResultSet.  # noqa: E501


        :return: The allowed of this ReportingMailIncomingWebInteractionTrackUrlsAllowedDataResultSet.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._allowed

    @allowed.setter
    def allowed(self, allowed):
        """Sets the allowed of this ReportingMailIncomingWebInteractionTrackUrlsAllowedDataResultSet.


        :param allowed: The allowed of this ReportingMailIncomingWebInteractionTrackUrlsAllowedDataResultSet.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._allowed = allowed

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
        if issubclass(ReportingMailIncomingWebInteractionTrackUrlsAllowedDataResultSet, dict):
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
        if not isinstance(other, ReportingMailIncomingWebInteractionTrackUrlsAllowedDataResultSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
