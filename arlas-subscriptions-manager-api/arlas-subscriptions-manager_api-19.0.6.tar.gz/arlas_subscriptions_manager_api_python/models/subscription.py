# coding: utf-8

"""
    ARLAS Subscriptions Manager API

    Manage ARLAS subscriptions on ARLAS collections' events.

    OpenAPI spec version: 19.0.6
    Contact: contact@gisaia.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Subscription(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'trigger': 'dict(str, object)',
        'callback': 'str',
        'hits': 'Hits'
    }

    attribute_map = {
        'trigger': 'trigger',
        'callback': 'callback',
        'hits': 'hits'
    }

    def __init__(self, trigger=None, callback=None, hits=None):
        """
        Subscription - a model defined in Swagger
        """

        self._trigger = None
        self._callback = None
        self._hits = None

        self.trigger = trigger
        self.callback = callback
        self.hits = hits

    @property
    def trigger(self):
        """
        Gets the trigger of this Subscription.

        :return: The trigger of this Subscription.
        :rtype: dict(str, object)
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        """
        Sets the trigger of this Subscription.

        :param trigger: The trigger of this Subscription.
        :type: dict(str, object)
        """
        if trigger is None:
            raise ValueError("Invalid value for `trigger`, must not be `None`")

        self._trigger = trigger

    @property
    def callback(self):
        """
        Gets the callback of this Subscription.

        :return: The callback of this Subscription.
        :rtype: str
        """
        return self._callback

    @callback.setter
    def callback(self, callback):
        """
        Sets the callback of this Subscription.

        :param callback: The callback of this Subscription.
        :type: str
        """
        if callback is None:
            raise ValueError("Invalid value for `callback`, must not be `None`")

        self._callback = callback

    @property
    def hits(self):
        """
        Gets the hits of this Subscription.

        :return: The hits of this Subscription.
        :rtype: Hits
        """
        return self._hits

    @hits.setter
    def hits(self, hits):
        """
        Sets the hits of this Subscription.

        :param hits: The hits of this Subscription.
        :type: Hits
        """
        if hits is None:
            raise ValueError("Invalid value for `hits`, must not be `None`")

        self._hits = hits

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Subscription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
