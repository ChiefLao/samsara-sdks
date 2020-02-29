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
from samsara.models.v1_hos_logs_summary_response_pagination import V1HosLogsSummaryResponsePagination  # noqa: E501
from samsara.rest import ApiException

class TestV1HosLogsSummaryResponsePagination(unittest.TestCase):
    """V1HosLogsSummaryResponsePagination unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1HosLogsSummaryResponsePagination
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.v1_hos_logs_summary_response_pagination.V1HosLogsSummaryResponsePagination()  # noqa: E501
        if include_optional :
            return V1HosLogsSummaryResponsePagination(
                end_cursor = 'MTA1MDc5MB==', 
                has_next_page = True
            )
        else :
            return V1HosLogsSummaryResponsePagination(
                end_cursor = 'MTA1MDc5MB==',
                has_next_page = True,
        )

    def testV1HosLogsSummaryResponsePagination(self):
        """Test V1HosLogsSummaryResponsePagination"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
