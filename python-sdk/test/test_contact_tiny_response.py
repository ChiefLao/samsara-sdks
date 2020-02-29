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
from samsara.models.contact_tiny_response import ContactTinyResponse  # noqa: E501
from samsara.rest import ApiException

class TestContactTinyResponse(unittest.TestCase):
    """ContactTinyResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ContactTinyResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.contact_tiny_response.ContactTinyResponse()  # noqa: E501
        if include_optional :
            return ContactTinyResponse(
                first_name = 'Jane', 
                id = '22408', 
                last_name = 'Jones'
            )
        else :
            return ContactTinyResponse(
        )

    def testContactTinyResponse(self):
        """Test ContactTinyResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
