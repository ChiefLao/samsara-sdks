# coding: utf-8

"""
    Samsara API

    Integrate your data with the Samsara API, customize the Samsara experience, and join a community of developers building with Samsara.  # noqa: E501

    The version of the OpenAPI document: 2019-12-12
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import samsara_test
from samsara_test.models.vehicle_location import VehicleLocation  # noqa: E501
from samsara_test.rest import ApiException

class TestVehicleLocation(unittest.TestCase):
    """VehicleLocation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test VehicleLocation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara_test.models.vehicle_location.VehicleLocation()  # noqa: E501
        if include_optional :
            return VehicleLocation(
                latitude = 122.142, 
                longitude = -93.343, 
                heading = 120.0, 
                reverse_geo = samsara_test.models.vehicle_location_reverse_geo.VehicleLocationReverseGeo(
                    formatted_location = '16 N Fair Oaks Ave, Pasadena, CA 91103', ), 
                speed = 48.3, 
                time = '2019-05-03T04:30:31.492Z'
            )
        else :
            return VehicleLocation(
                latitude = 122.142,
                longitude = -93.343,
                heading = 120.0,
                reverse_geo = samsara_test.models.vehicle_location_reverse_geo.VehicleLocationReverseGeo(
                    formatted_location = '16 N Fair Oaks Ave, Pasadena, CA 91103', ),
                speed = 48.3,
                time = '2019-05-03T04:30:31.492Z',
        )

    def testVehicleLocation(self):
        """Test VehicleLocation"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()