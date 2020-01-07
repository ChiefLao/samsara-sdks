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


class VehicleResponse(object):
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
        'aux_input_type1': 'str',
        'aux_input_type2': 'str',
        'external_ids': 'dict(str, str)',
        'harsh_acceleration_setting_type': 'str',
        'id': 'str',
        'license_plate': 'str',
        'make': 'str',
        'model': 'str',
        'name': 'str',
        'notes': 'str',
        'static_assigned_driver': 'VehicleListResponseStaticAssignedDriver',
        'tags': 'list[AddressAllOfTags]',
        'vin': 'str',
        'year': 'str'
    }

    attribute_map = {
        'aux_input_type1': 'auxInputType1',
        'aux_input_type2': 'auxInputType2',
        'external_ids': 'externalIds',
        'harsh_acceleration_setting_type': 'harshAccelerationSettingType',
        'id': 'id',
        'license_plate': 'licensePlate',
        'make': 'make',
        'model': 'model',
        'name': 'name',
        'notes': 'notes',
        'static_assigned_driver': 'staticAssignedDriver',
        'tags': 'tags',
        'vin': 'vin',
        'year': 'year'
    }

    def __init__(self, aux_input_type1=None, aux_input_type2=None, external_ids=None, harsh_acceleration_setting_type=None, id=None, license_plate=None, make=None, model=None, name=None, notes=None, static_assigned_driver=None, tags=None, vin=None, year=None, local_vars_configuration=None):  # noqa: E501
        """VehicleResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._aux_input_type1 = None
        self._aux_input_type2 = None
        self._external_ids = None
        self._harsh_acceleration_setting_type = None
        self._id = None
        self._license_plate = None
        self._make = None
        self._model = None
        self._name = None
        self._notes = None
        self._static_assigned_driver = None
        self._tags = None
        self._vin = None
        self._year = None
        self.discriminator = None

        if aux_input_type1 is not None:
            self.aux_input_type1 = aux_input_type1
        if aux_input_type2 is not None:
            self.aux_input_type2 = aux_input_type2
        if external_ids is not None:
            self.external_ids = external_ids
        if harsh_acceleration_setting_type is not None:
            self.harsh_acceleration_setting_type = harsh_acceleration_setting_type
        self.id = id
        if license_plate is not None:
            self.license_plate = license_plate
        if make is not None:
            self.make = make
        if model is not None:
            self.model = model
        if name is not None:
            self.name = name
        if notes is not None:
            self.notes = notes
        if static_assigned_driver is not None:
            self.static_assigned_driver = static_assigned_driver
        if tags is not None:
            self.tags = tags
        if vin is not None:
            self.vin = vin
        if year is not None:
            self.year = year

    @property
    def aux_input_type1(self):
        """Gets the aux_input_type1 of this VehicleResponse.  # noqa: E501

        The type of aux input that this vehicle has connected to port 1. Setting to \"none\" will remove the configured aux input.  # noqa: E501

        :return: The aux_input_type1 of this VehicleResponse.  # noqa: E501
        :rtype: str
        """
        return self._aux_input_type1

    @aux_input_type1.setter
    def aux_input_type1(self, aux_input_type1):
        """Sets the aux_input_type1 of this VehicleResponse.

        The type of aux input that this vehicle has connected to port 1. Setting to \"none\" will remove the configured aux input.  # noqa: E501

        :param aux_input_type1: The aux_input_type1 of this VehicleResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["none", "emergencyLights", "emergencyAlarm", "stopPaddle", "powerTakeOff", "plow", "sweeper", "salter", "reefer", "door", "boom", "auxiliaryEngine", "generator", "eightWayLights"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and aux_input_type1 not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `aux_input_type1` ({0}), must be one of {1}"  # noqa: E501
                .format(aux_input_type1, allowed_values)
            )

        self._aux_input_type1 = aux_input_type1

    @property
    def aux_input_type2(self):
        """Gets the aux_input_type2 of this VehicleResponse.  # noqa: E501

        The type of aux input that this vehicle has connected to port 2. Setting to \"none\" will remove the configured aux input.  # noqa: E501

        :return: The aux_input_type2 of this VehicleResponse.  # noqa: E501
        :rtype: str
        """
        return self._aux_input_type2

    @aux_input_type2.setter
    def aux_input_type2(self, aux_input_type2):
        """Sets the aux_input_type2 of this VehicleResponse.

        The type of aux input that this vehicle has connected to port 2. Setting to \"none\" will remove the configured aux input.  # noqa: E501

        :param aux_input_type2: The aux_input_type2 of this VehicleResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["none", "emergencyLights", "emergencyAlarm", "stopPaddle", "powerTakeOff", "plow", "sweeper", "salter", "reefer", "door", "boom", "auxiliaryEngine", "generator", "eightWayLights"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and aux_input_type2 not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `aux_input_type2` ({0}), must be one of {1}"  # noqa: E501
                .format(aux_input_type2, allowed_values)
            )

        self._aux_input_type2 = aux_input_type2

    @property
    def external_ids(self):
        """Gets the external_ids of this VehicleResponse.  # noqa: E501

        User-defined dictionary of external IDs (key-value pairs). Both the keys and the values of the dictionary are of type string and must be alphanumeric. Each organization can have at most 10 unique external ID keys. To delete an external ID, set its value to null or the empty string (`\"\"`). An external ID can be used as a path parameter to retrieve or update that resource.  # noqa: E501

        :return: The external_ids of this VehicleResponse.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._external_ids

    @external_ids.setter
    def external_ids(self, external_ids):
        """Sets the external_ids of this VehicleResponse.

        User-defined dictionary of external IDs (key-value pairs). Both the keys and the values of the dictionary are of type string and must be alphanumeric. Each organization can have at most 10 unique external ID keys. To delete an external ID, set its value to null or the empty string (`\"\"`). An external ID can be used as a path parameter to retrieve or update that resource.  # noqa: E501

        :param external_ids: The external_ids of this VehicleResponse.  # noqa: E501
        :type: dict(str, str)
        """

        self._external_ids = external_ids

    @property
    def harsh_acceleration_setting_type(self):
        """Gets the harsh_acceleration_setting_type of this VehicleResponse.  # noqa: E501

        Enumeration of the harsh acceleration setting types. This setting influences the acceleration sensitivity from which a harsh event is triggered. If set to `off`, then no acceleration based harsh events are triggered for the vehicle.  # noqa: E501

        :return: The harsh_acceleration_setting_type of this VehicleResponse.  # noqa: E501
        :rtype: str
        """
        return self._harsh_acceleration_setting_type

    @harsh_acceleration_setting_type.setter
    def harsh_acceleration_setting_type(self, harsh_acceleration_setting_type):
        """Sets the harsh_acceleration_setting_type of this VehicleResponse.

        Enumeration of the harsh acceleration setting types. This setting influences the acceleration sensitivity from which a harsh event is triggered. If set to `off`, then no acceleration based harsh events are triggered for the vehicle.  # noqa: E501

        :param harsh_acceleration_setting_type: The harsh_acceleration_setting_type of this VehicleResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["passengerCar", "lightTruck", "heavyDuty", "off", "automatic"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and harsh_acceleration_setting_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `harsh_acceleration_setting_type` ({0}), must be one of {1}"  # noqa: E501
                .format(harsh_acceleration_setting_type, allowed_values)
            )

        self._harsh_acceleration_setting_type = harsh_acceleration_setting_type

    @property
    def id(self):
        """Gets the id of this VehicleResponse.  # noqa: E501

        Unique Samsara ID for the vehicle.  # noqa: E501

        :return: The id of this VehicleResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VehicleResponse.

        Unique Samsara ID for the vehicle.  # noqa: E501

        :param id: The id of this VehicleResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def license_plate(self):
        """Gets the license_plate of this VehicleResponse.  # noqa: E501

        The license plate of this vehicle.  # noqa: E501

        :return: The license_plate of this VehicleResponse.  # noqa: E501
        :rtype: str
        """
        return self._license_plate

    @license_plate.setter
    def license_plate(self, license_plate):
        """Sets the license_plate of this VehicleResponse.

        The license plate of this vehicle.  # noqa: E501

        :param license_plate: The license_plate of this VehicleResponse.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                license_plate is not None and len(license_plate) > 12):
            raise ValueError("Invalid value for `license_plate`, length must be less than or equal to `12`")  # noqa: E501

        self._license_plate = license_plate

    @property
    def make(self):
        """Gets the make of this VehicleResponse.  # noqa: E501

        Vehicle's manufacturing make.  # noqa: E501

        :return: The make of this VehicleResponse.  # noqa: E501
        :rtype: str
        """
        return self._make

    @make.setter
    def make(self, make):
        """Sets the make of this VehicleResponse.

        Vehicle's manufacturing make.  # noqa: E501

        :param make: The make of this VehicleResponse.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                make is not None and len(make) > 255):
            raise ValueError("Invalid value for `make`, length must be less than or equal to `255`")  # noqa: E501

        self._make = make

    @property
    def model(self):
        """Gets the model of this VehicleResponse.  # noqa: E501

        Vehicle's manufacturing model.  # noqa: E501

        :return: The model of this VehicleResponse.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this VehicleResponse.

        Vehicle's manufacturing model.  # noqa: E501

        :param model: The model of this VehicleResponse.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                model is not None and len(model) > 255):
            raise ValueError("Invalid value for `model`, length must be less than or equal to `255`")  # noqa: E501

        self._model = model

    @property
    def name(self):
        """Gets the name of this VehicleResponse.  # noqa: E501

        Name of the vehicle.  # noqa: E501

        :return: The name of this VehicleResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VehicleResponse.

        Name of the vehicle.  # noqa: E501

        :param name: The name of this VehicleResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def notes(self):
        """Gets the notes of this VehicleResponse.  # noqa: E501

        Notes about a vehicle. Samsara supports a maximum of 255 chars.  # noqa: E501

        :return: The notes of this VehicleResponse.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this VehicleResponse.

        Notes about a vehicle. Samsara supports a maximum of 255 chars.  # noqa: E501

        :param notes: The notes of this VehicleResponse.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                notes is not None and len(notes) > 255):
            raise ValueError("Invalid value for `notes`, length must be less than or equal to `255`")  # noqa: E501

        self._notes = notes

    @property
    def static_assigned_driver(self):
        """Gets the static_assigned_driver of this VehicleResponse.  # noqa: E501


        :return: The static_assigned_driver of this VehicleResponse.  # noqa: E501
        :rtype: VehicleListResponseStaticAssignedDriver
        """
        return self._static_assigned_driver

    @static_assigned_driver.setter
    def static_assigned_driver(self, static_assigned_driver):
        """Sets the static_assigned_driver of this VehicleResponse.


        :param static_assigned_driver: The static_assigned_driver of this VehicleResponse.  # noqa: E501
        :type: VehicleListResponseStaticAssignedDriver
        """

        self._static_assigned_driver = static_assigned_driver

    @property
    def tags(self):
        """Gets the tags of this VehicleResponse.  # noqa: E501

        An array of all tag mini-objects that are associated with the given vehicle.  # noqa: E501

        :return: The tags of this VehicleResponse.  # noqa: E501
        :rtype: list[AddressAllOfTags]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this VehicleResponse.

        An array of all tag mini-objects that are associated with the given vehicle.  # noqa: E501

        :param tags: The tags of this VehicleResponse.  # noqa: E501
        :type: list[AddressAllOfTags]
        """

        self._tags = tags

    @property
    def vin(self):
        """Gets the vin of this VehicleResponse.  # noqa: E501

        A vehicle identification number.  # noqa: E501

        :return: The vin of this VehicleResponse.  # noqa: E501
        :rtype: str
        """
        return self._vin

    @vin.setter
    def vin(self, vin):
        """Sets the vin of this VehicleResponse.

        A vehicle identification number.  # noqa: E501

        :param vin: The vin of this VehicleResponse.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                vin is not None and len(vin) > 17):
            raise ValueError("Invalid value for `vin`, length must be less than or equal to `17`")  # noqa: E501

        self._vin = vin

    @property
    def year(self):
        """Gets the year of this VehicleResponse.  # noqa: E501

        Vehicle's manufacturing year.  # noqa: E501

        :return: The year of this VehicleResponse.  # noqa: E501
        :rtype: str
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this VehicleResponse.

        Vehicle's manufacturing year.  # noqa: E501

        :param year: The year of this VehicleResponse.  # noqa: E501
        :type: str
        """

        self._year = year

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
        if not isinstance(other, VehicleResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VehicleResponse):
            return True

        return self.to_dict() != other.to_dict()
