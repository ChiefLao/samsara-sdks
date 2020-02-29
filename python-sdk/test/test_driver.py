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
from samsara.models.driver import Driver  # noqa: E501
from samsara.rest import ApiException

class TestDriver(unittest.TestCase):
    """Driver unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Driver
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.driver.Driver()  # noqa: E501
        if include_optional :
            return Driver(
                carrier_settings = samsara.models.driver_carrier_settings.DriverCarrierSettings(
                    carrier_name = 'Acme Inc.', 
                    dot_number = 98231, 
                    main_office_address = '1234 Pear St., Scranton, PA 62814', ), 
                created_at_time = '2019-05-18T20:27:35Z', 
                eld_adverse_weather_exemption_enabled = True, 
                eld_big_day_exemption_enabled = True, 
                eld_day_start_hour = 56, 
                eld_exempt = True, 
                eld_exempt_reason = 'Bad driver', 
                eld_pc_enabled = True, 
                eld_ym_enabled = True, 
                external_ids = {maintenanceId=250020, payrollId=ABFS18600}, 
                id = '123', 
                is_deactivated = False, 
                license_number = 'E1234567', 
                license_state = 'CA', 
                locale = 'us', 
                name = 'Susan Jones', 
                notes = 'Also goes by the nickname Furious Fred.', 
                phone = '5558234327', 
                static_assigned_vehicle = null, 
                tachograph_card_number = '1000000492436002', 
                tags = [
                    samsara.models.tag_tiny_response.tagTinyResponse(
                        id = '3914', 
                        name = 'East Coast', 
                        parent_tag_id = '4815', )
                    ], 
                timezone = 'America/Los_Angeles', 
                updated_at_time = '2019-06-13T19:08:25Z', 
                username = 'SusanJones', 
                vehicle_group_tag = null
            )
        else :
            return Driver(
        )

    def testDriver(self):
        """Test Driver"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
