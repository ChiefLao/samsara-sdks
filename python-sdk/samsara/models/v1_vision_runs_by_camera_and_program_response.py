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


class V1VisionRunsByCameraAndProgramResponse(object):
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
        'device_id': 'int',
        'ended_at_ms': 'int',
        'program_id': 'int',
        'report_metadata': 'V1VisionRunByCameraResponseRunSummary',
        'results': 'list[V1VisionRunByCameraResponseInspectionResults]',
        'started_at_ms': 'int'
    }

    attribute_map = {
        'device_id': 'deviceId',
        'ended_at_ms': 'endedAtMs',
        'program_id': 'programId',
        'report_metadata': 'reportMetadata',
        'results': 'results',
        'started_at_ms': 'startedAtMs'
    }

    def __init__(self, device_id=None, ended_at_ms=None, program_id=None, report_metadata=None, results=None, started_at_ms=None, local_vars_configuration=None):  # noqa: E501
        """V1VisionRunsByCameraAndProgramResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._device_id = None
        self._ended_at_ms = None
        self._program_id = None
        self._report_metadata = None
        self._results = None
        self._started_at_ms = None
        self.discriminator = None

        if device_id is not None:
            self.device_id = device_id
        if ended_at_ms is not None:
            self.ended_at_ms = ended_at_ms
        if program_id is not None:
            self.program_id = program_id
        if report_metadata is not None:
            self.report_metadata = report_metadata
        if results is not None:
            self.results = results
        if started_at_ms is not None:
            self.started_at_ms = started_at_ms

    @property
    def device_id(self):
        """Gets the device_id of this V1VisionRunsByCameraAndProgramResponse.  # noqa: E501


        :return: The device_id of this V1VisionRunsByCameraAndProgramResponse.  # noqa: E501
        :rtype: int
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this V1VisionRunsByCameraAndProgramResponse.


        :param device_id: The device_id of this V1VisionRunsByCameraAndProgramResponse.  # noqa: E501
        :type: int
        """

        self._device_id = device_id

    @property
    def ended_at_ms(self):
        """Gets the ended_at_ms of this V1VisionRunsByCameraAndProgramResponse.  # noqa: E501


        :return: The ended_at_ms of this V1VisionRunsByCameraAndProgramResponse.  # noqa: E501
        :rtype: int
        """
        return self._ended_at_ms

    @ended_at_ms.setter
    def ended_at_ms(self, ended_at_ms):
        """Sets the ended_at_ms of this V1VisionRunsByCameraAndProgramResponse.


        :param ended_at_ms: The ended_at_ms of this V1VisionRunsByCameraAndProgramResponse.  # noqa: E501
        :type: int
        """

        self._ended_at_ms = ended_at_ms

    @property
    def program_id(self):
        """Gets the program_id of this V1VisionRunsByCameraAndProgramResponse.  # noqa: E501


        :return: The program_id of this V1VisionRunsByCameraAndProgramResponse.  # noqa: E501
        :rtype: int
        """
        return self._program_id

    @program_id.setter
    def program_id(self, program_id):
        """Sets the program_id of this V1VisionRunsByCameraAndProgramResponse.


        :param program_id: The program_id of this V1VisionRunsByCameraAndProgramResponse.  # noqa: E501
        :type: int
        """

        self._program_id = program_id

    @property
    def report_metadata(self):
        """Gets the report_metadata of this V1VisionRunsByCameraAndProgramResponse.  # noqa: E501


        :return: The report_metadata of this V1VisionRunsByCameraAndProgramResponse.  # noqa: E501
        :rtype: V1VisionRunByCameraResponseRunSummary
        """
        return self._report_metadata

    @report_metadata.setter
    def report_metadata(self, report_metadata):
        """Sets the report_metadata of this V1VisionRunsByCameraAndProgramResponse.


        :param report_metadata: The report_metadata of this V1VisionRunsByCameraAndProgramResponse.  # noqa: E501
        :type: V1VisionRunByCameraResponseRunSummary
        """

        self._report_metadata = report_metadata

    @property
    def results(self):
        """Gets the results of this V1VisionRunsByCameraAndProgramResponse.  # noqa: E501


        :return: The results of this V1VisionRunsByCameraAndProgramResponse.  # noqa: E501
        :rtype: list[V1VisionRunByCameraResponseInspectionResults]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this V1VisionRunsByCameraAndProgramResponse.


        :param results: The results of this V1VisionRunsByCameraAndProgramResponse.  # noqa: E501
        :type: list[V1VisionRunByCameraResponseInspectionResults]
        """

        self._results = results

    @property
    def started_at_ms(self):
        """Gets the started_at_ms of this V1VisionRunsByCameraAndProgramResponse.  # noqa: E501


        :return: The started_at_ms of this V1VisionRunsByCameraAndProgramResponse.  # noqa: E501
        :rtype: int
        """
        return self._started_at_ms

    @started_at_ms.setter
    def started_at_ms(self, started_at_ms):
        """Sets the started_at_ms of this V1VisionRunsByCameraAndProgramResponse.


        :param started_at_ms: The started_at_ms of this V1VisionRunsByCameraAndProgramResponse.  # noqa: E501
        :type: int
        """

        self._started_at_ms = started_at_ms

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
        if not isinstance(other, V1VisionRunsByCameraAndProgramResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1VisionRunsByCameraAndProgramResponse):
            return True

        return self.to_dict() != other.to_dict()