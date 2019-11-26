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


class DriverCreate(object):
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
        'carrier_settings': 'object',
        'current_vehicle_id': 'str',
        'eld_adverse_weather_exemption_enabled': 'bool',
        'eld_big_day_exemption_enabled': 'bool',
        'eld_day_start_hour': 'int',
        'eld_exempt': 'bool',
        'eld_exempt_reason': 'str',
        'eld_pc_enabled': 'bool',
        'eld_ym_enabled': 'bool',
        'external_ids': 'ExternalIds',
        'license_number': 'str',
        'license_state': 'str',
        'locale': 'str',
        'name': 'str',
        'notes': 'str',
        'password': 'str',
        'phone': 'str',
        'static_assigned_vehicle_id': 'str',
        'tag_ids': 'list[str]',
        'timezone': 'str',
        'username': 'str',
        'vehicle_group_tag_id': 'str'
    }

    attribute_map = {
        'carrier_settings': 'carrierSettings',
        'current_vehicle_id': 'currentVehicleId',
        'eld_adverse_weather_exemption_enabled': 'eldAdverseWeatherExemptionEnabled',
        'eld_big_day_exemption_enabled': 'eldBigDayExemptionEnabled',
        'eld_day_start_hour': 'eldDayStartHour',
        'eld_exempt': 'eldExempt',
        'eld_exempt_reason': 'eldExemptReason',
        'eld_pc_enabled': 'eldPcEnabled',
        'eld_ym_enabled': 'eldYmEnabled',
        'external_ids': 'externalIds',
        'license_number': 'licenseNumber',
        'license_state': 'licenseState',
        'locale': 'locale',
        'name': 'name',
        'notes': 'notes',
        'password': 'password',
        'phone': 'phone',
        'static_assigned_vehicle_id': 'staticAssignedVehicleId',
        'tag_ids': 'tagIds',
        'timezone': 'timezone',
        'username': 'username',
        'vehicle_group_tag_id': 'vehicleGroupTagId'
    }

    def __init__(self, carrier_settings=None, current_vehicle_id=None, eld_adverse_weather_exemption_enabled=False, eld_big_day_exemption_enabled=False, eld_day_start_hour=None, eld_exempt=False, eld_exempt_reason=None, eld_pc_enabled=False, eld_ym_enabled=False, external_ids=None, license_number=None, license_state=None, locale=None, name=None, notes=None, password=None, phone=None, static_assigned_vehicle_id=None, tag_ids=None, timezone=None, username=None, vehicle_group_tag_id=None):  # noqa: E501
        """DriverCreate - a model defined in Swagger"""  # noqa: E501
        self._carrier_settings = None
        self._current_vehicle_id = None
        self._eld_adverse_weather_exemption_enabled = None
        self._eld_big_day_exemption_enabled = None
        self._eld_day_start_hour = None
        self._eld_exempt = None
        self._eld_exempt_reason = None
        self._eld_pc_enabled = None
        self._eld_ym_enabled = None
        self._external_ids = None
        self._license_number = None
        self._license_state = None
        self._locale = None
        self._name = None
        self._notes = None
        self._password = None
        self._phone = None
        self._static_assigned_vehicle_id = None
        self._tag_ids = None
        self._timezone = None
        self._username = None
        self._vehicle_group_tag_id = None
        self.discriminator = None
        if carrier_settings is not None:
            self.carrier_settings = carrier_settings
        if current_vehicle_id is not None:
            self.current_vehicle_id = current_vehicle_id
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
        if license_number is not None:
            self.license_number = license_number
        if license_state is not None:
            self.license_state = license_state
        if locale is not None:
            self.locale = locale
        self.name = name
        if notes is not None:
            self.notes = notes
        self.password = password
        if phone is not None:
            self.phone = phone
        if static_assigned_vehicle_id is not None:
            self.static_assigned_vehicle_id = static_assigned_vehicle_id
        if tag_ids is not None:
            self.tag_ids = tag_ids
        if timezone is not None:
            self.timezone = timezone
        self.username = username
        if vehicle_group_tag_id is not None:
            self.vehicle_group_tag_id = vehicle_group_tag_id

    @property
    def carrier_settings(self):
        """Gets the carrier_settings of this DriverCreate.  # noqa: E501

        Carrier for a given driver. If the driver's carrier differs from the general organization's carrier settings, the override value is used. Updating this value only updates the override setting for this driver.  # noqa: E501

        :return: The carrier_settings of this DriverCreate.  # noqa: E501
        :rtype: object
        """
        return self._carrier_settings

    @carrier_settings.setter
    def carrier_settings(self, carrier_settings):
        """Sets the carrier_settings of this DriverCreate.

        Carrier for a given driver. If the driver's carrier differs from the general organization's carrier settings, the override value is used. Updating this value only updates the override setting for this driver.  # noqa: E501

        :param carrier_settings: The carrier_settings of this DriverCreate.  # noqa: E501
        :type: object
        """

        self._carrier_settings = carrier_settings

    @property
    def current_vehicle_id(self):
        """Gets the current_vehicle_id of this DriverCreate.  # noqa: E501

        ID of vehicle that driver is currently assigned to.  # noqa: E501

        :return: The current_vehicle_id of this DriverCreate.  # noqa: E501
        :rtype: str
        """
        return self._current_vehicle_id

    @current_vehicle_id.setter
    def current_vehicle_id(self, current_vehicle_id):
        """Sets the current_vehicle_id of this DriverCreate.

        ID of vehicle that driver is currently assigned to.  # noqa: E501

        :param current_vehicle_id: The current_vehicle_id of this DriverCreate.  # noqa: E501
        :type: str
        """

        self._current_vehicle_id = current_vehicle_id

    @property
    def eld_adverse_weather_exemption_enabled(self):
        """Gets the eld_adverse_weather_exemption_enabled of this DriverCreate.  # noqa: E501

        Flag indicating this driver may use Adverse Weather exemptions in ELD logs.  # noqa: E501

        :return: The eld_adverse_weather_exemption_enabled of this DriverCreate.  # noqa: E501
        :rtype: bool
        """
        return self._eld_adverse_weather_exemption_enabled

    @eld_adverse_weather_exemption_enabled.setter
    def eld_adverse_weather_exemption_enabled(self, eld_adverse_weather_exemption_enabled):
        """Sets the eld_adverse_weather_exemption_enabled of this DriverCreate.

        Flag indicating this driver may use Adverse Weather exemptions in ELD logs.  # noqa: E501

        :param eld_adverse_weather_exemption_enabled: The eld_adverse_weather_exemption_enabled of this DriverCreate.  # noqa: E501
        :type: bool
        """

        self._eld_adverse_weather_exemption_enabled = eld_adverse_weather_exemption_enabled

    @property
    def eld_big_day_exemption_enabled(self):
        """Gets the eld_big_day_exemption_enabled of this DriverCreate.  # noqa: E501

        Flag indicating this driver may use Big Day exemption in ELD logs.  # noqa: E501

        :return: The eld_big_day_exemption_enabled of this DriverCreate.  # noqa: E501
        :rtype: bool
        """
        return self._eld_big_day_exemption_enabled

    @eld_big_day_exemption_enabled.setter
    def eld_big_day_exemption_enabled(self, eld_big_day_exemption_enabled):
        """Sets the eld_big_day_exemption_enabled of this DriverCreate.

        Flag indicating this driver may use Big Day exemption in ELD logs.  # noqa: E501

        :param eld_big_day_exemption_enabled: The eld_big_day_exemption_enabled of this DriverCreate.  # noqa: E501
        :type: bool
        """

        self._eld_big_day_exemption_enabled = eld_big_day_exemption_enabled

    @property
    def eld_day_start_hour(self):
        """Gets the eld_day_start_hour of this DriverCreate.  # noqa: E501

        `0` indicating midnight-to-midnight ELD driving hours, `12` to indicate noon-to-noon driving hours.  # noqa: E501

        :return: The eld_day_start_hour of this DriverCreate.  # noqa: E501
        :rtype: int
        """
        return self._eld_day_start_hour

    @eld_day_start_hour.setter
    def eld_day_start_hour(self, eld_day_start_hour):
        """Sets the eld_day_start_hour of this DriverCreate.

        `0` indicating midnight-to-midnight ELD driving hours, `12` to indicate noon-to-noon driving hours.  # noqa: E501

        :param eld_day_start_hour: The eld_day_start_hour of this DriverCreate.  # noqa: E501
        :type: int
        """

        self._eld_day_start_hour = eld_day_start_hour

    @property
    def eld_exempt(self):
        """Gets the eld_exempt of this DriverCreate.  # noqa: E501

        Flag indicating this driver is exempt from the Electronic Logging Mandate.  # noqa: E501

        :return: The eld_exempt of this DriverCreate.  # noqa: E501
        :rtype: bool
        """
        return self._eld_exempt

    @eld_exempt.setter
    def eld_exempt(self, eld_exempt):
        """Sets the eld_exempt of this DriverCreate.

        Flag indicating this driver is exempt from the Electronic Logging Mandate.  # noqa: E501

        :param eld_exempt: The eld_exempt of this DriverCreate.  # noqa: E501
        :type: bool
        """

        self._eld_exempt = eld_exempt

    @property
    def eld_exempt_reason(self):
        """Gets the eld_exempt_reason of this DriverCreate.  # noqa: E501

        Reason that this driver is exempt from the Electronic Logging Mandate (see eldExempt).  # noqa: E501

        :return: The eld_exempt_reason of this DriverCreate.  # noqa: E501
        :rtype: str
        """
        return self._eld_exempt_reason

    @eld_exempt_reason.setter
    def eld_exempt_reason(self, eld_exempt_reason):
        """Sets the eld_exempt_reason of this DriverCreate.

        Reason that this driver is exempt from the Electronic Logging Mandate (see eldExempt).  # noqa: E501

        :param eld_exempt_reason: The eld_exempt_reason of this DriverCreate.  # noqa: E501
        :type: str
        """

        self._eld_exempt_reason = eld_exempt_reason

    @property
    def eld_pc_enabled(self):
        """Gets the eld_pc_enabled of this DriverCreate.  # noqa: E501

        Flag indicating this driver may select the Personal Conveyance duty status in ELD logs.  # noqa: E501

        :return: The eld_pc_enabled of this DriverCreate.  # noqa: E501
        :rtype: bool
        """
        return self._eld_pc_enabled

    @eld_pc_enabled.setter
    def eld_pc_enabled(self, eld_pc_enabled):
        """Sets the eld_pc_enabled of this DriverCreate.

        Flag indicating this driver may select the Personal Conveyance duty status in ELD logs.  # noqa: E501

        :param eld_pc_enabled: The eld_pc_enabled of this DriverCreate.  # noqa: E501
        :type: bool
        """

        self._eld_pc_enabled = eld_pc_enabled

    @property
    def eld_ym_enabled(self):
        """Gets the eld_ym_enabled of this DriverCreate.  # noqa: E501

        Flag indicating this driver may select the Yard Move duty status in ELD logs.  # noqa: E501

        :return: The eld_ym_enabled of this DriverCreate.  # noqa: E501
        :rtype: bool
        """
        return self._eld_ym_enabled

    @eld_ym_enabled.setter
    def eld_ym_enabled(self, eld_ym_enabled):
        """Sets the eld_ym_enabled of this DriverCreate.

        Flag indicating this driver may select the Yard Move duty status in ELD logs.  # noqa: E501

        :param eld_ym_enabled: The eld_ym_enabled of this DriverCreate.  # noqa: E501
        :type: bool
        """

        self._eld_ym_enabled = eld_ym_enabled

    @property
    def external_ids(self):
        """Gets the external_ids of this DriverCreate.  # noqa: E501


        :return: The external_ids of this DriverCreate.  # noqa: E501
        :rtype: ExternalIds
        """
        return self._external_ids

    @external_ids.setter
    def external_ids(self, external_ids):
        """Sets the external_ids of this DriverCreate.


        :param external_ids: The external_ids of this DriverCreate.  # noqa: E501
        :type: ExternalIds
        """

        self._external_ids = external_ids

    @property
    def license_number(self):
        """Gets the license_number of this DriverCreate.  # noqa: E501

        Driver's state issued license number. The combination of this number and `licenseState` must be unique.  # noqa: E501

        :return: The license_number of this DriverCreate.  # noqa: E501
        :rtype: str
        """
        return self._license_number

    @license_number.setter
    def license_number(self, license_number):
        """Sets the license_number of this DriverCreate.

        Driver's state issued license number. The combination of this number and `licenseState` must be unique.  # noqa: E501

        :param license_number: The license_number of this DriverCreate.  # noqa: E501
        :type: str
        """

        self._license_number = license_number

    @property
    def license_state(self):
        """Gets the license_state of this DriverCreate.  # noqa: E501

        Abbreviation of state that issued driver's license.  # noqa: E501

        :return: The license_state of this DriverCreate.  # noqa: E501
        :rtype: str
        """
        return self._license_state

    @license_state.setter
    def license_state(self, license_state):
        """Sets the license_state of this DriverCreate.

        Abbreviation of state that issued driver's license.  # noqa: E501

        :param license_state: The license_state of this DriverCreate.  # noqa: E501
        :type: str
        """

        self._license_state = license_state

    @property
    def locale(self):
        """Gets the locale of this DriverCreate.  # noqa: E501

        Locale override (uncommon). These are specified by ISO 3166-2 country codes for supported locales.  # noqa: E501

        :return: The locale of this DriverCreate.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this DriverCreate.

        Locale override (uncommon). These are specified by ISO 3166-2 country codes for supported locales.  # noqa: E501

        :param locale: The locale of this DriverCreate.  # noqa: E501
        :type: str
        """
        allowed_values = ["us", "at", "be", "ca", "gb", "fr", "de", "ie", "it", "lu", "mx", "nl", "es", "ch"]  # noqa: E501
        if locale not in allowed_values:
            raise ValueError(
                "Invalid value for `locale` ({0}), must be one of {1}"  # noqa: E501
                .format(locale, allowed_values)
            )

        self._locale = locale

    @property
    def name(self):
        """Gets the name of this DriverCreate.  # noqa: E501

        Driver's name.  # noqa: E501

        :return: The name of this DriverCreate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DriverCreate.

        Driver's name.  # noqa: E501

        :param name: The name of this DriverCreate.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def notes(self):
        """Gets the notes of this DriverCreate.  # noqa: E501

        Notes about the driver.  # noqa: E501

        :return: The notes of this DriverCreate.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this DriverCreate.

        Notes about the driver.  # noqa: E501

        :param notes: The notes of this DriverCreate.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def password(self):
        """Gets the password of this DriverCreate.  # noqa: E501

        Password that the driver can use to login to the Samsara driver app.  # noqa: E501

        :return: The password of this DriverCreate.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this DriverCreate.

        Password that the driver can use to login to the Samsara driver app.  # noqa: E501

        :param password: The password of this DriverCreate.  # noqa: E501
        :type: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def phone(self):
        """Gets the phone of this DriverCreate.  # noqa: E501

        Phone number of the driver.  # noqa: E501

        :return: The phone of this DriverCreate.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this DriverCreate.

        Phone number of the driver.  # noqa: E501

        :param phone: The phone of this DriverCreate.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def static_assigned_vehicle_id(self):
        """Gets the static_assigned_vehicle_id of this DriverCreate.  # noqa: E501

        ID of vehicle that the driver is permanently assigned to. (uncommon).  # noqa: E501

        :return: The static_assigned_vehicle_id of this DriverCreate.  # noqa: E501
        :rtype: str
        """
        return self._static_assigned_vehicle_id

    @static_assigned_vehicle_id.setter
    def static_assigned_vehicle_id(self, static_assigned_vehicle_id):
        """Sets the static_assigned_vehicle_id of this DriverCreate.

        ID of vehicle that the driver is permanently assigned to. (uncommon).  # noqa: E501

        :param static_assigned_vehicle_id: The static_assigned_vehicle_id of this DriverCreate.  # noqa: E501
        :type: str
        """

        self._static_assigned_vehicle_id = static_assigned_vehicle_id

    @property
    def tag_ids(self):
        """Gets the tag_ids of this DriverCreate.  # noqa: E501

        IDs of tags the driver is associated with.  # noqa: E501

        :return: The tag_ids of this DriverCreate.  # noqa: E501
        :rtype: list[str]
        """
        return self._tag_ids

    @tag_ids.setter
    def tag_ids(self, tag_ids):
        """Sets the tag_ids of this DriverCreate.

        IDs of tags the driver is associated with.  # noqa: E501

        :param tag_ids: The tag_ids of this DriverCreate.  # noqa: E501
        :type: list[str]
        """

        self._tag_ids = tag_ids

    @property
    def timezone(self):
        """Gets the timezone of this DriverCreate.  # noqa: E501

        Home terminal timezone, in order to indicate what time zone should be used to calculate the ELD logs.  # noqa: E501

        :return: The timezone of this DriverCreate.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this DriverCreate.

        Home terminal timezone, in order to indicate what time zone should be used to calculate the ELD logs.  # noqa: E501

        :param timezone: The timezone of this DriverCreate.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def username(self):
        """Gets the username of this DriverCreate.  # noqa: E501

        Driver's login username into the driver app. The username may not contain spaces or the '@' symbol. The username must be unique.  # noqa: E501

        :return: The username of this DriverCreate.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this DriverCreate.

        Driver's login username into the driver app. The username may not contain spaces or the '@' symbol. The username must be unique.  # noqa: E501

        :param username: The username of this DriverCreate.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def vehicle_group_tag_id(self):
        """Gets the vehicle_group_tag_id of this DriverCreate.  # noqa: E501

        Tag ID which determines which vehicles a driver will see when selecting vehicles.  # noqa: E501

        :return: The vehicle_group_tag_id of this DriverCreate.  # noqa: E501
        :rtype: str
        """
        return self._vehicle_group_tag_id

    @vehicle_group_tag_id.setter
    def vehicle_group_tag_id(self, vehicle_group_tag_id):
        """Sets the vehicle_group_tag_id of this DriverCreate.

        Tag ID which determines which vehicles a driver will see when selecting vehicles.  # noqa: E501

        :param vehicle_group_tag_id: The vehicle_group_tag_id of this DriverCreate.  # noqa: E501
        :type: str
        """

        self._vehicle_group_tag_id = vehicle_group_tag_id

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
        if issubclass(DriverCreate, dict):
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
        if not isinstance(other, DriverCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
