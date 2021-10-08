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


class V1Status(object):
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
        'uuid': 'str',
        'status': 'V1Statuses',
        'status_conditions': 'list[V1StatusCondition]'
    }

    attribute_map = {
        'uuid': 'uuid',
        'status': 'status',
        'status_conditions': 'status_conditions'
    }

    def __init__(self, uuid=None, status=None, status_conditions=None, local_vars_configuration=None):  # noqa: E501
        """V1Status - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._uuid = None
        self._status = None
        self._status_conditions = None
        self.discriminator = None

        if uuid is not None:
            self.uuid = uuid
        if status is not None:
            self.status = status
        if status_conditions is not None:
            self.status_conditions = status_conditions

    @property
    def uuid(self):
        """Gets the uuid of this V1Status.  # noqa: E501


        :return: The uuid of this V1Status.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this V1Status.


        :param uuid: The uuid of this V1Status.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def status(self):
        """Gets the status of this V1Status.  # noqa: E501


        :return: The status of this V1Status.  # noqa: E501
        :rtype: V1Statuses
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this V1Status.


        :param status: The status of this V1Status.  # noqa: E501
        :type: V1Statuses
        """

        self._status = status

    @property
    def status_conditions(self):
        """Gets the status_conditions of this V1Status.  # noqa: E501


        :return: The status_conditions of this V1Status.  # noqa: E501
        :rtype: list[V1StatusCondition]
        """
        return self._status_conditions

    @status_conditions.setter
    def status_conditions(self, status_conditions):
        """Sets the status_conditions of this V1Status.


        :param status_conditions: The status_conditions of this V1Status.  # noqa: E501
        :type: list[V1StatusCondition]
        """

        self._status_conditions = status_conditions

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
        if not isinstance(other, V1Status):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1Status):
            return True

        return self.to_dict() != other.to_dict()
