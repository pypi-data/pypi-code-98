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


class Bbox(object):
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
        'north': 'float',
        'south': 'float',
        'east': 'float',
        'west': 'float'
    }

    attribute_map = {
        'north': 'north',
        'south': 'south',
        'east': 'east',
        'west': 'west'
    }

    def __init__(self, north=None, south=None, east=None, west=None):  # noqa: E501
        """Bbox - a model defined in Swagger"""  # noqa: E501

        self._north = None
        self._south = None
        self._east = None
        self._west = None
        self.discriminator = None

        self.north = north
        self.south = south
        self.east = east
        self.west = west

    @property
    def north(self):
        """Gets the north of this Bbox.  # noqa: E501


        :return: The north of this Bbox.  # noqa: E501
        :rtype: float
        """
        return self._north

    @north.setter
    def north(self, north):
        """Sets the north of this Bbox.


        :param north: The north of this Bbox.  # noqa: E501
        :type: float
        """
        if north is None:
            raise ValueError("Invalid value for `north`, must not be `None`")  # noqa: E501

        self._north = north

    @property
    def south(self):
        """Gets the south of this Bbox.  # noqa: E501


        :return: The south of this Bbox.  # noqa: E501
        :rtype: float
        """
        return self._south

    @south.setter
    def south(self, south):
        """Sets the south of this Bbox.


        :param south: The south of this Bbox.  # noqa: E501
        :type: float
        """
        if south is None:
            raise ValueError("Invalid value for `south`, must not be `None`")  # noqa: E501

        self._south = south

    @property
    def east(self):
        """Gets the east of this Bbox.  # noqa: E501


        :return: The east of this Bbox.  # noqa: E501
        :rtype: float
        """
        return self._east

    @east.setter
    def east(self, east):
        """Sets the east of this Bbox.


        :param east: The east of this Bbox.  # noqa: E501
        :type: float
        """
        if east is None:
            raise ValueError("Invalid value for `east`, must not be `None`")  # noqa: E501

        self._east = east

    @property
    def west(self):
        """Gets the west of this Bbox.  # noqa: E501


        :return: The west of this Bbox.  # noqa: E501
        :rtype: float
        """
        return self._west

    @west.setter
    def west(self, west):
        """Sets the west of this Bbox.


        :param west: The west of this Bbox.  # noqa: E501
        :type: float
        """
        if west is None:
            raise ValueError("Invalid value for `west`, must not be `None`")  # noqa: E501

        self._west = west

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
        if issubclass(Bbox, dict):
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
        if not isinstance(other, Bbox):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
