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


class V1VehicleHarshEventResponseLocation(object):
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
        'address': 'str',
        'latitude': 'float',
        'longitude': 'float'
    }

    attribute_map = {
        'address': 'address',
        'latitude': 'latitude',
        'longitude': 'longitude'
    }

    def __init__(self, address=None, latitude=None, longitude=None, local_vars_configuration=None):  # noqa: E501
        """V1VehicleHarshEventResponseLocation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._address = None
        self._latitude = None
        self._longitude = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if latitude is not None:
            self.latitude = latitude
        if longitude is not None:
            self.longitude = longitude

    @property
    def address(self):
        """Gets the address of this V1VehicleHarshEventResponseLocation.  # noqa: E501

        Address of location where the harsh event occurred  # noqa: E501

        :return: The address of this V1VehicleHarshEventResponseLocation.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this V1VehicleHarshEventResponseLocation.

        Address of location where the harsh event occurred  # noqa: E501

        :param address: The address of this V1VehicleHarshEventResponseLocation.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def latitude(self):
        """Gets the latitude of this V1VehicleHarshEventResponseLocation.  # noqa: E501

        Latitude of location where the harsh event occurred  # noqa: E501

        :return: The latitude of this V1VehicleHarshEventResponseLocation.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this V1VehicleHarshEventResponseLocation.

        Latitude of location where the harsh event occurred  # noqa: E501

        :param latitude: The latitude of this V1VehicleHarshEventResponseLocation.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this V1VehicleHarshEventResponseLocation.  # noqa: E501

        Longitude of location where the harsh event occurred  # noqa: E501

        :return: The longitude of this V1VehicleHarshEventResponseLocation.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this V1VehicleHarshEventResponseLocation.

        Longitude of location where the harsh event occurred  # noqa: E501

        :param longitude: The longitude of this V1VehicleHarshEventResponseLocation.  # noqa: E501
        :type: float
        """

        self._longitude = longitude

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
        if not isinstance(other, V1VehicleHarshEventResponseLocation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1VehicleHarshEventResponseLocation):
            return True

        return self.to_dict() != other.to_dict()
