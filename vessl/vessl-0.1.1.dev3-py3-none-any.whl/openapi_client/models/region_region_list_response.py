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


class RegionRegionListResponse(object):
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
        'default_region': 'str',
        'regions': 'list[ResponseRegion]'
    }

    attribute_map = {
        'default_region': 'default_region',
        'regions': 'regions'
    }

    def __init__(self, default_region=None, regions=None, local_vars_configuration=None):  # noqa: E501
        """RegionRegionListResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._default_region = None
        self._regions = None
        self.discriminator = None

        if default_region is not None:
            self.default_region = default_region
        if regions is not None:
            self.regions = regions

    @property
    def default_region(self):
        """Gets the default_region of this RegionRegionListResponse.  # noqa: E501


        :return: The default_region of this RegionRegionListResponse.  # noqa: E501
        :rtype: str
        """
        return self._default_region

    @default_region.setter
    def default_region(self, default_region):
        """Sets the default_region of this RegionRegionListResponse.


        :param default_region: The default_region of this RegionRegionListResponse.  # noqa: E501
        :type default_region: str
        """

        self._default_region = default_region

    @property
    def regions(self):
        """Gets the regions of this RegionRegionListResponse.  # noqa: E501


        :return: The regions of this RegionRegionListResponse.  # noqa: E501
        :rtype: list[ResponseRegion]
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        """Sets the regions of this RegionRegionListResponse.


        :param regions: The regions of this RegionRegionListResponse.  # noqa: E501
        :type regions: list[ResponseRegion]
        """

        self._regions = regions

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
        if not isinstance(other, RegionRegionListResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RegionRegionListResponse):
            return True

        return self.to_dict() != other.to_dict()
