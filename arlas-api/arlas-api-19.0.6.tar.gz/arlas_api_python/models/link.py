# coding: utf-8

"""
    ARLAS Exploration API

    Explore the content of ARLAS collections  # noqa: E501

    OpenAPI spec version: 19.0.6
    Contact: contact@gisaia.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Link(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'href': 'str',
        'method': 'str',
        'body': 'object'
    }

    attribute_map = {
        'href': 'href',
        'method': 'method',
        'body': 'body'
    }

    def __init__(self, href=None, method=None, body=None):  # noqa: E501
        """Link - a model defined in Swagger"""  # noqa: E501

        self._href = None
        self._method = None
        self._body = None
        self.discriminator = None

        self.href = href
        self.method = method
        if body is not None:
            self.body = body

    @property
    def href(self):
        """Gets the href of this Link.  # noqa: E501


        :return: The href of this Link.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Link.


        :param href: The href of this Link.  # noqa: E501
        :type: str
        """
        if href is None:
            raise ValueError("Invalid value for `href`, must not be `None`")  # noqa: E501

        self._href = href

    @property
    def method(self):
        """Gets the method of this Link.  # noqa: E501


        :return: The method of this Link.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this Link.


        :param method: The method of this Link.  # noqa: E501
        :type: str
        """
        if method is None:
            raise ValueError("Invalid value for `method`, must not be `None`")  # noqa: E501

        self._method = method

    @property
    def body(self):
        """Gets the body of this Link.  # noqa: E501


        :return: The body of this Link.  # noqa: E501
        :rtype: object
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this Link.


        :param body: The body of this Link.  # noqa: E501
        :type: object
        """

        self._body = body

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(Link, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Link):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
