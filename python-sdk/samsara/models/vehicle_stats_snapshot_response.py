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


class VehicleStatsSnapshotResponse(object):
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
        'name': 'str',
        'engine_state': 'VehicleEngineState',
        'fuel_percent': 'VehicleFuelPercent',
        'gps_distance_meters': 'VehicleGpsDistanceMeters',
        'gps_odometer_meters': 'VehicleGpsOdometerMeters',
        'obd_engine_seconds': 'VehicleObdEngineSeconds',
        'obd_odometer_meters': 'VehicleObdOdometerMeters'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'engine_state': 'engineState',
        'fuel_percent': 'fuelPercent',
        'gps_distance_meters': 'gpsDistanceMeters',
        'gps_odometer_meters': 'gpsOdometerMeters',
        'obd_engine_seconds': 'obdEngineSeconds',
        'obd_odometer_meters': 'obdOdometerMeters'
    }

    def __init__(self, id=None, name=None, engine_state=None, fuel_percent=None, gps_distance_meters=None, gps_odometer_meters=None, obd_engine_seconds=None, obd_odometer_meters=None, local_vars_configuration=None):  # noqa: E501
        """VehicleStatsSnapshotResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._engine_state = None
        self._fuel_percent = None
        self._gps_distance_meters = None
        self._gps_odometer_meters = None
        self._obd_engine_seconds = None
        self._obd_odometer_meters = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if engine_state is not None:
            self.engine_state = engine_state
        if fuel_percent is not None:
            self.fuel_percent = fuel_percent
        if gps_distance_meters is not None:
            self.gps_distance_meters = gps_distance_meters
        if gps_odometer_meters is not None:
            self.gps_odometer_meters = gps_odometer_meters
        if obd_engine_seconds is not None:
            self.obd_engine_seconds = obd_engine_seconds
        if obd_odometer_meters is not None:
            self.obd_odometer_meters = obd_odometer_meters

    @property
    def id(self):
        """Gets the id of this VehicleStatsSnapshotResponse.  # noqa: E501

        ID of the vehicle.  # noqa: E501

        :return: The id of this VehicleStatsSnapshotResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VehicleStatsSnapshotResponse.

        ID of the vehicle.  # noqa: E501

        :param id: The id of this VehicleStatsSnapshotResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this VehicleStatsSnapshotResponse.  # noqa: E501

        Name of the vehicle.  # noqa: E501

        :return: The name of this VehicleStatsSnapshotResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VehicleStatsSnapshotResponse.

        Name of the vehicle.  # noqa: E501

        :param name: The name of this VehicleStatsSnapshotResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def engine_state(self):
        """Gets the engine_state of this VehicleStatsSnapshotResponse.  # noqa: E501


        :return: The engine_state of this VehicleStatsSnapshotResponse.  # noqa: E501
        :rtype: VehicleEngineState
        """
        return self._engine_state

    @engine_state.setter
    def engine_state(self, engine_state):
        """Sets the engine_state of this VehicleStatsSnapshotResponse.


        :param engine_state: The engine_state of this VehicleStatsSnapshotResponse.  # noqa: E501
        :type: VehicleEngineState
        """

        self._engine_state = engine_state

    @property
    def fuel_percent(self):
        """Gets the fuel_percent of this VehicleStatsSnapshotResponse.  # noqa: E501


        :return: The fuel_percent of this VehicleStatsSnapshotResponse.  # noqa: E501
        :rtype: VehicleFuelPercent
        """
        return self._fuel_percent

    @fuel_percent.setter
    def fuel_percent(self, fuel_percent):
        """Sets the fuel_percent of this VehicleStatsSnapshotResponse.


        :param fuel_percent: The fuel_percent of this VehicleStatsSnapshotResponse.  # noqa: E501
        :type: VehicleFuelPercent
        """

        self._fuel_percent = fuel_percent

    @property
    def gps_distance_meters(self):
        """Gets the gps_distance_meters of this VehicleStatsSnapshotResponse.  # noqa: E501


        :return: The gps_distance_meters of this VehicleStatsSnapshotResponse.  # noqa: E501
        :rtype: VehicleGpsDistanceMeters
        """
        return self._gps_distance_meters

    @gps_distance_meters.setter
    def gps_distance_meters(self, gps_distance_meters):
        """Sets the gps_distance_meters of this VehicleStatsSnapshotResponse.


        :param gps_distance_meters: The gps_distance_meters of this VehicleStatsSnapshotResponse.  # noqa: E501
        :type: VehicleGpsDistanceMeters
        """

        self._gps_distance_meters = gps_distance_meters

    @property
    def gps_odometer_meters(self):
        """Gets the gps_odometer_meters of this VehicleStatsSnapshotResponse.  # noqa: E501


        :return: The gps_odometer_meters of this VehicleStatsSnapshotResponse.  # noqa: E501
        :rtype: VehicleGpsOdometerMeters
        """
        return self._gps_odometer_meters

    @gps_odometer_meters.setter
    def gps_odometer_meters(self, gps_odometer_meters):
        """Sets the gps_odometer_meters of this VehicleStatsSnapshotResponse.


        :param gps_odometer_meters: The gps_odometer_meters of this VehicleStatsSnapshotResponse.  # noqa: E501
        :type: VehicleGpsOdometerMeters
        """

        self._gps_odometer_meters = gps_odometer_meters

    @property
    def obd_engine_seconds(self):
        """Gets the obd_engine_seconds of this VehicleStatsSnapshotResponse.  # noqa: E501


        :return: The obd_engine_seconds of this VehicleStatsSnapshotResponse.  # noqa: E501
        :rtype: VehicleObdEngineSeconds
        """
        return self._obd_engine_seconds

    @obd_engine_seconds.setter
    def obd_engine_seconds(self, obd_engine_seconds):
        """Sets the obd_engine_seconds of this VehicleStatsSnapshotResponse.


        :param obd_engine_seconds: The obd_engine_seconds of this VehicleStatsSnapshotResponse.  # noqa: E501
        :type: VehicleObdEngineSeconds
        """

        self._obd_engine_seconds = obd_engine_seconds

    @property
    def obd_odometer_meters(self):
        """Gets the obd_odometer_meters of this VehicleStatsSnapshotResponse.  # noqa: E501


        :return: The obd_odometer_meters of this VehicleStatsSnapshotResponse.  # noqa: E501
        :rtype: VehicleObdOdometerMeters
        """
        return self._obd_odometer_meters

    @obd_odometer_meters.setter
    def obd_odometer_meters(self, obd_odometer_meters):
        """Sets the obd_odometer_meters of this VehicleStatsSnapshotResponse.


        :param obd_odometer_meters: The obd_odometer_meters of this VehicleStatsSnapshotResponse.  # noqa: E501
        :type: VehicleObdOdometerMeters
        """

        self._obd_odometer_meters = obd_odometer_meters

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
        if not isinstance(other, VehicleStatsSnapshotResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VehicleStatsSnapshotResponse):
            return True

        return self.to_dict() != other.to_dict()
