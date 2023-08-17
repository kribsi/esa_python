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

class QuarantineMessagesDetailsDataAttributes(object):
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
        'attachments': 'list[str]',
        '_date': 'str',
        'envelope_recipient': 'list[str]',
        'from_address': 'list[str]',
        'message_body': 'str',
        'subject': 'str',
        'to_address': 'list[str]'
    }

    attribute_map = {
        'attachments': 'attachments',
        '_date': 'date',
        'envelope_recipient': 'envelopeRecipient',
        'from_address': 'fromAddress',
        'message_body': 'messageBody',
        'subject': 'subject',
        'to_address': 'toAddress'
    }

    def __init__(self, attachments=None, _date=None, envelope_recipient=None, from_address=None, message_body=None, subject=None, to_address=None):  # noqa: E501
        """QuarantineMessagesDetailsDataAttributes - a model defined in Swagger"""  # noqa: E501
        self._attachments = None
        self.__date = None
        self._envelope_recipient = None
        self._from_address = None
        self._message_body = None
        self._subject = None
        self._to_address = None
        self.discriminator = None
        if attachments is not None:
            self.attachments = attachments
        if _date is not None:
            self._date = _date
        if envelope_recipient is not None:
            self.envelope_recipient = envelope_recipient
        if from_address is not None:
            self.from_address = from_address
        if message_body is not None:
            self.message_body = message_body
        if subject is not None:
            self.subject = subject
        if to_address is not None:
            self.to_address = to_address

    @property
    def attachments(self):
        """Gets the attachments of this QuarantineMessagesDetailsDataAttributes.  # noqa: E501


        :return: The attachments of this QuarantineMessagesDetailsDataAttributes.  # noqa: E501
        :rtype: list[str]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this QuarantineMessagesDetailsDataAttributes.


        :param attachments: The attachments of this QuarantineMessagesDetailsDataAttributes.  # noqa: E501
        :type: list[str]
        """

        self._attachments = attachments

    @property
    def _date(self):
        """Gets the _date of this QuarantineMessagesDetailsDataAttributes.  # noqa: E501


        :return: The _date of this QuarantineMessagesDetailsDataAttributes.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this QuarantineMessagesDetailsDataAttributes.


        :param _date: The _date of this QuarantineMessagesDetailsDataAttributes.  # noqa: E501
        :type: str
        """

        self.__date = _date

    @property
    def envelope_recipient(self):
        """Gets the envelope_recipient of this QuarantineMessagesDetailsDataAttributes.  # noqa: E501


        :return: The envelope_recipient of this QuarantineMessagesDetailsDataAttributes.  # noqa: E501
        :rtype: list[str]
        """
        return self._envelope_recipient

    @envelope_recipient.setter
    def envelope_recipient(self, envelope_recipient):
        """Sets the envelope_recipient of this QuarantineMessagesDetailsDataAttributes.


        :param envelope_recipient: The envelope_recipient of this QuarantineMessagesDetailsDataAttributes.  # noqa: E501
        :type: list[str]
        """

        self._envelope_recipient = envelope_recipient

    @property
    def from_address(self):
        """Gets the from_address of this QuarantineMessagesDetailsDataAttributes.  # noqa: E501


        :return: The from_address of this QuarantineMessagesDetailsDataAttributes.  # noqa: E501
        :rtype: list[str]
        """
        return self._from_address

    @from_address.setter
    def from_address(self, from_address):
        """Sets the from_address of this QuarantineMessagesDetailsDataAttributes.


        :param from_address: The from_address of this QuarantineMessagesDetailsDataAttributes.  # noqa: E501
        :type: list[str]
        """

        self._from_address = from_address

    @property
    def message_body(self):
        """Gets the message_body of this QuarantineMessagesDetailsDataAttributes.  # noqa: E501


        :return: The message_body of this QuarantineMessagesDetailsDataAttributes.  # noqa: E501
        :rtype: str
        """
        return self._message_body

    @message_body.setter
    def message_body(self, message_body):
        """Sets the message_body of this QuarantineMessagesDetailsDataAttributes.


        :param message_body: The message_body of this QuarantineMessagesDetailsDataAttributes.  # noqa: E501
        :type: str
        """

        self._message_body = message_body

    @property
    def subject(self):
        """Gets the subject of this QuarantineMessagesDetailsDataAttributes.  # noqa: E501


        :return: The subject of this QuarantineMessagesDetailsDataAttributes.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this QuarantineMessagesDetailsDataAttributes.


        :param subject: The subject of this QuarantineMessagesDetailsDataAttributes.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def to_address(self):
        """Gets the to_address of this QuarantineMessagesDetailsDataAttributes.  # noqa: E501


        :return: The to_address of this QuarantineMessagesDetailsDataAttributes.  # noqa: E501
        :rtype: list[str]
        """
        return self._to_address

    @to_address.setter
    def to_address(self, to_address):
        """Sets the to_address of this QuarantineMessagesDetailsDataAttributes.


        :param to_address: The to_address of this QuarantineMessagesDetailsDataAttributes.  # noqa: E501
        :type: list[str]
        """

        self._to_address = to_address

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
        if issubclass(QuarantineMessagesDetailsDataAttributes, dict):
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
        if not isinstance(other, QuarantineMessagesDetailsDataAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
