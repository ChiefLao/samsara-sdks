# coding: utf-8

"""
    Samsara API

    This is the Samsara API.  # noqa: E501

    The version of the OpenAPI document: 2019-12-12
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from samsara.configuration import Configuration


class V1DvirListResponse(object):
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
        'dvirs': 'list[V1DvirBase]'
    }

    attribute_map = {
        'dvirs': 'dvirs'
    }

    def __init__(self, dvirs=None, local_vars_configuration=None):  # noqa: E501
        """V1DvirListResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._dvirs = None
        self.discriminator = None

        if dvirs is not None:
            self.dvirs = dvirs

    @property
    def dvirs(self):
        """Gets the dvirs of this V1DvirListResponse.  # noqa: E501


        :return: The dvirs of this V1DvirListResponse.  # noqa: E501
        :rtype: list[V1DvirBase]
        """
        return self._dvirs

    @dvirs.setter
    def dvirs(self, dvirs):
        """Sets the dvirs of this V1DvirListResponse.


        :param dvirs: The dvirs of this V1DvirListResponse.  # noqa: E501
        :type: list[V1DvirBase]
        """

        self._dvirs = dvirs

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
        if not isinstance(other, V1DvirListResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1DvirListResponse):
            return True

        return self.to_dict() != other.to_dict()
