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


class V1HosLogsSummaryResponse(object):
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
        'drivers': 'list[V1HosLogsSummaryResponseDrivers]',
        'pagination': 'V1HosLogsSummaryResponsePagination'
    }

    attribute_map = {
        'drivers': 'drivers',
        'pagination': 'pagination'
    }

    def __init__(self, drivers=None, pagination=None, local_vars_configuration=None):  # noqa: E501
        """V1HosLogsSummaryResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._drivers = None
        self._pagination = None
        self.discriminator = None

        if drivers is not None:
            self.drivers = drivers
        if pagination is not None:
            self.pagination = pagination

    @property
    def drivers(self):
        """Gets the drivers of this V1HosLogsSummaryResponse.  # noqa: E501


        :return: The drivers of this V1HosLogsSummaryResponse.  # noqa: E501
        :rtype: list[V1HosLogsSummaryResponseDrivers]
        """
        return self._drivers

    @drivers.setter
    def drivers(self, drivers):
        """Sets the drivers of this V1HosLogsSummaryResponse.


        :param drivers: The drivers of this V1HosLogsSummaryResponse.  # noqa: E501
        :type: list[V1HosLogsSummaryResponseDrivers]
        """

        self._drivers = drivers

    @property
    def pagination(self):
        """Gets the pagination of this V1HosLogsSummaryResponse.  # noqa: E501


        :return: The pagination of this V1HosLogsSummaryResponse.  # noqa: E501
        :rtype: V1HosLogsSummaryResponsePagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this V1HosLogsSummaryResponse.


        :param pagination: The pagination of this V1HosLogsSummaryResponse.  # noqa: E501
        :type: V1HosLogsSummaryResponsePagination
        """

        self._pagination = pagination

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
        if not isinstance(other, V1HosLogsSummaryResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1HosLogsSummaryResponse):
            return True

        return self.to_dict() != other.to_dict()
