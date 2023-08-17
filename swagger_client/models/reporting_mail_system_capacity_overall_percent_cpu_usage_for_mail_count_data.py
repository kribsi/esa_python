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

class ReportingMailSystemCapacityOverallPercentCpuUsageForMailCountData(object):
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
        'result_set': 'ReportingMailSystemCapacityOverallPercentCpuUsageForMailCountDataResultSet',
        'type': 'str'
    }

    attribute_map = {
        'result_set': 'resultSet',
        'type': 'type'
    }

    def __init__(self, result_set=None, type=None):  # noqa: E501
        """ReportingMailSystemCapacityOverallPercentCpuUsageForMailCountData - a model defined in Swagger"""  # noqa: E501
        self._result_set = None
        self._type = None
        self.discriminator = None
        if result_set is not None:
            self.result_set = result_set
        if type is not None:
            self.type = type

    @property
    def result_set(self):
        """Gets the result_set of this ReportingMailSystemCapacityOverallPercentCpuUsageForMailCountData.  # noqa: E501


        :return: The result_set of this ReportingMailSystemCapacityOverallPercentCpuUsageForMailCountData.  # noqa: E501
        :rtype: ReportingMailSystemCapacityOverallPercentCpuUsageForMailCountDataResultSet
        """
        return self._result_set

    @result_set.setter
    def result_set(self, result_set):
        """Sets the result_set of this ReportingMailSystemCapacityOverallPercentCpuUsageForMailCountData.


        :param result_set: The result_set of this ReportingMailSystemCapacityOverallPercentCpuUsageForMailCountData.  # noqa: E501
        :type: ReportingMailSystemCapacityOverallPercentCpuUsageForMailCountDataResultSet
        """

        self._result_set = result_set

    @property
    def type(self):
        """Gets the type of this ReportingMailSystemCapacityOverallPercentCpuUsageForMailCountData.  # noqa: E501


        :return: The type of this ReportingMailSystemCapacityOverallPercentCpuUsageForMailCountData.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ReportingMailSystemCapacityOverallPercentCpuUsageForMailCountData.


        :param type: The type of this ReportingMailSystemCapacityOverallPercentCpuUsageForMailCountData.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(ReportingMailSystemCapacityOverallPercentCpuUsageForMailCountData, dict):
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
        if not isinstance(other, ReportingMailSystemCapacityOverallPercentCpuUsageForMailCountData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
