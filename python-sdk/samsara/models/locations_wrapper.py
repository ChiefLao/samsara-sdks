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


class LocationsWrapper(object):
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
        'latitude': 'float',
        'longitude': 'float',
        'heading': 'float',
        'reverse_geo': 'ReverseGeo',
        'speed': 'float',
        'time': 'str'
    }

    attribute_map = {
        'latitude': 'latitude',
        'longitude': 'longitude',
        'heading': 'heading',
        'reverse_geo': 'reverseGeo',
        'speed': 'speed',
        'time': 'time'
    }

    def __init__(self, latitude=None, longitude=None, heading=None, reverse_geo=None, speed=None, time=None, local_vars_configuration=None):  # noqa: E501
        """LocationsWrapper - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._latitude = None
        self._longitude = None
        self._heading = None
        self._reverse_geo = None
        self._speed = None
        self._time = None
        self.discriminator = None

        self.latitude = latitude
        self.longitude = longitude
        if heading is not None:
            self.heading = heading
        if reverse_geo is not None:
            self.reverse_geo = reverse_geo
        if speed is not None:
            self.speed = speed
        self.time = time

    @property
    def latitude(self):
        """Gets the latitude of this LocationsWrapper.  # noqa: E501

        GPS latitude represented in degrees  # noqa: E501

        :return: The latitude of this LocationsWrapper.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this LocationsWrapper.

        GPS latitude represented in degrees  # noqa: E501

        :param latitude: The latitude of this LocationsWrapper.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and latitude is None:  # noqa: E501
            raise ValueError("Invalid value for `latitude`, must not be `None`")  # noqa: E501

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this LocationsWrapper.  # noqa: E501

        GPS longitude represented in degrees  # noqa: E501

        :return: The longitude of this LocationsWrapper.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this LocationsWrapper.

        GPS longitude represented in degrees  # noqa: E501

        :param longitude: The longitude of this LocationsWrapper.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and longitude is None:  # noqa: E501
            raise ValueError("Invalid value for `longitude`, must not be `None`")  # noqa: E501

        self._longitude = longitude

    @property
    def heading(self):
        """Gets the heading of this LocationsWrapper.  # noqa: E501

        Heading of the vehicle in degrees.  # noqa: E501

        :return: The heading of this LocationsWrapper.  # noqa: E501
        :rtype: float
        """
        return self._heading

    @heading.setter
    def heading(self, heading):
        """Sets the heading of this LocationsWrapper.

        Heading of the vehicle in degrees.  # noqa: E501

        :param heading: The heading of this LocationsWrapper.  # noqa: E501
        :type: float
        """

        self._heading = heading

    @property
    def reverse_geo(self):
        """Gets the reverse_geo of this LocationsWrapper.  # noqa: E501


        :return: The reverse_geo of this LocationsWrapper.  # noqa: E501
        :rtype: ReverseGeo
        """
        return self._reverse_geo

    @reverse_geo.setter
    def reverse_geo(self, reverse_geo):
        """Sets the reverse_geo of this LocationsWrapper.


        :param reverse_geo: The reverse_geo of this LocationsWrapper.  # noqa: E501
        :type: ReverseGeo
        """

        self._reverse_geo = reverse_geo

    @property
    def speed(self):
        """Gets the speed of this LocationsWrapper.  # noqa: E501

        Speed of the vehicle in miles per hour.  # noqa: E501

        :return: The speed of this LocationsWrapper.  # noqa: E501
        :rtype: float
        """
        return self._speed

    @speed.setter
    def speed(self, speed):
        """Sets the speed of this LocationsWrapper.

        Speed of the vehicle in miles per hour.  # noqa: E501

        :param speed: The speed of this LocationsWrapper.  # noqa: E501
        :type: float
        """

        self._speed = speed

    @property
    def time(self):
        """Gets the time of this LocationsWrapper.  # noqa: E501

        UTC timestamp in RFC 3339 milliseconds format.  # noqa: E501

        :return: The time of this LocationsWrapper.  # noqa: E501
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this LocationsWrapper.

        UTC timestamp in RFC 3339 milliseconds format.  # noqa: E501

        :param time: The time of this LocationsWrapper.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and time is None:  # noqa: E501
            raise ValueError("Invalid value for `time`, must not be `None`")  # noqa: E501

        self._time = time

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
        if not isinstance(other, LocationsWrapper):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LocationsWrapper):
            return True

        return self.to_dict() != other.to_dict()
