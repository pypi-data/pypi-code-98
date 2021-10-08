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


class ExperimentExperimentParameterListResponse(object):
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
        'env_vars': 'list[str]',
        'metrics': 'list[str]'
    }

    attribute_map = {
        'env_vars': 'env_vars',
        'metrics': 'metrics'
    }

    def __init__(self, env_vars=None, metrics=None, local_vars_configuration=None):  # noqa: E501
        """ExperimentExperimentParameterListResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._env_vars = None
        self._metrics = None
        self.discriminator = None

        self.env_vars = env_vars
        self.metrics = metrics

    @property
    def env_vars(self):
        """Gets the env_vars of this ExperimentExperimentParameterListResponse.  # noqa: E501


        :return: The env_vars of this ExperimentExperimentParameterListResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._env_vars

    @env_vars.setter
    def env_vars(self, env_vars):
        """Sets the env_vars of this ExperimentExperimentParameterListResponse.


        :param env_vars: The env_vars of this ExperimentExperimentParameterListResponse.  # noqa: E501
        :type env_vars: list[str]
        """
        if self.local_vars_configuration.client_side_validation and env_vars is None:  # noqa: E501
            raise ValueError("Invalid value for `env_vars`, must not be `None`")  # noqa: E501

        self._env_vars = env_vars

    @property
    def metrics(self):
        """Gets the metrics of this ExperimentExperimentParameterListResponse.  # noqa: E501


        :return: The metrics of this ExperimentExperimentParameterListResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this ExperimentExperimentParameterListResponse.


        :param metrics: The metrics of this ExperimentExperimentParameterListResponse.  # noqa: E501
        :type metrics: list[str]
        """
        if self.local_vars_configuration.client_side_validation and metrics is None:  # noqa: E501
            raise ValueError("Invalid value for `metrics`, must not be `None`")  # noqa: E501

        self._metrics = metrics

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
        if not isinstance(other, ExperimentExperimentParameterListResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExperimentExperimentParameterListResponse):
            return True

        return self.to_dict() != other.to_dict()
