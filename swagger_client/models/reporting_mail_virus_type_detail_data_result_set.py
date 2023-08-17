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

class ReportingMailVirusTypeDetailDataResultSet(object):
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
        'incoming_total_recipients': 'list[dict(str, object)]',
        'outgoing_total_recipients': 'list[dict(str, object)]',
        'total_recipients': 'list[dict(str, object)]'
    }

    attribute_map = {
        'incoming_total_recipients': 'incoming_total_recipients',
        'outgoing_total_recipients': 'outgoing_total_recipients',
        'total_recipients': 'total_recipients'
    }

    def __init__(self, incoming_total_recipients=None, outgoing_total_recipients=None, total_recipients=None):  # noqa: E501
        """ReportingMailVirusTypeDetailDataResultSet - a model defined in Swagger"""  # noqa: E501
        self._incoming_total_recipients = None
        self._outgoing_total_recipients = None
        self._total_recipients = None
        self.discriminator = None
        if incoming_total_recipients is not None:
            self.incoming_total_recipients = incoming_total_recipients
        if outgoing_total_recipients is not None:
            self.outgoing_total_recipients = outgoing_total_recipients
        if total_recipients is not None:
            self.total_recipients = total_recipients

    @property
    def incoming_total_recipients(self):
        """Gets the incoming_total_recipients of this ReportingMailVirusTypeDetailDataResultSet.  # noqa: E501


        :return: The incoming_total_recipients of this ReportingMailVirusTypeDetailDataResultSet.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._incoming_total_recipients

    @incoming_total_recipients.setter
    def incoming_total_recipients(self, incoming_total_recipients):
        """Sets the incoming_total_recipients of this ReportingMailVirusTypeDetailDataResultSet.


        :param incoming_total_recipients: The incoming_total_recipients of this ReportingMailVirusTypeDetailDataResultSet.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._incoming_total_recipients = incoming_total_recipients

    @property
    def outgoing_total_recipients(self):
        """Gets the outgoing_total_recipients of this ReportingMailVirusTypeDetailDataResultSet.  # noqa: E501


        :return: The outgoing_total_recipients of this ReportingMailVirusTypeDetailDataResultSet.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._outgoing_total_recipients

    @outgoing_total_recipients.setter
    def outgoing_total_recipients(self, outgoing_total_recipients):
        """Sets the outgoing_total_recipients of this ReportingMailVirusTypeDetailDataResultSet.


        :param outgoing_total_recipients: The outgoing_total_recipients of this ReportingMailVirusTypeDetailDataResultSet.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._outgoing_total_recipients = outgoing_total_recipients

    @property
    def total_recipients(self):
        """Gets the total_recipients of this ReportingMailVirusTypeDetailDataResultSet.  # noqa: E501


        :return: The total_recipients of this ReportingMailVirusTypeDetailDataResultSet.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._total_recipients

    @total_recipients.setter
    def total_recipients(self, total_recipients):
        """Sets the total_recipients of this ReportingMailVirusTypeDetailDataResultSet.


        :param total_recipients: The total_recipients of this ReportingMailVirusTypeDetailDataResultSet.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._total_recipients = total_recipients

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
        if issubclass(ReportingMailVirusTypeDetailDataResultSet, dict):
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
        if not isinstance(other, ReportingMailVirusTypeDetailDataResultSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
