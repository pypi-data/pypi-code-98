# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

#  (C) Copyright IBM Corp. 2020.
#  #
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#  #
#       http://www.apache.org/licenses/LICENSE-2.0
#  #
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from pprint import pformat
from six import iteritems


class EvaluationDefinitionRepository(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self,method=None, metrics=None):
        """
        EvaluationDefinitionRepository - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'method': 'str',
            'metrics': 'list[EvaluationDefinitionRepositoryMetrics]'
        }

        self.attribute_map = {
            'method': 'method',
            'metrics': 'metrics'
        }

        self._method = method
        self._metrics = metrics

    @property
    def method(self):
        """
        Gets the method of this EvaluationDefinitionRepository.
        The name of the evaluation algorithm

        :return: The method of this EvaluationDefinitionRepository.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """
        Sets the method of this EvaluationDefinitionRepository.
        The name of the evaluation algorithm

        :param method: The method of this EvaluationDefinitionRepository.
        :type: str
        """
        allowed_values = ["regression", "binary", "multiclass"]
        if method not in allowed_values:
            raise ValueError(
                "Invalid value for `method`, must be one of {0}"
                .format(allowed_values)
            )
        self._method = method

    @property
    def metrics(self):
        """
        Gets the metrics of this EvaluationDefinitionRepository.


        :return: The metrics of this EvaluationDefinitionRepository.
        :rtype: list[EvaluationDefinitionRepositoryMetrics]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """
        Sets the metrics of this EvaluationDefinitionRepository.


        :param metrics: The metrics of this EvaluationDefinitionRepository.
        :type: list[EvaluationDefinitionRepositoryMetrics]
        """
        self._metrics = metrics

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

