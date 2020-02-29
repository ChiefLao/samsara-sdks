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


class V1DvirDefectBase(object):
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
        'comment': 'str',
        'defect_type': 'str',
        'id': 'int',
        'resolved': 'bool',
        'resolved_at': 'int',
        'resolved_by_driver_id': 'int',
        'resolved_by_mechanic_id': 'int'
    }

    attribute_map = {
        'comment': 'comment',
        'defect_type': 'defectType',
        'id': 'id',
        'resolved': 'resolved',
        'resolved_at': 'resolvedAt',
        'resolved_by_driver_id': 'resolvedByDriverId',
        'resolved_by_mechanic_id': 'resolvedByMechanicId'
    }

    def __init__(self, comment=None, defect_type=None, id=None, resolved=None, resolved_at=None, resolved_by_driver_id=None, resolved_by_mechanic_id=None, local_vars_configuration=None):  # noqa: E501
        """V1DvirDefectBase - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._comment = None
        self._defect_type = None
        self._id = None
        self._resolved = None
        self._resolved_at = None
        self._resolved_by_driver_id = None
        self._resolved_by_mechanic_id = None
        self.discriminator = None

        if comment is not None:
            self.comment = comment
        if defect_type is not None:
            self.defect_type = defect_type
        if id is not None:
            self.id = id
        if resolved is not None:
            self.resolved = resolved
        if resolved_at is not None:
            self.resolved_at = resolved_at
        if resolved_by_driver_id is not None:
            self.resolved_by_driver_id = resolved_by_driver_id
        if resolved_by_mechanic_id is not None:
            self.resolved_by_mechanic_id = resolved_by_mechanic_id

    @property
    def comment(self):
        """Gets the comment of this V1DvirDefectBase.  # noqa: E501

        The comment describing the type of DVIR defect.  # noqa: E501

        :return: The comment of this V1DvirDefectBase.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this V1DvirDefectBase.

        The comment describing the type of DVIR defect.  # noqa: E501

        :param comment: The comment of this V1DvirDefectBase.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def defect_type(self):
        """Gets the defect_type of this V1DvirDefectBase.  # noqa: E501

        The type of DVIR defect. Possible values: [`AIR_COMPRESSOR`, `AIR_CONDITIONER`, `AIR_LINES`, `BATTERY`, `BELTS_HOSES`, `BRAKE_ACCESSORIES`, `BRAKE_CHECK`, `BRAKE_CONNECTIONS`, `BRAKES`, `CLUTCH`, `COUPLING_DEVICES`, `DEFROSTER_HEATER`, `DOORS`, `DRIVE_LINE`, `EMERGENCY_DOOR_AND_BUZZER`, `ENGINE`, `ENTRANCE_STEPS`, `EXHAUST`, `FIFTH_WHEEL`, `FIRST_AID_KIT`, `FLUID_LEVELS`, `FRAME_ASSEMBLY`, `FRONT_AXLE`, `FUEL_TANKS`, `HORN`, `INTERIOR_AND_FLOOR`, `LANDING_GEAR`, `LIGHTS`, `MIRRORS`, `MUFFLER`, `OIL_PRESSURE`, `OTHER`, `RADIATOR`, `REAR_END`, `REFLECTORS`, `ROOF`, `SAFETY_EQUIPMENT`, `STARTER`, `STEERING`, `STOP_ARM_CONTROL`, `STOP_ARM`, `SUSPENSION`, `TIRE_CHAINS`, `TIRES`, `TRANSMISSION`, `TRIP_RECORDER`, `WHEELS_RIMS`, `WINDOWS`, `WINDSHIELD_WIPERS`, `UNSET`]  # noqa: E501

        :return: The defect_type of this V1DvirDefectBase.  # noqa: E501
        :rtype: str
        """
        return self._defect_type

    @defect_type.setter
    def defect_type(self, defect_type):
        """Sets the defect_type of this V1DvirDefectBase.

        The type of DVIR defect. Possible values: [`AIR_COMPRESSOR`, `AIR_CONDITIONER`, `AIR_LINES`, `BATTERY`, `BELTS_HOSES`, `BRAKE_ACCESSORIES`, `BRAKE_CHECK`, `BRAKE_CONNECTIONS`, `BRAKES`, `CLUTCH`, `COUPLING_DEVICES`, `DEFROSTER_HEATER`, `DOORS`, `DRIVE_LINE`, `EMERGENCY_DOOR_AND_BUZZER`, `ENGINE`, `ENTRANCE_STEPS`, `EXHAUST`, `FIFTH_WHEEL`, `FIRST_AID_KIT`, `FLUID_LEVELS`, `FRAME_ASSEMBLY`, `FRONT_AXLE`, `FUEL_TANKS`, `HORN`, `INTERIOR_AND_FLOOR`, `LANDING_GEAR`, `LIGHTS`, `MIRRORS`, `MUFFLER`, `OIL_PRESSURE`, `OTHER`, `RADIATOR`, `REAR_END`, `REFLECTORS`, `ROOF`, `SAFETY_EQUIPMENT`, `STARTER`, `STEERING`, `STOP_ARM_CONTROL`, `STOP_ARM`, `SUSPENSION`, `TIRE_CHAINS`, `TIRES`, `TRANSMISSION`, `TRIP_RECORDER`, `WHEELS_RIMS`, `WINDOWS`, `WINDSHIELD_WIPERS`, `UNSET`]  # noqa: E501

        :param defect_type: The defect_type of this V1DvirDefectBase.  # noqa: E501
        :type: str
        """

        self._defect_type = defect_type

    @property
    def id(self):
        """Gets the id of this V1DvirDefectBase.  # noqa: E501

        The id of this defect.  # noqa: E501

        :return: The id of this V1DvirDefectBase.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V1DvirDefectBase.

        The id of this defect.  # noqa: E501

        :param id: The id of this V1DvirDefectBase.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def resolved(self):
        """Gets the resolved of this V1DvirDefectBase.  # noqa: E501

        Signifies if this defect is resolved.  # noqa: E501

        :return: The resolved of this V1DvirDefectBase.  # noqa: E501
        :rtype: bool
        """
        return self._resolved

    @resolved.setter
    def resolved(self, resolved):
        """Sets the resolved of this V1DvirDefectBase.

        Signifies if this defect is resolved.  # noqa: E501

        :param resolved: The resolved of this V1DvirDefectBase.  # noqa: E501
        :type: bool
        """

        self._resolved = resolved

    @property
    def resolved_at(self):
        """Gets the resolved_at of this V1DvirDefectBase.  # noqa: E501

        Timestamp when this defect was resolved, in UNIX milliseconds.  Will not be returned if the defect is unresolved.  # noqa: E501

        :return: The resolved_at of this V1DvirDefectBase.  # noqa: E501
        :rtype: int
        """
        return self._resolved_at

    @resolved_at.setter
    def resolved_at(self, resolved_at):
        """Sets the resolved_at of this V1DvirDefectBase.

        Timestamp when this defect was resolved, in UNIX milliseconds.  Will not be returned if the defect is unresolved.  # noqa: E501

        :param resolved_at: The resolved_at of this V1DvirDefectBase.  # noqa: E501
        :type: int
        """

        self._resolved_at = resolved_at

    @property
    def resolved_by_driver_id(self):
        """Gets the resolved_by_driver_id of this V1DvirDefectBase.  # noqa: E501

        ID of the driver who resolved this defect. Will not be returned if the defect is unresolved or resolvedByMechanicId is returned.  # noqa: E501

        :return: The resolved_by_driver_id of this V1DvirDefectBase.  # noqa: E501
        :rtype: int
        """
        return self._resolved_by_driver_id

    @resolved_by_driver_id.setter
    def resolved_by_driver_id(self, resolved_by_driver_id):
        """Sets the resolved_by_driver_id of this V1DvirDefectBase.

        ID of the driver who resolved this defect. Will not be returned if the defect is unresolved or resolvedByMechanicId is returned.  # noqa: E501

        :param resolved_by_driver_id: The resolved_by_driver_id of this V1DvirDefectBase.  # noqa: E501
        :type: int
        """

        self._resolved_by_driver_id = resolved_by_driver_id

    @property
    def resolved_by_mechanic_id(self):
        """Gets the resolved_by_mechanic_id of this V1DvirDefectBase.  # noqa: E501

        ID of the mechanic who resolved this defect. Will not be returned if the defect is unresolved or resolvedByDriverId is returned.  # noqa: E501

        :return: The resolved_by_mechanic_id of this V1DvirDefectBase.  # noqa: E501
        :rtype: int
        """
        return self._resolved_by_mechanic_id

    @resolved_by_mechanic_id.setter
    def resolved_by_mechanic_id(self, resolved_by_mechanic_id):
        """Sets the resolved_by_mechanic_id of this V1DvirDefectBase.

        ID of the mechanic who resolved this defect. Will not be returned if the defect is unresolved or resolvedByDriverId is returned.  # noqa: E501

        :param resolved_by_mechanic_id: The resolved_by_mechanic_id of this V1DvirDefectBase.  # noqa: E501
        :type: int
        """

        self._resolved_by_mechanic_id = resolved_by_mechanic_id

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
        if not isinstance(other, V1DvirDefectBase):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1DvirDefectBase):
            return True

        return self.to_dict() != other.to_dict()
