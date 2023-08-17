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

class ConfigLocalQuarantinesGetData(object):
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
        'quarantine_automatic_action': 'bool',
        'quarantine_name': 'str',
        'quarantine_type': 'str',
        'quarantine_retention_period': 'int',
        'quarantine_custom_roles': 'list[object]',
        'quarantine_normal_actions': 'ConfigLocalQuarantinesGetDataQuarantineNormalActions',
        'quarantine_size_used': 'str',
        'quarantine_created_by': 'str',
        'quarantine_groups': 'list[object]',
        'quarantine_users': 'list[object]',
        'quarantine_created_on': 'str',
        'quarantine_retention_units': 'str',
        'quarantine_overflow_actions': 'ConfigLocalQuarantinesGetDataQuarantineOverflowActions'
    }

    attribute_map = {
        'quarantine_automatic_action': 'quarantine_automatic_action',
        'quarantine_name': 'quarantine_name',
        'quarantine_type': 'quarantine_type',
        'quarantine_retention_period': 'quarantine_retention_period',
        'quarantine_custom_roles': 'quarantine_custom_roles',
        'quarantine_normal_actions': 'quarantine_normal_actions',
        'quarantine_size_used': 'quarantine_size_used',
        'quarantine_created_by': 'quarantine_created_by',
        'quarantine_groups': 'quarantine_groups',
        'quarantine_users': 'quarantine_users',
        'quarantine_created_on': 'quarantine_created_on',
        'quarantine_retention_units': 'quarantine_retention_units',
        'quarantine_overflow_actions': 'quarantine_overflow_actions'
    }

    def __init__(self, quarantine_automatic_action=None, quarantine_name=None, quarantine_type=None, quarantine_retention_period=None, quarantine_custom_roles=None, quarantine_normal_actions=None, quarantine_size_used=None, quarantine_created_by=None, quarantine_groups=None, quarantine_users=None, quarantine_created_on=None, quarantine_retention_units=None, quarantine_overflow_actions=None):  # noqa: E501
        """ConfigLocalQuarantinesGetData - a model defined in Swagger"""  # noqa: E501
        self._quarantine_automatic_action = None
        self._quarantine_name = None
        self._quarantine_type = None
        self._quarantine_retention_period = None
        self._quarantine_custom_roles = None
        self._quarantine_normal_actions = None
        self._quarantine_size_used = None
        self._quarantine_created_by = None
        self._quarantine_groups = None
        self._quarantine_users = None
        self._quarantine_created_on = None
        self._quarantine_retention_units = None
        self._quarantine_overflow_actions = None
        self.discriminator = None
        if quarantine_automatic_action is not None:
            self.quarantine_automatic_action = quarantine_automatic_action
        if quarantine_name is not None:
            self.quarantine_name = quarantine_name
        if quarantine_type is not None:
            self.quarantine_type = quarantine_type
        if quarantine_retention_period is not None:
            self.quarantine_retention_period = quarantine_retention_period
        if quarantine_custom_roles is not None:
            self.quarantine_custom_roles = quarantine_custom_roles
        if quarantine_normal_actions is not None:
            self.quarantine_normal_actions = quarantine_normal_actions
        if quarantine_size_used is not None:
            self.quarantine_size_used = quarantine_size_used
        if quarantine_created_by is not None:
            self.quarantine_created_by = quarantine_created_by
        if quarantine_groups is not None:
            self.quarantine_groups = quarantine_groups
        if quarantine_users is not None:
            self.quarantine_users = quarantine_users
        if quarantine_created_on is not None:
            self.quarantine_created_on = quarantine_created_on
        if quarantine_retention_units is not None:
            self.quarantine_retention_units = quarantine_retention_units
        if quarantine_overflow_actions is not None:
            self.quarantine_overflow_actions = quarantine_overflow_actions

    @property
    def quarantine_automatic_action(self):
        """Gets the quarantine_automatic_action of this ConfigLocalQuarantinesGetData.  # noqa: E501


        :return: The quarantine_automatic_action of this ConfigLocalQuarantinesGetData.  # noqa: E501
        :rtype: bool
        """
        return self._quarantine_automatic_action

    @quarantine_automatic_action.setter
    def quarantine_automatic_action(self, quarantine_automatic_action):
        """Sets the quarantine_automatic_action of this ConfigLocalQuarantinesGetData.


        :param quarantine_automatic_action: The quarantine_automatic_action of this ConfigLocalQuarantinesGetData.  # noqa: E501
        :type: bool
        """

        self._quarantine_automatic_action = quarantine_automatic_action

    @property
    def quarantine_name(self):
        """Gets the quarantine_name of this ConfigLocalQuarantinesGetData.  # noqa: E501


        :return: The quarantine_name of this ConfigLocalQuarantinesGetData.  # noqa: E501
        :rtype: str
        """
        return self._quarantine_name

    @quarantine_name.setter
    def quarantine_name(self, quarantine_name):
        """Sets the quarantine_name of this ConfigLocalQuarantinesGetData.


        :param quarantine_name: The quarantine_name of this ConfigLocalQuarantinesGetData.  # noqa: E501
        :type: str
        """

        self._quarantine_name = quarantine_name

    @property
    def quarantine_type(self):
        """Gets the quarantine_type of this ConfigLocalQuarantinesGetData.  # noqa: E501


        :return: The quarantine_type of this ConfigLocalQuarantinesGetData.  # noqa: E501
        :rtype: str
        """
        return self._quarantine_type

    @quarantine_type.setter
    def quarantine_type(self, quarantine_type):
        """Sets the quarantine_type of this ConfigLocalQuarantinesGetData.


        :param quarantine_type: The quarantine_type of this ConfigLocalQuarantinesGetData.  # noqa: E501
        :type: str
        """

        self._quarantine_type = quarantine_type

    @property
    def quarantine_retention_period(self):
        """Gets the quarantine_retention_period of this ConfigLocalQuarantinesGetData.  # noqa: E501


        :return: The quarantine_retention_period of this ConfigLocalQuarantinesGetData.  # noqa: E501
        :rtype: int
        """
        return self._quarantine_retention_period

    @quarantine_retention_period.setter
    def quarantine_retention_period(self, quarantine_retention_period):
        """Sets the quarantine_retention_period of this ConfigLocalQuarantinesGetData.


        :param quarantine_retention_period: The quarantine_retention_period of this ConfigLocalQuarantinesGetData.  # noqa: E501
        :type: int
        """

        self._quarantine_retention_period = quarantine_retention_period

    @property
    def quarantine_custom_roles(self):
        """Gets the quarantine_custom_roles of this ConfigLocalQuarantinesGetData.  # noqa: E501


        :return: The quarantine_custom_roles of this ConfigLocalQuarantinesGetData.  # noqa: E501
        :rtype: list[object]
        """
        return self._quarantine_custom_roles

    @quarantine_custom_roles.setter
    def quarantine_custom_roles(self, quarantine_custom_roles):
        """Sets the quarantine_custom_roles of this ConfigLocalQuarantinesGetData.


        :param quarantine_custom_roles: The quarantine_custom_roles of this ConfigLocalQuarantinesGetData.  # noqa: E501
        :type: list[object]
        """

        self._quarantine_custom_roles = quarantine_custom_roles

    @property
    def quarantine_normal_actions(self):
        """Gets the quarantine_normal_actions of this ConfigLocalQuarantinesGetData.  # noqa: E501


        :return: The quarantine_normal_actions of this ConfigLocalQuarantinesGetData.  # noqa: E501
        :rtype: ConfigLocalQuarantinesGetDataQuarantineNormalActions
        """
        return self._quarantine_normal_actions

    @quarantine_normal_actions.setter
    def quarantine_normal_actions(self, quarantine_normal_actions):
        """Sets the quarantine_normal_actions of this ConfigLocalQuarantinesGetData.


        :param quarantine_normal_actions: The quarantine_normal_actions of this ConfigLocalQuarantinesGetData.  # noqa: E501
        :type: ConfigLocalQuarantinesGetDataQuarantineNormalActions
        """

        self._quarantine_normal_actions = quarantine_normal_actions

    @property
    def quarantine_size_used(self):
        """Gets the quarantine_size_used of this ConfigLocalQuarantinesGetData.  # noqa: E501


        :return: The quarantine_size_used of this ConfigLocalQuarantinesGetData.  # noqa: E501
        :rtype: str
        """
        return self._quarantine_size_used

    @quarantine_size_used.setter
    def quarantine_size_used(self, quarantine_size_used):
        """Sets the quarantine_size_used of this ConfigLocalQuarantinesGetData.


        :param quarantine_size_used: The quarantine_size_used of this ConfigLocalQuarantinesGetData.  # noqa: E501
        :type: str
        """

        self._quarantine_size_used = quarantine_size_used

    @property
    def quarantine_created_by(self):
        """Gets the quarantine_created_by of this ConfigLocalQuarantinesGetData.  # noqa: E501


        :return: The quarantine_created_by of this ConfigLocalQuarantinesGetData.  # noqa: E501
        :rtype: str
        """
        return self._quarantine_created_by

    @quarantine_created_by.setter
    def quarantine_created_by(self, quarantine_created_by):
        """Sets the quarantine_created_by of this ConfigLocalQuarantinesGetData.


        :param quarantine_created_by: The quarantine_created_by of this ConfigLocalQuarantinesGetData.  # noqa: E501
        :type: str
        """

        self._quarantine_created_by = quarantine_created_by

    @property
    def quarantine_groups(self):
        """Gets the quarantine_groups of this ConfigLocalQuarantinesGetData.  # noqa: E501


        :return: The quarantine_groups of this ConfigLocalQuarantinesGetData.  # noqa: E501
        :rtype: list[object]
        """
        return self._quarantine_groups

    @quarantine_groups.setter
    def quarantine_groups(self, quarantine_groups):
        """Sets the quarantine_groups of this ConfigLocalQuarantinesGetData.


        :param quarantine_groups: The quarantine_groups of this ConfigLocalQuarantinesGetData.  # noqa: E501
        :type: list[object]
        """

        self._quarantine_groups = quarantine_groups

    @property
    def quarantine_users(self):
        """Gets the quarantine_users of this ConfigLocalQuarantinesGetData.  # noqa: E501


        :return: The quarantine_users of this ConfigLocalQuarantinesGetData.  # noqa: E501
        :rtype: list[object]
        """
        return self._quarantine_users

    @quarantine_users.setter
    def quarantine_users(self, quarantine_users):
        """Sets the quarantine_users of this ConfigLocalQuarantinesGetData.


        :param quarantine_users: The quarantine_users of this ConfigLocalQuarantinesGetData.  # noqa: E501
        :type: list[object]
        """

        self._quarantine_users = quarantine_users

    @property
    def quarantine_created_on(self):
        """Gets the quarantine_created_on of this ConfigLocalQuarantinesGetData.  # noqa: E501


        :return: The quarantine_created_on of this ConfigLocalQuarantinesGetData.  # noqa: E501
        :rtype: str
        """
        return self._quarantine_created_on

    @quarantine_created_on.setter
    def quarantine_created_on(self, quarantine_created_on):
        """Sets the quarantine_created_on of this ConfigLocalQuarantinesGetData.


        :param quarantine_created_on: The quarantine_created_on of this ConfigLocalQuarantinesGetData.  # noqa: E501
        :type: str
        """

        self._quarantine_created_on = quarantine_created_on

    @property
    def quarantine_retention_units(self):
        """Gets the quarantine_retention_units of this ConfigLocalQuarantinesGetData.  # noqa: E501


        :return: The quarantine_retention_units of this ConfigLocalQuarantinesGetData.  # noqa: E501
        :rtype: str
        """
        return self._quarantine_retention_units

    @quarantine_retention_units.setter
    def quarantine_retention_units(self, quarantine_retention_units):
        """Sets the quarantine_retention_units of this ConfigLocalQuarantinesGetData.


        :param quarantine_retention_units: The quarantine_retention_units of this ConfigLocalQuarantinesGetData.  # noqa: E501
        :type: str
        """

        self._quarantine_retention_units = quarantine_retention_units

    @property
    def quarantine_overflow_actions(self):
        """Gets the quarantine_overflow_actions of this ConfigLocalQuarantinesGetData.  # noqa: E501


        :return: The quarantine_overflow_actions of this ConfigLocalQuarantinesGetData.  # noqa: E501
        :rtype: ConfigLocalQuarantinesGetDataQuarantineOverflowActions
        """
        return self._quarantine_overflow_actions

    @quarantine_overflow_actions.setter
    def quarantine_overflow_actions(self, quarantine_overflow_actions):
        """Sets the quarantine_overflow_actions of this ConfigLocalQuarantinesGetData.


        :param quarantine_overflow_actions: The quarantine_overflow_actions of this ConfigLocalQuarantinesGetData.  # noqa: E501
        :type: ConfigLocalQuarantinesGetDataQuarantineOverflowActions
        """

        self._quarantine_overflow_actions = quarantine_overflow_actions

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
        if issubclass(ConfigLocalQuarantinesGetData, dict):
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
        if not isinstance(other, ConfigLocalQuarantinesGetData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
