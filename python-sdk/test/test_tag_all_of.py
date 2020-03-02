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
from samsara.models.tag_all_of import TagAllOf  # noqa: E501
from samsara.rest import ApiException

class TestTagAllOf(unittest.TestCase):
    """TagAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TagAllOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.tag_all_of.TagAllOf()  # noqa: E501
        if include_optional :
            return TagAllOf(
                addresses = [
                    samsara.models.tagged_object.TaggedObject(
                        id = '23502866574', 
                        name = 'Driver Don', )
                    ], 
                assets = [
                    samsara.models.tagged_object.TaggedObject(
                        id = '23502866574', 
                        name = 'Driver Don', )
                    ], 
                drivers = [
                    samsara.models.tagged_object.TaggedObject(
                        id = '23502866574', 
                        name = 'Driver Don', )
                    ], 
                machines = [
                    samsara.models.tagged_object.TaggedObject(
                        id = '23502866574', 
                        name = 'Driver Don', )
                    ], 
                parent_tag = samsara.models.parent_tag.ParentTag(
                    id = '23502866574', 
                    name = 'US West Vehicles', ), 
                sensors = [
                    samsara.models.tagged_object.TaggedObject(
                        id = '23502866574', 
                        name = 'Driver Don', )
                    ], 
                vehicles = [
                    samsara.models.tagged_object.TaggedObject(
                        id = '23502866574', 
                        name = 'Driver Don', )
                    ]
            )
        else :
            return TagAllOf(
        )

    def testTagAllOf(self):
        """Test TagAllOf"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
