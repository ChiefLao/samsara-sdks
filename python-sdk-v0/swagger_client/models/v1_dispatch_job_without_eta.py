# coding: utf-8

"""
    Samsara API

    <style type=\"text/css\"> n {     padding: 1em;     width: 100%;     display: block;     margin: 28px 0; } n.info {     background-color: rgba(0, 51, 160, 0.1); } n.warning {     background-color: #fdf6e3; } i:before {     margin-right: 6px; } nh {     font-size: 1.5rem;     font-weight: 700;     line-height: 1.1;     display: block; } nb {     margin-top: 10px;     padding-left: 22px;     display: block; } </style>  # Overview  <n class=\"info\"> <nh> <i class=\"fa fa-info-circle\"></i> Something new! </nh> <nb> Welcome Samsara's new and improved API. Check out our FAQ [here](https://developers.samsara.com/docs/introducing-our-next-generation-api) to see what's changed and learn how to get started.<br> <br> Want to access the legacy API docs? You can find them [here](https://www.samsara.com/api).<br> <br> *Note: Because this is a new set of APIs, we have not transitioned all endpoints over to this standard. Endpoints that still use the legacy standards are indicated in the reference documentation. If you can't find an API that you're looking for, we encourage you to look for it in our [legacy API docs](https://www.samsara.com/api) as we continue to transition all endpoints over. Check back here for updates!*<br> <br> Submit your feedback [here](https://forms.gle/r4bs6HQshQAvBuwv6)! </nb> </n>  Samsara provides API endpoints so that you can build powerful applications and custom solutions with sensor data. Samsara has endpoints available to track and analyze sensors, vehicles, and entire fleets.  The Samsara API is a [RESTful API](https://en.wikipedia.org/wiki/Representational_state_transfer). It uses standard [HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol) authentication, verbs, and response codes, and it returns [JSON](http://www.json.org/) response bodies. If you're familiar with what you can build with a REST API, then this will be your go-to API reference.  Visit [developers.samsara.com](https://developers.samsara.com) to find getting started guides and an API overview.  If you have any questions, reach out to us at [support@samsara.com](mailto:support@samsara.com).  ## Endpoints  All our APIs can be accessed through HTTP requests to URLs like:  ``` https://api.samsara.com/<endpoint> ```  For EU customers, this URL will be:  ``` https://api.eu.samsara.com/<endpoint> ```  <n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> Note </nh> <nb> Legacy endpoints will have the URL: `https://api.samsara.com/v1/<endpoint>` or `https://api.eu.samsara.com/v1/<endpoint>` </nb> </n>  ## Authentication  To authenticate your API request you will need to include your secret token. You can manage your API tokens in the [Dashboard](https://cloud.samsara.com). They are visible under `Settings->Organization->API Tokens`.  Your API tokens carry many privileges, so be sure to keep them secure. Do not share your secret API tokens in publicly accessible areas such as GitHub, client-side code, and so on.  Authentication to the API is performed via Bearer Token in the HTTP Authorization header. Provide your API token as the `access_token` value in an `Authorization: Bearer` header. You do not need to provide a password:  ```curl Authorization: Bearer {access_token} ```  All API requests must be made over [HTTPS](https://en.wikipedia.org/wiki/HTTPS). Calls made over plain HTTP or without authentication will fail.  ## Common Patterns  You can find more info about request methods, response codes, error codes, versioning, pagination, timestamps, and mini-objects [here](https://developers.samsara.com/docs/common-structures).   # noqa: E501

    OpenAPI spec version: 2019-09-13
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class V1DispatchJobWithoutETA(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'destination_address': 'str',
        'destination_address_id': 'int',
        'destination_lat': 'float',
        'destination_lng': 'float',
        'destination_name': 'str',
        'notes': 'str',
        'scheduled_arrival_time_ms': 'int',
        'scheduled_departure_time_ms': 'int'
    }

    attribute_map = {
        'destination_address': 'destination_address',
        'destination_address_id': 'destination_address_id',
        'destination_lat': 'destination_lat',
        'destination_lng': 'destination_lng',
        'destination_name': 'destination_name',
        'notes': 'notes',
        'scheduled_arrival_time_ms': 'scheduled_arrival_time_ms',
        'scheduled_departure_time_ms': 'scheduled_departure_time_ms'
    }

    def __init__(self, destination_address=None, destination_address_id=None, destination_lat=None, destination_lng=None, destination_name=None, notes=None, scheduled_arrival_time_ms=None, scheduled_departure_time_ms=None):  # noqa: E501
        """V1DispatchJobWithoutETA - a model defined in Swagger"""  # noqa: E501
        self._destination_address = None
        self._destination_address_id = None
        self._destination_lat = None
        self._destination_lng = None
        self._destination_name = None
        self._notes = None
        self._scheduled_arrival_time_ms = None
        self._scheduled_departure_time_ms = None
        self.discriminator = None
        if destination_address is not None:
            self.destination_address = destination_address
        if destination_address_id is not None:
            self.destination_address_id = destination_address_id
        if destination_lat is not None:
            self.destination_lat = destination_lat
        if destination_lng is not None:
            self.destination_lng = destination_lng
        if destination_name is not None:
            self.destination_name = destination_name
        if notes is not None:
            self.notes = notes
        self.scheduled_arrival_time_ms = scheduled_arrival_time_ms
        if scheduled_departure_time_ms is not None:
            self.scheduled_departure_time_ms = scheduled_departure_time_ms

    @property
    def destination_address(self):
        """Gets the destination_address of this V1DispatchJobWithoutETA.  # noqa: E501

        The address of the job destination, as it would be recognized if provided to maps.google.com. Optional if a valid destination address ID is provided.  # noqa: E501

        :return: The destination_address of this V1DispatchJobWithoutETA.  # noqa: E501
        :rtype: str
        """
        return self._destination_address

    @destination_address.setter
    def destination_address(self, destination_address):
        """Sets the destination_address of this V1DispatchJobWithoutETA.

        The address of the job destination, as it would be recognized if provided to maps.google.com. Optional if a valid destination address ID is provided.  # noqa: E501

        :param destination_address: The destination_address of this V1DispatchJobWithoutETA.  # noqa: E501
        :type: str
        """

        self._destination_address = destination_address

    @property
    def destination_address_id(self):
        """Gets the destination_address_id of this V1DispatchJobWithoutETA.  # noqa: E501

        ID of the job destination associated with an address book entry. Optional if valid values are provided for destination address and latitude/longitude. If a valid destination address ID is provided, address/latitude/longitude will be used from the address book entry. Name of the address book entry will only be used if the destination name is not provided.  # noqa: E501

        :return: The destination_address_id of this V1DispatchJobWithoutETA.  # noqa: E501
        :rtype: int
        """
        return self._destination_address_id

    @destination_address_id.setter
    def destination_address_id(self, destination_address_id):
        """Sets the destination_address_id of this V1DispatchJobWithoutETA.

        ID of the job destination associated with an address book entry. Optional if valid values are provided for destination address and latitude/longitude. If a valid destination address ID is provided, address/latitude/longitude will be used from the address book entry. Name of the address book entry will only be used if the destination name is not provided.  # noqa: E501

        :param destination_address_id: The destination_address_id of this V1DispatchJobWithoutETA.  # noqa: E501
        :type: int
        """

        self._destination_address_id = destination_address_id

    @property
    def destination_lat(self):
        """Gets the destination_lat of this V1DispatchJobWithoutETA.  # noqa: E501

        Latitude of the destination in decimal degrees. Optional if a valid destination address ID is provided.  # noqa: E501

        :return: The destination_lat of this V1DispatchJobWithoutETA.  # noqa: E501
        :rtype: float
        """
        return self._destination_lat

    @destination_lat.setter
    def destination_lat(self, destination_lat):
        """Sets the destination_lat of this V1DispatchJobWithoutETA.

        Latitude of the destination in decimal degrees. Optional if a valid destination address ID is provided.  # noqa: E501

        :param destination_lat: The destination_lat of this V1DispatchJobWithoutETA.  # noqa: E501
        :type: float
        """

        self._destination_lat = destination_lat

    @property
    def destination_lng(self):
        """Gets the destination_lng of this V1DispatchJobWithoutETA.  # noqa: E501

        Longitude of the destination in decimal degrees. Optional if a valid destination address ID is provided.  # noqa: E501

        :return: The destination_lng of this V1DispatchJobWithoutETA.  # noqa: E501
        :rtype: float
        """
        return self._destination_lng

    @destination_lng.setter
    def destination_lng(self, destination_lng):
        """Sets the destination_lng of this V1DispatchJobWithoutETA.

        Longitude of the destination in decimal degrees. Optional if a valid destination address ID is provided.  # noqa: E501

        :param destination_lng: The destination_lng of this V1DispatchJobWithoutETA.  # noqa: E501
        :type: float
        """

        self._destination_lng = destination_lng

    @property
    def destination_name(self):
        """Gets the destination_name of this V1DispatchJobWithoutETA.  # noqa: E501

        The name of the job destination. If provided, it will take precedence over the name of the address book entry.  # noqa: E501

        :return: The destination_name of this V1DispatchJobWithoutETA.  # noqa: E501
        :rtype: str
        """
        return self._destination_name

    @destination_name.setter
    def destination_name(self, destination_name):
        """Sets the destination_name of this V1DispatchJobWithoutETA.

        The name of the job destination. If provided, it will take precedence over the name of the address book entry.  # noqa: E501

        :param destination_name: The destination_name of this V1DispatchJobWithoutETA.  # noqa: E501
        :type: str
        """

        self._destination_name = destination_name

    @property
    def notes(self):
        """Gets the notes of this V1DispatchJobWithoutETA.  # noqa: E501

        Notes regarding the details of this job, maximum of 2000 characters; newline characters ('\\n')can be used for formatting.  # noqa: E501

        :return: The notes of this V1DispatchJobWithoutETA.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this V1DispatchJobWithoutETA.

        Notes regarding the details of this job, maximum of 2000 characters; newline characters ('\\n')can be used for formatting.  # noqa: E501

        :param notes: The notes of this V1DispatchJobWithoutETA.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def scheduled_arrival_time_ms(self):
        """Gets the scheduled_arrival_time_ms of this V1DispatchJobWithoutETA.  # noqa: E501

        The time at which the assigned driver is scheduled to arrive at the job destination.  # noqa: E501

        :return: The scheduled_arrival_time_ms of this V1DispatchJobWithoutETA.  # noqa: E501
        :rtype: int
        """
        return self._scheduled_arrival_time_ms

    @scheduled_arrival_time_ms.setter
    def scheduled_arrival_time_ms(self, scheduled_arrival_time_ms):
        """Sets the scheduled_arrival_time_ms of this V1DispatchJobWithoutETA.

        The time at which the assigned driver is scheduled to arrive at the job destination.  # noqa: E501

        :param scheduled_arrival_time_ms: The scheduled_arrival_time_ms of this V1DispatchJobWithoutETA.  # noqa: E501
        :type: int
        """
        if scheduled_arrival_time_ms is None:
            raise ValueError("Invalid value for `scheduled_arrival_time_ms`, must not be `None`")  # noqa: E501

        self._scheduled_arrival_time_ms = scheduled_arrival_time_ms

    @property
    def scheduled_departure_time_ms(self):
        """Gets the scheduled_departure_time_ms of this V1DispatchJobWithoutETA.  # noqa: E501

        The time at which the assigned driver is scheduled to depart from the job destination.  # noqa: E501

        :return: The scheduled_departure_time_ms of this V1DispatchJobWithoutETA.  # noqa: E501
        :rtype: int
        """
        return self._scheduled_departure_time_ms

    @scheduled_departure_time_ms.setter
    def scheduled_departure_time_ms(self, scheduled_departure_time_ms):
        """Sets the scheduled_departure_time_ms of this V1DispatchJobWithoutETA.

        The time at which the assigned driver is scheduled to depart from the job destination.  # noqa: E501

        :param scheduled_departure_time_ms: The scheduled_departure_time_ms of this V1DispatchJobWithoutETA.  # noqa: E501
        :type: int
        """

        self._scheduled_departure_time_ms = scheduled_departure_time_ms

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(V1DispatchJobWithoutETA, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1DispatchJobWithoutETA):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
