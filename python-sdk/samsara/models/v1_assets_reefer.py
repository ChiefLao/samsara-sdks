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


class V1AssetsReefer(object):
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
        'asset_type': 'str',
        'id': 'int',
        'name': 'str',
        'reefer_stats': 'V1AssetsReeferReeferStats'
    }

    attribute_map = {
        'asset_type': 'assetType',
        'id': 'id',
        'name': 'name',
        'reefer_stats': 'reeferStats'
    }

    def __init__(self, asset_type=None, id=None, name=None, reefer_stats=None, local_vars_configuration=None):  # noqa: E501
        """V1AssetsReefer - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._asset_type = None
        self._id = None
        self._name = None
        self._reefer_stats = None
        self.discriminator = None

        if asset_type is not None:
            self.asset_type = asset_type
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if reefer_stats is not None:
            self.reefer_stats = reefer_stats

    @property
    def asset_type(self):
        """Gets the asset_type of this V1AssetsReefer.  # noqa: E501

        Asset type  # noqa: E501

        :return: The asset_type of this V1AssetsReefer.  # noqa: E501
        :rtype: str
        """
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type):
        """Sets the asset_type of this V1AssetsReefer.

        Asset type  # noqa: E501

        :param asset_type: The asset_type of this V1AssetsReefer.  # noqa: E501
        :type: str
        """

        self._asset_type = asset_type

    @property
    def id(self):
        """Gets the id of this V1AssetsReefer.  # noqa: E501

        Asset ID  # noqa: E501

        :return: The id of this V1AssetsReefer.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V1AssetsReefer.

        Asset ID  # noqa: E501

        :param id: The id of this V1AssetsReefer.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this V1AssetsReefer.  # noqa: E501

        Asset name  # noqa: E501

        :return: The name of this V1AssetsReefer.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1AssetsReefer.

        Asset name  # noqa: E501

        :param name: The name of this V1AssetsReefer.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def reefer_stats(self):
        """Gets the reefer_stats of this V1AssetsReefer.  # noqa: E501


        :return: The reefer_stats of this V1AssetsReefer.  # noqa: E501
        :rtype: V1AssetsReeferReeferStats
        """
        return self._reefer_stats

    @reefer_stats.setter
    def reefer_stats(self, reefer_stats):
        """Sets the reefer_stats of this V1AssetsReefer.


        :param reefer_stats: The reefer_stats of this V1AssetsReefer.  # noqa: E501
        :type: V1AssetsReeferReeferStats
        """

        self._reefer_stats = reefer_stats

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
        if not isinstance(other, V1AssetsReefer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1AssetsReefer):
            return True

        return self.to_dict() != other.to_dict()
