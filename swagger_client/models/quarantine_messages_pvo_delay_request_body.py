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

class QuarantineMessagesPvoDelayRequestBody(object):
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
        'delay': 'str',
        'mids': 'list[int]',
        'quarantine_name': 'str',
        'quarantine_type': 'str'
    }

    attribute_map = {
        'action': 'action',
        'delay': 'delay',
        'mids': 'mids',
        'quarantine_name': 'quarantineName',
        'quarantine_type': 'quarantineType'
    }

    def __init__(self, action=None, delay=None, mids=None, quarantine_name=None, quarantine_type=None):  # noqa: E501
        """QuarantineMessagesPvoDelayRequestBody - a model defined in Swagger"""  # noqa: E501
        self._action = None
        self._delay = None
        self._mids = None
        self._quarantine_name = None
        self._quarantine_type = None
        self.discriminator = None
        if action is not None:
            self.action = action
        if delay is not None:
            self.delay = delay
        if mids is not None:
            self.mids = mids
        if quarantine_name is not None:
            self.quarantine_name = quarantine_name
        if quarantine_type is not None:
            self.quarantine_type = quarantine_type

    @property
    def action(self):
        """Gets the action of this QuarantineMessagesPvoDelayRequestBody.  # noqa: E501


        :return: The action of this QuarantineMessagesPvoDelayRequestBody.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this QuarantineMessagesPvoDelayRequestBody.


        :param action: The action of this QuarantineMessagesPvoDelayRequestBody.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def delay(self):
        """Gets the delay of this QuarantineMessagesPvoDelayRequestBody.  # noqa: E501


        :return: The delay of this QuarantineMessagesPvoDelayRequestBody.  # noqa: E501
        :rtype: str
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        """Sets the delay of this QuarantineMessagesPvoDelayRequestBody.


        :param delay: The delay of this QuarantineMessagesPvoDelayRequestBody.  # noqa: E501
        :type: str
        """

        self._delay = delay

    @property
    def mids(self):
        """Gets the mids of this QuarantineMessagesPvoDelayRequestBody.  # noqa: E501


        :return: The mids of this QuarantineMessagesPvoDelayRequestBody.  # noqa: E501
        :rtype: list[int]
        """
        return self._mids

    @mids.setter
    def mids(self, mids):
        """Sets the mids of this QuarantineMessagesPvoDelayRequestBody.


        :param mids: The mids of this QuarantineMessagesPvoDelayRequestBody.  # noqa: E501
        :type: list[int]
        """

        self._mids = mids

    @property
    def quarantine_name(self):
        """Gets the quarantine_name of this QuarantineMessagesPvoDelayRequestBody.  # noqa: E501


        :return: The quarantine_name of this QuarantineMessagesPvoDelayRequestBody.  # noqa: E501
        :rtype: str
        """
        return self._quarantine_name

    @quarantine_name.setter
    def quarantine_name(self, quarantine_name):
        """Sets the quarantine_name of this QuarantineMessagesPvoDelayRequestBody.


        :param quarantine_name: The quarantine_name of this QuarantineMessagesPvoDelayRequestBody.  # noqa: E501
        :type: str
        """

        self._quarantine_name = quarantine_name

    @property
    def quarantine_type(self):
        """Gets the quarantine_type of this QuarantineMessagesPvoDelayRequestBody.  # noqa: E501


        :return: The quarantine_type of this QuarantineMessagesPvoDelayRequestBody.  # noqa: E501
        :rtype: str
        """
        return self._quarantine_type

    @quarantine_type.setter
    def quarantine_type(self, quarantine_type):
        """Sets the quarantine_type of this QuarantineMessagesPvoDelayRequestBody.


        :param quarantine_type: The quarantine_type of this QuarantineMessagesPvoDelayRequestBody.  # noqa: E501
        :type: str
        """

        self._quarantine_type = quarantine_type

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
        if issubclass(QuarantineMessagesPvoDelayRequestBody, dict):
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
        if not isinstance(other, QuarantineMessagesPvoDelayRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
