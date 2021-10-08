#!/usr/bin/python
#
# Copyright 2018-2021 Polyaxon, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# coding: utf-8

"""
    Polyaxon SDKs and REST API specification.

    Polyaxon SDKs and REST API specification.  # noqa: E501

    The version of the OpenAPI document: 1.11.3
    Contact: contact@polyaxon.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from polyaxon_sdk.configuration import Configuration


class V1RunEdge(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'upstream': 'V1Run',
        'downstream': 'V1Run',
        'kind': 'V1RunEdgeKind',
        'values': 'object',
        'statuses': 'list[V1Statuses]'
    }

    attribute_map = {
        'upstream': 'upstream',
        'downstream': 'downstream',
        'kind': 'kind',
        'values': 'values',
        'statuses': 'statuses'
    }

    def __init__(self, upstream=None, downstream=None, kind=None, values=None, statuses=None, local_vars_configuration=None):  # noqa: E501
        """V1RunEdge - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._upstream = None
        self._downstream = None
        self._kind = None
        self._values = None
        self._statuses = None
        self.discriminator = None

        if upstream is not None:
            self.upstream = upstream
        if downstream is not None:
            self.downstream = downstream
        if kind is not None:
            self.kind = kind
        if values is not None:
            self.values = values
        if statuses is not None:
            self.statuses = statuses

    @property
    def upstream(self):
        """Gets the upstream of this V1RunEdge.  # noqa: E501


        :return: The upstream of this V1RunEdge.  # noqa: E501
        :rtype: V1Run
        """
        return self._upstream

    @upstream.setter
    def upstream(self, upstream):
        """Sets the upstream of this V1RunEdge.


        :param upstream: The upstream of this V1RunEdge.  # noqa: E501
        :type: V1Run
        """

        self._upstream = upstream

    @property
    def downstream(self):
        """Gets the downstream of this V1RunEdge.  # noqa: E501


        :return: The downstream of this V1RunEdge.  # noqa: E501
        :rtype: V1Run
        """
        return self._downstream

    @downstream.setter
    def downstream(self, downstream):
        """Sets the downstream of this V1RunEdge.


        :param downstream: The downstream of this V1RunEdge.  # noqa: E501
        :type: V1Run
        """

        self._downstream = downstream

    @property
    def kind(self):
        """Gets the kind of this V1RunEdge.  # noqa: E501


        :return: The kind of this V1RunEdge.  # noqa: E501
        :rtype: V1RunEdgeKind
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this V1RunEdge.


        :param kind: The kind of this V1RunEdge.  # noqa: E501
        :type: V1RunEdgeKind
        """

        self._kind = kind

    @property
    def values(self):
        """Gets the values of this V1RunEdge.  # noqa: E501


        :return: The values of this V1RunEdge.  # noqa: E501
        :rtype: object
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this V1RunEdge.


        :param values: The values of this V1RunEdge.  # noqa: E501
        :type: object
        """

        self._values = values

    @property
    def statuses(self):
        """Gets the statuses of this V1RunEdge.  # noqa: E501


        :return: The statuses of this V1RunEdge.  # noqa: E501
        :rtype: list[V1Statuses]
        """
        return self._statuses

    @statuses.setter
    def statuses(self, statuses):
        """Sets the statuses of this V1RunEdge.


        :param statuses: The statuses of this V1RunEdge.  # noqa: E501
        :type: list[V1Statuses]
        """

        self._statuses = statuses

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1RunEdge):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1RunEdge):
            return True

        return self.to_dict() != other.to_dict()
