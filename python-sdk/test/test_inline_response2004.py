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
from samsara.models.inline_response2004 import InlineResponse2004  # noqa: E501
from samsara.rest import ApiException

class TestInlineResponse2004(unittest.TestCase):
    """InlineResponse2004 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse2004
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.inline_response2004.InlineResponse2004()  # noqa: E501
        if include_optional :
            return InlineResponse2004(
                data = [
                    samsara.models.v1_message_response.V1MessageResponse(
                        driver_id = 555, 
                        is_read = True, 
                        sender = samsara.models.v1_message_sender.V1MessageSender(
                            name = 'John Doe', 
                            type = 'dispatch', ), 
                        sent_at_ms = 1462881998034, 
                        text = 'This is a message.', )
                    ]
            )
        else :
            return InlineResponse2004(
        )

    def testInlineResponse2004(self):
        """Test InlineResponse2004"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
