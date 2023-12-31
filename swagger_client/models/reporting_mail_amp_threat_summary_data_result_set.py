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

class ReportingMailAmpThreatSummaryDataResultSet(object):
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
        'incoming_malicious': 'int',
        'outgoing_malicious': 'int'
    }

    attribute_map = {
        'incoming_malicious': 'incoming_malicious',
        'outgoing_malicious': 'outgoing_malicious'
    }

    def __init__(self, incoming_malicious=None, outgoing_malicious=None):  # noqa: E501
        """ReportingMailAmpThreatSummaryDataResultSet - a model defined in Swagger"""  # noqa: E501
        self._incoming_malicious = None
        self._outgoing_malicious = None
        self.discriminator = None
        if incoming_malicious is not None:
            self.incoming_malicious = incoming_malicious
        if outgoing_malicious is not None:
            self.outgoing_malicious = outgoing_malicious

    @property
    def incoming_malicious(self):
        """Gets the incoming_malicious of this ReportingMailAmpThreatSummaryDataResultSet.  # noqa: E501


        :return: The incoming_malicious of this ReportingMailAmpThreatSummaryDataResultSet.  # noqa: E501
        :rtype: int
        """
        return self._incoming_malicious

    @incoming_malicious.setter
    def incoming_malicious(self, incoming_malicious):
        """Sets the incoming_malicious of this ReportingMailAmpThreatSummaryDataResultSet.


        :param incoming_malicious: The incoming_malicious of this ReportingMailAmpThreatSummaryDataResultSet.  # noqa: E501
        :type: int
        """

        self._incoming_malicious = incoming_malicious

    @property
    def outgoing_malicious(self):
        """Gets the outgoing_malicious of this ReportingMailAmpThreatSummaryDataResultSet.  # noqa: E501


        :return: The outgoing_malicious of this ReportingMailAmpThreatSummaryDataResultSet.  # noqa: E501
        :rtype: int
        """
        return self._outgoing_malicious

    @outgoing_malicious.setter
    def outgoing_malicious(self, outgoing_malicious):
        """Sets the outgoing_malicious of this ReportingMailAmpThreatSummaryDataResultSet.


        :param outgoing_malicious: The outgoing_malicious of this ReportingMailAmpThreatSummaryDataResultSet.  # noqa: E501
        :type: int
        """

        self._outgoing_malicious = outgoing_malicious

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
        if issubclass(ReportingMailAmpThreatSummaryDataResultSet, dict):
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
        if not isinstance(other, ReportingMailAmpThreatSummaryDataResultSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
