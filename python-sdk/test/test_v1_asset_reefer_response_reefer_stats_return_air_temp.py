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
from samsara.models.v1_asset_reefer_response_reefer_stats_return_air_temp import V1AssetReeferResponseReeferStatsReturnAirTemp  # noqa: E501
from samsara.rest import ApiException

class TestV1AssetReeferResponseReeferStatsReturnAirTemp(unittest.TestCase):
    """V1AssetReeferResponseReeferStatsReturnAirTemp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1AssetReeferResponseReeferStatsReturnAirTemp
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.v1_asset_reefer_response_reefer_stats_return_air_temp.V1AssetReeferResponseReeferStatsReturnAirTemp()  # noqa: E501
        if include_optional :
            return V1AssetReeferResponseReeferStatsReturnAirTemp(
                changed_at_ms = 1453449599999, 
                temp_in_milli_c = 31110
            )
        else :
            return V1AssetReeferResponseReeferStatsReturnAirTemp(
        )

    def testV1AssetReeferResponseReeferStatsReturnAirTemp(self):
        """Test V1AssetReeferResponseReeferStatsReturnAirTemp"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
