# coding: utf-8

"""
    Samsara API

    Integrate your data with the Samsara API, customize the Samsara experience, and join a community of developers building with Samsara.  # noqa: E501

    The version of the OpenAPI document: 2019-12-12
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from samsara.configuration import Configuration


class V1DispatchRouteWithoutETAAllOf(object):
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
        'dispatch_jobs': 'list[V1DispatchJobWithoutETA]',
        'id': 'int'
    }

    attribute_map = {
        'dispatch_jobs': 'dispatch_jobs',
        'id': 'id'
    }

    def __init__(self, dispatch_jobs=None, id=None, local_vars_configuration=None):  # noqa: E501
        """V1DispatchRouteWithoutETAAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._dispatch_jobs = None
        self._id = None
        self.discriminator = None

        if dispatch_jobs is not None:
            self.dispatch_jobs = dispatch_jobs
        if id is not None:
            self.id = id

    @property
    def dispatch_jobs(self):
        """Gets the dispatch_jobs of this V1DispatchRouteWithoutETAAllOf.  # noqa: E501

        The dispatch jobs associated with this route.  # noqa: E501

        :return: The dispatch_jobs of this V1DispatchRouteWithoutETAAllOf.  # noqa: E501
        :rtype: list[V1DispatchJobWithoutETA]
        """
        return self._dispatch_jobs

    @dispatch_jobs.setter
    def dispatch_jobs(self, dispatch_jobs):
        """Sets the dispatch_jobs of this V1DispatchRouteWithoutETAAllOf.

        The dispatch jobs associated with this route.  # noqa: E501

        :param dispatch_jobs: The dispatch_jobs of this V1DispatchRouteWithoutETAAllOf.  # noqa: E501
        :type: list[V1DispatchJobWithoutETA]
        """

        self._dispatch_jobs = dispatch_jobs

    @property
    def id(self):
        """Gets the id of this V1DispatchRouteWithoutETAAllOf.  # noqa: E501

        ID of the Samsara dispatch route.  # noqa: E501

        :return: The id of this V1DispatchRouteWithoutETAAllOf.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V1DispatchRouteWithoutETAAllOf.

        ID of the Samsara dispatch route.  # noqa: E501

        :param id: The id of this V1DispatchRouteWithoutETAAllOf.  # noqa: E501
        :type: int
        """

        self._id = id

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
        if not isinstance(other, V1DispatchRouteWithoutETAAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1DispatchRouteWithoutETAAllOf):
            return True

        return self.to_dict() != other.to_dict()