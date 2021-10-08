# coding: utf-8

"""
    Aron API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from openapi_client.configuration import Configuration


class DashboardDashboardExperimentFieldValueListResponse(object):
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
        'enum_results': 'list[str]',
        'number_results': 'list[float]',
        'object_results': 'list[ResponseFieldObjectValue]',
        'string_results': 'list[str]',
        'tag_results': 'list[ResponseTagResponse]'
    }

    attribute_map = {
        'enum_results': 'enum_results',
        'number_results': 'number_results',
        'object_results': 'object_results',
        'string_results': 'string_results',
        'tag_results': 'tag_results'
    }

    def __init__(self, enum_results=None, number_results=None, object_results=None, string_results=None, tag_results=None, local_vars_configuration=None):  # noqa: E501
        """DashboardDashboardExperimentFieldValueListResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._enum_results = None
        self._number_results = None
        self._object_results = None
        self._string_results = None
        self._tag_results = None
        self.discriminator = None

        self.enum_results = enum_results
        self.number_results = number_results
        self.object_results = object_results
        self.string_results = string_results
        self.tag_results = tag_results

    @property
    def enum_results(self):
        """Gets the enum_results of this DashboardDashboardExperimentFieldValueListResponse.  # noqa: E501


        :return: The enum_results of this DashboardDashboardExperimentFieldValueListResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._enum_results

    @enum_results.setter
    def enum_results(self, enum_results):
        """Sets the enum_results of this DashboardDashboardExperimentFieldValueListResponse.


        :param enum_results: The enum_results of this DashboardDashboardExperimentFieldValueListResponse.  # noqa: E501
        :type enum_results: list[str]
        """
        if self.local_vars_configuration.client_side_validation and enum_results is None:  # noqa: E501
            raise ValueError("Invalid value for `enum_results`, must not be `None`")  # noqa: E501

        self._enum_results = enum_results

    @property
    def number_results(self):
        """Gets the number_results of this DashboardDashboardExperimentFieldValueListResponse.  # noqa: E501


        :return: The number_results of this DashboardDashboardExperimentFieldValueListResponse.  # noqa: E501
        :rtype: list[float]
        """
        return self._number_results

    @number_results.setter
    def number_results(self, number_results):
        """Sets the number_results of this DashboardDashboardExperimentFieldValueListResponse.


        :param number_results: The number_results of this DashboardDashboardExperimentFieldValueListResponse.  # noqa: E501
        :type number_results: list[float]
        """
        if self.local_vars_configuration.client_side_validation and number_results is None:  # noqa: E501
            raise ValueError("Invalid value for `number_results`, must not be `None`")  # noqa: E501

        self._number_results = number_results

    @property
    def object_results(self):
        """Gets the object_results of this DashboardDashboardExperimentFieldValueListResponse.  # noqa: E501


        :return: The object_results of this DashboardDashboardExperimentFieldValueListResponse.  # noqa: E501
        :rtype: list[ResponseFieldObjectValue]
        """
        return self._object_results

    @object_results.setter
    def object_results(self, object_results):
        """Sets the object_results of this DashboardDashboardExperimentFieldValueListResponse.


        :param object_results: The object_results of this DashboardDashboardExperimentFieldValueListResponse.  # noqa: E501
        :type object_results: list[ResponseFieldObjectValue]
        """
        if self.local_vars_configuration.client_side_validation and object_results is None:  # noqa: E501
            raise ValueError("Invalid value for `object_results`, must not be `None`")  # noqa: E501

        self._object_results = object_results

    @property
    def string_results(self):
        """Gets the string_results of this DashboardDashboardExperimentFieldValueListResponse.  # noqa: E501


        :return: The string_results of this DashboardDashboardExperimentFieldValueListResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._string_results

    @string_results.setter
    def string_results(self, string_results):
        """Sets the string_results of this DashboardDashboardExperimentFieldValueListResponse.


        :param string_results: The string_results of this DashboardDashboardExperimentFieldValueListResponse.  # noqa: E501
        :type string_results: list[str]
        """
        if self.local_vars_configuration.client_side_validation and string_results is None:  # noqa: E501
            raise ValueError("Invalid value for `string_results`, must not be `None`")  # noqa: E501

        self._string_results = string_results

    @property
    def tag_results(self):
        """Gets the tag_results of this DashboardDashboardExperimentFieldValueListResponse.  # noqa: E501


        :return: The tag_results of this DashboardDashboardExperimentFieldValueListResponse.  # noqa: E501
        :rtype: list[ResponseTagResponse]
        """
        return self._tag_results

    @tag_results.setter
    def tag_results(self, tag_results):
        """Sets the tag_results of this DashboardDashboardExperimentFieldValueListResponse.


        :param tag_results: The tag_results of this DashboardDashboardExperimentFieldValueListResponse.  # noqa: E501
        :type tag_results: list[ResponseTagResponse]
        """
        if self.local_vars_configuration.client_side_validation and tag_results is None:  # noqa: E501
            raise ValueError("Invalid value for `tag_results`, must not be `None`")  # noqa: E501

        self._tag_results = tag_results

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DashboardDashboardExperimentFieldValueListResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DashboardDashboardExperimentFieldValueListResponse):
            return True

        return self.to_dict() != other.to_dict()
