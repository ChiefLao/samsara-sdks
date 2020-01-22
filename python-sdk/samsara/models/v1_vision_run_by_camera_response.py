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


class V1VisionRunByCameraResponse(object):
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
        'camera_id': 'int',
        'ended_at_ms': 'int',
        'inspection_results': 'list[V1VisionRunByCameraResponseInspectionResults]',
        'is_ongoing': 'bool',
        'program': 'V1VisionRunByCameraResponseProgram',
        'run_summary': 'V1VisionRunByCameraResponseRunSummary',
        'started_at_ms': 'int'
    }

    attribute_map = {
        'camera_id': 'cameraId',
        'ended_at_ms': 'endedAtMs',
        'inspection_results': 'inspectionResults',
        'is_ongoing': 'isOngoing',
        'program': 'program',
        'run_summary': 'runSummary',
        'started_at_ms': 'startedAtMs'
    }

    def __init__(self, camera_id=None, ended_at_ms=None, inspection_results=None, is_ongoing=None, program=None, run_summary=None, started_at_ms=None, local_vars_configuration=None):  # noqa: E501
        """V1VisionRunByCameraResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._camera_id = None
        self._ended_at_ms = None
        self._inspection_results = None
        self._is_ongoing = None
        self._program = None
        self._run_summary = None
        self._started_at_ms = None
        self.discriminator = None

        if camera_id is not None:
            self.camera_id = camera_id
        if ended_at_ms is not None:
            self.ended_at_ms = ended_at_ms
        if inspection_results is not None:
            self.inspection_results = inspection_results
        if is_ongoing is not None:
            self.is_ongoing = is_ongoing
        if program is not None:
            self.program = program
        if run_summary is not None:
            self.run_summary = run_summary
        if started_at_ms is not None:
            self.started_at_ms = started_at_ms

    @property
    def camera_id(self):
        """Gets the camera_id of this V1VisionRunByCameraResponse.  # noqa: E501


        :return: The camera_id of this V1VisionRunByCameraResponse.  # noqa: E501
        :rtype: int
        """
        return self._camera_id

    @camera_id.setter
    def camera_id(self, camera_id):
        """Sets the camera_id of this V1VisionRunByCameraResponse.


        :param camera_id: The camera_id of this V1VisionRunByCameraResponse.  # noqa: E501
        :type: int
        """

        self._camera_id = camera_id

    @property
    def ended_at_ms(self):
        """Gets the ended_at_ms of this V1VisionRunByCameraResponse.  # noqa: E501


        :return: The ended_at_ms of this V1VisionRunByCameraResponse.  # noqa: E501
        :rtype: int
        """
        return self._ended_at_ms

    @ended_at_ms.setter
    def ended_at_ms(self, ended_at_ms):
        """Sets the ended_at_ms of this V1VisionRunByCameraResponse.


        :param ended_at_ms: The ended_at_ms of this V1VisionRunByCameraResponse.  # noqa: E501
        :type: int
        """

        self._ended_at_ms = ended_at_ms

    @property
    def inspection_results(self):
        """Gets the inspection_results of this V1VisionRunByCameraResponse.  # noqa: E501


        :return: The inspection_results of this V1VisionRunByCameraResponse.  # noqa: E501
        :rtype: list[V1VisionRunByCameraResponseInspectionResults]
        """
        return self._inspection_results

    @inspection_results.setter
    def inspection_results(self, inspection_results):
        """Sets the inspection_results of this V1VisionRunByCameraResponse.


        :param inspection_results: The inspection_results of this V1VisionRunByCameraResponse.  # noqa: E501
        :type: list[V1VisionRunByCameraResponseInspectionResults]
        """

        self._inspection_results = inspection_results

    @property
    def is_ongoing(self):
        """Gets the is_ongoing of this V1VisionRunByCameraResponse.  # noqa: E501


        :return: The is_ongoing of this V1VisionRunByCameraResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_ongoing

    @is_ongoing.setter
    def is_ongoing(self, is_ongoing):
        """Sets the is_ongoing of this V1VisionRunByCameraResponse.


        :param is_ongoing: The is_ongoing of this V1VisionRunByCameraResponse.  # noqa: E501
        :type: bool
        """

        self._is_ongoing = is_ongoing

    @property
    def program(self):
        """Gets the program of this V1VisionRunByCameraResponse.  # noqa: E501


        :return: The program of this V1VisionRunByCameraResponse.  # noqa: E501
        :rtype: V1VisionRunByCameraResponseProgram
        """
        return self._program

    @program.setter
    def program(self, program):
        """Sets the program of this V1VisionRunByCameraResponse.


        :param program: The program of this V1VisionRunByCameraResponse.  # noqa: E501
        :type: V1VisionRunByCameraResponseProgram
        """

        self._program = program

    @property
    def run_summary(self):
        """Gets the run_summary of this V1VisionRunByCameraResponse.  # noqa: E501


        :return: The run_summary of this V1VisionRunByCameraResponse.  # noqa: E501
        :rtype: V1VisionRunByCameraResponseRunSummary
        """
        return self._run_summary

    @run_summary.setter
    def run_summary(self, run_summary):
        """Sets the run_summary of this V1VisionRunByCameraResponse.


        :param run_summary: The run_summary of this V1VisionRunByCameraResponse.  # noqa: E501
        :type: V1VisionRunByCameraResponseRunSummary
        """

        self._run_summary = run_summary

    @property
    def started_at_ms(self):
        """Gets the started_at_ms of this V1VisionRunByCameraResponse.  # noqa: E501


        :return: The started_at_ms of this V1VisionRunByCameraResponse.  # noqa: E501
        :rtype: int
        """
        return self._started_at_ms

    @started_at_ms.setter
    def started_at_ms(self, started_at_ms):
        """Sets the started_at_ms of this V1VisionRunByCameraResponse.


        :param started_at_ms: The started_at_ms of this V1VisionRunByCameraResponse.  # noqa: E501
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
        if not isinstance(other, V1VisionRunByCameraResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1VisionRunByCameraResponse):
            return True

        return self.to_dict() != other.to_dict()
