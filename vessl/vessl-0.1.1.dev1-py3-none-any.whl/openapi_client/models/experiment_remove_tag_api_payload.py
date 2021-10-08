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


class ExperimentRemoveTagAPIPayload(object):
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
        'experiment_numbers': 'list[int]',
        'tag_names': 'list[str]'
    }

    attribute_map = {
        'experiment_numbers': 'experiment_numbers',
        'tag_names': 'tag_names'
    }

    def __init__(self, experiment_numbers=None, tag_names=None, local_vars_configuration=None):  # noqa: E501
        """ExperimentRemoveTagAPIPayload - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._experiment_numbers = None
        self._tag_names = None
        self.discriminator = None

        self.experiment_numbers = experiment_numbers
        self.tag_names = tag_names

    @property
    def experiment_numbers(self):
        """Gets the experiment_numbers of this ExperimentRemoveTagAPIPayload.  # noqa: E501


        :return: The experiment_numbers of this ExperimentRemoveTagAPIPayload.  # noqa: E501
        :rtype: list[int]
        """
        return self._experiment_numbers

    @experiment_numbers.setter
    def experiment_numbers(self, experiment_numbers):
        """Sets the experiment_numbers of this ExperimentRemoveTagAPIPayload.


        :param experiment_numbers: The experiment_numbers of this ExperimentRemoveTagAPIPayload.  # noqa: E501
        :type experiment_numbers: list[int]
        """
        if self.local_vars_configuration.client_side_validation and experiment_numbers is None:  # noqa: E501
            raise ValueError("Invalid value for `experiment_numbers`, must not be `None`")  # noqa: E501

        self._experiment_numbers = experiment_numbers

    @property
    def tag_names(self):
        """Gets the tag_names of this ExperimentRemoveTagAPIPayload.  # noqa: E501


        :return: The tag_names of this ExperimentRemoveTagAPIPayload.  # noqa: E501
        :rtype: list[str]
        """
        return self._tag_names

    @tag_names.setter
    def tag_names(self, tag_names):
        """Sets the tag_names of this ExperimentRemoveTagAPIPayload.


        :param tag_names: The tag_names of this ExperimentRemoveTagAPIPayload.  # noqa: E501
        :type tag_names: list[str]
        """
        if self.local_vars_configuration.client_side_validation and tag_names is None:  # noqa: E501
            raise ValueError("Invalid value for `tag_names`, must not be `None`")  # noqa: E501

        self._tag_names = tag_names

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
        if not isinstance(other, ExperimentRemoveTagAPIPayload):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExperimentRemoveTagAPIPayload):
            return True

        return self.to_dict() != other.to_dict()
