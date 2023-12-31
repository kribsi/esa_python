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

class ReportingMailDestinationDomainDetailDetectedAmpDataResultSet(object):
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
        'detected_amp': 'list[dict(str, object)]'
    }

    attribute_map = {
        'detected_amp': 'detected_amp'
    }

    def __init__(self, detected_amp=None):  # noqa: E501
        """ReportingMailDestinationDomainDetailDetectedAmpDataResultSet - a model defined in Swagger"""  # noqa: E501
        self._detected_amp = None
        self.discriminator = None
        if detected_amp is not None:
            self.detected_amp = detected_amp

    @property
    def detected_amp(self):
        """Gets the detected_amp of this ReportingMailDestinationDomainDetailDetectedAmpDataResultSet.  # noqa: E501


        :return: The detected_amp of this ReportingMailDestinationDomainDetailDetectedAmpDataResultSet.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._detected_amp

    @detected_amp.setter
    def detected_amp(self, detected_amp):
        """Sets the detected_amp of this ReportingMailDestinationDomainDetailDetectedAmpDataResultSet.


        :param detected_amp: The detected_amp of this ReportingMailDestinationDomainDetailDetectedAmpDataResultSet.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._detected_amp = detected_amp

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
        if issubclass(ReportingMailDestinationDomainDetailDetectedAmpDataResultSet, dict):
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
        if not isinstance(other, ReportingMailDestinationDomainDetailDetectedAmpDataResultSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
