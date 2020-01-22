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


class V1VehicleHarshEventResponse(object):
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
        'download_forward_video_url': 'str',
        'download_inward_video_url': 'str',
        'download_tracked_inward_video_url': 'str',
        'harsh_event_type': 'str',
        'incident_report_url': 'str',
        'is_distracted': 'bool',
        'location': 'V1VehicleHarshEventResponseLocation'
    }

    attribute_map = {
        'download_forward_video_url': 'downloadForwardVideoUrl',
        'download_inward_video_url': 'downloadInwardVideoUrl',
        'download_tracked_inward_video_url': 'downloadTrackedInwardVideoUrl',
        'harsh_event_type': 'harshEventType',
        'incident_report_url': 'incidentReportUrl',
        'is_distracted': 'isDistracted',
        'location': 'location'
    }

    def __init__(self, download_forward_video_url=None, download_inward_video_url=None, download_tracked_inward_video_url=None, harsh_event_type=None, incident_report_url=None, is_distracted=None, location=None, local_vars_configuration=None):  # noqa: E501
        """V1VehicleHarshEventResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._download_forward_video_url = None
        self._download_inward_video_url = None
        self._download_tracked_inward_video_url = None
        self._harsh_event_type = None
        self._incident_report_url = None
        self._is_distracted = None
        self._location = None
        self.discriminator = None

        if download_forward_video_url is not None:
            self.download_forward_video_url = download_forward_video_url
        if download_inward_video_url is not None:
            self.download_inward_video_url = download_inward_video_url
        if download_tracked_inward_video_url is not None:
            self.download_tracked_inward_video_url = download_tracked_inward_video_url
        self.harsh_event_type = harsh_event_type
        self.incident_report_url = incident_report_url
        if is_distracted is not None:
            self.is_distracted = is_distracted
        if location is not None:
            self.location = location

    @property
    def download_forward_video_url(self):
        """Gets the download_forward_video_url of this V1VehicleHarshEventResponse.  # noqa: E501

        URL for downloading the forward facing video  # noqa: E501

        :return: The download_forward_video_url of this V1VehicleHarshEventResponse.  # noqa: E501
        :rtype: str
        """
        return self._download_forward_video_url

    @download_forward_video_url.setter
    def download_forward_video_url(self, download_forward_video_url):
        """Sets the download_forward_video_url of this V1VehicleHarshEventResponse.

        URL for downloading the forward facing video  # noqa: E501

        :param download_forward_video_url: The download_forward_video_url of this V1VehicleHarshEventResponse.  # noqa: E501
        :type: str
        """

        self._download_forward_video_url = download_forward_video_url

    @property
    def download_inward_video_url(self):
        """Gets the download_inward_video_url of this V1VehicleHarshEventResponse.  # noqa: E501

        URL for downloading the inward facing video  # noqa: E501

        :return: The download_inward_video_url of this V1VehicleHarshEventResponse.  # noqa: E501
        :rtype: str
        """
        return self._download_inward_video_url

    @download_inward_video_url.setter
    def download_inward_video_url(self, download_inward_video_url):
        """Sets the download_inward_video_url of this V1VehicleHarshEventResponse.

        URL for downloading the inward facing video  # noqa: E501

        :param download_inward_video_url: The download_inward_video_url of this V1VehicleHarshEventResponse.  # noqa: E501
        :type: str
        """

        self._download_inward_video_url = download_inward_video_url

    @property
    def download_tracked_inward_video_url(self):
        """Gets the download_tracked_inward_video_url of this V1VehicleHarshEventResponse.  # noqa: E501

        URL for downloading the tracked inward facing video  # noqa: E501

        :return: The download_tracked_inward_video_url of this V1VehicleHarshEventResponse.  # noqa: E501
        :rtype: str
        """
        return self._download_tracked_inward_video_url

    @download_tracked_inward_video_url.setter
    def download_tracked_inward_video_url(self, download_tracked_inward_video_url):
        """Sets the download_tracked_inward_video_url of this V1VehicleHarshEventResponse.

        URL for downloading the tracked inward facing video  # noqa: E501

        :param download_tracked_inward_video_url: The download_tracked_inward_video_url of this V1VehicleHarshEventResponse.  # noqa: E501
        :type: str
        """

        self._download_tracked_inward_video_url = download_tracked_inward_video_url

    @property
    def harsh_event_type(self):
        """Gets the harsh_event_type of this V1VehicleHarshEventResponse.  # noqa: E501

        Type of the harsh event. One of: [Crash, Harsh Acceleration, Harsh Braking, Harsh Turn, ROP Engine, ROP Brake, YC Engine, YC Brake, Harsh Event]  # noqa: E501

        :return: The harsh_event_type of this V1VehicleHarshEventResponse.  # noqa: E501
        :rtype: str
        """
        return self._harsh_event_type

    @harsh_event_type.setter
    def harsh_event_type(self, harsh_event_type):
        """Sets the harsh_event_type of this V1VehicleHarshEventResponse.

        Type of the harsh event. One of: [Crash, Harsh Acceleration, Harsh Braking, Harsh Turn, ROP Engine, ROP Brake, YC Engine, YC Brake, Harsh Event]  # noqa: E501

        :param harsh_event_type: The harsh_event_type of this V1VehicleHarshEventResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and harsh_event_type is None:  # noqa: E501
            raise ValueError("Invalid value for `harsh_event_type`, must not be `None`")  # noqa: E501

        self._harsh_event_type = harsh_event_type

    @property
    def incident_report_url(self):
        """Gets the incident_report_url of this V1VehicleHarshEventResponse.  # noqa: E501

        URL of the associated incident report page  # noqa: E501

        :return: The incident_report_url of this V1VehicleHarshEventResponse.  # noqa: E501
        :rtype: str
        """
        return self._incident_report_url

    @incident_report_url.setter
    def incident_report_url(self, incident_report_url):
        """Sets the incident_report_url of this V1VehicleHarshEventResponse.

        URL of the associated incident report page  # noqa: E501

        :param incident_report_url: The incident_report_url of this V1VehicleHarshEventResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and incident_report_url is None:  # noqa: E501
            raise ValueError("Invalid value for `incident_report_url`, must not be `None`")  # noqa: E501

        self._incident_report_url = incident_report_url

    @property
    def is_distracted(self):
        """Gets the is_distracted of this V1VehicleHarshEventResponse.  # noqa: E501

        Whether the driver was deemed distracted during this harsh event  # noqa: E501

        :return: The is_distracted of this V1VehicleHarshEventResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_distracted

    @is_distracted.setter
    def is_distracted(self, is_distracted):
        """Sets the is_distracted of this V1VehicleHarshEventResponse.

        Whether the driver was deemed distracted during this harsh event  # noqa: E501

        :param is_distracted: The is_distracted of this V1VehicleHarshEventResponse.  # noqa: E501
        :type: bool
        """

        self._is_distracted = is_distracted

    @property
    def location(self):
        """Gets the location of this V1VehicleHarshEventResponse.  # noqa: E501


        :return: The location of this V1VehicleHarshEventResponse.  # noqa: E501
        :rtype: V1VehicleHarshEventResponseLocation
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this V1VehicleHarshEventResponse.


        :param location: The location of this V1VehicleHarshEventResponse.  # noqa: E501
        :type: V1VehicleHarshEventResponseLocation
        """

        self._location = location

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
        if not isinstance(other, V1VehicleHarshEventResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1VehicleHarshEventResponse):
            return True

        return self.to_dict() != other.to_dict()
