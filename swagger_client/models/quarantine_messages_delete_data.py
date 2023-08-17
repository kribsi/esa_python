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

class QuarantineMessagesDeleteData(object):
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
        'action': 'str',
        'total_count': 'int'
    }

    attribute_map = {
        'action': 'action',
        'total_count': 'totalCount'
    }

    def __init__(self, action=None, total_count=None):  # noqa: E501
        """QuarantineMessagesDeleteData - a model defined in Swagger"""  # noqa: E501
        self._action = None
        self._total_count = None
        self.discriminator = None
        if action is not None:
            self.action = action
        if total_count is not None:
            self.total_count = total_count

    @property
    def action(self):
        """Gets the action of this QuarantineMessagesDeleteData.  # noqa: E501


        :return: The action of this QuarantineMessagesDeleteData.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this QuarantineMessagesDeleteData.


        :param action: The action of this QuarantineMessagesDeleteData.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def total_count(self):
        """Gets the total_count of this QuarantineMessagesDeleteData.  # noqa: E501


        :return: The total_count of this QuarantineMessagesDeleteData.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this QuarantineMessagesDeleteData.


        :param total_count: The total_count of this QuarantineMessagesDeleteData.  # noqa: E501
        :type: int
        """

        self._total_count = total_count

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
        if issubclass(QuarantineMessagesDeleteData, dict):
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
        if not isinstance(other, QuarantineMessagesDeleteData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
