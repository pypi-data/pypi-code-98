# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3586
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from lusid_asyncio.api_client import ApiClient
from lusid_asyncio.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class EntitiesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_portfolio_changes(self, scope, effective_at, **kwargs):  # noqa: E501
        """[EARLY ACCESS] GetPortfolioChanges: Get the next change to each portfolio in a scope.  # noqa: E501

        Gets the time of the next (earliest effective at) modification (correction and/or amendment) to each portfolio in a scope relative to a point in bitemporal time.  Includes changes from parent portfolios in different scopes.  Excludes changes from subcriptions (e.g corporate actions).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_portfolio_changes(scope, effective_at, async_req=True)
        >>> result = thread.get()

        :param scope: The scope (required)
        :type scope: str
        :param effective_at: The effective date of the origin. (required)
        :type effective_at: str
        :param as_at: The as-at date of the origin.
        :type as_at: datetime
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ResourceListOfChange
        """
        kwargs['_return_http_data_only'] = True
        return self.get_portfolio_changes_with_http_info(scope, effective_at, **kwargs)  # noqa: E501

    def get_portfolio_changes_with_http_info(self, scope, effective_at, **kwargs):  # noqa: E501
        """[EARLY ACCESS] GetPortfolioChanges: Get the next change to each portfolio in a scope.  # noqa: E501

        Gets the time of the next (earliest effective at) modification (correction and/or amendment) to each portfolio in a scope relative to a point in bitemporal time.  Includes changes from parent portfolios in different scopes.  Excludes changes from subcriptions (e.g corporate actions).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_portfolio_changes_with_http_info(scope, effective_at, async_req=True)
        >>> result = thread.get()

        :param scope: The scope (required)
        :type scope: str
        :param effective_at: The effective date of the origin. (required)
        :type effective_at: str
        :param as_at: The as-at date of the origin.
        :type as_at: datetime
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ResourceListOfChange, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'scope',
            'effective_at',
            'as_at'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_portfolio_changes" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'scope' is set
        if self.api_client.client_side_validation and ('scope' not in local_var_params or  # noqa: E501
                                                        local_var_params['scope'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `scope` when calling `get_portfolio_changes`")  # noqa: E501
        # verify the required parameter 'effective_at' is set
        if self.api_client.client_side_validation and ('effective_at' not in local_var_params or  # noqa: E501
                                                        local_var_params['effective_at'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `effective_at` when calling `get_portfolio_changes`")  # noqa: E501

        if self.api_client.client_side_validation and ('scope' in local_var_params and  # noqa: E501
                                                        len(local_var_params['scope']) > 64):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `scope` when calling `get_portfolio_changes`, length must be less than or equal to `64`")  # noqa: E501
        if self.api_client.client_side_validation and ('scope' in local_var_params and  # noqa: E501
                                                        len(local_var_params['scope']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `scope` when calling `get_portfolio_changes`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'scope' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_]+$', local_var_params['scope']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `scope` when calling `get_portfolio_changes`, must conform to the pattern `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501
        if self.api_client.client_side_validation and ('effective_at' in local_var_params and  # noqa: E501
                                                        len(local_var_params['effective_at']) > 256):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `effective_at` when calling `get_portfolio_changes`, length must be less than or equal to `256`")  # noqa: E501
        if self.api_client.client_side_validation and ('effective_at' in local_var_params and  # noqa: E501
                                                        len(local_var_params['effective_at']) < 0):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `effective_at` when calling `get_portfolio_changes`, length must be greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'effective_at' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_\+:\.]+$', local_var_params['effective_at']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `effective_at` when calling `get_portfolio_changes`, must conform to the pattern `/^[a-zA-Z0-9\-_\+:\.]+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'scope' in local_var_params and local_var_params['scope'] is not None:  # noqa: E501
            query_params.append(('scope', local_var_params['scope']))  # noqa: E501
        if 'effective_at' in local_var_params and local_var_params['effective_at'] is not None:  # noqa: E501
            query_params.append(('effectiveAt', local_var_params['effective_at']))  # noqa: E501
        if 'as_at' in local_var_params and local_var_params['as_at'] is not None:  # noqa: E501
            query_params.append(('asAt', local_var_params['as_at']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        header_params['Accept-Encoding'] = "gzip, deflate, br"

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501
        
        response_types_map = {
            400: "LusidValidationProblemDetails",
            200: "ResourceListOfChange",
        }

        return self.api_client.call_api(
            '/api/entities/changes/portfolios', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
