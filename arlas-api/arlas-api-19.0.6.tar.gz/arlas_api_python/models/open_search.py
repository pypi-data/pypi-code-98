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


class OpenSearch(object):
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
        'short_name': 'str',
        'description': 'str',
        'contact': 'str',
        'tags': 'str',
        'long_name': 'str',
        'image_height': 'str',
        'image_width': 'str',
        'image_type': 'str',
        'image_url': 'str',
        'developer': 'str',
        'attribution': 'str',
        'syndication_right': 'str',
        'adult_content': 'str',
        'language': 'str',
        'input_encoding': 'str',
        'output_encoding': 'str'
    }

    attribute_map = {
        'short_name': 'short_name',
        'description': 'description',
        'contact': 'contact',
        'tags': 'tags',
        'long_name': 'long_name',
        'image_height': 'image_height',
        'image_width': 'image_width',
        'image_type': 'image_type',
        'image_url': 'image_url',
        'developer': 'developer',
        'attribution': 'attribution',
        'syndication_right': 'syndication_right',
        'adult_content': 'adult_content',
        'language': 'language',
        'input_encoding': 'input_encoding',
        'output_encoding': 'output_encoding'
    }

    def __init__(self, short_name=None, description=None, contact=None, tags=None, long_name=None, image_height=None, image_width=None, image_type=None, image_url=None, developer=None, attribution=None, syndication_right=None, adult_content=None, language=None, input_encoding=None, output_encoding=None):  # noqa: E501
        """OpenSearch - a model defined in Swagger"""  # noqa: E501

        self._short_name = None
        self._description = None
        self._contact = None
        self._tags = None
        self._long_name = None
        self._image_height = None
        self._image_width = None
        self._image_type = None
        self._image_url = None
        self._developer = None
        self._attribution = None
        self._syndication_right = None
        self._adult_content = None
        self._language = None
        self._input_encoding = None
        self._output_encoding = None
        self.discriminator = None

        if short_name is not None:
            self.short_name = short_name
        if description is not None:
            self.description = description
        if contact is not None:
            self.contact = contact
        if tags is not None:
            self.tags = tags
        if long_name is not None:
            self.long_name = long_name
        if image_height is not None:
            self.image_height = image_height
        if image_width is not None:
            self.image_width = image_width
        if image_type is not None:
            self.image_type = image_type
        if image_url is not None:
            self.image_url = image_url
        if developer is not None:
            self.developer = developer
        if attribution is not None:
            self.attribution = attribution
        if syndication_right is not None:
            self.syndication_right = syndication_right
        if adult_content is not None:
            self.adult_content = adult_content
        if language is not None:
            self.language = language
        if input_encoding is not None:
            self.input_encoding = input_encoding
        if output_encoding is not None:
            self.output_encoding = output_encoding

    @property
    def short_name(self):
        """Gets the short_name of this OpenSearch.  # noqa: E501


        :return: The short_name of this OpenSearch.  # noqa: E501
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """Sets the short_name of this OpenSearch.


        :param short_name: The short_name of this OpenSearch.  # noqa: E501
        :type: str
        """

        self._short_name = short_name

    @property
    def description(self):
        """Gets the description of this OpenSearch.  # noqa: E501


        :return: The description of this OpenSearch.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this OpenSearch.


        :param description: The description of this OpenSearch.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def contact(self):
        """Gets the contact of this OpenSearch.  # noqa: E501


        :return: The contact of this OpenSearch.  # noqa: E501
        :rtype: str
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this OpenSearch.


        :param contact: The contact of this OpenSearch.  # noqa: E501
        :type: str
        """

        self._contact = contact

    @property
    def tags(self):
        """Gets the tags of this OpenSearch.  # noqa: E501


        :return: The tags of this OpenSearch.  # noqa: E501
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this OpenSearch.


        :param tags: The tags of this OpenSearch.  # noqa: E501
        :type: str
        """

        self._tags = tags

    @property
    def long_name(self):
        """Gets the long_name of this OpenSearch.  # noqa: E501


        :return: The long_name of this OpenSearch.  # noqa: E501
        :rtype: str
        """
        return self._long_name

    @long_name.setter
    def long_name(self, long_name):
        """Sets the long_name of this OpenSearch.


        :param long_name: The long_name of this OpenSearch.  # noqa: E501
        :type: str
        """

        self._long_name = long_name

    @property
    def image_height(self):
        """Gets the image_height of this OpenSearch.  # noqa: E501


        :return: The image_height of this OpenSearch.  # noqa: E501
        :rtype: str
        """
        return self._image_height

    @image_height.setter
    def image_height(self, image_height):
        """Sets the image_height of this OpenSearch.


        :param image_height: The image_height of this OpenSearch.  # noqa: E501
        :type: str
        """

        self._image_height = image_height

    @property
    def image_width(self):
        """Gets the image_width of this OpenSearch.  # noqa: E501


        :return: The image_width of this OpenSearch.  # noqa: E501
        :rtype: str
        """
        return self._image_width

    @image_width.setter
    def image_width(self, image_width):
        """Sets the image_width of this OpenSearch.


        :param image_width: The image_width of this OpenSearch.  # noqa: E501
        :type: str
        """

        self._image_width = image_width

    @property
    def image_type(self):
        """Gets the image_type of this OpenSearch.  # noqa: E501


        :return: The image_type of this OpenSearch.  # noqa: E501
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        """Sets the image_type of this OpenSearch.


        :param image_type: The image_type of this OpenSearch.  # noqa: E501
        :type: str
        """

        self._image_type = image_type

    @property
    def image_url(self):
        """Gets the image_url of this OpenSearch.  # noqa: E501


        :return: The image_url of this OpenSearch.  # noqa: E501
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this OpenSearch.


        :param image_url: The image_url of this OpenSearch.  # noqa: E501
        :type: str
        """

        self._image_url = image_url

    @property
    def developer(self):
        """Gets the developer of this OpenSearch.  # noqa: E501


        :return: The developer of this OpenSearch.  # noqa: E501
        :rtype: str
        """
        return self._developer

    @developer.setter
    def developer(self, developer):
        """Sets the developer of this OpenSearch.


        :param developer: The developer of this OpenSearch.  # noqa: E501
        :type: str
        """

        self._developer = developer

    @property
    def attribution(self):
        """Gets the attribution of this OpenSearch.  # noqa: E501


        :return: The attribution of this OpenSearch.  # noqa: E501
        :rtype: str
        """
        return self._attribution

    @attribution.setter
    def attribution(self, attribution):
        """Sets the attribution of this OpenSearch.


        :param attribution: The attribution of this OpenSearch.  # noqa: E501
        :type: str
        """

        self._attribution = attribution

    @property
    def syndication_right(self):
        """Gets the syndication_right of this OpenSearch.  # noqa: E501


        :return: The syndication_right of this OpenSearch.  # noqa: E501
        :rtype: str
        """
        return self._syndication_right

    @syndication_right.setter
    def syndication_right(self, syndication_right):
        """Sets the syndication_right of this OpenSearch.


        :param syndication_right: The syndication_right of this OpenSearch.  # noqa: E501
        :type: str
        """

        self._syndication_right = syndication_right

    @property
    def adult_content(self):
        """Gets the adult_content of this OpenSearch.  # noqa: E501


        :return: The adult_content of this OpenSearch.  # noqa: E501
        :rtype: str
        """
        return self._adult_content

    @adult_content.setter
    def adult_content(self, adult_content):
        """Sets the adult_content of this OpenSearch.


        :param adult_content: The adult_content of this OpenSearch.  # noqa: E501
        :type: str
        """

        self._adult_content = adult_content

    @property
    def language(self):
        """Gets the language of this OpenSearch.  # noqa: E501


        :return: The language of this OpenSearch.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this OpenSearch.


        :param language: The language of this OpenSearch.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def input_encoding(self):
        """Gets the input_encoding of this OpenSearch.  # noqa: E501


        :return: The input_encoding of this OpenSearch.  # noqa: E501
        :rtype: str
        """
        return self._input_encoding

    @input_encoding.setter
    def input_encoding(self, input_encoding):
        """Sets the input_encoding of this OpenSearch.


        :param input_encoding: The input_encoding of this OpenSearch.  # noqa: E501
        :type: str
        """

        self._input_encoding = input_encoding

    @property
    def output_encoding(self):
        """Gets the output_encoding of this OpenSearch.  # noqa: E501


        :return: The output_encoding of this OpenSearch.  # noqa: E501
        :rtype: str
        """
        return self._output_encoding

    @output_encoding.setter
    def output_encoding(self, output_encoding):
        """Sets the output_encoding of this OpenSearch.


        :param output_encoding: The output_encoding of this OpenSearch.  # noqa: E501
        :type: str
        """

        self._output_encoding = output_encoding

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
        if issubclass(OpenSearch, dict):
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
        if not isinstance(other, OpenSearch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
