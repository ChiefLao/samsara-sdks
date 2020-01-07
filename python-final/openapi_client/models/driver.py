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


class Driver(object):
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
        'current_vehicle': 'object',
        'id': 'str',
        'static_assigned_vehicle': 'object',
        'tags': 'list[AddressAllOfTags]',
        'vehicle_group_tag': 'object',
        'carrier_settings': 'DriverAllOf1CarrierSettings',
        'eld_adverse_weather_exemption_enabled': 'bool',
        'eld_big_day_exemption_enabled': 'bool',
        'eld_day_start_hour': 'int',
        'eld_exempt': 'bool',
        'eld_exempt_reason': 'str',
        'eld_pc_enabled': 'bool',
        'eld_ym_enabled': 'bool',
        'external_ids': 'dict(str, str)',
        'is_deactivated': 'bool',
        'license_number': 'str',
        'license_state': 'str',
        'locale': 'str',
        'name': 'str',
        'notes': 'str',
        'phone': 'str',
        'timezone': 'str',
        'username': 'str'
    }

    attribute_map = {
        'current_vehicle': 'currentVehicle',
        'id': 'id',
        'static_assigned_vehicle': 'staticAssignedVehicle',
        'tags': 'tags',
        'vehicle_group_tag': 'vehicleGroupTag',
        'carrier_settings': 'carrierSettings',
        'eld_adverse_weather_exemption_enabled': 'eldAdverseWeatherExemptionEnabled',
        'eld_big_day_exemption_enabled': 'eldBigDayExemptionEnabled',
        'eld_day_start_hour': 'eldDayStartHour',
        'eld_exempt': 'eldExempt',
        'eld_exempt_reason': 'eldExemptReason',
        'eld_pc_enabled': 'eldPcEnabled',
        'eld_ym_enabled': 'eldYmEnabled',
        'external_ids': 'externalIds',
        'is_deactivated': 'isDeactivated',
        'license_number': 'licenseNumber',
        'license_state': 'licenseState',
        'locale': 'locale',
        'name': 'name',
        'notes': 'notes',
        'phone': 'phone',
        'timezone': 'timezone',
        'username': 'username'
    }

    def __init__(self, current_vehicle=None, id=None, static_assigned_vehicle=None, tags=None, vehicle_group_tag=None, carrier_settings=None, eld_adverse_weather_exemption_enabled=None, eld_big_day_exemption_enabled=None, eld_day_start_hour=None, eld_exempt=None, eld_exempt_reason=None, eld_pc_enabled=False, eld_ym_enabled=False, external_ids=None, is_deactivated=None, license_number=None, license_state=None, locale=None, name=None, notes=None, phone=None, timezone=None, username=None, local_vars_configuration=None):  # noqa: E501
        """Driver - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._current_vehicle = None
        self._id = None
        self._static_assigned_vehicle = None
        self._tags = None
        self._vehicle_group_tag = None
        self._carrier_settings = None
        self._eld_adverse_weather_exemption_enabled = None
        self._eld_big_day_exemption_enabled = None
        self._eld_day_start_hour = None
        self._eld_exempt = None
        self._eld_exempt_reason = None
        self._eld_pc_enabled = None
        self._eld_ym_enabled = None
        self._external_ids = None
        self._is_deactivated = None
        self._license_number = None
        self._license_state = None
        self._locale = None
        self._name = None
        self._notes = None
        self._phone = None
        self._timezone = None
        self._username = None
        self.discriminator = None

        if current_vehicle is not None:
            self.current_vehicle = current_vehicle
        if id is not None:
            self.id = id
        if static_assigned_vehicle is not None:
            self.static_assigned_vehicle = static_assigned_vehicle
        if tags is not None:
            self.tags = tags
        if vehicle_group_tag is not None:
            self.vehicle_group_tag = vehicle_group_tag
        if carrier_settings is not None:
            self.carrier_settings = carrier_settings
        if eld_adverse_weather_exemption_enabled is not None:
            self.eld_adverse_weather_exemption_enabled = eld_adverse_weather_exemption_enabled
        if eld_big_day_exemption_enabled is not None:
            self.eld_big_day_exemption_enabled = eld_big_day_exemption_enabled
        if eld_day_start_hour is not None:
            self.eld_day_start_hour = eld_day_start_hour
        if eld_exempt is not None:
            self.eld_exempt = eld_exempt
        if eld_exempt_reason is not None:
            self.eld_exempt_reason = eld_exempt_reason
        if eld_pc_enabled is not None:
            self.eld_pc_enabled = eld_pc_enabled
        if eld_ym_enabled is not None:
            self.eld_ym_enabled = eld_ym_enabled
        if external_ids is not None:
            self.external_ids = external_ids
        if is_deactivated is not None:
            self.is_deactivated = is_deactivated
        if license_number is not None:
            self.license_number = license_number
        if license_state is not None:
            self.license_state = license_state
        if locale is not None:
            self.locale = locale
        if name is not None:
            self.name = name
        if notes is not None:
            self.notes = notes
        if phone is not None:
            self.phone = phone
        if timezone is not None:
            self.timezone = timezone
        if username is not None:
            self.username = username

    @property
    def current_vehicle(self):
        """Gets the current_vehicle of this Driver.  # noqa: E501


        :return: The current_vehicle of this Driver.  # noqa: E501
        :rtype: object
        """
        return self._current_vehicle

    @current_vehicle.setter
    def current_vehicle(self, current_vehicle):
        """Sets the current_vehicle of this Driver.


        :param current_vehicle: The current_vehicle of this Driver.  # noqa: E501
        :type: object
        """

        self._current_vehicle = current_vehicle

    @property
    def id(self):
        """Gets the id of this Driver.  # noqa: E501

        Samsara ID for the driver.  # noqa: E501

        :return: The id of this Driver.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Driver.

        Samsara ID for the driver.  # noqa: E501

        :param id: The id of this Driver.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def static_assigned_vehicle(self):
        """Gets the static_assigned_vehicle of this Driver.  # noqa: E501


        :return: The static_assigned_vehicle of this Driver.  # noqa: E501
        :rtype: object
        """
        return self._static_assigned_vehicle

    @static_assigned_vehicle.setter
    def static_assigned_vehicle(self, static_assigned_vehicle):
        """Sets the static_assigned_vehicle of this Driver.


        :param static_assigned_vehicle: The static_assigned_vehicle of this Driver.  # noqa: E501
        :type: object
        """

        self._static_assigned_vehicle = static_assigned_vehicle

    @property
    def tags(self):
        """Gets the tags of this Driver.  # noqa: E501

        The tags this driver belongs to.  # noqa: E501

        :return: The tags of this Driver.  # noqa: E501
        :rtype: list[AddressAllOfTags]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Driver.

        The tags this driver belongs to.  # noqa: E501

        :param tags: The tags of this Driver.  # noqa: E501
        :type: list[AddressAllOfTags]
        """

        self._tags = tags

    @property
    def vehicle_group_tag(self):
        """Gets the vehicle_group_tag of this Driver.  # noqa: E501


        :return: The vehicle_group_tag of this Driver.  # noqa: E501
        :rtype: object
        """
        return self._vehicle_group_tag

    @vehicle_group_tag.setter
    def vehicle_group_tag(self, vehicle_group_tag):
        """Sets the vehicle_group_tag of this Driver.


        :param vehicle_group_tag: The vehicle_group_tag of this Driver.  # noqa: E501
        :type: object
        """

        self._vehicle_group_tag = vehicle_group_tag

    @property
    def carrier_settings(self):
        """Gets the carrier_settings of this Driver.  # noqa: E501


        :return: The carrier_settings of this Driver.  # noqa: E501
        :rtype: DriverAllOf1CarrierSettings
        """
        return self._carrier_settings

    @carrier_settings.setter
    def carrier_settings(self, carrier_settings):
        """Sets the carrier_settings of this Driver.


        :param carrier_settings: The carrier_settings of this Driver.  # noqa: E501
        :type: DriverAllOf1CarrierSettings
        """

        self._carrier_settings = carrier_settings

    @property
    def eld_adverse_weather_exemption_enabled(self):
        """Gets the eld_adverse_weather_exemption_enabled of this Driver.  # noqa: E501

        Flag indicating this driver may use Adverse Weather exemptions in ELD logs.  # noqa: E501

        :return: The eld_adverse_weather_exemption_enabled of this Driver.  # noqa: E501
        :rtype: bool
        """
        return self._eld_adverse_weather_exemption_enabled

    @eld_adverse_weather_exemption_enabled.setter
    def eld_adverse_weather_exemption_enabled(self, eld_adverse_weather_exemption_enabled):
        """Sets the eld_adverse_weather_exemption_enabled of this Driver.

        Flag indicating this driver may use Adverse Weather exemptions in ELD logs.  # noqa: E501

        :param eld_adverse_weather_exemption_enabled: The eld_adverse_weather_exemption_enabled of this Driver.  # noqa: E501
        :type: bool
        """

        self._eld_adverse_weather_exemption_enabled = eld_adverse_weather_exemption_enabled

    @property
    def eld_big_day_exemption_enabled(self):
        """Gets the eld_big_day_exemption_enabled of this Driver.  # noqa: E501

        Flag indicating this driver may use Big Day exemption in ELD logs.  # noqa: E501

        :return: The eld_big_day_exemption_enabled of this Driver.  # noqa: E501
        :rtype: bool
        """
        return self._eld_big_day_exemption_enabled

    @eld_big_day_exemption_enabled.setter
    def eld_big_day_exemption_enabled(self, eld_big_day_exemption_enabled):
        """Sets the eld_big_day_exemption_enabled of this Driver.

        Flag indicating this driver may use Big Day exemption in ELD logs.  # noqa: E501

        :param eld_big_day_exemption_enabled: The eld_big_day_exemption_enabled of this Driver.  # noqa: E501
        :type: bool
        """

        self._eld_big_day_exemption_enabled = eld_big_day_exemption_enabled

    @property
    def eld_day_start_hour(self):
        """Gets the eld_day_start_hour of this Driver.  # noqa: E501

        `0` indicating midnight-to-midnight ELD driving hours, `12` to indicate noon-to-noon driving hours.  # noqa: E501

        :return: The eld_day_start_hour of this Driver.  # noqa: E501
        :rtype: int
        """
        return self._eld_day_start_hour

    @eld_day_start_hour.setter
    def eld_day_start_hour(self, eld_day_start_hour):
        """Sets the eld_day_start_hour of this Driver.

        `0` indicating midnight-to-midnight ELD driving hours, `12` to indicate noon-to-noon driving hours.  # noqa: E501

        :param eld_day_start_hour: The eld_day_start_hour of this Driver.  # noqa: E501
        :type: int
        """

        self._eld_day_start_hour = eld_day_start_hour

    @property
    def eld_exempt(self):
        """Gets the eld_exempt of this Driver.  # noqa: E501

        Flag indicating this driver is exempt from the Electronic Logging Mandate.  # noqa: E501

        :return: The eld_exempt of this Driver.  # noqa: E501
        :rtype: bool
        """
        return self._eld_exempt

    @eld_exempt.setter
    def eld_exempt(self, eld_exempt):
        """Sets the eld_exempt of this Driver.

        Flag indicating this driver is exempt from the Electronic Logging Mandate.  # noqa: E501

        :param eld_exempt: The eld_exempt of this Driver.  # noqa: E501
        :type: bool
        """

        self._eld_exempt = eld_exempt

    @property
    def eld_exempt_reason(self):
        """Gets the eld_exempt_reason of this Driver.  # noqa: E501

        Reason that this driver is exempt from the Electronic Logging Mandate (see eldExempt).  # noqa: E501

        :return: The eld_exempt_reason of this Driver.  # noqa: E501
        :rtype: str
        """
        return self._eld_exempt_reason

    @eld_exempt_reason.setter
    def eld_exempt_reason(self, eld_exempt_reason):
        """Sets the eld_exempt_reason of this Driver.

        Reason that this driver is exempt from the Electronic Logging Mandate (see eldExempt).  # noqa: E501

        :param eld_exempt_reason: The eld_exempt_reason of this Driver.  # noqa: E501
        :type: str
        """

        self._eld_exempt_reason = eld_exempt_reason

    @property
    def eld_pc_enabled(self):
        """Gets the eld_pc_enabled of this Driver.  # noqa: E501

        Flag indicating this driver may select the Personal Conveyance duty status in ELD logs.  # noqa: E501

        :return: The eld_pc_enabled of this Driver.  # noqa: E501
        :rtype: bool
        """
        return self._eld_pc_enabled

    @eld_pc_enabled.setter
    def eld_pc_enabled(self, eld_pc_enabled):
        """Sets the eld_pc_enabled of this Driver.

        Flag indicating this driver may select the Personal Conveyance duty status in ELD logs.  # noqa: E501

        :param eld_pc_enabled: The eld_pc_enabled of this Driver.  # noqa: E501
        :type: bool
        """

        self._eld_pc_enabled = eld_pc_enabled

    @property
    def eld_ym_enabled(self):
        """Gets the eld_ym_enabled of this Driver.  # noqa: E501

        Flag indicating this driver may select the Yard Move duty status in ELD logs.  # noqa: E501

        :return: The eld_ym_enabled of this Driver.  # noqa: E501
        :rtype: bool
        """
        return self._eld_ym_enabled

    @eld_ym_enabled.setter
    def eld_ym_enabled(self, eld_ym_enabled):
        """Sets the eld_ym_enabled of this Driver.

        Flag indicating this driver may select the Yard Move duty status in ELD logs.  # noqa: E501

        :param eld_ym_enabled: The eld_ym_enabled of this Driver.  # noqa: E501
        :type: bool
        """

        self._eld_ym_enabled = eld_ym_enabled

    @property
    def external_ids(self):
        """Gets the external_ids of this Driver.  # noqa: E501

        User-defined dictionary of external IDs (key-value pairs). Both the keys and the values of the dictionary are of type string and must be alphanumeric. Each organization can have at most 10 unique external ID keys. To delete an external ID, set its value to null or the empty string (`\"\"`). An external ID can be used as a path parameter to retrieve or update that resource.  # noqa: E501

        :return: The external_ids of this Driver.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._external_ids

    @external_ids.setter
    def external_ids(self, external_ids):
        """Sets the external_ids of this Driver.

        User-defined dictionary of external IDs (key-value pairs). Both the keys and the values of the dictionary are of type string and must be alphanumeric. Each organization can have at most 10 unique external ID keys. To delete an external ID, set its value to null or the empty string (`\"\"`). An external ID can be used as a path parameter to retrieve or update that resource.  # noqa: E501

        :param external_ids: The external_ids of this Driver.  # noqa: E501
        :type: dict(str, str)
        """

        self._external_ids = external_ids

    @property
    def is_deactivated(self):
        """Gets the is_deactivated of this Driver.  # noqa: E501

        A boolean that indicates whether or not this driver is deactivated.  # noqa: E501

        :return: The is_deactivated of this Driver.  # noqa: E501
        :rtype: bool
        """
        return self._is_deactivated

    @is_deactivated.setter
    def is_deactivated(self, is_deactivated):
        """Sets the is_deactivated of this Driver.

        A boolean that indicates whether or not this driver is deactivated.  # noqa: E501

        :param is_deactivated: The is_deactivated of this Driver.  # noqa: E501
        :type: bool
        """

        self._is_deactivated = is_deactivated

    @property
    def license_number(self):
        """Gets the license_number of this Driver.  # noqa: E501

        Driver's state issued license number. The combination of this number and `licenseState` must be unique.  # noqa: E501

        :return: The license_number of this Driver.  # noqa: E501
        :rtype: str
        """
        return self._license_number

    @license_number.setter
    def license_number(self, license_number):
        """Sets the license_number of this Driver.

        Driver's state issued license number. The combination of this number and `licenseState` must be unique.  # noqa: E501

        :param license_number: The license_number of this Driver.  # noqa: E501
        :type: str
        """

        self._license_number = license_number

    @property
    def license_state(self):
        """Gets the license_state of this Driver.  # noqa: E501

        Abbreviation of state that issued driver's license.  # noqa: E501

        :return: The license_state of this Driver.  # noqa: E501
        :rtype: str
        """
        return self._license_state

    @license_state.setter
    def license_state(self, license_state):
        """Sets the license_state of this Driver.

        Abbreviation of state that issued driver's license.  # noqa: E501

        :param license_state: The license_state of this Driver.  # noqa: E501
        :type: str
        """

        self._license_state = license_state

    @property
    def locale(self):
        """Gets the locale of this Driver.  # noqa: E501

        Locale override (uncommon).  # noqa: E501

        :return: The locale of this Driver.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this Driver.

        Locale override (uncommon).  # noqa: E501

        :param locale: The locale of this Driver.  # noqa: E501
        :type: str
        """
        allowed_values = ["us", "at", "be", "ca", "gb", "fr", "de", "ie", "it", "lu", "mx", "es", "ch"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and locale not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `locale` ({0}), must be one of {1}"  # noqa: E501
                .format(locale, allowed_values)
            )

        self._locale = locale

    @property
    def name(self):
        """Gets the name of this Driver.  # noqa: E501

        Driver's name.  # noqa: E501

        :return: The name of this Driver.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Driver.

        Driver's name.  # noqa: E501

        :param name: The name of this Driver.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501

        self._name = name

    @property
    def notes(self):
        """Gets the notes of this Driver.  # noqa: E501

        Notes about the driver.  # noqa: E501

        :return: The notes of this Driver.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this Driver.

        Notes about the driver.  # noqa: E501

        :param notes: The notes of this Driver.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                notes is not None and len(notes) > 4096):
            raise ValueError("Invalid value for `notes`, length must be less than or equal to `4096`")  # noqa: E501

        self._notes = notes

    @property
    def phone(self):
        """Gets the phone of this Driver.  # noqa: E501

        Driver's phone number.  # noqa: E501

        :return: The phone of this Driver.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this Driver.

        Driver's phone number.  # noqa: E501

        :param phone: The phone of this Driver.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                phone is not None and len(phone) > 255):
            raise ValueError("Invalid value for `phone`, length must be less than or equal to `255`")  # noqa: E501

        self._phone = phone

    @property
    def timezone(self):
        """Gets the timezone of this Driver.  # noqa: E501

        Home terminal timezone, in order to indicate what time zone should be used to calculate the ELD logs.  # noqa: E501

        :return: The timezone of this Driver.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this Driver.

        Home terminal timezone, in order to indicate what time zone should be used to calculate the ELD logs.  # noqa: E501

        :param timezone: The timezone of this Driver.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def username(self):
        """Gets the username of this Driver.  # noqa: E501

        Driver's login username into the driver app. The username may not contain spaces or the '@' symbol. The username must be unique.  # noqa: E501

        :return: The username of this Driver.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this Driver.

        Driver's login username into the driver app. The username may not contain spaces or the '@' symbol. The username must be unique.  # noqa: E501

        :param username: The username of this Driver.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                username is not None and len(username) > 189):
            raise ValueError("Invalid value for `username`, length must be less than or equal to `189`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                username is not None and len(username) < 1):
            raise ValueError("Invalid value for `username`, length must be greater than or equal to `1`")  # noqa: E501

        self._username = username

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
        if not isinstance(other, Driver):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Driver):
            return True

        return self.to_dict() != other.to_dict()
