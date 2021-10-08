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


class ProtoVolumeMountRequestSourceVolume(object):
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
        'sub_path': 'str',
        'volume_id': 'int'
    }

    attribute_map = {
        'sub_path': 'sub_path',
        'volume_id': 'volume_id'
    }

    def __init__(self, sub_path=None, volume_id=None, local_vars_configuration=None):  # noqa: E501
        """ProtoVolumeMountRequestSourceVolume - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._sub_path = None
        self._volume_id = None
        self.discriminator = None

        if sub_path is not None:
            self.sub_path = sub_path
        if volume_id is not None:
            self.volume_id = volume_id

    @property
    def sub_path(self):
        """Gets the sub_path of this ProtoVolumeMountRequestSourceVolume.  # noqa: E501


        :return: The sub_path of this ProtoVolumeMountRequestSourceVolume.  # noqa: E501
        :rtype: str
        """
        return self._sub_path

    @sub_path.setter
    def sub_path(self, sub_path):
        """Sets the sub_path of this ProtoVolumeMountRequestSourceVolume.


        :param sub_path: The sub_path of this ProtoVolumeMountRequestSourceVolume.  # noqa: E501
        :type sub_path: str
        """

        self._sub_path = sub_path

    @property
    def volume_id(self):
        """Gets the volume_id of this ProtoVolumeMountRequestSourceVolume.  # noqa: E501


        :return: The volume_id of this ProtoVolumeMountRequestSourceVolume.  # noqa: E501
        :rtype: int
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """Sets the volume_id of this ProtoVolumeMountRequestSourceVolume.


        :param volume_id: The volume_id of this ProtoVolumeMountRequestSourceVolume.  # noqa: E501
        :type volume_id: int
        """

        self._volume_id = volume_id

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
        if not isinstance(other, ProtoVolumeMountRequestSourceVolume):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProtoVolumeMountRequestSourceVolume):
            return True

        return self.to_dict() != other.to_dict()
