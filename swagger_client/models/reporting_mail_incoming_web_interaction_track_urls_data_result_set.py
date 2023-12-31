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

class ReportingMailIncomingWebInteractionTrackUrlsDataResultSet(object):
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
        'allowed': 'list[dict(str, object)]',
        'blocked': 'list[dict(str, object)]',
        'msg_count': 'list[dict(str, object)]',
        'unknown': 'list[dict(str, object)]'
    }

    attribute_map = {
        'allowed': 'allowed',
        'blocked': 'blocked',
        'msg_count': 'msg_count',
        'unknown': 'unknown'
    }

    def __init__(self, allowed=None, blocked=None, msg_count=None, unknown=None):  # noqa: E501
        """ReportingMailIncomingWebInteractionTrackUrlsDataResultSet - a model defined in Swagger"""  # noqa: E501
        self._allowed = None
        self._blocked = None
        self._msg_count = None
        self._unknown = None
        self.discriminator = None
        if allowed is not None:
            self.allowed = allowed
        if blocked is not None:
            self.blocked = blocked
        if msg_count is not None:
            self.msg_count = msg_count
        if unknown is not None:
            self.unknown = unknown

    @property
    def allowed(self):
        """Gets the allowed of this ReportingMailIncomingWebInteractionTrackUrlsDataResultSet.  # noqa: E501


        :return: The allowed of this ReportingMailIncomingWebInteractionTrackUrlsDataResultSet.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._allowed

    @allowed.setter
    def allowed(self, allowed):
        """Sets the allowed of this ReportingMailIncomingWebInteractionTrackUrlsDataResultSet.


        :param allowed: The allowed of this ReportingMailIncomingWebInteractionTrackUrlsDataResultSet.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._allowed = allowed

    @property
    def blocked(self):
        """Gets the blocked of this ReportingMailIncomingWebInteractionTrackUrlsDataResultSet.  # noqa: E501


        :return: The blocked of this ReportingMailIncomingWebInteractionTrackUrlsDataResultSet.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._blocked

    @blocked.setter
    def blocked(self, blocked):
        """Sets the blocked of this ReportingMailIncomingWebInteractionTrackUrlsDataResultSet.


        :param blocked: The blocked of this ReportingMailIncomingWebInteractionTrackUrlsDataResultSet.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._blocked = blocked

    @property
    def msg_count(self):
        """Gets the msg_count of this ReportingMailIncomingWebInteractionTrackUrlsDataResultSet.  # noqa: E501


        :return: The msg_count of this ReportingMailIncomingWebInteractionTrackUrlsDataResultSet.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._msg_count

    @msg_count.setter
    def msg_count(self, msg_count):
        """Sets the msg_count of this ReportingMailIncomingWebInteractionTrackUrlsDataResultSet.


        :param msg_count: The msg_count of this ReportingMailIncomingWebInteractionTrackUrlsDataResultSet.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._msg_count = msg_count

    @property
    def unknown(self):
        """Gets the unknown of this ReportingMailIncomingWebInteractionTrackUrlsDataResultSet.  # noqa: E501


        :return: The unknown of this ReportingMailIncomingWebInteractionTrackUrlsDataResultSet.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._unknown

    @unknown.setter
    def unknown(self, unknown):
        """Sets the unknown of this ReportingMailIncomingWebInteractionTrackUrlsDataResultSet.


        :param unknown: The unknown of this ReportingMailIncomingWebInteractionTrackUrlsDataResultSet.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._unknown = unknown

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
        if issubclass(ReportingMailIncomingWebInteractionTrackUrlsDataResultSet, dict):
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
        if not isinstance(other, ReportingMailIncomingWebInteractionTrackUrlsDataResultSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
