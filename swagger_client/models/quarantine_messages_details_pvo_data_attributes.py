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

class QuarantineMessagesDetailsPvoDataAttributes(object):
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
        'headers': 'str',
        'matched_contents': 'list[object]',
        'message_body': 'str',
        'message_details': 'QuarantineMessagesDetailsPvoDataAttributesMessageDetails',
        'message_part_details': 'list[QuarantineMessagesDetailsPvoDataAttributesMessagePartDetails]',
        'quarantine_details': 'list[QuarantineMessagesDetailsPvoDataAttributesQuarantineDetails]'
    }

    attribute_map = {
        'headers': 'headers',
        'matched_contents': 'matchedContents',
        'message_body': 'messageBody',
        'message_details': 'messageDetails',
        'message_part_details': 'messagePartDetails',
        'quarantine_details': 'quarantineDetails'
    }

    def __init__(self, headers=None, matched_contents=None, message_body=None, message_details=None, message_part_details=None, quarantine_details=None):  # noqa: E501
        """QuarantineMessagesDetailsPvoDataAttributes - a model defined in Swagger"""  # noqa: E501
        self._headers = None
        self._matched_contents = None
        self._message_body = None
        self._message_details = None
        self._message_part_details = None
        self._quarantine_details = None
        self.discriminator = None
        if headers is not None:
            self.headers = headers
        if matched_contents is not None:
            self.matched_contents = matched_contents
        if message_body is not None:
            self.message_body = message_body
        if message_details is not None:
            self.message_details = message_details
        if message_part_details is not None:
            self.message_part_details = message_part_details
        if quarantine_details is not None:
            self.quarantine_details = quarantine_details

    @property
    def headers(self):
        """Gets the headers of this QuarantineMessagesDetailsPvoDataAttributes.  # noqa: E501


        :return: The headers of this QuarantineMessagesDetailsPvoDataAttributes.  # noqa: E501
        :rtype: str
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this QuarantineMessagesDetailsPvoDataAttributes.


        :param headers: The headers of this QuarantineMessagesDetailsPvoDataAttributes.  # noqa: E501
        :type: str
        """

        self._headers = headers

    @property
    def matched_contents(self):
        """Gets the matched_contents of this QuarantineMessagesDetailsPvoDataAttributes.  # noqa: E501


        :return: The matched_contents of this QuarantineMessagesDetailsPvoDataAttributes.  # noqa: E501
        :rtype: list[object]
        """
        return self._matched_contents

    @matched_contents.setter
    def matched_contents(self, matched_contents):
        """Sets the matched_contents of this QuarantineMessagesDetailsPvoDataAttributes.


        :param matched_contents: The matched_contents of this QuarantineMessagesDetailsPvoDataAttributes.  # noqa: E501
        :type: list[object]
        """

        self._matched_contents = matched_contents

    @property
    def message_body(self):
        """Gets the message_body of this QuarantineMessagesDetailsPvoDataAttributes.  # noqa: E501


        :return: The message_body of this QuarantineMessagesDetailsPvoDataAttributes.  # noqa: E501
        :rtype: str
        """
        return self._message_body

    @message_body.setter
    def message_body(self, message_body):
        """Sets the message_body of this QuarantineMessagesDetailsPvoDataAttributes.


        :param message_body: The message_body of this QuarantineMessagesDetailsPvoDataAttributes.  # noqa: E501
        :type: str
        """

        self._message_body = message_body

    @property
    def message_details(self):
        """Gets the message_details of this QuarantineMessagesDetailsPvoDataAttributes.  # noqa: E501


        :return: The message_details of this QuarantineMessagesDetailsPvoDataAttributes.  # noqa: E501
        :rtype: QuarantineMessagesDetailsPvoDataAttributesMessageDetails
        """
        return self._message_details

    @message_details.setter
    def message_details(self, message_details):
        """Sets the message_details of this QuarantineMessagesDetailsPvoDataAttributes.


        :param message_details: The message_details of this QuarantineMessagesDetailsPvoDataAttributes.  # noqa: E501
        :type: QuarantineMessagesDetailsPvoDataAttributesMessageDetails
        """

        self._message_details = message_details

    @property
    def message_part_details(self):
        """Gets the message_part_details of this QuarantineMessagesDetailsPvoDataAttributes.  # noqa: E501


        :return: The message_part_details of this QuarantineMessagesDetailsPvoDataAttributes.  # noqa: E501
        :rtype: list[QuarantineMessagesDetailsPvoDataAttributesMessagePartDetails]
        """
        return self._message_part_details

    @message_part_details.setter
    def message_part_details(self, message_part_details):
        """Sets the message_part_details of this QuarantineMessagesDetailsPvoDataAttributes.


        :param message_part_details: The message_part_details of this QuarantineMessagesDetailsPvoDataAttributes.  # noqa: E501
        :type: list[QuarantineMessagesDetailsPvoDataAttributesMessagePartDetails]
        """

        self._message_part_details = message_part_details

    @property
    def quarantine_details(self):
        """Gets the quarantine_details of this QuarantineMessagesDetailsPvoDataAttributes.  # noqa: E501


        :return: The quarantine_details of this QuarantineMessagesDetailsPvoDataAttributes.  # noqa: E501
        :rtype: list[QuarantineMessagesDetailsPvoDataAttributesQuarantineDetails]
        """
        return self._quarantine_details

    @quarantine_details.setter
    def quarantine_details(self, quarantine_details):
        """Sets the quarantine_details of this QuarantineMessagesDetailsPvoDataAttributes.


        :param quarantine_details: The quarantine_details of this QuarantineMessagesDetailsPvoDataAttributes.  # noqa: E501
        :type: list[QuarantineMessagesDetailsPvoDataAttributesQuarantineDetails]
        """

        self._quarantine_details = quarantine_details

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
        if issubclass(QuarantineMessagesDetailsPvoDataAttributes, dict):
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
        if not isinstance(other, QuarantineMessagesDetailsPvoDataAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other