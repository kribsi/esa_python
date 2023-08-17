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

class QuarantineBlocklistSenderDeleteRequestBody(object):
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
        'quarantine_type': 'str',
        'sender_list': 'list[str]',
        'view_by': 'str'
    }

    attribute_map = {
        'quarantine_type': 'quarantineType',
        'sender_list': 'senderList',
        'view_by': 'viewBy'
    }

    def __init__(self, quarantine_type=None, sender_list=None, view_by=None):  # noqa: E501
        """QuarantineBlocklistSenderDeleteRequestBody - a model defined in Swagger"""  # noqa: E501
        self._quarantine_type = None
        self._sender_list = None
        self._view_by = None
        self.discriminator = None
        if quarantine_type is not None:
            self.quarantine_type = quarantine_type
        if sender_list is not None:
            self.sender_list = sender_list
        if view_by is not None:
            self.view_by = view_by

    @property
    def quarantine_type(self):
        """Gets the quarantine_type of this QuarantineBlocklistSenderDeleteRequestBody.  # noqa: E501


        :return: The quarantine_type of this QuarantineBlocklistSenderDeleteRequestBody.  # noqa: E501
        :rtype: str
        """
        return self._quarantine_type

    @quarantine_type.setter
    def quarantine_type(self, quarantine_type):
        """Sets the quarantine_type of this QuarantineBlocklistSenderDeleteRequestBody.


        :param quarantine_type: The quarantine_type of this QuarantineBlocklistSenderDeleteRequestBody.  # noqa: E501
        :type: str
        """

        self._quarantine_type = quarantine_type

    @property
    def sender_list(self):
        """Gets the sender_list of this QuarantineBlocklistSenderDeleteRequestBody.  # noqa: E501


        :return: The sender_list of this QuarantineBlocklistSenderDeleteRequestBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._sender_list

    @sender_list.setter
    def sender_list(self, sender_list):
        """Sets the sender_list of this QuarantineBlocklistSenderDeleteRequestBody.


        :param sender_list: The sender_list of this QuarantineBlocklistSenderDeleteRequestBody.  # noqa: E501
        :type: list[str]
        """

        self._sender_list = sender_list

    @property
    def view_by(self):
        """Gets the view_by of this QuarantineBlocklistSenderDeleteRequestBody.  # noqa: E501


        :return: The view_by of this QuarantineBlocklistSenderDeleteRequestBody.  # noqa: E501
        :rtype: str
        """
        return self._view_by

    @view_by.setter
    def view_by(self, view_by):
        """Sets the view_by of this QuarantineBlocklistSenderDeleteRequestBody.


        :param view_by: The view_by of this QuarantineBlocklistSenderDeleteRequestBody.  # noqa: E501
        :type: str
        """

        self._view_by = view_by

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
        if issubclass(QuarantineBlocklistSenderDeleteRequestBody, dict):
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
        if not isinstance(other, QuarantineBlocklistSenderDeleteRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
