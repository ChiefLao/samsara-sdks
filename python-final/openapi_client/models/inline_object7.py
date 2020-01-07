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


class InlineObject7(object):
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
        'end_ms': 'int',
        'fill_missing': 'str',
        'group_id': 'int',
        'series': 'list[V1SensorsHistorySeries]',
        'start_ms': 'int',
        'step_ms': 'int'
    }

    attribute_map = {
        'end_ms': 'endMs',
        'fill_missing': 'fillMissing',
        'group_id': 'groupId',
        'series': 'series',
        'start_ms': 'startMs',
        'step_ms': 'stepMs'
    }

    def __init__(self, end_ms=None, fill_missing='withNull', group_id=None, series=None, start_ms=None, step_ms=None, local_vars_configuration=None):  # noqa: E501
        """InlineObject7 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._end_ms = None
        self._fill_missing = None
        self._group_id = None
        self._series = None
        self._start_ms = None
        self._step_ms = None
        self.discriminator = None

        self.end_ms = end_ms
        if fill_missing is not None:
            self.fill_missing = fill_missing
        self.group_id = group_id
        self.series = series
        self.start_ms = start_ms
        self.step_ms = step_ms

    @property
    def end_ms(self):
        """Gets the end_ms of this InlineObject7.  # noqa: E501

        End of the time range, specified in milliseconds UNIX time.  # noqa: E501

        :return: The end_ms of this InlineObject7.  # noqa: E501
        :rtype: int
        """
        return self._end_ms

    @end_ms.setter
    def end_ms(self, end_ms):
        """Sets the end_ms of this InlineObject7.

        End of the time range, specified in milliseconds UNIX time.  # noqa: E501

        :param end_ms: The end_ms of this InlineObject7.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and end_ms is None:  # noqa: E501
            raise ValueError("Invalid value for `end_ms`, must not be `None`")  # noqa: E501

        self._end_ms = end_ms

    @property
    def fill_missing(self):
        """Gets the fill_missing of this InlineObject7.  # noqa: E501


        :return: The fill_missing of this InlineObject7.  # noqa: E501
        :rtype: str
        """
        return self._fill_missing

    @fill_missing.setter
    def fill_missing(self, fill_missing):
        """Sets the fill_missing of this InlineObject7.


        :param fill_missing: The fill_missing of this InlineObject7.  # noqa: E501
        :type: str
        """
        allowed_values = ["withNull", "withPrevious"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and fill_missing not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `fill_missing` ({0}), must be one of {1}"  # noqa: E501
                .format(fill_missing, allowed_values)
            )

        self._fill_missing = fill_missing

    @property
    def group_id(self):
        """Gets the group_id of this InlineObject7.  # noqa: E501

        Group ID  # noqa: E501

        :return: The group_id of this InlineObject7.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this InlineObject7.

        Group ID  # noqa: E501

        :param group_id: The group_id of this InlineObject7.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and group_id is None:  # noqa: E501
            raise ValueError("Invalid value for `group_id`, must not be `None`")  # noqa: E501

        self._group_id = group_id

    @property
    def series(self):
        """Gets the series of this InlineObject7.  # noqa: E501


        :return: The series of this InlineObject7.  # noqa: E501
        :rtype: list[V1SensorsHistorySeries]
        """
        return self._series

    @series.setter
    def series(self, series):
        """Sets the series of this InlineObject7.


        :param series: The series of this InlineObject7.  # noqa: E501
        :type: list[V1SensorsHistorySeries]
        """
        if self.local_vars_configuration.client_side_validation and series is None:  # noqa: E501
            raise ValueError("Invalid value for `series`, must not be `None`")  # noqa: E501

        self._series = series

    @property
    def start_ms(self):
        """Gets the start_ms of this InlineObject7.  # noqa: E501

        Beginning of the time range, specified in milliseconds UNIX time.  # noqa: E501

        :return: The start_ms of this InlineObject7.  # noqa: E501
        :rtype: int
        """
        return self._start_ms

    @start_ms.setter
    def start_ms(self, start_ms):
        """Sets the start_ms of this InlineObject7.

        Beginning of the time range, specified in milliseconds UNIX time.  # noqa: E501

        :param start_ms: The start_ms of this InlineObject7.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and start_ms is None:  # noqa: E501
            raise ValueError("Invalid value for `start_ms`, must not be `None`")  # noqa: E501

        self._start_ms = start_ms

    @property
    def step_ms(self):
        """Gets the step_ms of this InlineObject7.  # noqa: E501

        Time resolution for which data should be returned, in milliseconds. Specifying 3600000 will return data at hour intervals.  # noqa: E501

        :return: The step_ms of this InlineObject7.  # noqa: E501
        :rtype: int
        """
        return self._step_ms

    @step_ms.setter
    def step_ms(self, step_ms):
        """Sets the step_ms of this InlineObject7.

        Time resolution for which data should be returned, in milliseconds. Specifying 3600000 will return data at hour intervals.  # noqa: E501

        :param step_ms: The step_ms of this InlineObject7.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and step_ms is None:  # noqa: E501
            raise ValueError("Invalid value for `step_ms`, must not be `None`")  # noqa: E501

        self._step_ms = step_ms

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
        if not isinstance(other, InlineObject7):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineObject7):
            return True

        return self.to_dict() != other.to_dict()
