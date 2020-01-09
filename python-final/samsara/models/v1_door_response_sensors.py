# coding: utf-8

"""
    Samsara API

    <style type=\"text/css\"> n {     padding: 1em;     width: 100%;     display: block;     margin: 28px 0; } n.info {     background-color: rgba(0, 51, 160, 0.1); } n.warning {     background-color: #fdf6e3; } i:before {     margin-right: 6px; } nh {     font-size: 1.5rem;     font-weight: 700;     line-height: 1.1;     display: block; } nb {     margin-top: 10px;     padding-left: 22px;     display: block; } </style>  # Overview  <n class=\"info\"> <nh> <i class=\"fa fa-info-circle\"></i> Something new! </nh> <nb> Welcome Samsara's new and improved API. Check out our FAQ [here](https://developers.samsara.com/docs/introducing-our-next-generation-api) to see what's changed and learn how to get started.<br> <br> Want to access the legacy API docs? You can find them [here](https://www.samsara.com/api).<br> <br> *Note: Because this is a new set of APIs, we have not transitioned all endpoints over to this standard. Endpoints that still use the legacy standards are indicated in the reference documentation. If you can't find an API that you're looking for, we encourage you to look for it in our [legacy API docs](https://www.samsara.com/api) as we continue to transition all endpoints over. Check back here for updates!*<br> <br> Submit your feedback [here](https://forms.gle/r4bs6HQshQAvBuwv6)! </nb> </n>  Samsara provides API endpoints so that you can build powerful applications and custom solutions with sensor data. Samsara has endpoints available to track and analyze sensors, vehicles, and entire fleets.  The Samsara API is a [RESTful API](https://en.wikipedia.org/wiki/Representational_state_transfer). It uses standard [HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol) authentication, verbs, and response codes, and it returns [JSON](http://www.json.org/) response bodies. If you're familiar with what you can build with a REST API, then this will be your go-to API reference.  Visit [developers.samsara.com](https://developers.samsara.com) to find getting started guides and an API overview.  If you have any questions, reach out to us at [support@samsara.com](mailto:support@samsara.com).  ## Endpoints  All our APIs can be accessed through HTTP requests to URLs like:  ``` https://api.samsara.com/<endpoint> ```  For EU customers, this URL will be:  ``` https://api.eu.samsara.com/<endpoint> ```  <n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> Note </nh> <nb> Legacy endpoints will have the URL: `https://api.samsara.com/v1/<endpoint>` or `https://api.eu.samsara.com/v1/<endpoint>` </nb> </n>  ## Authentication  To authenticate your API request you will need to include your secret token. You can manage your API tokens in the [Dashboard](https://cloud.samsara.com). They are visible under `Settings->Organization->API Tokens`.  Your API tokens carry many privileges, so be sure to keep them secure. Do not share your secret API tokens in publicly accessible areas such as GitHub, client-side code, and so on.  Authentication to the API is performed via Bearer Token in the HTTP Authorization header. Provide your API token as the `access_token` value in an `Authorization: Bearer` header. You do not need to provide a password:  ```curl Authorization: Bearer {access_token} ```  All API requests must be made over [HTTPS](https://en.wikipedia.org/wiki/HTTPS). Calls made over plain HTTP or without authentication will fail.  ## Common Patterns  You can find more info about request methods, response codes, error codes, versioning, pagination, timestamps, and mini-objects [here](https://developers.samsara.com/docs/common-structures).   # noqa: E501

    The version of the OpenAPI document: 2019-11-19
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from samsara.configuration import Configuration


class V1DoorResponseSensors(object):
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
        'door_closed': 'bool',
        'door_status_time': 'str',
        'id': 'int',
        'name': 'str',
        'trailer_id': 'int',
        'vehicle_id': 'int'
    }

    attribute_map = {
        'door_closed': 'doorClosed',
        'door_status_time': 'doorStatusTime',
        'id': 'id',
        'name': 'name',
        'trailer_id': 'trailerId',
        'vehicle_id': 'vehicleId'
    }

    def __init__(self, door_closed=None, door_status_time=None, id=None, name=None, trailer_id=None, vehicle_id=None, local_vars_configuration=None):  # noqa: E501
        """V1DoorResponseSensors - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._door_closed = None
        self._door_status_time = None
        self._id = None
        self._name = None
        self._trailer_id = None
        self._vehicle_id = None
        self.discriminator = None

        if door_closed is not None:
            self.door_closed = door_closed
        if door_status_time is not None:
            self.door_status_time = door_status_time
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if trailer_id is not None:
            self.trailer_id = trailer_id
        if vehicle_id is not None:
            self.vehicle_id = vehicle_id

    @property
    def door_closed(self):
        """Gets the door_closed of this V1DoorResponseSensors.  # noqa: E501

        Flag indicating whether the current door is closed or open.  # noqa: E501

        :return: The door_closed of this V1DoorResponseSensors.  # noqa: E501
        :rtype: bool
        """
        return self._door_closed

    @door_closed.setter
    def door_closed(self, door_closed):
        """Sets the door_closed of this V1DoorResponseSensors.

        Flag indicating whether the current door is closed or open.  # noqa: E501

        :param door_closed: The door_closed of this V1DoorResponseSensors.  # noqa: E501
        :type: bool
        """

        self._door_closed = door_closed

    @property
    def door_status_time(self):
        """Gets the door_status_time of this V1DoorResponseSensors.  # noqa: E501

        The timestamp of reported door status, specified in RFC 3339 time.  # noqa: E501

        :return: The door_status_time of this V1DoorResponseSensors.  # noqa: E501
        :rtype: str
        """
        return self._door_status_time

    @door_status_time.setter
    def door_status_time(self, door_status_time):
        """Sets the door_status_time of this V1DoorResponseSensors.

        The timestamp of reported door status, specified in RFC 3339 time.  # noqa: E501

        :param door_status_time: The door_status_time of this V1DoorResponseSensors.  # noqa: E501
        :type: str
        """

        self._door_status_time = door_status_time

    @property
    def id(self):
        """Gets the id of this V1DoorResponseSensors.  # noqa: E501

        ID of the sensor.  # noqa: E501

        :return: The id of this V1DoorResponseSensors.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V1DoorResponseSensors.

        ID of the sensor.  # noqa: E501

        :param id: The id of this V1DoorResponseSensors.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this V1DoorResponseSensors.  # noqa: E501

        Name of the sensor.  # noqa: E501

        :return: The name of this V1DoorResponseSensors.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1DoorResponseSensors.

        Name of the sensor.  # noqa: E501

        :param name: The name of this V1DoorResponseSensors.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def trailer_id(self):
        """Gets the trailer_id of this V1DoorResponseSensors.  # noqa: E501

        ID of the trailer associated with the sensor for the data point. If no trailer is connected, this parameter will not be reported.  # noqa: E501

        :return: The trailer_id of this V1DoorResponseSensors.  # noqa: E501
        :rtype: int
        """
        return self._trailer_id

    @trailer_id.setter
    def trailer_id(self, trailer_id):
        """Sets the trailer_id of this V1DoorResponseSensors.

        ID of the trailer associated with the sensor for the data point. If no trailer is connected, this parameter will not be reported.  # noqa: E501

        :param trailer_id: The trailer_id of this V1DoorResponseSensors.  # noqa: E501
        :type: int
        """

        self._trailer_id = trailer_id

    @property
    def vehicle_id(self):
        """Gets the vehicle_id of this V1DoorResponseSensors.  # noqa: E501

        ID of the vehicle associated with the sensor for the data point. If no vehicle is connected, this parameter will not be reported.  # noqa: E501

        :return: The vehicle_id of this V1DoorResponseSensors.  # noqa: E501
        :rtype: int
        """
        return self._vehicle_id

    @vehicle_id.setter
    def vehicle_id(self, vehicle_id):
        """Sets the vehicle_id of this V1DoorResponseSensors.

        ID of the vehicle associated with the sensor for the data point. If no vehicle is connected, this parameter will not be reported.  # noqa: E501

        :param vehicle_id: The vehicle_id of this V1DoorResponseSensors.  # noqa: E501
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
        if not isinstance(other, V1DoorResponseSensors):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1DoorResponseSensors):
            return True

        return self.to_dict() != other.to_dict()