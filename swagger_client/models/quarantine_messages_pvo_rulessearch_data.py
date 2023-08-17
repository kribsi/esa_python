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

class QuarantineMessagesPvoRulessearchData(object):
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
        'attributes': 'QuarantineMessagesPvoRulessearchAttributes',
        'mid': 'str'
    }

    attribute_map = {
        'attributes': 'attributes',
        'mid': 'mid'
    }

    def __init__(self, attributes=None, mid=None):  # noqa: E501
        """QuarantineMessagesPvoRulessearchData - a model defined in Swagger"""  # noqa: E501
        self._attributes = None
        self._mid = None
        self.discriminator = None
        if attributes is not None:
            self.attributes = attributes
        if mid is not None:
            self.mid = mid

    @property
    def attributes(self):
        """Gets the attributes of this QuarantineMessagesPvoRulessearchData.  # noqa: E501


        :return: The attributes of this QuarantineMessagesPvoRulessearchData.  # noqa: E501
        :rtype: QuarantineMessagesPvoRulessearchAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this QuarantineMessagesPvoRulessearchData.


        :param attributes: The attributes of this QuarantineMessagesPvoRulessearchData.  # noqa: E501
        :type: QuarantineMessagesPvoRulessearchAttributes
        """

        self._attributes = attributes

    @property
    def mid(self):
        """Gets the mid of this QuarantineMessagesPvoRulessearchData.  # noqa: E501


        :return: The mid of this QuarantineMessagesPvoRulessearchData.  # noqa: E501
        :rtype: str
        """
        return self._mid

    @mid.setter
    def mid(self, mid):
        """Sets the mid of this QuarantineMessagesPvoRulessearchData.


        :param mid: The mid of this QuarantineMessagesPvoRulessearchData.  # noqa: E501
        :type: str
        """

        self._mid = mid

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
        if issubclass(QuarantineMessagesPvoRulessearchData, dict):
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
        if not isinstance(other, QuarantineMessagesPvoRulessearchData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other