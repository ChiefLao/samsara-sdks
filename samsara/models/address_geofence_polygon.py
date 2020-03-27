# coding: utf-8

"""
    Samsara API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2019-12-12
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from samsara.configuration import Configuration


class AddressGeofencePolygon(object):
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
        'vertices': 'list[AddressGeofencePolygonVertices]'
    }

    attribute_map = {
        'vertices': 'vertices'
    }

    def __init__(self, vertices=None, local_vars_configuration=None):  # noqa: E501
        """AddressGeofencePolygon - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._vertices = None
        self.discriminator = None

        self.vertices = vertices

    @property
    def vertices(self):
        """Gets the vertices of this AddressGeofencePolygon.  # noqa: E501

        The vertices of the polygon geofence. These geofence vertices describe the perimeter of the polygon, and must consist of at least 3 vertices and less than 40.  # noqa: E501

        :return: The vertices of this AddressGeofencePolygon.  # noqa: E501
        :rtype: list[AddressGeofencePolygonVertices]
        """
        return self._vertices

    @vertices.setter
    def vertices(self, vertices):
        """Sets the vertices of this AddressGeofencePolygon.

        The vertices of the polygon geofence. These geofence vertices describe the perimeter of the polygon, and must consist of at least 3 vertices and less than 40.  # noqa: E501

        :param vertices: The vertices of this AddressGeofencePolygon.  # noqa: E501
        :type: list[AddressGeofencePolygonVertices]
        """
        if self.local_vars_configuration.client_side_validation and vertices is None:  # noqa: E501
            raise ValueError("Invalid value for `vertices`, must not be `None`")  # noqa: E501

        self._vertices = vertices

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
        if not isinstance(other, AddressGeofencePolygon):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddressGeofencePolygon):
            return True

        return self.to_dict() != other.to_dict()
