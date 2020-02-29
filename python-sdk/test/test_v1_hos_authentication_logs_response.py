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
from samsara.models.v1_hos_authentication_logs_response import V1HosAuthenticationLogsResponse  # noqa: E501
from samsara.rest import ApiException

class TestV1HosAuthenticationLogsResponse(unittest.TestCase):
    """V1HosAuthenticationLogsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1HosAuthenticationLogsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.v1_hos_authentication_logs_response.V1HosAuthenticationLogsResponse()  # noqa: E501
        if include_optional :
            return V1HosAuthenticationLogsResponse(
                authentication_logs = [
                    samsara.models.v1_hos_authentication_logs_response_authentication_logs.V1HosAuthenticationLogsResponse_authenticationLogs(
                        action_type = 'signin', 
                        address = 'THIS FIELD IS NOT USED', 
                        address_name = 'THIS FIELD IS NOT USED', 
                        city = 'THIS FIELD IS NOT USED', 
                        happened_at_ms = 1462881998034, 
                        state = 'THIS FIELD IS NOT USED', )
                    ]
            )
        else :
            return V1HosAuthenticationLogsResponse(
        )

    def testV1HosAuthenticationLogsResponse(self):
        """Test V1HosAuthenticationLogsResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
