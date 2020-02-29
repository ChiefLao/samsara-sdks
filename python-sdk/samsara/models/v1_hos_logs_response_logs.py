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


class V1HosLogsResponseLogs(object):
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
        'codriver_ids': 'list[float]',
        'driver_id': 'int',
        'group_id': 'int',
        'hos_status_type': 'str',
        'loc_city': 'str',
        'loc_lat': 'float',
        'loc_lng': 'float',
        'loc_name': 'str',
        'loc_state': 'str',
        'log_start_ms': 'int',
        'remark': 'str',
        'vehicle_id': 'int'
    }

    attribute_map = {
        'codriver_ids': 'codriverIds',
        'driver_id': 'driverId',
        'group_id': 'groupId',
        'hos_status_type': 'hosStatusType',
        'loc_city': 'locCity',
        'loc_lat': 'locLat',
        'loc_lng': 'locLng',
        'loc_name': 'locName',
        'loc_state': 'locState',
        'log_start_ms': 'logStartMs',
        'remark': 'remark',
        'vehicle_id': 'vehicleId'
    }

    def __init__(self, codriver_ids=None, driver_id=None, group_id=None, hos_status_type=None, loc_city=None, loc_lat=None, loc_lng=None, loc_name=None, loc_state=None, log_start_ms=None, remark=None, vehicle_id=None, local_vars_configuration=None):  # noqa: E501
        """V1HosLogsResponseLogs - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._codriver_ids = None
        self._driver_id = None
        self._group_id = None
        self._hos_status_type = None
        self._loc_city = None
        self._loc_lat = None
        self._loc_lng = None
        self._loc_name = None
        self._loc_state = None
        self._log_start_ms = None
        self._remark = None
        self._vehicle_id = None
        self.discriminator = None

        if codriver_ids is not None:
            self.codriver_ids = codriver_ids
        if driver_id is not None:
            self.driver_id = driver_id
        if group_id is not None:
            self.group_id = group_id
        if hos_status_type is not None:
            self.hos_status_type = hos_status_type
        if loc_city is not None:
            self.loc_city = loc_city
        if loc_lat is not None:
            self.loc_lat = loc_lat
        if loc_lng is not None:
            self.loc_lng = loc_lng
        if loc_name is not None:
            self.loc_name = loc_name
        if loc_state is not None:
            self.loc_state = loc_state
        if log_start_ms is not None:
            self.log_start_ms = log_start_ms
        if remark is not None:
            self.remark = remark
        if vehicle_id is not None:
            self.vehicle_id = vehicle_id

    @property
    def codriver_ids(self):
        """Gets the codriver_ids of this V1HosLogsResponseLogs.  # noqa: E501


        :return: The codriver_ids of this V1HosLogsResponseLogs.  # noqa: E501
        :rtype: list[float]
        """
        return self._codriver_ids

    @codriver_ids.setter
    def codriver_ids(self, codriver_ids):
        """Sets the codriver_ids of this V1HosLogsResponseLogs.


        :param codriver_ids: The codriver_ids of this V1HosLogsResponseLogs.  # noqa: E501
        :type: list[float]
        """

        self._codriver_ids = codriver_ids

    @property
    def driver_id(self):
        """Gets the driver_id of this V1HosLogsResponseLogs.  # noqa: E501

        ID of the driver.  # noqa: E501

        :return: The driver_id of this V1HosLogsResponseLogs.  # noqa: E501
        :rtype: int
        """
        return self._driver_id

    @driver_id.setter
    def driver_id(self, driver_id):
        """Sets the driver_id of this V1HosLogsResponseLogs.

        ID of the driver.  # noqa: E501

        :param driver_id: The driver_id of this V1HosLogsResponseLogs.  # noqa: E501
        :type: int
        """

        self._driver_id = driver_id

    @property
    def group_id(self):
        """Gets the group_id of this V1HosLogsResponseLogs.  # noqa: E501

        Deprecated.  # noqa: E501

        :return: The group_id of this V1HosLogsResponseLogs.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this V1HosLogsResponseLogs.

        Deprecated.  # noqa: E501

        :param group_id: The group_id of this V1HosLogsResponseLogs.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def hos_status_type(self):
        """Gets the hos_status_type of this V1HosLogsResponseLogs.  # noqa: E501

        The Hours of Service status type. One of `OFF_DUTY`, `SLEEPER_BED`, `DRIVING`, `ON_DUTY`, `YARD_MOVE`, `PERSONAL_CONVEYANCE`.  # noqa: E501

        :return: The hos_status_type of this V1HosLogsResponseLogs.  # noqa: E501
        :rtype: str
        """
        return self._hos_status_type

    @hos_status_type.setter
    def hos_status_type(self, hos_status_type):
        """Sets the hos_status_type of this V1HosLogsResponseLogs.

        The Hours of Service status type. One of `OFF_DUTY`, `SLEEPER_BED`, `DRIVING`, `ON_DUTY`, `YARD_MOVE`, `PERSONAL_CONVEYANCE`.  # noqa: E501

        :param hos_status_type: The hos_status_type of this V1HosLogsResponseLogs.  # noqa: E501
        :type: str
        """

        self._hos_status_type = hos_status_type

    @property
    def loc_city(self):
        """Gets the loc_city of this V1HosLogsResponseLogs.  # noqa: E501

        City in which the log was recorded.  # noqa: E501

        :return: The loc_city of this V1HosLogsResponseLogs.  # noqa: E501
        :rtype: str
        """
        return self._loc_city

    @loc_city.setter
    def loc_city(self, loc_city):
        """Sets the loc_city of this V1HosLogsResponseLogs.

        City in which the log was recorded.  # noqa: E501

        :param loc_city: The loc_city of this V1HosLogsResponseLogs.  # noqa: E501
        :type: str
        """

        self._loc_city = loc_city

    @property
    def loc_lat(self):
        """Gets the loc_lat of this V1HosLogsResponseLogs.  # noqa: E501

        Latitude at which the log was recorded.  # noqa: E501

        :return: The loc_lat of this V1HosLogsResponseLogs.  # noqa: E501
        :rtype: float
        """
        return self._loc_lat

    @loc_lat.setter
    def loc_lat(self, loc_lat):
        """Sets the loc_lat of this V1HosLogsResponseLogs.

        Latitude at which the log was recorded.  # noqa: E501

        :param loc_lat: The loc_lat of this V1HosLogsResponseLogs.  # noqa: E501
        :type: float
        """

        self._loc_lat = loc_lat

    @property
    def loc_lng(self):
        """Gets the loc_lng of this V1HosLogsResponseLogs.  # noqa: E501

        Longitude at which the log was recorded.  # noqa: E501

        :return: The loc_lng of this V1HosLogsResponseLogs.  # noqa: E501
        :rtype: float
        """
        return self._loc_lng

    @loc_lng.setter
    def loc_lng(self, loc_lng):
        """Sets the loc_lng of this V1HosLogsResponseLogs.

        Longitude at which the log was recorded.  # noqa: E501

        :param loc_lng: The loc_lng of this V1HosLogsResponseLogs.  # noqa: E501
        :type: float
        """

        self._loc_lng = loc_lng

    @property
    def loc_name(self):
        """Gets the loc_name of this V1HosLogsResponseLogs.  # noqa: E501

        Name of location at which the log was recorded.  # noqa: E501

        :return: The loc_name of this V1HosLogsResponseLogs.  # noqa: E501
        :rtype: str
        """
        return self._loc_name

    @loc_name.setter
    def loc_name(self, loc_name):
        """Sets the loc_name of this V1HosLogsResponseLogs.

        Name of location at which the log was recorded.  # noqa: E501

        :param loc_name: The loc_name of this V1HosLogsResponseLogs.  # noqa: E501
        :type: str
        """

        self._loc_name = loc_name

    @property
    def loc_state(self):
        """Gets the loc_state of this V1HosLogsResponseLogs.  # noqa: E501

        State in which the log was recorded.  # noqa: E501

        :return: The loc_state of this V1HosLogsResponseLogs.  # noqa: E501
        :rtype: str
        """
        return self._loc_state

    @loc_state.setter
    def loc_state(self, loc_state):
        """Sets the loc_state of this V1HosLogsResponseLogs.

        State in which the log was recorded.  # noqa: E501

        :param loc_state: The loc_state of this V1HosLogsResponseLogs.  # noqa: E501
        :type: str
        """

        self._loc_state = loc_state

    @property
    def log_start_ms(self):
        """Gets the log_start_ms of this V1HosLogsResponseLogs.  # noqa: E501

        The time at which the log/HOS status started in UNIX milliseconds.  # noqa: E501

        :return: The log_start_ms of this V1HosLogsResponseLogs.  # noqa: E501
        :rtype: int
        """
        return self._log_start_ms

    @log_start_ms.setter
    def log_start_ms(self, log_start_ms):
        """Sets the log_start_ms of this V1HosLogsResponseLogs.

        The time at which the log/HOS status started in UNIX milliseconds.  # noqa: E501

        :param log_start_ms: The log_start_ms of this V1HosLogsResponseLogs.  # noqa: E501
        :type: int
        """

        self._log_start_ms = log_start_ms

    @property
    def remark(self):
        """Gets the remark of this V1HosLogsResponseLogs.  # noqa: E501

        Remark associated with the log entry.  # noqa: E501

        :return: The remark of this V1HosLogsResponseLogs.  # noqa: E501
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this V1HosLogsResponseLogs.

        Remark associated with the log entry.  # noqa: E501

        :param remark: The remark of this V1HosLogsResponseLogs.  # noqa: E501
        :type: str
        """

        self._remark = remark

    @property
    def vehicle_id(self):
        """Gets the vehicle_id of this V1HosLogsResponseLogs.  # noqa: E501

        ID of the vehicle.  # noqa: E501

        :return: The vehicle_id of this V1HosLogsResponseLogs.  # noqa: E501
        :rtype: int
        """
        return self._vehicle_id

    @vehicle_id.setter
    def vehicle_id(self, vehicle_id):
        """Sets the vehicle_id of this V1HosLogsResponseLogs.

        ID of the vehicle.  # noqa: E501

        :param vehicle_id: The vehicle_id of this V1HosLogsResponseLogs.  # noqa: E501
        :type: int
        """

        self._vehicle_id = vehicle_id

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
        if not isinstance(other, V1HosLogsResponseLogs):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1HosLogsResponseLogs):
            return True

        return self.to_dict() != other.to_dict()
