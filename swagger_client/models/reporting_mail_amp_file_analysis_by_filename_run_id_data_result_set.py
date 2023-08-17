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

class ReportingMailAmpFileAnalysisByFilenameRunIdDataResultSet(object):
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
        'run_id': 'list[dict(str, object)]'
    }

    attribute_map = {
        'run_id': 'run_id'
    }

    def __init__(self, run_id=None):  # noqa: E501
        """ReportingMailAmpFileAnalysisByFilenameRunIdDataResultSet - a model defined in Swagger"""  # noqa: E501
        self._run_id = None
        self.discriminator = None
        if run_id is not None:
            self.run_id = run_id

    @property
    def run_id(self):
        """Gets the run_id of this ReportingMailAmpFileAnalysisByFilenameRunIdDataResultSet.  # noqa: E501


        :return: The run_id of this ReportingMailAmpFileAnalysisByFilenameRunIdDataResultSet.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._run_id

    @run_id.setter
    def run_id(self, run_id):
        """Sets the run_id of this ReportingMailAmpFileAnalysisByFilenameRunIdDataResultSet.


        :param run_id: The run_id of this ReportingMailAmpFileAnalysisByFilenameRunIdDataResultSet.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._run_id = run_id

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
        if issubclass(ReportingMailAmpFileAnalysisByFilenameRunIdDataResultSet, dict):
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
        if not isinstance(other, ReportingMailAmpFileAnalysisByFilenameRunIdDataResultSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
