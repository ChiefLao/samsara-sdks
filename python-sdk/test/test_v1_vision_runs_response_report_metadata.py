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
from samsara.models.v1_vision_runs_response_report_metadata import V1VisionRunsResponseReportMetadata  # noqa: E501
from samsara.rest import ApiException

class TestV1VisionRunsResponseReportMetadata(unittest.TestCase):
    """V1VisionRunsResponseReportMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1VisionRunsResponseReportMetadata
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.v1_vision_runs_response_report_metadata.V1VisionRunsResponseReportMetadata()  # noqa: E501
        if include_optional :
            return V1VisionRunsResponseReportMetadata(
                items_per_minute = 0.1, 
                no_read_count = 181, 
                reject_count = 0, 
                success_count = 181
            )
        else :
            return V1VisionRunsResponseReportMetadata(
        )

    def testV1VisionRunsResponseReportMetadata(self):
        """Test V1VisionRunsResponseReportMetadata"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
