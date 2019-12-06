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


class V1DocumentCreateBase(object):
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
        'dispatch_job_id': 'int',
        'notes': 'str',
        'state': 'str'
    }

    attribute_map = {
        'dispatch_job_id': 'dispatchJobId',
        'notes': 'notes',
        'state': 'state'
    }

    def __init__(self, dispatch_job_id=None, notes=None, state='Required'):  # noqa: E501
        """V1DocumentCreateBase - a model defined in Swagger"""  # noqa: E501
        self._dispatch_job_id = None
        self._notes = None
        self._state = None
        self.discriminator = None
        if dispatch_job_id is not None:
            self.dispatch_job_id = dispatch_job_id
        if notes is not None:
            self.notes = notes
        if state is not None:
            self.state = state

    @property
    def dispatch_job_id(self):
        """Gets the dispatch_job_id of this V1DocumentCreateBase.  # noqa: E501

        ID of the Samsara dispatch job for which the document is submitted  # noqa: E501

        :return: The dispatch_job_id of this V1DocumentCreateBase.  # noqa: E501
        :rtype: int
        """
        return self._dispatch_job_id

    @dispatch_job_id.setter
    def dispatch_job_id(self, dispatch_job_id):
        """Sets the dispatch_job_id of this V1DocumentCreateBase.

        ID of the Samsara dispatch job for which the document is submitted  # noqa: E501

        :param dispatch_job_id: The dispatch_job_id of this V1DocumentCreateBase.  # noqa: E501
        :type: int
        """

        self._dispatch_job_id = dispatch_job_id

    @property
    def notes(self):
        """Gets the notes of this V1DocumentCreateBase.  # noqa: E501

        Notes submitted with this document.  # noqa: E501

        :return: The notes of this V1DocumentCreateBase.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this V1DocumentCreateBase.

        Notes submitted with this document.  # noqa: E501

        :param notes: The notes of this V1DocumentCreateBase.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def state(self):
        """Gets the state of this V1DocumentCreateBase.  # noqa: E501

        The condition of the document created for the driver. Can be either `Required` or `Submitted`, if no value is specified, `state` defaults to `Required`. `Required` documents are pre-populated documents for the Driver to fill out in the Driver App.  # noqa: E501

        :return: The state of this V1DocumentCreateBase.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this V1DocumentCreateBase.

        The condition of the document created for the driver. Can be either `Required` or `Submitted`, if no value is specified, `state` defaults to `Required`. `Required` documents are pre-populated documents for the Driver to fill out in the Driver App.  # noqa: E501

        :param state: The state of this V1DocumentCreateBase.  # noqa: E501
        :type: str
        """
        allowed_values = ["Required", "Submitted"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

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
        if issubclass(V1DocumentCreateBase, dict):
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
        if not isinstance(other, V1DocumentCreateBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
