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

class MessagetrackingDlpdetailsDataMessages(object):
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
        'direction': 'str',
        'dlp_details': 'MessagetrackingDlpdetailsDataMessagesDlpDetails',
        'host_name': 'str',
        'message_size': 'str',
        'mid': 'list[int]',
        'mid_header': 'str',
        'recipient': 'list[str]',
        'sender': 'str',
        'sender_group': 'str',
        'sending_host_summary': 'MessagetrackingAmpdetailsDataMessagesSendingHostSummary',
        'show_dlp_details': 'bool',
        'smtp_auth_id': 'str',
        'subject': 'str',
        'timestamp': 'str'
    }

    attribute_map = {
        'attachments': 'attachments',
        'direction': 'direction',
        'dlp_details': 'dlpDetails',
        'host_name': 'hostName',
        'message_size': 'messageSize',
        'mid': 'mid',
        'mid_header': 'midHeader',
        'recipient': 'recipient',
        'sender': 'sender',
        'sender_group': 'senderGroup',
        'sending_host_summary': 'sendingHostSummary',
        'show_dlp_details': 'showDLPDetails',
        'smtp_auth_id': 'smtpAuthId',
        'subject': 'subject',
        'timestamp': 'timestamp'
    }

    def __init__(self, attachments=None, direction=None, dlp_details=None, host_name=None, message_size=None, mid=None, mid_header=None, recipient=None, sender=None, sender_group=None, sending_host_summary=None, show_dlp_details=None, smtp_auth_id=None, subject=None, timestamp=None):  # noqa: E501
        """MessagetrackingDlpdetailsDataMessages - a model defined in Swagger"""  # noqa: E501
        self._attachments = None
        self._direction = None
        self._dlp_details = None
        self._host_name = None
        self._message_size = None
        self._mid = None
        self._mid_header = None
        self._recipient = None
        self._sender = None
        self._sender_group = None
        self._sending_host_summary = None
        self._show_dlp_details = None
        self._smtp_auth_id = None
        self._subject = None
        self._timestamp = None
        self.discriminator = None
        if attachments is not None:
            self.attachments = attachments
        if direction is not None:
            self.direction = direction
        if dlp_details is not None:
            self.dlp_details = dlp_details
        if host_name is not None:
            self.host_name = host_name
        if message_size is not None:
            self.message_size = message_size
        if mid is not None:
            self.mid = mid
        if mid_header is not None:
            self.mid_header = mid_header
        if recipient is not None:
            self.recipient = recipient
        if sender is not None:
            self.sender = sender
        if sender_group is not None:
            self.sender_group = sender_group
        if sending_host_summary is not None:
            self.sending_host_summary = sending_host_summary
        if show_dlp_details is not None:
            self.show_dlp_details = show_dlp_details
        if smtp_auth_id is not None:
            self.smtp_auth_id = smtp_auth_id
        if subject is not None:
            self.subject = subject
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def attachments(self):
        """Gets the attachments of this MessagetrackingDlpdetailsDataMessages.  # noqa: E501


        :return: The attachments of this MessagetrackingDlpdetailsDataMessages.  # noqa: E501
        :rtype: list[str]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this MessagetrackingDlpdetailsDataMessages.


        :param attachments: The attachments of this MessagetrackingDlpdetailsDataMessages.  # noqa: E501
        :type: list[str]
        """

        self._attachments = attachments

    @property
    def direction(self):
        """Gets the direction of this MessagetrackingDlpdetailsDataMessages.  # noqa: E501


        :return: The direction of this MessagetrackingDlpdetailsDataMessages.  # noqa: E501
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this MessagetrackingDlpdetailsDataMessages.


        :param direction: The direction of this MessagetrackingDlpdetailsDataMessages.  # noqa: E501
        :type: str
        """

        self._direction = direction

    @property
    def dlp_details(self):
        """Gets the dlp_details of this MessagetrackingDlpdetailsDataMessages.  # noqa: E501


        :return: The dlp_details of this MessagetrackingDlpdetailsDataMessages.  # noqa: E501
        :rtype: MessagetrackingDlpdetailsDataMessagesDlpDetails
        """
        return self._dlp_details

    @dlp_details.setter
    def dlp_details(self, dlp_details):
        """Sets the dlp_details of this MessagetrackingDlpdetailsDataMessages.


        :param dlp_details: The dlp_details of this MessagetrackingDlpdetailsDataMessages.  # noqa: E501
        :type: MessagetrackingDlpdetailsDataMessagesDlpDetails
        """

        self._dlp_details = dlp_details

    @property
    def host_name(self):
        """Gets the host_name of this MessagetrackingDlpdetailsDataMessages.  # noqa: E501


        :return: The host_name of this MessagetrackingDlpdetailsDataMessages.  # noqa: E501
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this MessagetrackingDlpdetailsDataMessages.


        :param host_name: The host_name of this MessagetrackingDlpdetailsDataMessages.  # noqa: E501
        :type: str
        """

        self._host_name = host_name

    @property
    def message_size(self):
        """Gets the message_size of this MessagetrackingDlpdetailsDataMessages.  # noqa: E501


        :return: The message_size of this MessagetrackingDlpdetailsDataMessages.  # noqa: E501
        :rtype: str
        """
        return self._message_size

    @message_size.setter
    def message_size(self, message_size):
        """Sets the message_size of this MessagetrackingDlpdetailsDataMessages.


        :param message_size: The message_size of this MessagetrackingDlpdetailsDataMessages.  # noqa: E501
        :type: str
        """

        self._message_size = message_size

    @property
    def mid(self):
        """Gets the mid of this MessagetrackingDlpdetailsDataMessages.  # noqa: E501


        :return: The mid of this MessagetrackingDlpdetailsDataMessages.  # noqa: E501
        :rtype: list[int]
        """
        return self._mid

    @mid.setter
    def mid(self, mid):
        """Sets the mid of this MessagetrackingDlpdetailsDataMessages.


        :param mid: The mid of this MessagetrackingDlpdetailsDataMessages.  # noqa: E501
        :type: list[int]
        """

        self._mid = mid

    @property
    def mid_header(self):
        """Gets the mid_header of this MessagetrackingDlpdetailsDataMessages.  # noqa: E501


        :return: The mid_header of this MessagetrackingDlpdetailsDataMessages.  # noqa: E501
        :rtype: str
        """
        return self._mid_header

    @mid_header.setter
    def mid_header(self, mid_header):
        """Sets the mid_header of this MessagetrackingDlpdetailsDataMessages.


        :param mid_header: The mid_header of this MessagetrackingDlpdetailsDataMessages.  # noqa: E501
        :type: str
        """

        self._mid_header = mid_header

    @property
    def recipient(self):
        """Gets the recipient of this MessagetrackingDlpdetailsDataMessages.  # noqa: E501


        :return: The recipient of this MessagetrackingDlpdetailsDataMessages.  # noqa: E501
        :rtype: list[str]
        """
        return self._recipient

    @recipient.setter
    def recipient(self, recipient):
        """Sets the recipient of this MessagetrackingDlpdetailsDataMessages.


        :param recipient: The recipient of this MessagetrackingDlpdetailsDataMessages.  # noqa: E501
        :type: list[str]
        """

        self._recipient = recipient

    @property
    def sender(self):
        """Gets the sender of this MessagetrackingDlpdetailsDataMessages.  # noqa: E501


        :return: The sender of this MessagetrackingDlpdetailsDataMessages.  # noqa: E501
        :rtype: str
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """Sets the sender of this MessagetrackingDlpdetailsDataMessages.


        :param sender: The sender of this MessagetrackingDlpdetailsDataMessages.  # noqa: E501
        :type: str
        """

        self._sender = sender

    @property
    def sender_group(self):
        """Gets the sender_group of this MessagetrackingDlpdetailsDataMessages.  # noqa: E501


        :return: The sender_group of this MessagetrackingDlpdetailsDataMessages.  # noqa: E501
        :rtype: str
        """
        return self._sender_group

    @sender_group.setter
    def sender_group(self, sender_group):
        """Sets the sender_group of this MessagetrackingDlpdetailsDataMessages.


        :param sender_group: The sender_group of this MessagetrackingDlpdetailsDataMessages.  # noqa: E501
        :type: str
        """

        self._sender_group = sender_group

    @property
    def sending_host_summary(self):
        """Gets the sending_host_summary of this MessagetrackingDlpdetailsDataMessages.  # noqa: E501


        :return: The sending_host_summary of this MessagetrackingDlpdetailsDataMessages.  # noqa: E501
        :rtype: MessagetrackingAmpdetailsDataMessagesSendingHostSummary
        """
        return self._sending_host_summary

    @sending_host_summary.setter
    def sending_host_summary(self, sending_host_summary):
        """Sets the sending_host_summary of this MessagetrackingDlpdetailsDataMessages.


        :param sending_host_summary: The sending_host_summary of this MessagetrackingDlpdetailsDataMessages.  # noqa: E501
        :type: MessagetrackingAmpdetailsDataMessagesSendingHostSummary
        """

        self._sending_host_summary = sending_host_summary

    @property
    def show_dlp_details(self):
        """Gets the show_dlp_details of this MessagetrackingDlpdetailsDataMessages.  # noqa: E501


        :return: The show_dlp_details of this MessagetrackingDlpdetailsDataMessages.  # noqa: E501
        :rtype: bool
        """
        return self._show_dlp_details

    @show_dlp_details.setter
    def show_dlp_details(self, show_dlp_details):
        """Sets the show_dlp_details of this MessagetrackingDlpdetailsDataMessages.


        :param show_dlp_details: The show_dlp_details of this MessagetrackingDlpdetailsDataMessages.  # noqa: E501
        :type: bool
        """

        self._show_dlp_details = show_dlp_details

    @property
    def smtp_auth_id(self):
        """Gets the smtp_auth_id of this MessagetrackingDlpdetailsDataMessages.  # noqa: E501


        :return: The smtp_auth_id of this MessagetrackingDlpdetailsDataMessages.  # noqa: E501
        :rtype: str
        """
        return self._smtp_auth_id

    @smtp_auth_id.setter
    def smtp_auth_id(self, smtp_auth_id):
        """Sets the smtp_auth_id of this MessagetrackingDlpdetailsDataMessages.


        :param smtp_auth_id: The smtp_auth_id of this MessagetrackingDlpdetailsDataMessages.  # noqa: E501
        :type: str
        """

        self._smtp_auth_id = smtp_auth_id

    @property
    def subject(self):
        """Gets the subject of this MessagetrackingDlpdetailsDataMessages.  # noqa: E501


        :return: The subject of this MessagetrackingDlpdetailsDataMessages.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this MessagetrackingDlpdetailsDataMessages.


        :param subject: The subject of this MessagetrackingDlpdetailsDataMessages.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def timestamp(self):
        """Gets the timestamp of this MessagetrackingDlpdetailsDataMessages.  # noqa: E501


        :return: The timestamp of this MessagetrackingDlpdetailsDataMessages.  # noqa: E501
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this MessagetrackingDlpdetailsDataMessages.


        :param timestamp: The timestamp of this MessagetrackingDlpdetailsDataMessages.  # noqa: E501
        :type: str
        """

        self._timestamp = timestamp

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
        if issubclass(MessagetrackingDlpdetailsDataMessages, dict):
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
        if not isinstance(other, MessagetrackingDlpdetailsDataMessages):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
