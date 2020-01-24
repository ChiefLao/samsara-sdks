# coding: utf-8

"""
    Samsara API

    Integrate your data with the Samsara API, customize the Samsara experience, and join a community of developers building with Samsara.  # noqa: E501

    The version of the OpenAPI document: 2019-12-12
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from samsara.api_client import ApiClient
from samsara.exceptions import (
    ApiTypeError,
    ApiValueError
)


class MaintenanceApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v1create_dvir(self, create_dvir_param, **kwargs):  # noqa: E501
        """Create a DVIR  # noqa: E501

        <n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Create a new dvir, marking a vehicle or trailer safe or unsafe.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1create_dvir(create_dvir_param, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param InlineObject2 create_dvir_param: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: V1DvirBase
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.v1create_dvir_with_http_info(create_dvir_param, **kwargs)  # noqa: E501

    def v1create_dvir_with_http_info(self, create_dvir_param, **kwargs):  # noqa: E501
        """Create a DVIR  # noqa: E501

        <n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Create a new dvir, marking a vehicle or trailer safe or unsafe.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1create_dvir_with_http_info(create_dvir_param, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param InlineObject2 create_dvir_param: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(V1DvirBase, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['create_dvir_param']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1create_dvir" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'create_dvir_param' is set
        if self.api_client.client_side_validation and ('create_dvir_param' not in local_var_params or  # noqa: E501
                                                        local_var_params['create_dvir_param'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `create_dvir_param` when calling `v1create_dvir`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_dvir_param' in local_var_params:
            body_params = local_var_params['create_dvir_param']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/fleet/maintenance/dvirs', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1DvirBase',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1get_dvirs(self, end_ms, duration_ms, **kwargs):  # noqa: E501
        """Get DVIRs  # noqa: E501

        <n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get DVIRs for the org within provided time constraints  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1get_dvirs(end_ms, duration_ms, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int end_ms: Time in millis until the last dvir log. (required)
        :param int duration_ms: Time in millis which corresponds to the duration before the end_ms. Must be less than or equal to 90 days. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: V1DvirListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.v1get_dvirs_with_http_info(end_ms, duration_ms, **kwargs)  # noqa: E501

    def v1get_dvirs_with_http_info(self, end_ms, duration_ms, **kwargs):  # noqa: E501
        """Get DVIRs  # noqa: E501

        <n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get DVIRs for the org within provided time constraints  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1get_dvirs_with_http_info(end_ms, duration_ms, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int end_ms: Time in millis until the last dvir log. (required)
        :param int duration_ms: Time in millis which corresponds to the duration before the end_ms. Must be less than or equal to 90 days. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(V1DvirListResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['end_ms', 'duration_ms']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1get_dvirs" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'end_ms' is set
        if self.api_client.client_side_validation and ('end_ms' not in local_var_params or  # noqa: E501
                                                        local_var_params['end_ms'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `end_ms` when calling `v1get_dvirs`")  # noqa: E501
        # verify the required parameter 'duration_ms' is set
        if self.api_client.client_side_validation and ('duration_ms' not in local_var_params or  # noqa: E501
                                                        local_var_params['duration_ms'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `duration_ms` when calling `v1get_dvirs`")  # noqa: E501

        if self.api_client.client_side_validation and 'duration_ms' in local_var_params and local_var_params['duration_ms'] > 7776000000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `duration_ms` when calling `v1get_dvirs`, must be a value less than or equal to `7776000000`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'end_ms' in local_var_params and local_var_params['end_ms'] is not None:  # noqa: E501
            query_params.append(('end_ms', local_var_params['end_ms']))  # noqa: E501
        if 'duration_ms' in local_var_params and local_var_params['duration_ms'] is not None:  # noqa: E501
            query_params.append(('duration_ms', local_var_params['duration_ms']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/fleet/maintenance/dvirs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1DvirListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1get_fleet_maintenance_list(self, **kwargs):  # noqa: E501
        """Get vehicles with engine faults or check lights  # noqa: E501

        <n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get list of the vehicles with any engine faults or check light data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1get_fleet_maintenance_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: V1getFleetMaintenanceListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.v1get_fleet_maintenance_list_with_http_info(**kwargs)  # noqa: E501

    def v1get_fleet_maintenance_list_with_http_info(self, **kwargs):  # noqa: E501
        """Get vehicles with engine faults or check lights  # noqa: E501

        <n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get list of the vehicles with any engine faults or check light data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1get_fleet_maintenance_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(V1getFleetMaintenanceListResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1get_fleet_maintenance_list" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/fleet/maintenance/list', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1getFleetMaintenanceListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)