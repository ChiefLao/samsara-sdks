# coding: utf-8

"""
    Samsara API

    Integrate your data with the Samsara API, customize the Samsara experience, and join a community of developers building with Samsara.  # noqa: E501

    The version of the OpenAPI document: 2019-12-12
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from samsara.configuration import Configuration


class V1AssetReeferResponseReeferStatsAlarms1(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'alarms': 'list[V1AssetReeferResponseReeferStatsAlarms]',
        'changed_at_ms': 'int'
    }

    attribute_map = {
        'alarms': 'alarms',
        'changed_at_ms': 'changedAtMs'
    }

    def __init__(self, alarms=None, changed_at_ms=None, local_vars_configuration=None):  # noqa: E501
        """V1AssetReeferResponseReeferStatsAlarms1 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._alarms = None
        self._changed_at_ms = None
        self.discriminator = None

        if alarms is not None:
            self.alarms = alarms
        if changed_at_ms is not None:
            self.changed_at_ms = changed_at_ms

    @property
    def alarms(self):
        """Gets the alarms of this V1AssetReeferResponseReeferStatsAlarms1.  # noqa: E501


        :return: The alarms of this V1AssetReeferResponseReeferStatsAlarms1.  # noqa: E501
        :rtype: list[V1AssetReeferResponseReeferStatsAlarms]
        """
        return self._alarms

    @alarms.setter
    def alarms(self, alarms):
        """Sets the alarms of this V1AssetReeferResponseReeferStatsAlarms1.


        :param alarms: The alarms of this V1AssetReeferResponseReeferStatsAlarms1.  # noqa: E501
        :type: list[V1AssetReeferResponseReeferStatsAlarms]
        """

        self._alarms = alarms

    @property
    def changed_at_ms(self):
        """Gets the changed_at_ms of this V1AssetReeferResponseReeferStatsAlarms1.  # noqa: E501

        Timestamp when the alarms were reported, in Unix milliseconds since epoch  # noqa: E501

        :return: The changed_at_ms of this V1AssetReeferResponseReeferStatsAlarms1.  # noqa: E501
        :rtype: int
        """
        return self._changed_at_ms

    @changed_at_ms.setter
    def changed_at_ms(self, changed_at_ms):
        """Sets the changed_at_ms of this V1AssetReeferResponseReeferStatsAlarms1.

        Timestamp when the alarms were reported, in Unix milliseconds since epoch  # noqa: E501

        :param changed_at_ms: The changed_at_ms of this V1AssetReeferResponseReeferStatsAlarms1.  # noqa: E501
        :type: int
        """

        self._changed_at_ms = changed_at_ms

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1AssetReeferResponseReeferStatsAlarms1):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1AssetReeferResponseReeferStatsAlarms1):
            return True

        return self.to_dict() != other.to_dict()
