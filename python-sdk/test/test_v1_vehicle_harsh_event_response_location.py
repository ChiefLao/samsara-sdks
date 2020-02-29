# coding: utf-8

"""
    Samsara API

    This is the Samsara API.  # noqa: E501

    The version of the OpenAPI document: 2019-12-12
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import samsara
from samsara.models.v1_vehicle_harsh_event_response_location import V1VehicleHarshEventResponseLocation  # noqa: E501
from samsara.rest import ApiException

class TestV1VehicleHarshEventResponseLocation(unittest.TestCase):
    """V1VehicleHarshEventResponseLocation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1VehicleHarshEventResponseLocation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.v1_vehicle_harsh_event_response_location.V1VehicleHarshEventResponseLocation()  # noqa: E501
        if include_optional :
            return V1VehicleHarshEventResponseLocation(
                address = '350 Rhode Island St, San Francisco, CA', 
                latitude = 33.07614328, 
                longitude = -96.14907287
            )
        else :
            return V1VehicleHarshEventResponseLocation(
        )

    def testV1VehicleHarshEventResponseLocation(self):
        """Test V1VehicleHarshEventResponseLocation"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
