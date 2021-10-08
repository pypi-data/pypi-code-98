# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3586
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from lusid.configuration import Configuration


class PortfolioCashLadder(object):
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
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'currency': 'str',
        'sub_holding_keys': 'dict(str, PerpetualProperty)',
        'records': 'list[CashLadderRecord]',
        'links': 'list[Link]'
    }

    attribute_map = {
        'currency': 'currency',
        'sub_holding_keys': 'subHoldingKeys',
        'records': 'records',
        'links': 'links'
    }

    required_map = {
        'currency': 'required',
        'sub_holding_keys': 'optional',
        'records': 'required',
        'links': 'optional'
    }

    def __init__(self, currency=None, sub_holding_keys=None, records=None, links=None, local_vars_configuration=None):  # noqa: E501
        """PortfolioCashLadder - a model defined in OpenAPI"
        
        :param currency:  The currency of the cash-flows. (required)
        :type currency: str
        :param sub_holding_keys:  The sub-holding properties which identify the holding. Each property will be from the 'Transaction' domain. These are configured when a transaction portfolio is created.
        :type sub_holding_keys: dict[str, lusid.PerpetualProperty]
        :param records:  A record of cash flows on a specific date. (required)
        :type records: list[lusid.CashLadderRecord]
        :param links:  Collection of links.
        :type links: list[lusid.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._currency = None
        self._sub_holding_keys = None
        self._records = None
        self._links = None
        self.discriminator = None

        self.currency = currency
        self.sub_holding_keys = sub_holding_keys
        self.records = records
        self.links = links

    @property
    def currency(self):
        """Gets the currency of this PortfolioCashLadder.  # noqa: E501

        The currency of the cash-flows.  # noqa: E501

        :return: The currency of this PortfolioCashLadder.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this PortfolioCashLadder.

        The currency of the cash-flows.  # noqa: E501

        :param currency: The currency of this PortfolioCashLadder.  # noqa: E501
        :type currency: str
        """
        if self.local_vars_configuration.client_side_validation and currency is None:  # noqa: E501
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def sub_holding_keys(self):
        """Gets the sub_holding_keys of this PortfolioCashLadder.  # noqa: E501

        The sub-holding properties which identify the holding. Each property will be from the 'Transaction' domain. These are configured when a transaction portfolio is created.  # noqa: E501

        :return: The sub_holding_keys of this PortfolioCashLadder.  # noqa: E501
        :rtype: dict[str, lusid.PerpetualProperty]
        """
        return self._sub_holding_keys

    @sub_holding_keys.setter
    def sub_holding_keys(self, sub_holding_keys):
        """Sets the sub_holding_keys of this PortfolioCashLadder.

        The sub-holding properties which identify the holding. Each property will be from the 'Transaction' domain. These are configured when a transaction portfolio is created.  # noqa: E501

        :param sub_holding_keys: The sub_holding_keys of this PortfolioCashLadder.  # noqa: E501
        :type sub_holding_keys: dict[str, lusid.PerpetualProperty]
        """

        self._sub_holding_keys = sub_holding_keys

    @property
    def records(self):
        """Gets the records of this PortfolioCashLadder.  # noqa: E501

        A record of cash flows on a specific date.  # noqa: E501

        :return: The records of this PortfolioCashLadder.  # noqa: E501
        :rtype: list[lusid.CashLadderRecord]
        """
        return self._records

    @records.setter
    def records(self, records):
        """Sets the records of this PortfolioCashLadder.

        A record of cash flows on a specific date.  # noqa: E501

        :param records: The records of this PortfolioCashLadder.  # noqa: E501
        :type records: list[lusid.CashLadderRecord]
        """
        if self.local_vars_configuration.client_side_validation and records is None:  # noqa: E501
            raise ValueError("Invalid value for `records`, must not be `None`")  # noqa: E501

        self._records = records

    @property
    def links(self):
        """Gets the links of this PortfolioCashLadder.  # noqa: E501

        Collection of links.  # noqa: E501

        :return: The links of this PortfolioCashLadder.  # noqa: E501
        :rtype: list[lusid.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PortfolioCashLadder.

        Collection of links.  # noqa: E501

        :param links: The links of this PortfolioCashLadder.  # noqa: E501
        :type links: list[lusid.Link]
        """

        self._links = links

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
        if not isinstance(other, PortfolioCashLadder):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PortfolioCashLadder):
            return True

        return self.to_dict() != other.to_dict()
