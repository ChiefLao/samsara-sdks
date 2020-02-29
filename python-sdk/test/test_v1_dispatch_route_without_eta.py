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
from samsara.models.v1_dispatch_route_without_eta import V1DispatchRouteWithoutETA  # noqa: E501
from samsara.rest import ApiException

class TestV1DispatchRouteWithoutETA(unittest.TestCase):
    """V1DispatchRouteWithoutETA unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1DispatchRouteWithoutETA
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.v1_dispatch_route_without_eta.V1DispatchRouteWithoutETA()  # noqa: E501
        if include_optional :
            return V1DispatchRouteWithoutETA(
                dispatch_jobs = [
                    null
                    ], 
                id = 556, 
                actual_end_ms = 1462882101000, 
                actual_start_ms = 1462882098000, 
                driver_id = 555, 
                group_id = 101, 
                name = 'Bid #123', 
                notes = 'Please make sure to confirm crate count at each stop on this route.
Total number of crates for route: 23.', 
                odometer_end_meters = 2000000, 
                odometer_start_meters = 1000000, 
                scheduled_end_ms = 1462881998034, 
                scheduled_meters = 10000, 
                scheduled_start_ms = 1462881998034, 
                start_location_address = '123 Main St, Philadelphia, PA 19106', 
                start_location_address_id = 67890, 
                start_location_lat = 123.456, 
                start_location_lng = 37.459, 
                start_location_name = 'ACME Inc. Philadelphia HQ', 
                trailer_id = 666, 
                vehicle_id = 444
            )
        else :
            return V1DispatchRouteWithoutETA(
        )

    def testV1DispatchRouteWithoutETA(self):
        """Test V1DispatchRouteWithoutETA"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
