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
from samsara.models.inline_response2005 import InlineResponse2005  # noqa: E501
from samsara.rest import ApiException

class TestInlineResponse2005(unittest.TestCase):
    """InlineResponse2005 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse2005
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.inline_response2005.InlineResponse2005()  # noqa: E501
        if include_optional :
            return InlineResponse2005(
                data = [
                    samsara.models.v1_message.V1Message(
                        driver_id = 555, 
                        text = 'This is a message.', )
                    ]
            )
        else :
            return InlineResponse2005(
        )

    def testInlineResponse2005(self):
        """Test InlineResponse2005"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
