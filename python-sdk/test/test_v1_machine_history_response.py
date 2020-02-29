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
from samsara.models.v1_machine_history_response import V1MachineHistoryResponse  # noqa: E501
from samsara.rest import ApiException

class TestV1MachineHistoryResponse(unittest.TestCase):
    """V1MachineHistoryResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1MachineHistoryResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.v1_machine_history_response.V1MachineHistoryResponse()  # noqa: E501
        if include_optional :
            return V1MachineHistoryResponse(
                machines = [
                    samsara.models.v1_machine_history_response_machines.V1MachineHistoryResponse_machines(
                        id = 1, 
                        name = '1/3 HP Motor', 
                        vibrations = [
                            samsara.models.v1_machine_history_response_vibrations.V1MachineHistoryResponse_vibrations(
                                x = 0.01, 
                                y = 1.23, 
                                z = 2.55, 
                                time = 1453449599999, )
                            ], )
                    ]
            )
        else :
            return V1MachineHistoryResponse(
        )

    def testV1MachineHistoryResponse(self):
        """Test V1MachineHistoryResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
