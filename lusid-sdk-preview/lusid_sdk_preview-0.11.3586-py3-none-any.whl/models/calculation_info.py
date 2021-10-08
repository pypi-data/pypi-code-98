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


class CalculationInfo(object):
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
        'calculation_description': 'str',
        'calculation_method': 'str',
        'multiplier': 'str',
        'calculation_amount': 'float'
    }

    attribute_map = {
        'calculation_description': 'calculationDescription',
        'calculation_method': 'calculationMethod',
        'multiplier': 'multiplier',
        'calculation_amount': 'calculationAmount'
    }

    required_map = {
        'calculation_description': 'required',
        'calculation_method': 'required',
        'multiplier': 'required',
        'calculation_amount': 'required'
    }

    def __init__(self, calculation_description=None, calculation_method=None, multiplier=None, calculation_amount=None, local_vars_configuration=None):  # noqa: E501
        """CalculationInfo - a model defined in OpenAPI"
        
        :param calculation_description:  Description of what the calculation applies to eg. Fee, MinFee, MaxFee (required)
        :type calculation_description: str
        :param calculation_method:  Method of calculating the fees or commission among: BasisPoints, Percentage, Rate, Flat etc. The available values are: Rate, BasisPoints, Percentage, Flat (required)
        :type calculation_method: str
        :param multiplier:  . The available values are: None, Quantity, Value (required)
        :type multiplier: str
        :param calculation_amount:  Numerical fee amount (required)
        :type calculation_amount: float

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._calculation_description = None
        self._calculation_method = None
        self._multiplier = None
        self._calculation_amount = None
        self.discriminator = None

        self.calculation_description = calculation_description
        self.calculation_method = calculation_method
        self.multiplier = multiplier
        self.calculation_amount = calculation_amount

    @property
    def calculation_description(self):
        """Gets the calculation_description of this CalculationInfo.  # noqa: E501

        Description of what the calculation applies to eg. Fee, MinFee, MaxFee  # noqa: E501

        :return: The calculation_description of this CalculationInfo.  # noqa: E501
        :rtype: str
        """
        return self._calculation_description

    @calculation_description.setter
    def calculation_description(self, calculation_description):
        """Sets the calculation_description of this CalculationInfo.

        Description of what the calculation applies to eg. Fee, MinFee, MaxFee  # noqa: E501

        :param calculation_description: The calculation_description of this CalculationInfo.  # noqa: E501
        :type calculation_description: str
        """
        if self.local_vars_configuration.client_side_validation and calculation_description is None:  # noqa: E501
            raise ValueError("Invalid value for `calculation_description`, must not be `None`")  # noqa: E501

        self._calculation_description = calculation_description

    @property
    def calculation_method(self):
        """Gets the calculation_method of this CalculationInfo.  # noqa: E501

        Method of calculating the fees or commission among: BasisPoints, Percentage, Rate, Flat etc. The available values are: Rate, BasisPoints, Percentage, Flat  # noqa: E501

        :return: The calculation_method of this CalculationInfo.  # noqa: E501
        :rtype: str
        """
        return self._calculation_method

    @calculation_method.setter
    def calculation_method(self, calculation_method):
        """Sets the calculation_method of this CalculationInfo.

        Method of calculating the fees or commission among: BasisPoints, Percentage, Rate, Flat etc. The available values are: Rate, BasisPoints, Percentage, Flat  # noqa: E501

        :param calculation_method: The calculation_method of this CalculationInfo.  # noqa: E501
        :type calculation_method: str
        """
        if self.local_vars_configuration.client_side_validation and calculation_method is None:  # noqa: E501
            raise ValueError("Invalid value for `calculation_method`, must not be `None`")  # noqa: E501
        allowed_values = ["Rate", "BasisPoints", "Percentage", "Flat"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and calculation_method not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `calculation_method` ({0}), must be one of {1}"  # noqa: E501
                .format(calculation_method, allowed_values)
            )

        self._calculation_method = calculation_method

    @property
    def multiplier(self):
        """Gets the multiplier of this CalculationInfo.  # noqa: E501

        . The available values are: None, Quantity, Value  # noqa: E501

        :return: The multiplier of this CalculationInfo.  # noqa: E501
        :rtype: str
        """
        return self._multiplier

    @multiplier.setter
    def multiplier(self, multiplier):
        """Sets the multiplier of this CalculationInfo.

        . The available values are: None, Quantity, Value  # noqa: E501

        :param multiplier: The multiplier of this CalculationInfo.  # noqa: E501
        :type multiplier: str
        """
        if self.local_vars_configuration.client_side_validation and multiplier is None:  # noqa: E501
            raise ValueError("Invalid value for `multiplier`, must not be `None`")  # noqa: E501
        allowed_values = ["None", "Quantity", "Value"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and multiplier not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `multiplier` ({0}), must be one of {1}"  # noqa: E501
                .format(multiplier, allowed_values)
            )

        self._multiplier = multiplier

    @property
    def calculation_amount(self):
        """Gets the calculation_amount of this CalculationInfo.  # noqa: E501

        Numerical fee amount  # noqa: E501

        :return: The calculation_amount of this CalculationInfo.  # noqa: E501
        :rtype: float
        """
        return self._calculation_amount

    @calculation_amount.setter
    def calculation_amount(self, calculation_amount):
        """Sets the calculation_amount of this CalculationInfo.

        Numerical fee amount  # noqa: E501

        :param calculation_amount: The calculation_amount of this CalculationInfo.  # noqa: E501
        :type calculation_amount: float
        """
        if self.local_vars_configuration.client_side_validation and calculation_amount is None:  # noqa: E501
            raise ValueError("Invalid value for `calculation_amount`, must not be `None`")  # noqa: E501

        self._calculation_amount = calculation_amount

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
        if not isinstance(other, CalculationInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CalculationInfo):
            return True

        return self.to_dict() != other.to_dict()
