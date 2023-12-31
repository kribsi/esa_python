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

class ReportingMailAmpReputationUpdateDataResultSet(object):
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
        'console_url': 'list[dict(str, object)]',
        'filenames': 'list[dict(str, object)]',
        'msg_direction': 'list[dict(str, object)]',
        'old_disposition': 'list[dict(str, object)]',
        'timestamped_tuple': 'list[dict(str, object)]'
    }

    attribute_map = {
        'console_url': 'console_url',
        'filenames': 'filenames',
        'msg_direction': 'msg_direction',
        'old_disposition': 'old_disposition',
        'timestamped_tuple': 'timestamped_tuple'
    }

    def __init__(self, console_url=None, filenames=None, msg_direction=None, old_disposition=None, timestamped_tuple=None):  # noqa: E501
        """ReportingMailAmpReputationUpdateDataResultSet - a model defined in Swagger"""  # noqa: E501
        self._console_url = None
        self._filenames = None
        self._msg_direction = None
        self._old_disposition = None
        self._timestamped_tuple = None
        self.discriminator = None
        if console_url is not None:
            self.console_url = console_url
        if filenames is not None:
            self.filenames = filenames
        if msg_direction is not None:
            self.msg_direction = msg_direction
        if old_disposition is not None:
            self.old_disposition = old_disposition
        if timestamped_tuple is not None:
            self.timestamped_tuple = timestamped_tuple

    @property
    def console_url(self):
        """Gets the console_url of this ReportingMailAmpReputationUpdateDataResultSet.  # noqa: E501


        :return: The console_url of this ReportingMailAmpReputationUpdateDataResultSet.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._console_url

    @console_url.setter
    def console_url(self, console_url):
        """Sets the console_url of this ReportingMailAmpReputationUpdateDataResultSet.


        :param console_url: The console_url of this ReportingMailAmpReputationUpdateDataResultSet.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._console_url = console_url

    @property
    def filenames(self):
        """Gets the filenames of this ReportingMailAmpReputationUpdateDataResultSet.  # noqa: E501


        :return: The filenames of this ReportingMailAmpReputationUpdateDataResultSet.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._filenames

    @filenames.setter
    def filenames(self, filenames):
        """Sets the filenames of this ReportingMailAmpReputationUpdateDataResultSet.


        :param filenames: The filenames of this ReportingMailAmpReputationUpdateDataResultSet.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._filenames = filenames

    @property
    def msg_direction(self):
        """Gets the msg_direction of this ReportingMailAmpReputationUpdateDataResultSet.  # noqa: E501


        :return: The msg_direction of this ReportingMailAmpReputationUpdateDataResultSet.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._msg_direction

    @msg_direction.setter
    def msg_direction(self, msg_direction):
        """Sets the msg_direction of this ReportingMailAmpReputationUpdateDataResultSet.


        :param msg_direction: The msg_direction of this ReportingMailAmpReputationUpdateDataResultSet.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._msg_direction = msg_direction

    @property
    def old_disposition(self):
        """Gets the old_disposition of this ReportingMailAmpReputationUpdateDataResultSet.  # noqa: E501


        :return: The old_disposition of this ReportingMailAmpReputationUpdateDataResultSet.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._old_disposition

    @old_disposition.setter
    def old_disposition(self, old_disposition):
        """Sets the old_disposition of this ReportingMailAmpReputationUpdateDataResultSet.


        :param old_disposition: The old_disposition of this ReportingMailAmpReputationUpdateDataResultSet.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._old_disposition = old_disposition

    @property
    def timestamped_tuple(self):
        """Gets the timestamped_tuple of this ReportingMailAmpReputationUpdateDataResultSet.  # noqa: E501


        :return: The timestamped_tuple of this ReportingMailAmpReputationUpdateDataResultSet.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._timestamped_tuple

    @timestamped_tuple.setter
    def timestamped_tuple(self, timestamped_tuple):
        """Sets the timestamped_tuple of this ReportingMailAmpReputationUpdateDataResultSet.


        :param timestamped_tuple: The timestamped_tuple of this ReportingMailAmpReputationUpdateDataResultSet.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._timestamped_tuple = timestamped_tuple

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
        if issubclass(ReportingMailAmpReputationUpdateDataResultSet, dict):
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
        if not isinstance(other, ReportingMailAmpReputationUpdateDataResultSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
