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


class OrmProjectEdges(object):
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
        'experiments': 'list[OrmExperiment]',
        'models': 'list[OrmModel]',
        'organization': 'OrmOrganization',
        'primary_owner': 'OrmUser',
        'repositories': 'list[OrmProjectRepository]',
        'tags': 'list[OrmTag]',
        'volume': 'OrmVolume'
    }

    attribute_map = {
        'experiments': 'experiments',
        'models': 'models',
        'organization': 'organization',
        'primary_owner': 'primary_owner',
        'repositories': 'repositories',
        'tags': 'tags',
        'volume': 'volume'
    }

    def __init__(self, experiments=None, models=None, organization=None, primary_owner=None, repositories=None, tags=None, volume=None, local_vars_configuration=None):  # noqa: E501
        """OrmProjectEdges - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._experiments = None
        self._models = None
        self._organization = None
        self._primary_owner = None
        self._repositories = None
        self._tags = None
        self._volume = None
        self.discriminator = None

        if experiments is not None:
            self.experiments = experiments
        if models is not None:
            self.models = models
        if organization is not None:
            self.organization = organization
        if primary_owner is not None:
            self.primary_owner = primary_owner
        if repositories is not None:
            self.repositories = repositories
        if tags is not None:
            self.tags = tags
        if volume is not None:
            self.volume = volume

    @property
    def experiments(self):
        """Gets the experiments of this OrmProjectEdges.  # noqa: E501


        :return: The experiments of this OrmProjectEdges.  # noqa: E501
        :rtype: list[OrmExperiment]
        """
        return self._experiments

    @experiments.setter
    def experiments(self, experiments):
        """Sets the experiments of this OrmProjectEdges.


        :param experiments: The experiments of this OrmProjectEdges.  # noqa: E501
        :type experiments: list[OrmExperiment]
        """

        self._experiments = experiments

    @property
    def models(self):
        """Gets the models of this OrmProjectEdges.  # noqa: E501


        :return: The models of this OrmProjectEdges.  # noqa: E501
        :rtype: list[OrmModel]
        """
        return self._models

    @models.setter
    def models(self, models):
        """Sets the models of this OrmProjectEdges.


        :param models: The models of this OrmProjectEdges.  # noqa: E501
        :type models: list[OrmModel]
        """

        self._models = models

    @property
    def organization(self):
        """Gets the organization of this OrmProjectEdges.  # noqa: E501


        :return: The organization of this OrmProjectEdges.  # noqa: E501
        :rtype: OrmOrganization
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this OrmProjectEdges.


        :param organization: The organization of this OrmProjectEdges.  # noqa: E501
        :type organization: OrmOrganization
        """

        self._organization = organization

    @property
    def primary_owner(self):
        """Gets the primary_owner of this OrmProjectEdges.  # noqa: E501


        :return: The primary_owner of this OrmProjectEdges.  # noqa: E501
        :rtype: OrmUser
        """
        return self._primary_owner

    @primary_owner.setter
    def primary_owner(self, primary_owner):
        """Sets the primary_owner of this OrmProjectEdges.


        :param primary_owner: The primary_owner of this OrmProjectEdges.  # noqa: E501
        :type primary_owner: OrmUser
        """

        self._primary_owner = primary_owner

    @property
    def repositories(self):
        """Gets the repositories of this OrmProjectEdges.  # noqa: E501


        :return: The repositories of this OrmProjectEdges.  # noqa: E501
        :rtype: list[OrmProjectRepository]
        """
        return self._repositories

    @repositories.setter
    def repositories(self, repositories):
        """Sets the repositories of this OrmProjectEdges.


        :param repositories: The repositories of this OrmProjectEdges.  # noqa: E501
        :type repositories: list[OrmProjectRepository]
        """

        self._repositories = repositories

    @property
    def tags(self):
        """Gets the tags of this OrmProjectEdges.  # noqa: E501


        :return: The tags of this OrmProjectEdges.  # noqa: E501
        :rtype: list[OrmTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this OrmProjectEdges.


        :param tags: The tags of this OrmProjectEdges.  # noqa: E501
        :type tags: list[OrmTag]
        """

        self._tags = tags

    @property
    def volume(self):
        """Gets the volume of this OrmProjectEdges.  # noqa: E501


        :return: The volume of this OrmProjectEdges.  # noqa: E501
        :rtype: OrmVolume
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this OrmProjectEdges.


        :param volume: The volume of this OrmProjectEdges.  # noqa: E501
        :type volume: OrmVolume
        """

        self._volume = volume

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
        if not isinstance(other, OrmProjectEdges):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrmProjectEdges):
            return True

        return self.to_dict() != other.to_dict()
