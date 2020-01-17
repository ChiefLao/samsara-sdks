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

from openapi_client.configuration import Configuration


class V1TripResponseTrips(object):
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
        'asset_ids': 'list[int]',
        'codriver_ids': 'list[int]',
        'distance_meters': 'int',
        'driver_id': 'int',
        'end_address': 'V1TripResponseEndAddress',
        'end_coordinates': 'V1TripResponseEndCoordinates',
        'end_location': 'str',
        'end_ms': 'int',
        'end_odometer': 'int',
        'fuel_consumed_ml': 'int',
        'start_address': 'V1TripResponseStartAddress',
        'start_coordinates': 'V1TripResponseStartCoordinates',
        'start_location': 'str',
        'start_ms': 'int',
        'start_odometer': 'int',
        'toll_meters': 'int'
    }

    attribute_map = {
        'asset_ids': 'assetIds',
        'codriver_ids': 'codriverIds',
        'distance_meters': 'distanceMeters',
        'driver_id': 'driverId',
        'end_address': 'endAddress',
        'end_coordinates': 'endCoordinates',
        'end_location': 'endLocation',
        'end_ms': 'endMs',
        'end_odometer': 'endOdometer',
        'fuel_consumed_ml': 'fuelConsumedMl',
        'start_address': 'startAddress',
        'start_coordinates': 'startCoordinates',
        'start_location': 'startLocation',
        'start_ms': 'startMs',
        'start_odometer': 'startOdometer',
        'toll_meters': 'tollMeters'
    }

    def __init__(self, asset_ids=None, codriver_ids=None, distance_meters=None, driver_id=None, end_address=None, end_coordinates=None, end_location=None, end_ms=None, end_odometer=None, fuel_consumed_ml=None, start_address=None, start_coordinates=None, start_location=None, start_ms=None, start_odometer=None, toll_meters=None, local_vars_configuration=None):  # noqa: E501
        """V1TripResponseTrips - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._asset_ids = None
        self._codriver_ids = None
        self._distance_meters = None
        self._driver_id = None
        self._end_address = None
        self._end_coordinates = None
        self._end_location = None
        self._end_ms = None
        self._end_odometer = None
        self._fuel_consumed_ml = None
        self._start_address = None
        self._start_coordinates = None
        self._start_location = None
        self._start_ms = None
        self._start_odometer = None
        self._toll_meters = None
        self.discriminator = None

        if asset_ids is not None:
            self.asset_ids = asset_ids
        if codriver_ids is not None:
            self.codriver_ids = codriver_ids
        if distance_meters is not None:
            self.distance_meters = distance_meters
        if driver_id is not None:
            self.driver_id = driver_id
        if end_address is not None:
            self.end_address = end_address
        if end_coordinates is not None:
            self.end_coordinates = end_coordinates
        if end_location is not None:
            self.end_location = end_location
        if end_ms is not None:
            self.end_ms = end_ms
        if end_odometer is not None:
            self.end_odometer = end_odometer
        if fuel_consumed_ml is not None:
            self.fuel_consumed_ml = fuel_consumed_ml
        if start_address is not None:
            self.start_address = start_address
        if start_coordinates is not None:
            self.start_coordinates = start_coordinates
        if start_location is not None:
            self.start_location = start_location
        if start_ms is not None:
            self.start_ms = start_ms
        if start_odometer is not None:
            self.start_odometer = start_odometer
        if toll_meters is not None:
            self.toll_meters = toll_meters

    @property
    def asset_ids(self):
        """Gets the asset_ids of this V1TripResponseTrips.  # noqa: E501

        List of associated asset IDs  # noqa: E501

        :return: The asset_ids of this V1TripResponseTrips.  # noqa: E501
        :rtype: list[int]
        """
        return self._asset_ids

    @asset_ids.setter
    def asset_ids(self, asset_ids):
        """Sets the asset_ids of this V1TripResponseTrips.

        List of associated asset IDs  # noqa: E501

        :param asset_ids: The asset_ids of this V1TripResponseTrips.  # noqa: E501
        :type: list[int]
        """

        self._asset_ids = asset_ids

    @property
    def codriver_ids(self):
        """Gets the codriver_ids of this V1TripResponseTrips.  # noqa: E501

        List of codriver IDs  # noqa: E501

        :return: The codriver_ids of this V1TripResponseTrips.  # noqa: E501
        :rtype: list[int]
        """
        return self._codriver_ids

    @codriver_ids.setter
    def codriver_ids(self, codriver_ids):
        """Sets the codriver_ids of this V1TripResponseTrips.

        List of codriver IDs  # noqa: E501

        :param codriver_ids: The codriver_ids of this V1TripResponseTrips.  # noqa: E501
        :type: list[int]
        """

        self._codriver_ids = codriver_ids

    @property
    def distance_meters(self):
        """Gets the distance_meters of this V1TripResponseTrips.  # noqa: E501

        Length of the trip in meters. This value is calculated from the GPS data collected by the Samsara Vehicle Gateway.  # noqa: E501

        :return: The distance_meters of this V1TripResponseTrips.  # noqa: E501
        :rtype: int
        """
        return self._distance_meters

    @distance_meters.setter
    def distance_meters(self, distance_meters):
        """Sets the distance_meters of this V1TripResponseTrips.

        Length of the trip in meters. This value is calculated from the GPS data collected by the Samsara Vehicle Gateway.  # noqa: E501

        :param distance_meters: The distance_meters of this V1TripResponseTrips.  # noqa: E501
        :type: int
        """

        self._distance_meters = distance_meters

    @property
    def driver_id(self):
        """Gets the driver_id of this V1TripResponseTrips.  # noqa: E501

        ID of the driver.  # noqa: E501

        :return: The driver_id of this V1TripResponseTrips.  # noqa: E501
        :rtype: int
        """
        return self._driver_id

    @driver_id.setter
    def driver_id(self, driver_id):
        """Sets the driver_id of this V1TripResponseTrips.

        ID of the driver.  # noqa: E501

        :param driver_id: The driver_id of this V1TripResponseTrips.  # noqa: E501
        :type: int
        """

        self._driver_id = driver_id

    @property
    def end_address(self):
        """Gets the end_address of this V1TripResponseTrips.  # noqa: E501


        :return: The end_address of this V1TripResponseTrips.  # noqa: E501
        :rtype: V1TripResponseEndAddress
        """
        return self._end_address

    @end_address.setter
    def end_address(self, end_address):
        """Sets the end_address of this V1TripResponseTrips.


        :param end_address: The end_address of this V1TripResponseTrips.  # noqa: E501
        :type: V1TripResponseEndAddress
        """

        self._end_address = end_address

    @property
    def end_coordinates(self):
        """Gets the end_coordinates of this V1TripResponseTrips.  # noqa: E501


        :return: The end_coordinates of this V1TripResponseTrips.  # noqa: E501
        :rtype: V1TripResponseEndCoordinates
        """
        return self._end_coordinates

    @end_coordinates.setter
    def end_coordinates(self, end_coordinates):
        """Sets the end_coordinates of this V1TripResponseTrips.


        :param end_coordinates: The end_coordinates of this V1TripResponseTrips.  # noqa: E501
        :type: V1TripResponseEndCoordinates
        """

        self._end_coordinates = end_coordinates

    @property
    def end_location(self):
        """Gets the end_location of this V1TripResponseTrips.  # noqa: E501

        Geocoded street address of start (latitude, longitude) coordinates.  # noqa: E501

        :return: The end_location of this V1TripResponseTrips.  # noqa: E501
        :rtype: str
        """
        return self._end_location

    @end_location.setter
    def end_location(self, end_location):
        """Sets the end_location of this V1TripResponseTrips.

        Geocoded street address of start (latitude, longitude) coordinates.  # noqa: E501

        :param end_location: The end_location of this V1TripResponseTrips.  # noqa: E501
        :type: str
        """

        self._end_location = end_location

    @property
    def end_ms(self):
        """Gets the end_ms of this V1TripResponseTrips.  # noqa: E501

        End of the trip in UNIX milliseconds. Ongoing trips are indicated by an endMs value of 9223372036854775807.  # noqa: E501

        :return: The end_ms of this V1TripResponseTrips.  # noqa: E501
        :rtype: int
        """
        return self._end_ms

    @end_ms.setter
    def end_ms(self, end_ms):
        """Sets the end_ms of this V1TripResponseTrips.

        End of the trip in UNIX milliseconds. Ongoing trips are indicated by an endMs value of 9223372036854775807.  # noqa: E501

        :param end_ms: The end_ms of this V1TripResponseTrips.  # noqa: E501
        :type: int
        """

        self._end_ms = end_ms

    @property
    def end_odometer(self):
        """Gets the end_odometer of this V1TripResponseTrips.  # noqa: E501

        Odometer reading (in meters) at the end of the trip. This is read from the vehicle's on-board diagnostics. If Samsara cannot read the vehicle's odometer values from on-board diagnostics, this value will be 0.  # noqa: E501

        :return: The end_odometer of this V1TripResponseTrips.  # noqa: E501
        :rtype: int
        """
        return self._end_odometer

    @end_odometer.setter
    def end_odometer(self, end_odometer):
        """Sets the end_odometer of this V1TripResponseTrips.

        Odometer reading (in meters) at the end of the trip. This is read from the vehicle's on-board diagnostics. If Samsara cannot read the vehicle's odometer values from on-board diagnostics, this value will be 0.  # noqa: E501

        :param end_odometer: The end_odometer of this V1TripResponseTrips.  # noqa: E501
        :type: int
        """

        self._end_odometer = end_odometer

    @property
    def fuel_consumed_ml(self):
        """Gets the fuel_consumed_ml of this V1TripResponseTrips.  # noqa: E501

        Amount in milliliters of fuel consumed on this trip.  # noqa: E501

        :return: The fuel_consumed_ml of this V1TripResponseTrips.  # noqa: E501
        :rtype: int
        """
        return self._fuel_consumed_ml

    @fuel_consumed_ml.setter
    def fuel_consumed_ml(self, fuel_consumed_ml):
        """Sets the fuel_consumed_ml of this V1TripResponseTrips.

        Amount in milliliters of fuel consumed on this trip.  # noqa: E501

        :param fuel_consumed_ml: The fuel_consumed_ml of this V1TripResponseTrips.  # noqa: E501
        :type: int
        """

        self._fuel_consumed_ml = fuel_consumed_ml

    @property
    def start_address(self):
        """Gets the start_address of this V1TripResponseTrips.  # noqa: E501


        :return: The start_address of this V1TripResponseTrips.  # noqa: E501
        :rtype: V1TripResponseStartAddress
        """
        return self._start_address

    @start_address.setter
    def start_address(self, start_address):
        """Sets the start_address of this V1TripResponseTrips.


        :param start_address: The start_address of this V1TripResponseTrips.  # noqa: E501
        :type: V1TripResponseStartAddress
        """

        self._start_address = start_address

    @property
    def start_coordinates(self):
        """Gets the start_coordinates of this V1TripResponseTrips.  # noqa: E501


        :return: The start_coordinates of this V1TripResponseTrips.  # noqa: E501
        :rtype: V1TripResponseStartCoordinates
        """
        return self._start_coordinates

    @start_coordinates.setter
    def start_coordinates(self, start_coordinates):
        """Sets the start_coordinates of this V1TripResponseTrips.


        :param start_coordinates: The start_coordinates of this V1TripResponseTrips.  # noqa: E501
        :type: V1TripResponseStartCoordinates
        """

        self._start_coordinates = start_coordinates

    @property
    def start_location(self):
        """Gets the start_location of this V1TripResponseTrips.  # noqa: E501

        Geocoded street address of start (latitude, longitude) coordinates.  # noqa: E501

        :return: The start_location of this V1TripResponseTrips.  # noqa: E501
        :rtype: str
        """
        return self._start_location

    @start_location.setter
    def start_location(self, start_location):
        """Sets the start_location of this V1TripResponseTrips.

        Geocoded street address of start (latitude, longitude) coordinates.  # noqa: E501

        :param start_location: The start_location of this V1TripResponseTrips.  # noqa: E501
        :type: str
        """

        self._start_location = start_location

    @property
    def start_ms(self):
        """Gets the start_ms of this V1TripResponseTrips.  # noqa: E501

        Beginning of the trip in UNIX milliseconds.  # noqa: E501

        :return: The start_ms of this V1TripResponseTrips.  # noqa: E501
        :rtype: int
        """
        return self._start_ms

    @start_ms.setter
    def start_ms(self, start_ms):
        """Sets the start_ms of this V1TripResponseTrips.

        Beginning of the trip in UNIX milliseconds.  # noqa: E501

        :param start_ms: The start_ms of this V1TripResponseTrips.  # noqa: E501
        :type: int
        """

        self._start_ms = start_ms

    @property
    def start_odometer(self):
        """Gets the start_odometer of this V1TripResponseTrips.  # noqa: E501

        Odometer reading (in meters) at the beginning of the trip. This is read from the vehicle's on-board diagnostics. If Samsara cannot read the vehicle's odometer values from on-board diagnostics, this value will be 0.  # noqa: E501

        :return: The start_odometer of this V1TripResponseTrips.  # noqa: E501
        :rtype: int
        """
        return self._start_odometer

    @start_odometer.setter
    def start_odometer(self, start_odometer):
        """Sets the start_odometer of this V1TripResponseTrips.

        Odometer reading (in meters) at the beginning of the trip. This is read from the vehicle's on-board diagnostics. If Samsara cannot read the vehicle's odometer values from on-board diagnostics, this value will be 0.  # noqa: E501

        :param start_odometer: The start_odometer of this V1TripResponseTrips.  # noqa: E501
        :type: int
        """

        self._start_odometer = start_odometer

    @property
    def toll_meters(self):
        """Gets the toll_meters of this V1TripResponseTrips.  # noqa: E501

        Length in meters trip spent on toll roads.  # noqa: E501

        :return: The toll_meters of this V1TripResponseTrips.  # noqa: E501
        :rtype: int
        """
        return self._toll_meters

    @toll_meters.setter
    def toll_meters(self, toll_meters):
        """Sets the toll_meters of this V1TripResponseTrips.

        Length in meters trip spent on toll roads.  # noqa: E501

        :param toll_meters: The toll_meters of this V1TripResponseTrips.  # noqa: E501
        :type: int
        """

        self._toll_meters = toll_meters

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
        if not isinstance(other, V1TripResponseTrips):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1TripResponseTrips):
            return True

        return self.to_dict() != other.to_dict()
