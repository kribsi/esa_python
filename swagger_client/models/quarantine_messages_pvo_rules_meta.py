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

class QuarantineMessagesPvoRulesMeta(object):
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
        'total_average_message_size': 'str',
        'total_number_of_messages': 'int'
    }

    attribute_map = {
        'total_average_message_size': 'totalAverageMessageSize',
        'total_number_of_messages': 'totalNumberOfMessages'
    }

    def __init__(self, total_average_message_size=None, total_number_of_messages=None):  # noqa: E501
        """QuarantineMessagesPvoRulesMeta - a model defined in Swagger"""  # noqa: E501
        self._total_average_message_size = None
        self._total_number_of_messages = None
        self.discriminator = None
        if total_average_message_size is not None:
            self.total_average_message_size = total_average_message_size
        if total_number_of_messages is not None:
            self.total_number_of_messages = total_number_of_messages

    @property
    def total_average_message_size(self):
        """Gets the total_average_message_size of this QuarantineMessagesPvoRulesMeta.  # noqa: E501


        :return: The total_average_message_size of this QuarantineMessagesPvoRulesMeta.  # noqa: E501
        :rtype: str
        """
        return self._total_average_message_size

    @total_average_message_size.setter
    def total_average_message_size(self, total_average_message_size):
        """Sets the total_average_message_size of this QuarantineMessagesPvoRulesMeta.


        :param total_average_message_size: The total_average_message_size of this QuarantineMessagesPvoRulesMeta.  # noqa: E501
        :type: str
        """

        self._total_average_message_size = total_average_message_size

    @property
    def total_number_of_messages(self):
        """Gets the total_number_of_messages of this QuarantineMessagesPvoRulesMeta.  # noqa: E501


        :return: The total_number_of_messages of this QuarantineMessagesPvoRulesMeta.  # noqa: E501
        :rtype: int
        """
        return self._total_number_of_messages

    @total_number_of_messages.setter
    def total_number_of_messages(self, total_number_of_messages):
        """Sets the total_number_of_messages of this QuarantineMessagesPvoRulesMeta.


        :param total_number_of_messages: The total_number_of_messages of this QuarantineMessagesPvoRulesMeta.  # noqa: E501
        :type: int
        """

        self._total_number_of_messages = total_number_of_messages

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
        if issubclass(QuarantineMessagesPvoRulesMeta, dict):
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
        if not isinstance(other, QuarantineMessagesPvoRulesMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other