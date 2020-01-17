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


class InlineObject2(object):
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
        'inspection_type': 'str',
        'mechanic_notes': 'str',
        'odometer_miles': 'int',
        'previous_defects_corrected': 'bool',
        'previous_defects_ignored': 'bool',
        'resolved_defect_ids': 'list[int]',
        'safe': 'str',
        'trailer_id': 'int',
        'user_email': 'str',
        'vehicle_id': 'int'
    }

    attribute_map = {
        'inspection_type': 'inspectionType',
        'mechanic_notes': 'mechanicNotes',
        'odometer_miles': 'odometerMiles',
        'previous_defects_corrected': 'previousDefectsCorrected',
        'previous_defects_ignored': 'previousDefectsIgnored',
        'resolved_defect_ids': 'resolvedDefectIds',
        'safe': 'safe',
        'trailer_id': 'trailerId',
        'user_email': 'userEmail',
        'vehicle_id': 'vehicleId'
    }

    def __init__(self, inspection_type=None, mechanic_notes=None, odometer_miles=None, previous_defects_corrected=None, previous_defects_ignored=None, resolved_defect_ids=None, safe=None, trailer_id=None, user_email=None, vehicle_id=None, local_vars_configuration=None):  # noqa: E501
        """InlineObject2 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._inspection_type = None
        self._mechanic_notes = None
        self._odometer_miles = None
        self._previous_defects_corrected = None
        self._previous_defects_ignored = None
        self._resolved_defect_ids = None
        self._safe = None
        self._trailer_id = None
        self._user_email = None
        self._vehicle_id = None
        self.discriminator = None

        self.inspection_type = inspection_type
        if mechanic_notes is not None:
            self.mechanic_notes = mechanic_notes
        if odometer_miles is not None:
            self.odometer_miles = odometer_miles
        if previous_defects_corrected is not None:
            self.previous_defects_corrected = previous_defects_corrected
        if previous_defects_ignored is not None:
            self.previous_defects_ignored = previous_defects_ignored
        if resolved_defect_ids is not None:
            self.resolved_defect_ids = resolved_defect_ids
        self.safe = safe
        if trailer_id is not None:
            self.trailer_id = trailer_id
        self.user_email = user_email
        if vehicle_id is not None:
            self.vehicle_id = vehicle_id

    @property
    def inspection_type(self):
        """Gets the inspection_type of this InlineObject2.  # noqa: E501

        Only type 'mechanic' is currently accepted.  # noqa: E501

        :return: The inspection_type of this InlineObject2.  # noqa: E501
        :rtype: str
        """
        return self._inspection_type

    @inspection_type.setter
    def inspection_type(self, inspection_type):
        """Sets the inspection_type of this InlineObject2.

        Only type 'mechanic' is currently accepted.  # noqa: E501

        :param inspection_type: The inspection_type of this InlineObject2.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and inspection_type is None:  # noqa: E501
            raise ValueError("Invalid value for `inspection_type`, must not be `None`")  # noqa: E501
        allowed_values = ["mechanic"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and inspection_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `inspection_type` ({0}), must be one of {1}"  # noqa: E501
                .format(inspection_type, allowed_values)
            )

        self._inspection_type = inspection_type

    @property
    def mechanic_notes(self):
        """Gets the mechanic_notes of this InlineObject2.  # noqa: E501

        Any notes from the mechanic.  # noqa: E501

        :return: The mechanic_notes of this InlineObject2.  # noqa: E501
        :rtype: str
        """
        return self._mechanic_notes

    @mechanic_notes.setter
    def mechanic_notes(self, mechanic_notes):
        """Sets the mechanic_notes of this InlineObject2.

        Any notes from the mechanic.  # noqa: E501

        :param mechanic_notes: The mechanic_notes of this InlineObject2.  # noqa: E501
        :type: str
        """

        self._mechanic_notes = mechanic_notes

    @property
    def odometer_miles(self):
        """Gets the odometer_miles of this InlineObject2.  # noqa: E501

        The current odometer of the vehicle.  # noqa: E501

        :return: The odometer_miles of this InlineObject2.  # noqa: E501
        :rtype: int
        """
        return self._odometer_miles

    @odometer_miles.setter
    def odometer_miles(self, odometer_miles):
        """Sets the odometer_miles of this InlineObject2.

        The current odometer of the vehicle.  # noqa: E501

        :param odometer_miles: The odometer_miles of this InlineObject2.  # noqa: E501
        :type: int
        """

        self._odometer_miles = odometer_miles

    @property
    def previous_defects_corrected(self):
        """Gets the previous_defects_corrected of this InlineObject2.  # noqa: E501

        Whether any previous defects were corrected. If this vehicle or trailer was previously marked unsafe, and this DVIR marks it as safe, either previousDefectsCorrected or previousDefectsIgnored must be true.  # noqa: E501

        :return: The previous_defects_corrected of this InlineObject2.  # noqa: E501
        :rtype: bool
        """
        return self._previous_defects_corrected

    @previous_defects_corrected.setter
    def previous_defects_corrected(self, previous_defects_corrected):
        """Sets the previous_defects_corrected of this InlineObject2.

        Whether any previous defects were corrected. If this vehicle or trailer was previously marked unsafe, and this DVIR marks it as safe, either previousDefectsCorrected or previousDefectsIgnored must be true.  # noqa: E501

        :param previous_defects_corrected: The previous_defects_corrected of this InlineObject2.  # noqa: E501
        :type: bool
        """

        self._previous_defects_corrected = previous_defects_corrected

    @property
    def previous_defects_ignored(self):
        """Gets the previous_defects_ignored of this InlineObject2.  # noqa: E501

        Whether any previous defects were ignored. If this vehicle or trailer was previously marked unsafe, and this DVIR marks it as safe, either previousDefectsCorrected or previousDefectsIgnored must be true.  # noqa: E501

        :return: The previous_defects_ignored of this InlineObject2.  # noqa: E501
        :rtype: bool
        """
        return self._previous_defects_ignored

    @previous_defects_ignored.setter
    def previous_defects_ignored(self, previous_defects_ignored):
        """Sets the previous_defects_ignored of this InlineObject2.

        Whether any previous defects were ignored. If this vehicle or trailer was previously marked unsafe, and this DVIR marks it as safe, either previousDefectsCorrected or previousDefectsIgnored must be true.  # noqa: E501

        :param previous_defects_ignored: The previous_defects_ignored of this InlineObject2.  # noqa: E501
        :type: bool
        """

        self._previous_defects_ignored = previous_defects_ignored

    @property
    def resolved_defect_ids(self):
        """Gets the resolved_defect_ids of this InlineObject2.  # noqa: E501

        List of defect IDs to resolve.  The defects must be associated with the provided vehicle or trailer.  # noqa: E501

        :return: The resolved_defect_ids of this InlineObject2.  # noqa: E501
        :rtype: list[int]
        """
        return self._resolved_defect_ids

    @resolved_defect_ids.setter
    def resolved_defect_ids(self, resolved_defect_ids):
        """Sets the resolved_defect_ids of this InlineObject2.

        List of defect IDs to resolve.  The defects must be associated with the provided vehicle or trailer.  # noqa: E501

        :param resolved_defect_ids: The resolved_defect_ids of this InlineObject2.  # noqa: E501
        :type: list[int]
        """

        self._resolved_defect_ids = resolved_defect_ids

    @property
    def safe(self):
        """Gets the safe of this InlineObject2.  # noqa: E501

        Whether or not this vehicle or trailer is safe to drive.  # noqa: E501

        :return: The safe of this InlineObject2.  # noqa: E501
        :rtype: str
        """
        return self._safe

    @safe.setter
    def safe(self, safe):
        """Sets the safe of this InlineObject2.

        Whether or not this vehicle or trailer is safe to drive.  # noqa: E501

        :param safe: The safe of this InlineObject2.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and safe is None:  # noqa: E501
            raise ValueError("Invalid value for `safe`, must not be `None`")  # noqa: E501
        allowed_values = ["safe", "unsafe"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and safe not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `safe` ({0}), must be one of {1}"  # noqa: E501
                .format(safe, allowed_values)
            )

        self._safe = safe

    @property
    def trailer_id(self):
        """Gets the trailer_id of this InlineObject2.  # noqa: E501

        Id of trailer being inspected. Either vehicleId or trailerId must be provided.  # noqa: E501

        :return: The trailer_id of this InlineObject2.  # noqa: E501
        :rtype: int
        """
        return self._trailer_id

    @trailer_id.setter
    def trailer_id(self, trailer_id):
        """Sets the trailer_id of this InlineObject2.

        Id of trailer being inspected. Either vehicleId or trailerId must be provided.  # noqa: E501

        :param trailer_id: The trailer_id of this InlineObject2.  # noqa: E501
        :type: int
        """

        self._trailer_id = trailer_id

    @property
    def user_email(self):
        """Gets the user_email of this InlineObject2.  # noqa: E501

        The Samsara login email for the person creating the DVIR. The email must correspond to a Samsara user's email.  # noqa: E501

        :return: The user_email of this InlineObject2.  # noqa: E501
        :rtype: str
        """
        return self._user_email

    @user_email.setter
    def user_email(self, user_email):
        """Sets the user_email of this InlineObject2.

        The Samsara login email for the person creating the DVIR. The email must correspond to a Samsara user's email.  # noqa: E501

        :param user_email: The user_email of this InlineObject2.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and user_email is None:  # noqa: E501
            raise ValueError("Invalid value for `user_email`, must not be `None`")  # noqa: E501

        self._user_email = user_email

    @property
    def vehicle_id(self):
        """Gets the vehicle_id of this InlineObject2.  # noqa: E501

        Id of vehicle being inspected. Either vehicleId or trailerId must be provided.  # noqa: E501

        :return: The vehicle_id of this InlineObject2.  # noqa: E501
        :rtype: int
        """
        return self._vehicle_id

    @vehicle_id.setter
    def vehicle_id(self, vehicle_id):
        """Sets the vehicle_id of this InlineObject2.

        Id of vehicle being inspected. Either vehicleId or trailerId must be provided.  # noqa: E501

        :param vehicle_id: The vehicle_id of this InlineObject2.  # noqa: E501
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
        if not isinstance(other, InlineObject2):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineObject2):
            return True

        return self.to_dict() != other.to_dict()
