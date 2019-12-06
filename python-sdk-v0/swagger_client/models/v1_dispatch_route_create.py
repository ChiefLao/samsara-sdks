# coding: utf-8

"""
    Samsara API

    <style type=\"text/css\"> n {     padding: 1em;     width: 100%;     display: block;     margin: 28px 0; } n.info {     background-color: rgba(0, 51, 160, 0.1); } n.warning {     background-color: #fdf6e3; } i:before {     margin-right: 6px; } nh {     font-size: 1.5rem;     font-weight: 700;     line-height: 1.1;     display: block; } nb {     margin-top: 10px;     padding-left: 22px;     display: block; } </style>  # Overview  <n class=\"info\"> <nh> <i class=\"fa fa-info-circle\"></i> Something new! </nh> <nb> Welcome Samsara's new and improved API. Check out our FAQ [here](https://developers.samsara.com/docs/introducing-our-next-generation-api) to see what's changed and learn how to get started.<br> <br> Want to access the legacy API docs? You can find them [here](https://www.samsara.com/api).<br> <br> *Note: Because this is a new set of APIs, we have not transitioned all endpoints over to this standard. Endpoints that still use the legacy standards are indicated in the reference documentation. If you can't find an API that you're looking for, we encourage you to look for it in our [legacy API docs](https://www.samsara.com/api) as we continue to transition all endpoints over. Check back here for updates!*<br> <br> Submit your feedback [here](https://forms.gle/r4bs6HQshQAvBuwv6)! </nb> </n>  Samsara provides API endpoints so that you can build powerful applications and custom solutions with sensor data. Samsara has endpoints available to track and analyze sensors, vehicles, and entire fleets.  The Samsara API is a [RESTful API](https://en.wikipedia.org/wiki/Representational_state_transfer). It uses standard [HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol) authentication, verbs, and response codes, and it returns [JSON](http://www.json.org/) response bodies. If you're familiar with what you can build with a REST API, then this will be your go-to API reference.  Visit [developers.samsara.com](https://developers.samsara.com) to find getting started guides and an API overview.  If you have any questions, reach out to us at [support@samsara.com](mailto:support@samsara.com).  ## Endpoints  All our APIs can be accessed through HTTP requests to URLs like:  ``` https://api.samsara.com/<endpoint> ```  For EU customers, this URL will be:  ``` https://api.eu.samsara.com/<endpoint> ```  <n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> Note </nh> <nb> Legacy endpoints will have the URL: `https://api.samsara.com/v1/<endpoint>` or `https://api.eu.samsara.com/v1/<endpoint>` </nb> </n>  ## Authentication  To authenticate your API request you will need to include your secret token. You can manage your API tokens in the [Dashboard](https://cloud.samsara.com). They are visible under `Settings->Organization->API Tokens`.  Your API tokens carry many privileges, so be sure to keep them secure. Do not share your secret API tokens in publicly accessible areas such as GitHub, client-side code, and so on.  Authentication to the API is performed via Bearer Token in the HTTP Authorization header. Provide your API token as the `access_token` value in an `Authorization: Bearer` header. You do not need to provide a password:  ```curl Authorization: Bearer {access_token} ```  All API requests must be made over [HTTPS](https://en.wikipedia.org/wiki/HTTPS). Calls made over plain HTTP or without authentication will fail.  ## Common Patterns  You can find more info about request methods, response codes, error codes, versioning, pagination, timestamps, and mini-objects [here](https://developers.samsara.com/docs/common-structures).   # noqa: E501

    OpenAPI spec version: 2019-11-19
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class V1DispatchRouteCreate(object):
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
        'driver_id': 'int',
        'name': 'str',
        'notes': 'str',
        'scheduled_end_ms': 'int',
        'scheduled_meters': 'int',
        'scheduled_start_ms': 'int',
        'start_location_address': 'str',
        'start_location_address_id': 'int',
        'start_location_lat': 'float',
        'start_location_lng': 'float',
        'start_location_name': 'str',
        'trailer_id': 'int',
        'vehicle_id': 'int'
    }

    attribute_map = {
        'driver_id': 'driver_id',
        'name': 'name',
        'notes': 'notes',
        'scheduled_end_ms': 'scheduled_end_ms',
        'scheduled_meters': 'scheduled_meters',
        'scheduled_start_ms': 'scheduled_start_ms',
        'start_location_address': 'start_location_address',
        'start_location_address_id': 'start_location_address_id',
        'start_location_lat': 'start_location_lat',
        'start_location_lng': 'start_location_lng',
        'start_location_name': 'start_location_name',
        'trailer_id': 'trailer_id',
        'vehicle_id': 'vehicle_id'
    }

    def __init__(self, driver_id=None, name=None, notes=None, scheduled_end_ms=None, scheduled_meters=None, scheduled_start_ms=None, start_location_address=None, start_location_address_id=None, start_location_lat=None, start_location_lng=None, start_location_name=None, trailer_id=None, vehicle_id=None):  # noqa: E501
        """V1DispatchRouteCreate - a model defined in Swagger"""  # noqa: E501
        self._driver_id = None
        self._name = None
        self._notes = None
        self._scheduled_end_ms = None
        self._scheduled_meters = None
        self._scheduled_start_ms = None
        self._start_location_address = None
        self._start_location_address_id = None
        self._start_location_lat = None
        self._start_location_lng = None
        self._start_location_name = None
        self._trailer_id = None
        self._vehicle_id = None
        self.discriminator = None
        if driver_id is not None:
            self.driver_id = driver_id
        self.name = name
        if notes is not None:
            self.notes = notes
        if scheduled_end_ms is not None:
            self.scheduled_end_ms = scheduled_end_ms
        if scheduled_meters is not None:
            self.scheduled_meters = scheduled_meters
        self.scheduled_start_ms = scheduled_start_ms
        if start_location_address is not None:
            self.start_location_address = start_location_address
        if start_location_address_id is not None:
            self.start_location_address_id = start_location_address_id
        if start_location_lat is not None:
            self.start_location_lat = start_location_lat
        if start_location_lng is not None:
            self.start_location_lng = start_location_lng
        if start_location_name is not None:
            self.start_location_name = start_location_name
        if trailer_id is not None:
            self.trailer_id = trailer_id
        if vehicle_id is not None:
            self.vehicle_id = vehicle_id

    @property
    def driver_id(self):
        """Gets the driver_id of this V1DispatchRouteCreate.  # noqa: E501

        ID of the driver assigned to the dispatch route. Note that driver_id and vehicle_id are mutually exclusive. If neither is specified, then the route is unassigned.  # noqa: E501

        :return: The driver_id of this V1DispatchRouteCreate.  # noqa: E501
        :rtype: int
        """
        return self._driver_id

    @driver_id.setter
    def driver_id(self, driver_id):
        """Sets the driver_id of this V1DispatchRouteCreate.

        ID of the driver assigned to the dispatch route. Note that driver_id and vehicle_id are mutually exclusive. If neither is specified, then the route is unassigned.  # noqa: E501

        :param driver_id: The driver_id of this V1DispatchRouteCreate.  # noqa: E501
        :type: int
        """

        self._driver_id = driver_id

    @property
    def name(self):
        """Gets the name of this V1DispatchRouteCreate.  # noqa: E501

        Descriptive name of this route.  # noqa: E501

        :return: The name of this V1DispatchRouteCreate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1DispatchRouteCreate.

        Descriptive name of this route.  # noqa: E501

        :param name: The name of this V1DispatchRouteCreate.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def notes(self):
        """Gets the notes of this V1DispatchRouteCreate.  # noqa: E501

        Notes regarding the details of this route; maximum of 2000 characters; newline characters ('\\n')can be used for formatting.  # noqa: E501

        :return: The notes of this V1DispatchRouteCreate.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this V1DispatchRouteCreate.

        Notes regarding the details of this route; maximum of 2000 characters; newline characters ('\\n')can be used for formatting.  # noqa: E501

        :param notes: The notes of this V1DispatchRouteCreate.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def scheduled_end_ms(self):
        """Gets the scheduled_end_ms of this V1DispatchRouteCreate.  # noqa: E501

        The time in Unix epoch milliseconds that the last job in the route is scheduled to end.  # noqa: E501

        :return: The scheduled_end_ms of this V1DispatchRouteCreate.  # noqa: E501
        :rtype: int
        """
        return self._scheduled_end_ms

    @scheduled_end_ms.setter
    def scheduled_end_ms(self, scheduled_end_ms):
        """Sets the scheduled_end_ms of this V1DispatchRouteCreate.

        The time in Unix epoch milliseconds that the last job in the route is scheduled to end.  # noqa: E501

        :param scheduled_end_ms: The scheduled_end_ms of this V1DispatchRouteCreate.  # noqa: E501
        :type: int
        """

        self._scheduled_end_ms = scheduled_end_ms

    @property
    def scheduled_meters(self):
        """Gets the scheduled_meters of this V1DispatchRouteCreate.  # noqa: E501

        The distance expected to be traveled for this route in meters.  # noqa: E501

        :return: The scheduled_meters of this V1DispatchRouteCreate.  # noqa: E501
        :rtype: int
        """
        return self._scheduled_meters

    @scheduled_meters.setter
    def scheduled_meters(self, scheduled_meters):
        """Sets the scheduled_meters of this V1DispatchRouteCreate.

        The distance expected to be traveled for this route in meters.  # noqa: E501

        :param scheduled_meters: The scheduled_meters of this V1DispatchRouteCreate.  # noqa: E501
        :type: int
        """

        self._scheduled_meters = scheduled_meters

    @property
    def scheduled_start_ms(self):
        """Gets the scheduled_start_ms of this V1DispatchRouteCreate.  # noqa: E501

        The time in Unix epoch milliseconds that the route is scheduled to start.  # noqa: E501

        :return: The scheduled_start_ms of this V1DispatchRouteCreate.  # noqa: E501
        :rtype: int
        """
        return self._scheduled_start_ms

    @scheduled_start_ms.setter
    def scheduled_start_ms(self, scheduled_start_ms):
        """Sets the scheduled_start_ms of this V1DispatchRouteCreate.

        The time in Unix epoch milliseconds that the route is scheduled to start.  # noqa: E501

        :param scheduled_start_ms: The scheduled_start_ms of this V1DispatchRouteCreate.  # noqa: E501
        :type: int
        """
        if scheduled_start_ms is None:
            raise ValueError("Invalid value for `scheduled_start_ms`, must not be `None`")  # noqa: E501

        self._scheduled_start_ms = scheduled_start_ms

    @property
    def start_location_address(self):
        """Gets the start_location_address of this V1DispatchRouteCreate.  # noqa: E501

        The address of the route's starting location, as it would be recognized if provided to maps.google.com. Optional if a valid start location address ID is provided.  # noqa: E501

        :return: The start_location_address of this V1DispatchRouteCreate.  # noqa: E501
        :rtype: str
        """
        return self._start_location_address

    @start_location_address.setter
    def start_location_address(self, start_location_address):
        """Sets the start_location_address of this V1DispatchRouteCreate.

        The address of the route's starting location, as it would be recognized if provided to maps.google.com. Optional if a valid start location address ID is provided.  # noqa: E501

        :param start_location_address: The start_location_address of this V1DispatchRouteCreate.  # noqa: E501
        :type: str
        """

        self._start_location_address = start_location_address

    @property
    def start_location_address_id(self):
        """Gets the start_location_address_id of this V1DispatchRouteCreate.  # noqa: E501

        ID of the start location associated with an address book entry. Optional if valid values are provided for start location address and latitude/longitude. If a valid start location address ID is provided, address/latitude/longitude will be used from the address book entry. Name of the address book entry will only be used if the start location name is not provided.  # noqa: E501

        :return: The start_location_address_id of this V1DispatchRouteCreate.  # noqa: E501
        :rtype: int
        """
        return self._start_location_address_id

    @start_location_address_id.setter
    def start_location_address_id(self, start_location_address_id):
        """Sets the start_location_address_id of this V1DispatchRouteCreate.

        ID of the start location associated with an address book entry. Optional if valid values are provided for start location address and latitude/longitude. If a valid start location address ID is provided, address/latitude/longitude will be used from the address book entry. Name of the address book entry will only be used if the start location name is not provided.  # noqa: E501

        :param start_location_address_id: The start_location_address_id of this V1DispatchRouteCreate.  # noqa: E501
        :type: int
        """

        self._start_location_address_id = start_location_address_id

    @property
    def start_location_lat(self):
        """Gets the start_location_lat of this V1DispatchRouteCreate.  # noqa: E501

        Latitude of the start location in decimal degrees. Optional if a valid start location address ID is provided.  # noqa: E501

        :return: The start_location_lat of this V1DispatchRouteCreate.  # noqa: E501
        :rtype: float
        """
        return self._start_location_lat

    @start_location_lat.setter
    def start_location_lat(self, start_location_lat):
        """Sets the start_location_lat of this V1DispatchRouteCreate.

        Latitude of the start location in decimal degrees. Optional if a valid start location address ID is provided.  # noqa: E501

        :param start_location_lat: The start_location_lat of this V1DispatchRouteCreate.  # noqa: E501
        :type: float
        """

        self._start_location_lat = start_location_lat

    @property
    def start_location_lng(self):
        """Gets the start_location_lng of this V1DispatchRouteCreate.  # noqa: E501

        Longitude of the start location in decimal degrees. Optional if a valid start location address ID is provided.  # noqa: E501

        :return: The start_location_lng of this V1DispatchRouteCreate.  # noqa: E501
        :rtype: float
        """
        return self._start_location_lng

    @start_location_lng.setter
    def start_location_lng(self, start_location_lng):
        """Sets the start_location_lng of this V1DispatchRouteCreate.

        Longitude of the start location in decimal degrees. Optional if a valid start location address ID is provided.  # noqa: E501

        :param start_location_lng: The start_location_lng of this V1DispatchRouteCreate.  # noqa: E501
        :type: float
        """

        self._start_location_lng = start_location_lng

    @property
    def start_location_name(self):
        """Gets the start_location_name of this V1DispatchRouteCreate.  # noqa: E501

        The name of the route's starting location. If provided, it will take precedence over the name of the address book entry.  # noqa: E501

        :return: The start_location_name of this V1DispatchRouteCreate.  # noqa: E501
        :rtype: str
        """
        return self._start_location_name

    @start_location_name.setter
    def start_location_name(self, start_location_name):
        """Sets the start_location_name of this V1DispatchRouteCreate.

        The name of the route's starting location. If provided, it will take precedence over the name of the address book entry.  # noqa: E501

        :param start_location_name: The start_location_name of this V1DispatchRouteCreate.  # noqa: E501
        :type: str
        """

        self._start_location_name = start_location_name

    @property
    def trailer_id(self):
        """Gets the trailer_id of this V1DispatchRouteCreate.  # noqa: E501

        ID of the trailer assigned to the dispatch route. Note that trailers can only be assigned to routes that have a Vehicle or Driver assigned to them.  # noqa: E501

        :return: The trailer_id of this V1DispatchRouteCreate.  # noqa: E501
        :rtype: int
        """
        return self._trailer_id

    @trailer_id.setter
    def trailer_id(self, trailer_id):
        """Sets the trailer_id of this V1DispatchRouteCreate.

        ID of the trailer assigned to the dispatch route. Note that trailers can only be assigned to routes that have a Vehicle or Driver assigned to them.  # noqa: E501

        :param trailer_id: The trailer_id of this V1DispatchRouteCreate.  # noqa: E501
        :type: int
        """

        self._trailer_id = trailer_id

    @property
    def vehicle_id(self):
        """Gets the vehicle_id of this V1DispatchRouteCreate.  # noqa: E501

        ID of the vehicle assigned to the dispatch route. Note that vehicle_id and driver_id are mutually exclusive. If neither is specified, then the route is unassigned.  # noqa: E501

        :return: The vehicle_id of this V1DispatchRouteCreate.  # noqa: E501
        :rtype: int
        """
        return self._vehicle_id

    @vehicle_id.setter
    def vehicle_id(self, vehicle_id):
        """Sets the vehicle_id of this V1DispatchRouteCreate.

        ID of the vehicle assigned to the dispatch route. Note that vehicle_id and driver_id are mutually exclusive. If neither is specified, then the route is unassigned.  # noqa: E501

        :param vehicle_id: The vehicle_id of this V1DispatchRouteCreate.  # noqa: E501
        :type: int
        """

        self._vehicle_id = vehicle_id

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
        if issubclass(V1DispatchRouteCreate, dict):
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
        if not isinstance(other, V1DispatchRouteCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
