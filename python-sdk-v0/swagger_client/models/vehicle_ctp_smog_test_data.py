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


class VehicleCtpSmogTestData(object):
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
        'comm_protocol': 'str',
        'device_firmware': 'str',
        'dlc_pin_voltage_milli_volts': 'int',
        'dlc_pin_voltage_milli_volts_valid': 'bool',
        'link_id': 'str',
        'remote_obd_test_records': 'list[RemoteObdTestRecords]',
        'test_date_time': 'Time'
    }

    attribute_map = {
        'comm_protocol': 'commProtocol',
        'device_firmware': 'deviceFirmware',
        'dlc_pin_voltage_milli_volts': 'dlcPinVoltageMilliVolts',
        'dlc_pin_voltage_milli_volts_valid': 'dlcPinVoltageMilliVoltsValid',
        'link_id': 'linkId',
        'remote_obd_test_records': 'remoteObdTestRecords',
        'test_date_time': 'testDateTime'
    }

    def __init__(self, comm_protocol=None, device_firmware=None, dlc_pin_voltage_milli_volts=None, dlc_pin_voltage_milli_volts_valid=None, link_id=None, remote_obd_test_records=None, test_date_time=None):  # noqa: E501
        """VehicleCtpSmogTestData - a model defined in Swagger"""  # noqa: E501
        self._comm_protocol = None
        self._device_firmware = None
        self._dlc_pin_voltage_milli_volts = None
        self._dlc_pin_voltage_milli_volts_valid = None
        self._link_id = None
        self._remote_obd_test_records = None
        self._test_date_time = None
        self.discriminator = None
        if comm_protocol is not None:
            self.comm_protocol = comm_protocol
        if device_firmware is not None:
            self.device_firmware = device_firmware
        if dlc_pin_voltage_milli_volts is not None:
            self.dlc_pin_voltage_milli_volts = dlc_pin_voltage_milli_volts
        if dlc_pin_voltage_milli_volts_valid is not None:
            self.dlc_pin_voltage_milli_volts_valid = dlc_pin_voltage_milli_volts_valid
        if link_id is not None:
            self.link_id = link_id
        if remote_obd_test_records is not None:
            self.remote_obd_test_records = remote_obd_test_records
        if test_date_time is not None:
            self.test_date_time = test_date_time

    @property
    def comm_protocol(self):
        """Gets the comm_protocol of this VehicleCtpSmogTestData.  # noqa: E501

        CAN bus communication protocol as detected by the vehicle gateway.  # noqa: E501

        :return: The comm_protocol of this VehicleCtpSmogTestData.  # noqa: E501
        :rtype: str
        """
        return self._comm_protocol

    @comm_protocol.setter
    def comm_protocol(self, comm_protocol):
        """Sets the comm_protocol of this VehicleCtpSmogTestData.

        CAN bus communication protocol as detected by the vehicle gateway.  # noqa: E501

        :param comm_protocol: The comm_protocol of this VehicleCtpSmogTestData.  # noqa: E501
        :type: str
        """
        allowed_values = ["V", "P", "I", "Kf", "Ks", "C11", "C29", "C11s", "C29s"]  # noqa: E501
        if comm_protocol not in allowed_values:
            raise ValueError(
                "Invalid value for `comm_protocol` ({0}), must be one of {1}"  # noqa: E501
                .format(comm_protocol, allowed_values)
            )

        self._comm_protocol = comm_protocol

    @property
    def device_firmware(self):
        """Gets the device_firmware of this VehicleCtpSmogTestData.  # noqa: E501

        CTP firmware version as reported by the vehicle gateway.  # noqa: E501

        :return: The device_firmware of this VehicleCtpSmogTestData.  # noqa: E501
        :rtype: str
        """
        return self._device_firmware

    @device_firmware.setter
    def device_firmware(self, device_firmware):
        """Sets the device_firmware of this VehicleCtpSmogTestData.

        CTP firmware version as reported by the vehicle gateway.  # noqa: E501

        :param device_firmware: The device_firmware of this VehicleCtpSmogTestData.  # noqa: E501
        :type: str
        """

        self._device_firmware = device_firmware

    @property
    def dlc_pin_voltage_milli_volts(self):
        """Gets the dlc_pin_voltage_milli_volts of this VehicleCtpSmogTestData.  # noqa: E501

        Positive battery voltage as detected by the vehicle gateway reported in millivolts.  # noqa: E501

        :return: The dlc_pin_voltage_milli_volts of this VehicleCtpSmogTestData.  # noqa: E501
        :rtype: int
        """
        return self._dlc_pin_voltage_milli_volts

    @dlc_pin_voltage_milli_volts.setter
    def dlc_pin_voltage_milli_volts(self, dlc_pin_voltage_milli_volts):
        """Sets the dlc_pin_voltage_milli_volts of this VehicleCtpSmogTestData.

        Positive battery voltage as detected by the vehicle gateway reported in millivolts.  # noqa: E501

        :param dlc_pin_voltage_milli_volts: The dlc_pin_voltage_milli_volts of this VehicleCtpSmogTestData.  # noqa: E501
        :type: int
        """

        self._dlc_pin_voltage_milli_volts = dlc_pin_voltage_milli_volts

    @property
    def dlc_pin_voltage_milli_volts_valid(self):
        """Gets the dlc_pin_voltage_milli_volts_valid of this VehicleCtpSmogTestData.  # noqa: E501

        Indicates DlcPinVoltageMilliVolts was successfully read from the CAN bus.  # noqa: E501

        :return: The dlc_pin_voltage_milli_volts_valid of this VehicleCtpSmogTestData.  # noqa: E501
        :rtype: bool
        """
        return self._dlc_pin_voltage_milli_volts_valid

    @dlc_pin_voltage_milli_volts_valid.setter
    def dlc_pin_voltage_milli_volts_valid(self, dlc_pin_voltage_milli_volts_valid):
        """Sets the dlc_pin_voltage_milli_volts_valid of this VehicleCtpSmogTestData.

        Indicates DlcPinVoltageMilliVolts was successfully read from the CAN bus.  # noqa: E501

        :param dlc_pin_voltage_milli_volts_valid: The dlc_pin_voltage_milli_volts_valid of this VehicleCtpSmogTestData.  # noqa: E501
        :type: bool
        """

        self._dlc_pin_voltage_milli_volts_valid = dlc_pin_voltage_milli_volts_valid

    @property
    def link_id(self):
        """Gets the link_id of this VehicleCtpSmogTestData.  # noqa: E501

        Device serial number.  # noqa: E501

        :return: The link_id of this VehicleCtpSmogTestData.  # noqa: E501
        :rtype: str
        """
        return self._link_id

    @link_id.setter
    def link_id(self, link_id):
        """Sets the link_id of this VehicleCtpSmogTestData.

        Device serial number.  # noqa: E501

        :param link_id: The link_id of this VehicleCtpSmogTestData.  # noqa: E501
        :type: str
        """

        self._link_id = link_id

    @property
    def remote_obd_test_records(self):
        """Gets the remote_obd_test_records of this VehicleCtpSmogTestData.  # noqa: E501

        Contains all of the specific OBD data collected for a single ECU present on a vehicle. There can can be multiple ECUs on a vehicle.  # noqa: E501

        :return: The remote_obd_test_records of this VehicleCtpSmogTestData.  # noqa: E501
        :rtype: list[RemoteObdTestRecords]
        """
        return self._remote_obd_test_records

    @remote_obd_test_records.setter
    def remote_obd_test_records(self, remote_obd_test_records):
        """Sets the remote_obd_test_records of this VehicleCtpSmogTestData.

        Contains all of the specific OBD data collected for a single ECU present on a vehicle. There can can be multiple ECUs on a vehicle.  # noqa: E501

        :param remote_obd_test_records: The remote_obd_test_records of this VehicleCtpSmogTestData.  # noqa: E501
        :type: list[RemoteObdTestRecords]
        """

        self._remote_obd_test_records = remote_obd_test_records

    @property
    def test_date_time(self):
        """Gets the test_date_time of this VehicleCtpSmogTestData.  # noqa: E501


        :return: The test_date_time of this VehicleCtpSmogTestData.  # noqa: E501
        :rtype: Time
        """
        return self._test_date_time

    @test_date_time.setter
    def test_date_time(self, test_date_time):
        """Sets the test_date_time of this VehicleCtpSmogTestData.


        :param test_date_time: The test_date_time of this VehicleCtpSmogTestData.  # noqa: E501
        :type: Time
        """

        self._test_date_time = test_date_time

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
        if issubclass(VehicleCtpSmogTestData, dict):
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
        if not isinstance(other, VehicleCtpSmogTestData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
