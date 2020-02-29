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
from samsara.models.v1_vehicle_maintenance_j1939_check_engine_light import V1VehicleMaintenanceJ1939CheckEngineLight  # noqa: E501
from samsara.rest import ApiException

class TestV1VehicleMaintenanceJ1939CheckEngineLight(unittest.TestCase):
    """V1VehicleMaintenanceJ1939CheckEngineLight unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1VehicleMaintenanceJ1939CheckEngineLight
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.v1_vehicle_maintenance_j1939_check_engine_light.V1VehicleMaintenanceJ1939CheckEngineLight()  # noqa: E501
        if include_optional :
            return V1VehicleMaintenanceJ1939CheckEngineLight(
                emissions_is_on = True, 
                protect_is_on = True, 
                stop_is_on = True, 
                warning_is_on = True
            )
        else :
            return V1VehicleMaintenanceJ1939CheckEngineLight(
        )

    def testV1VehicleMaintenanceJ1939CheckEngineLight(self):
        """Test V1VehicleMaintenanceJ1939CheckEngineLight"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
