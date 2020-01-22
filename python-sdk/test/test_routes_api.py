# coding: utf-8

"""
    Samsara API

    Integrate your data with the Samsara API, customize the Samsara experience, and join a community of developers building with Samsara.  # noqa: E501

    The version of the OpenAPI document: 2019-12-12
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import samsara
from samsara.api.routes_api import RoutesApi  # noqa: E501
from samsara.rest import ApiException


class TestRoutesApi(unittest.TestCase):
    """RoutesApi unit test stubs"""

    def setUp(self):
        self.api = samsara.api.routes_api.RoutesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_v1create_dispatch_route(self):
        """Test case for v1create_dispatch_route

        Create a new route  # noqa: E501
        """
        pass

    def test_v1delete_dispatch_route_by_id(self):
        """Test case for v1delete_dispatch_route_by_id

        Delete a route  # noqa: E501
        """
        pass

    def test_v1fetch_all_dispatch_routes(self):
        """Test case for v1fetch_all_dispatch_routes

        Get all routes  # noqa: E501
        """
        pass

    def test_v1fetch_all_route_job_updates(self):
        """Test case for v1fetch_all_route_job_updates

        Get route updates  # noqa: E501
        """
        pass

    def test_v1get_dispatch_route_by_id(self):
        """Test case for v1get_dispatch_route_by_id

        Get a route  # noqa: E501
        """
        pass

    def test_v1get_dispatch_route_history(self):
        """Test case for v1get_dispatch_route_history

        Get route history  # noqa: E501
        """
        pass

    def test_v1update_dispatch_route_by_id(self):
        """Test case for v1update_dispatch_route_by_id

        Update a route  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
