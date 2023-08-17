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

class ReportingMailUsersDetailIncomingMarketingMailDataResultSet(object):
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
        'incoming_marketing_mail': 'list[dict(str, object)]'
    }

    attribute_map = {
        'incoming_marketing_mail': 'incoming_marketing_mail'
    }

    def __init__(self, incoming_marketing_mail=None):  # noqa: E501
        """ReportingMailUsersDetailIncomingMarketingMailDataResultSet - a model defined in Swagger"""  # noqa: E501
        self._incoming_marketing_mail = None
        self.discriminator = None
        if incoming_marketing_mail is not None:
            self.incoming_marketing_mail = incoming_marketing_mail

    @property
    def incoming_marketing_mail(self):
        """Gets the incoming_marketing_mail of this ReportingMailUsersDetailIncomingMarketingMailDataResultSet.  # noqa: E501


        :return: The incoming_marketing_mail of this ReportingMailUsersDetailIncomingMarketingMailDataResultSet.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._incoming_marketing_mail

    @incoming_marketing_mail.setter
    def incoming_marketing_mail(self, incoming_marketing_mail):
        """Sets the incoming_marketing_mail of this ReportingMailUsersDetailIncomingMarketingMailDataResultSet.


        :param incoming_marketing_mail: The incoming_marketing_mail of this ReportingMailUsersDetailIncomingMarketingMailDataResultSet.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._incoming_marketing_mail = incoming_marketing_mail

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
        if issubclass(ReportingMailUsersDetailIncomingMarketingMailDataResultSet, dict):
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
        if not isinstance(other, ReportingMailUsersDetailIncomingMarketingMailDataResultSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other