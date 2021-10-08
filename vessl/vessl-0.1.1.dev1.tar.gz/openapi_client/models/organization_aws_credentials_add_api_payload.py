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


class OrganizationAWSCredentialsAddAPIPayload(object):
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
        'access_key_id': 'str',
        'credentials_name': 'str',
        'region': 'str',
        'secret_access_key': 'str'
    }

    attribute_map = {
        'access_key_id': 'access_key_id',
        'credentials_name': 'credentials_name',
        'region': 'region',
        'secret_access_key': 'secret_access_key'
    }

    def __init__(self, access_key_id=None, credentials_name=None, region=None, secret_access_key=None, local_vars_configuration=None):  # noqa: E501
        """OrganizationAWSCredentialsAddAPIPayload - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._access_key_id = None
        self._credentials_name = None
        self._region = None
        self._secret_access_key = None
        self.discriminator = None

        self.access_key_id = access_key_id
        self.credentials_name = credentials_name
        self.region = region
        self.secret_access_key = secret_access_key

    @property
    def access_key_id(self):
        """Gets the access_key_id of this OrganizationAWSCredentialsAddAPIPayload.  # noqa: E501


        :return: The access_key_id of this OrganizationAWSCredentialsAddAPIPayload.  # noqa: E501
        :rtype: str
        """
        return self._access_key_id

    @access_key_id.setter
    def access_key_id(self, access_key_id):
        """Sets the access_key_id of this OrganizationAWSCredentialsAddAPIPayload.


        :param access_key_id: The access_key_id of this OrganizationAWSCredentialsAddAPIPayload.  # noqa: E501
        :type access_key_id: str
        """
        if self.local_vars_configuration.client_side_validation and access_key_id is None:  # noqa: E501
            raise ValueError("Invalid value for `access_key_id`, must not be `None`")  # noqa: E501

        self._access_key_id = access_key_id

    @property
    def credentials_name(self):
        """Gets the credentials_name of this OrganizationAWSCredentialsAddAPIPayload.  # noqa: E501


        :return: The credentials_name of this OrganizationAWSCredentialsAddAPIPayload.  # noqa: E501
        :rtype: str
        """
        return self._credentials_name

    @credentials_name.setter
    def credentials_name(self, credentials_name):
        """Sets the credentials_name of this OrganizationAWSCredentialsAddAPIPayload.


        :param credentials_name: The credentials_name of this OrganizationAWSCredentialsAddAPIPayload.  # noqa: E501
        :type credentials_name: str
        """
        if self.local_vars_configuration.client_side_validation and credentials_name is None:  # noqa: E501
            raise ValueError("Invalid value for `credentials_name`, must not be `None`")  # noqa: E501

        self._credentials_name = credentials_name

    @property
    def region(self):
        """Gets the region of this OrganizationAWSCredentialsAddAPIPayload.  # noqa: E501


        :return: The region of this OrganizationAWSCredentialsAddAPIPayload.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this OrganizationAWSCredentialsAddAPIPayload.


        :param region: The region of this OrganizationAWSCredentialsAddAPIPayload.  # noqa: E501
        :type region: str
        """
        if self.local_vars_configuration.client_side_validation and region is None:  # noqa: E501
            raise ValueError("Invalid value for `region`, must not be `None`")  # noqa: E501

        self._region = region

    @property
    def secret_access_key(self):
        """Gets the secret_access_key of this OrganizationAWSCredentialsAddAPIPayload.  # noqa: E501


        :return: The secret_access_key of this OrganizationAWSCredentialsAddAPIPayload.  # noqa: E501
        :rtype: str
        """
        return self._secret_access_key

    @secret_access_key.setter
    def secret_access_key(self, secret_access_key):
        """Sets the secret_access_key of this OrganizationAWSCredentialsAddAPIPayload.


        :param secret_access_key: The secret_access_key of this OrganizationAWSCredentialsAddAPIPayload.  # noqa: E501
        :type secret_access_key: str
        """
        if self.local_vars_configuration.client_side_validation and secret_access_key is None:  # noqa: E501
            raise ValueError("Invalid value for `secret_access_key`, must not be `None`")  # noqa: E501

        self._secret_access_key = secret_access_key

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
        if not isinstance(other, OrganizationAWSCredentialsAddAPIPayload):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrganizationAWSCredentialsAddAPIPayload):
            return True

        return self.to_dict() != other.to_dict()
