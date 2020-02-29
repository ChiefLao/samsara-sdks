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
from samsara.models.v1_vehicle_harsh_event_response import V1VehicleHarshEventResponse  # noqa: E501
from samsara.rest import ApiException

class TestV1VehicleHarshEventResponse(unittest.TestCase):
    """V1VehicleHarshEventResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1VehicleHarshEventResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.v1_vehicle_harsh_event_response.V1VehicleHarshEventResponse()  # noqa: E501
        if include_optional :
            return V1VehicleHarshEventResponse(
                download_forward_video_url = 'https://samsara-dashcam-videos.s3.us-west-2.amazonaws.com/123/212123456789012/1539201872984/abC123De4-camera-video-segment-123456789.mp4?...', 
                download_inward_video_url = 'https://samsara-dashcam-videos.s3.us-west-2.amazonaws.com/123/212123456789012/1539201872984/abC123De4-camera-video-segment-driver-123456789.mp4?...', 
                download_tracked_inward_video_url = 'https://samsara-dashcam-videos.s3.us-west-2.amazonaws.com/123/212123456789012/1539201872984/abC123De4-camera-video-segment-driver-123456789.tracked.mp4?...', 
                harsh_event_type = 'Harsh Braking', 
                incident_report_url = 'https://cloud.samsara.com/groups/1234/fleet/reports/safety/vehicle/212123456789012/incident/1539201882984', 
                is_distracted = True, 
                location = samsara.models.v1_vehicle_harsh_event_response_location.V1VehicleHarshEventResponse_location(
                    address = '350 Rhode Island St, San Francisco, CA', 
                    latitude = 33.07614328, 
                    longitude = -96.14907287, )
            )
        else :
            return V1VehicleHarshEventResponse(
                harsh_event_type = 'Harsh Braking',
                incident_report_url = 'https://cloud.samsara.com/groups/1234/fleet/reports/safety/vehicle/212123456789012/incident/1539201882984',
        )

    def testV1VehicleHarshEventResponse(self):
        """Test V1VehicleHarshEventResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
