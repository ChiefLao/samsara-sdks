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
from samsara.models.v1_vision_run_by_camera_response_run_summary import V1VisionRunByCameraResponseRunSummary  # noqa: E501
from samsara.rest import ApiException

class TestV1VisionRunByCameraResponseRunSummary(unittest.TestCase):
    """V1VisionRunByCameraResponseRunSummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1VisionRunByCameraResponseRunSummary
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.v1_vision_run_by_camera_response_run_summary.V1VisionRunByCameraResponseRunSummary()  # noqa: E501
        if include_optional :
            return V1VisionRunByCameraResponseRunSummary(
                items_per_minute = 0.1, 
                no_read_count = 0, 
                reject_count = 0, 
                success_count = 181
            )
        else :
            return V1VisionRunByCameraResponseRunSummary(
        )

    def testV1VisionRunByCameraResponseRunSummary(self):
        """Test V1VisionRunByCameraResponseRunSummary"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
