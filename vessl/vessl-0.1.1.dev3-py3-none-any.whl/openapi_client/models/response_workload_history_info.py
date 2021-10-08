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


class ResponseWorkloadHistoryInfo(object):
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
        'ended_timestamp': 'float',
        'message': 'str',
        'started_timestamp': 'float',
        'status': 'str'
    }

    attribute_map = {
        'ended_timestamp': 'ended_timestamp',
        'message': 'message',
        'started_timestamp': 'started_timestamp',
        'status': 'status'
    }

    def __init__(self, ended_timestamp=None, message=None, started_timestamp=None, status=None, local_vars_configuration=None):  # noqa: E501
        """ResponseWorkloadHistoryInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._ended_timestamp = None
        self._message = None
        self._started_timestamp = None
        self._status = None
        self.discriminator = None

        self.ended_timestamp = ended_timestamp
        self.message = message
        self.started_timestamp = started_timestamp
        self.status = status

    @property
    def ended_timestamp(self):
        """Gets the ended_timestamp of this ResponseWorkloadHistoryInfo.  # noqa: E501


        :return: The ended_timestamp of this ResponseWorkloadHistoryInfo.  # noqa: E501
        :rtype: float
        """
        return self._ended_timestamp

    @ended_timestamp.setter
    def ended_timestamp(self, ended_timestamp):
        """Sets the ended_timestamp of this ResponseWorkloadHistoryInfo.


        :param ended_timestamp: The ended_timestamp of this ResponseWorkloadHistoryInfo.  # noqa: E501
        :type ended_timestamp: float
        """

        self._ended_timestamp = ended_timestamp

    @property
    def message(self):
        """Gets the message of this ResponseWorkloadHistoryInfo.  # noqa: E501


        :return: The message of this ResponseWorkloadHistoryInfo.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ResponseWorkloadHistoryInfo.


        :param message: The message of this ResponseWorkloadHistoryInfo.  # noqa: E501
        :type message: str
        """
        if self.local_vars_configuration.client_side_validation and message is None:  # noqa: E501
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def started_timestamp(self):
        """Gets the started_timestamp of this ResponseWorkloadHistoryInfo.  # noqa: E501


        :return: The started_timestamp of this ResponseWorkloadHistoryInfo.  # noqa: E501
        :rtype: float
        """
        return self._started_timestamp

    @started_timestamp.setter
    def started_timestamp(self, started_timestamp):
        """Sets the started_timestamp of this ResponseWorkloadHistoryInfo.


        :param started_timestamp: The started_timestamp of this ResponseWorkloadHistoryInfo.  # noqa: E501
        :type started_timestamp: float
        """
        if self.local_vars_configuration.client_side_validation and started_timestamp is None:  # noqa: E501
            raise ValueError("Invalid value for `started_timestamp`, must not be `None`")  # noqa: E501

        self._started_timestamp = started_timestamp

    @property
    def status(self):
        """Gets the status of this ResponseWorkloadHistoryInfo.  # noqa: E501


        :return: The status of this ResponseWorkloadHistoryInfo.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ResponseWorkloadHistoryInfo.


        :param status: The status of this ResponseWorkloadHistoryInfo.  # noqa: E501
        :type status: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

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
        if not isinstance(other, ResponseWorkloadHistoryInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResponseWorkloadHistoryInfo):
            return True

        return self.to_dict() != other.to_dict()
