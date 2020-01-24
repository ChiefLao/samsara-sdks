# coding: utf-8

"""
    Samsara API

    Integrate your data with the Samsara API, customize the Samsara experience, and join a community of developers building with Samsara.  # noqa: E501

    The version of the OpenAPI document: 2019-12-12
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import samsara
from samsara.api.sensors_api import SensorsApi  # noqa: E501
from samsara.rest import ApiException


class TestSensorsApi(unittest.TestCase):
    """SensorsApi unit test stubs"""

    def setUp(self):
        self.api = samsara.api.sensors_api.SensorsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_v1get_sensors(self):
        """Test case for v1get_sensors

        Get all sensors  # noqa: E501
        """
        pass

    def test_v1get_sensors_cargo(self):
        """Test case for v1get_sensors_cargo

        Get cargo status  # noqa: E501
        """
        pass

    def test_v1get_sensors_door(self):
        """Test case for v1get_sensors_door

        Get door status  # noqa: E501
        """
        pass

    def test_v1get_sensors_history(self):
        """Test case for v1get_sensors_history

        Get sensor history  # noqa: E501
        """
        pass

    def test_v1get_sensors_humidity(self):
        """Test case for v1get_sensors_humidity

        Get humidity  # noqa: E501
        """
        pass

    def test_v1get_sensors_temperature(self):
        """Test case for v1get_sensors_temperature

        Get temperature  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()