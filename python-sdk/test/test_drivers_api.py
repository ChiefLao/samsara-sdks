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
from samsara.api.drivers_api import DriversApi  # noqa: E501
from samsara.rest import ApiException


class TestDriversApi(unittest.TestCase):
    """DriversApi unit test stubs"""

    def setUp(self):
        self.api = samsara.api.drivers_api.DriversApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_driver(self):
        """Test case for create_driver

        Create a driver  # noqa: E501
        """
        pass

    def test_get_driver_by_id(self):
        """Test case for get_driver_by_id

        Retrieve a driver  # noqa: E501
        """
        pass

    def test_get_drivers(self):
        """Test case for get_drivers

        List all drivers  # noqa: E501
        """
        pass

    def test_update_driver_by_id(self):
        """Test case for update_driver_by_id

        Update a driver  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()