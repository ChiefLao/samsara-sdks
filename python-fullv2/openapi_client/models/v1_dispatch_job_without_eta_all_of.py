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


class V1DispatchJobWithoutETAAllOf(object):
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
        'arrived_at_ms': 'int',
        'completed_at_ms': 'int',
        'dispatch_route_id': 'int',
        'documents': 'list[V1DispatchJobDocumentInfo]',
        'driver_id': 'int',
        'en_route_at_ms': 'int',
        'fleet_viewer_url': 'str',
        'group_id': 'int',
        'id': 'int',
        'job_state': 'V1jobStatus',
        'skipped_at_ms': 'int',
        'vehicle_id': 'int'
    }

    attribute_map = {
        'arrived_at_ms': 'arrived_at_ms',
        'completed_at_ms': 'completed_at_ms',
        'dispatch_route_id': 'dispatch_route_id',
        'documents': 'documents',
        'driver_id': 'driver_id',
        'en_route_at_ms': 'en_route_at_ms',
        'fleet_viewer_url': 'fleet_viewer_url',
        'group_id': 'group_id',
        'id': 'id',
        'job_state': 'job_state',
        'skipped_at_ms': 'skipped_at_ms',
        'vehicle_id': 'vehicle_id'
    }

    def __init__(self, arrived_at_ms=None, completed_at_ms=None, dispatch_route_id=None, documents=None, driver_id=None, en_route_at_ms=None, fleet_viewer_url=None, group_id=None, id=None, job_state=None, skipped_at_ms=None, vehicle_id=None, local_vars_configuration=None):  # noqa: E501
        """V1DispatchJobWithoutETAAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._arrived_at_ms = None
        self._completed_at_ms = None
        self._dispatch_route_id = None
        self._documents = None
        self._driver_id = None
        self._en_route_at_ms = None
        self._fleet_viewer_url = None
        self._group_id = None
        self._id = None
        self._job_state = None
        self._skipped_at_ms = None
        self._vehicle_id = None
        self.discriminator = None

        if arrived_at_ms is not None:
            self.arrived_at_ms = arrived_at_ms
        if completed_at_ms is not None:
            self.completed_at_ms = completed_at_ms
        self.dispatch_route_id = dispatch_route_id
        if documents is not None:
            self.documents = documents
        if driver_id is not None:
            self.driver_id = driver_id
        if en_route_at_ms is not None:
            self.en_route_at_ms = en_route_at_ms
        if fleet_viewer_url is not None:
            self.fleet_viewer_url = fleet_viewer_url
        if group_id is not None:
            self.group_id = group_id
        self.id = id
        self.job_state = job_state
        if skipped_at_ms is not None:
            self.skipped_at_ms = skipped_at_ms
        if vehicle_id is not None:
            self.vehicle_id = vehicle_id

    @property
    def arrived_at_ms(self):
        """Gets the arrived_at_ms of this V1DispatchJobWithoutETAAllOf.  # noqa: E501

        The time at which the driver arrived at the job destination.  # noqa: E501

        :return: The arrived_at_ms of this V1DispatchJobWithoutETAAllOf.  # noqa: E501
        :rtype: int
        """
        return self._arrived_at_ms

    @arrived_at_ms.setter
    def arrived_at_ms(self, arrived_at_ms):
        """Sets the arrived_at_ms of this V1DispatchJobWithoutETAAllOf.

        The time at which the driver arrived at the job destination.  # noqa: E501

        :param arrived_at_ms: The arrived_at_ms of this V1DispatchJobWithoutETAAllOf.  # noqa: E501
        :type: int
        """

        self._arrived_at_ms = arrived_at_ms

    @property
    def completed_at_ms(self):
        """Gets the completed_at_ms of this V1DispatchJobWithoutETAAllOf.  # noqa: E501

        The time at which the job was marked complete (e.g. started driving to the next destination).  # noqa: E501

        :return: The completed_at_ms of this V1DispatchJobWithoutETAAllOf.  # noqa: E501
        :rtype: int
        """
        return self._completed_at_ms

    @completed_at_ms.setter
    def completed_at_ms(self, completed_at_ms):
        """Sets the completed_at_ms of this V1DispatchJobWithoutETAAllOf.

        The time at which the job was marked complete (e.g. started driving to the next destination).  # noqa: E501

        :param completed_at_ms: The completed_at_ms of this V1DispatchJobWithoutETAAllOf.  # noqa: E501
        :type: int
        """

        self._completed_at_ms = completed_at_ms

    @property
    def dispatch_route_id(self):
        """Gets the dispatch_route_id of this V1DispatchJobWithoutETAAllOf.  # noqa: E501

        ID of the route that this job belongs to.  # noqa: E501

        :return: The dispatch_route_id of this V1DispatchJobWithoutETAAllOf.  # noqa: E501
        :rtype: int
        """
        return self._dispatch_route_id

    @dispatch_route_id.setter
    def dispatch_route_id(self, dispatch_route_id):
        """Sets the dispatch_route_id of this V1DispatchJobWithoutETAAllOf.

        ID of the route that this job belongs to.  # noqa: E501

        :param dispatch_route_id: The dispatch_route_id of this V1DispatchJobWithoutETAAllOf.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and dispatch_route_id is None:  # noqa: E501
            raise ValueError("Invalid value for `dispatch_route_id`, must not be `None`")  # noqa: E501

        self._dispatch_route_id = dispatch_route_id

    @property
    def documents(self):
        """Gets the documents of this V1DispatchJobWithoutETAAllOf.  # noqa: E501

        Document submissions associated with this job.  # noqa: E501

        :return: The documents of this V1DispatchJobWithoutETAAllOf.  # noqa: E501
        :rtype: list[V1DispatchJobDocumentInfo]
        """
        return self._documents

    @documents.setter
    def documents(self, documents):
        """Sets the documents of this V1DispatchJobWithoutETAAllOf.

        Document submissions associated with this job.  # noqa: E501

        :param documents: The documents of this V1DispatchJobWithoutETAAllOf.  # noqa: E501
        :type: list[V1DispatchJobDocumentInfo]
        """

        self._documents = documents

    @property
    def driver_id(self):
        """Gets the driver_id of this V1DispatchJobWithoutETAAllOf.  # noqa: E501

        ID of the driver assigned to the dispatch job.  # noqa: E501

        :return: The driver_id of this V1DispatchJobWithoutETAAllOf.  # noqa: E501
        :rtype: int
        """
        return self._driver_id

    @driver_id.setter
    def driver_id(self, driver_id):
        """Sets the driver_id of this V1DispatchJobWithoutETAAllOf.

        ID of the driver assigned to the dispatch job.  # noqa: E501

        :param driver_id: The driver_id of this V1DispatchJobWithoutETAAllOf.  # noqa: E501
        :type: int
        """

        self._driver_id = driver_id

    @property
    def en_route_at_ms(self):
        """Gets the en_route_at_ms of this V1DispatchJobWithoutETAAllOf.  # noqa: E501

        The time at which the assigned driver started fulfilling the job (e.g. started driving to the destination).  # noqa: E501

        :return: The en_route_at_ms of this V1DispatchJobWithoutETAAllOf.  # noqa: E501
        :rtype: int
        """
        return self._en_route_at_ms

    @en_route_at_ms.setter
    def en_route_at_ms(self, en_route_at_ms):
        """Sets the en_route_at_ms of this V1DispatchJobWithoutETAAllOf.

        The time at which the assigned driver started fulfilling the job (e.g. started driving to the destination).  # noqa: E501

        :param en_route_at_ms: The en_route_at_ms of this V1DispatchJobWithoutETAAllOf.  # noqa: E501
        :type: int
        """

        self._en_route_at_ms = en_route_at_ms

    @property
    def fleet_viewer_url(self):
        """Gets the fleet_viewer_url of this V1DispatchJobWithoutETAAllOf.  # noqa: E501

        Fleet viewer url of the dispatch job.  # noqa: E501

        :return: The fleet_viewer_url of this V1DispatchJobWithoutETAAllOf.  # noqa: E501
        :rtype: str
        """
        return self._fleet_viewer_url

    @fleet_viewer_url.setter
    def fleet_viewer_url(self, fleet_viewer_url):
        """Sets the fleet_viewer_url of this V1DispatchJobWithoutETAAllOf.

        Fleet viewer url of the dispatch job.  # noqa: E501

        :param fleet_viewer_url: The fleet_viewer_url of this V1DispatchJobWithoutETAAllOf.  # noqa: E501
        :type: str
        """

        self._fleet_viewer_url = fleet_viewer_url

    @property
    def group_id(self):
        """Gets the group_id of this V1DispatchJobWithoutETAAllOf.  # noqa: E501

        Deprecated.  # noqa: E501

        :return: The group_id of this V1DispatchJobWithoutETAAllOf.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this V1DispatchJobWithoutETAAllOf.

        Deprecated.  # noqa: E501

        :param group_id: The group_id of this V1DispatchJobWithoutETAAllOf.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def id(self):
        """Gets the id of this V1DispatchJobWithoutETAAllOf.  # noqa: E501

        ID of the Samsara dispatch job.  # noqa: E501

        :return: The id of this V1DispatchJobWithoutETAAllOf.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V1DispatchJobWithoutETAAllOf.

        ID of the Samsara dispatch job.  # noqa: E501

        :param id: The id of this V1DispatchJobWithoutETAAllOf.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def job_state(self):
        """Gets the job_state of this V1DispatchJobWithoutETAAllOf.  # noqa: E501


        :return: The job_state of this V1DispatchJobWithoutETAAllOf.  # noqa: E501
        :rtype: V1jobStatus
        """
        return self._job_state

    @job_state.setter
    def job_state(self, job_state):
        """Sets the job_state of this V1DispatchJobWithoutETAAllOf.


        :param job_state: The job_state of this V1DispatchJobWithoutETAAllOf.  # noqa: E501
        :type: V1jobStatus
        """
        if self.local_vars_configuration.client_side_validation and job_state is None:  # noqa: E501
            raise ValueError("Invalid value for `job_state`, must not be `None`")  # noqa: E501

        self._job_state = job_state

    @property
    def skipped_at_ms(self):
        """Gets the skipped_at_ms of this V1DispatchJobWithoutETAAllOf.  # noqa: E501

        The time at which the job was marked skipped.  # noqa: E501

        :return: The skipped_at_ms of this V1DispatchJobWithoutETAAllOf.  # noqa: E501
        :rtype: int
        """
        return self._skipped_at_ms

    @skipped_at_ms.setter
    def skipped_at_ms(self, skipped_at_ms):
        """Sets the skipped_at_ms of this V1DispatchJobWithoutETAAllOf.

        The time at which the job was marked skipped.  # noqa: E501

        :param skipped_at_ms: The skipped_at_ms of this V1DispatchJobWithoutETAAllOf.  # noqa: E501
        :type: int
        """

        self._skipped_at_ms = skipped_at_ms

    @property
    def vehicle_id(self):
        """Gets the vehicle_id of this V1DispatchJobWithoutETAAllOf.  # noqa: E501

        ID of the vehicle used for the dispatch job.  # noqa: E501

        :return: The vehicle_id of this V1DispatchJobWithoutETAAllOf.  # noqa: E501
        :rtype: int
        """
        return self._vehicle_id

    @vehicle_id.setter
    def vehicle_id(self, vehicle_id):
        """Sets the vehicle_id of this V1DispatchJobWithoutETAAllOf.

        ID of the vehicle used for the dispatch job.  # noqa: E501

        :param vehicle_id: The vehicle_id of this V1DispatchJobWithoutETAAllOf.  # noqa: E501
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
        if not isinstance(other, V1DispatchJobWithoutETAAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1DispatchJobWithoutETAAllOf):
            return True

        return self.to_dict() != other.to_dict()
