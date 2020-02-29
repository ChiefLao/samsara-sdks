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


class VehicleLocationsListResponseData(object):
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
        'id': 'str',
        'locations': 'list[VehicleLocation]',
        'name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'locations': 'locations',
        'name': 'name'
    }

    def __init__(self, id=None, locations=None, name=None, local_vars_configuration=None):  # noqa: E501
        """VehicleLocationsListResponseData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._locations = None
        self._name = None
        self.discriminator = None

        self.id = id
        self.locations = locations
        self.name = name

    @property
    def id(self):
        """Gets the id of this VehicleLocationsListResponseData.  # noqa: E501

        The unique Samsara ID of the Vehicle. This is automatically generated when the Vehicle object is created. It cannot be changed.  # noqa: E501

        :return: The id of this VehicleLocationsListResponseData.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VehicleLocationsListResponseData.

        The unique Samsara ID of the Vehicle. This is automatically generated when the Vehicle object is created. It cannot be changed.  # noqa: E501

        :param id: The id of this VehicleLocationsListResponseData.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def locations(self):
        """Gets the locations of this VehicleLocationsListResponseData.  # noqa: E501

        A list of location events for the given vehicle.  # noqa: E501

        :return: The locations of this VehicleLocationsListResponseData.  # noqa: E501
        :rtype: list[VehicleLocation]
        """
        return self._locations

    @locations.setter
    def locations(self, locations):
        """Sets the locations of this VehicleLocationsListResponseData.

        A list of location events for the given vehicle.  # noqa: E501

        :param locations: The locations of this VehicleLocationsListResponseData.  # noqa: E501
        :type: list[VehicleLocation]
        """
        if self.local_vars_configuration.client_side_validation and locations is None:  # noqa: E501
            raise ValueError("Invalid value for `locations`, must not be `None`")  # noqa: E501

        self._locations = locations

    @property
    def name(self):
        """Gets the name of this VehicleLocationsListResponseData.  # noqa: E501

        The human-readable name of the Vehicle. This is set by a fleet administrator and will appear in both Samsara’s cloud dashboard as well as the Samsara Driver mobile app. **By default**, this name is the serial number of the Samsara Vehicle Gateway. It can be set or updated through the Samsara Dashboard or through the API at any time.  # noqa: E501

        :return: The name of this VehicleLocationsListResponseData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VehicleLocationsListResponseData.

        The human-readable name of the Vehicle. This is set by a fleet administrator and will appear in both Samsara’s cloud dashboard as well as the Samsara Driver mobile app. **By default**, this name is the serial number of the Samsara Vehicle Gateway. It can be set or updated through the Samsara Dashboard or through the API at any time.  # noqa: E501

        :param name: The name of this VehicleLocationsListResponseData.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if not isinstance(other, VehicleLocationsListResponseData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VehicleLocationsListResponseData):
            return True

        return self.to_dict() != other.to_dict()
