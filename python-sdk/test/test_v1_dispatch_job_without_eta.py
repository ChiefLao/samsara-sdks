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
from samsara.models.v1_dispatch_job_without_eta import V1DispatchJobWithoutETA  # noqa: E501
from samsara.rest import ApiException

class TestV1DispatchJobWithoutETA(unittest.TestCase):
    """V1DispatchJobWithoutETA unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1DispatchJobWithoutETA
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.v1_dispatch_job_without_eta.V1DispatchJobWithoutETA()  # noqa: E501
        if include_optional :
            return V1DispatchJobWithoutETA(
                arrived_at_ms = 1462881998034, 
                completed_at_ms = 1462881998034, 
                dispatch_route_id = 55, 
                documents = [
                    samsara.models.v1_dispatch_job_document_info.V1DispatchJobDocumentInfo(
                        driver_id = 1234, 
                        id = '2018_42424242', )
                    ], 
                driver_id = 444, 
                en_route_at_ms = 1462881998034, 
                fleet_viewer_url = 'https://cloud.samsara.com/fleet/viewer/job/fleet_viewer_token', 
                group_id = 101, 
                id = 773, 
                job_state = 'JobState_Arrived', 
                skipped_at_ms = 1462881998034, 
                vehicle_id = 112, 
                destination_address = '123 Main St, Philadelphia, PA 19106', 
                destination_address_id = 67890, 
                destination_lat = 123.456, 
                destination_lng = 37.459, 
                destination_name = 'ACME Inc. Philadelphia HQ', 
                notes = 'Ensure crates are stacked no more than 3 high.', 
                scheduled_arrival_time_ms = 1462881998034, 
                scheduled_departure_time_ms = 1462881998034
            )
        else :
            return V1DispatchJobWithoutETA(
                dispatch_route_id = 55,
                id = 773,
                job_state = 'JobState_Arrived',
                scheduled_arrival_time_ms = 1462881998034,
        )

    def testV1DispatchJobWithoutETA(self):
        """Test V1DispatchJobWithoutETA"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
