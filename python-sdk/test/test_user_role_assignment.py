# coding: utf-8

"""
    Samsara API

    Integrate your data with the Samsara API, customize the Samsara experience, and join a community of developers building with Samsara.  # noqa: E501

    The version of the OpenAPI document: 2019-12-12
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import samsara
from samsara.models.user_role_assignment import UserRoleAssignment  # noqa: E501
from samsara.rest import ApiException

class TestUserRoleAssignment(unittest.TestCase):
    """UserRoleAssignment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UserRoleAssignment
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.user_role_assignment.UserRoleAssignment()  # noqa: E501
        if include_optional :
            return UserRoleAssignment(
                role = samsara.models.user_role.UserRole(
                    id = '8a9371af-82d1-4158-bf91-4ecc8d3a114c', 
                    name = 'Full Admin', ), 
                tag = samsara.models.user_role_assignment_tag.UserRoleAssignment_tag(
                    id = '3914', 
                    name = 'East Coast', )
            )
        else :
            return UserRoleAssignment(
        )

    def testUserRoleAssignment(self):
        """Test UserRoleAssignment"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()