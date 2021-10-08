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


class OrmNotificationConfig(object):
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
        'created_dt': 'datetime',
        'edges': 'OrmNotificationConfigEdges',
        'id': 'int',
        'immutable_slug': 'str',
        'notification_config_organization': 'int',
        'notification_config_project': 'int',
        'slack_team_name': 'str',
        'updated_dt': 'datetime'
    }

    attribute_map = {
        'created_dt': 'created_dt',
        'edges': 'edges',
        'id': 'id',
        'immutable_slug': 'immutable_slug',
        'notification_config_organization': 'notification_config_organization',
        'notification_config_project': 'notification_config_project',
        'slack_team_name': 'slack_team_name',
        'updated_dt': 'updated_dt'
    }

    def __init__(self, created_dt=None, edges=None, id=None, immutable_slug=None, notification_config_organization=None, notification_config_project=None, slack_team_name=None, updated_dt=None, local_vars_configuration=None):  # noqa: E501
        """OrmNotificationConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._created_dt = None
        self._edges = None
        self._id = None
        self._immutable_slug = None
        self._notification_config_organization = None
        self._notification_config_project = None
        self._slack_team_name = None
        self._updated_dt = None
        self.discriminator = None

        if created_dt is not None:
            self.created_dt = created_dt
        if edges is not None:
            self.edges = edges
        if id is not None:
            self.id = id
        if immutable_slug is not None:
            self.immutable_slug = immutable_slug
        if notification_config_organization is not None:
            self.notification_config_organization = notification_config_organization
        self.notification_config_project = notification_config_project
        self.slack_team_name = slack_team_name
        if updated_dt is not None:
            self.updated_dt = updated_dt

    @property
    def created_dt(self):
        """Gets the created_dt of this OrmNotificationConfig.  # noqa: E501


        :return: The created_dt of this OrmNotificationConfig.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this OrmNotificationConfig.


        :param created_dt: The created_dt of this OrmNotificationConfig.  # noqa: E501
        :type created_dt: datetime
        """

        self._created_dt = created_dt

    @property
    def edges(self):
        """Gets the edges of this OrmNotificationConfig.  # noqa: E501


        :return: The edges of this OrmNotificationConfig.  # noqa: E501
        :rtype: OrmNotificationConfigEdges
        """
        return self._edges

    @edges.setter
    def edges(self, edges):
        """Sets the edges of this OrmNotificationConfig.


        :param edges: The edges of this OrmNotificationConfig.  # noqa: E501
        :type edges: OrmNotificationConfigEdges
        """

        self._edges = edges

    @property
    def id(self):
        """Gets the id of this OrmNotificationConfig.  # noqa: E501


        :return: The id of this OrmNotificationConfig.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrmNotificationConfig.


        :param id: The id of this OrmNotificationConfig.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def immutable_slug(self):
        """Gets the immutable_slug of this OrmNotificationConfig.  # noqa: E501


        :return: The immutable_slug of this OrmNotificationConfig.  # noqa: E501
        :rtype: str
        """
        return self._immutable_slug

    @immutable_slug.setter
    def immutable_slug(self, immutable_slug):
        """Sets the immutable_slug of this OrmNotificationConfig.


        :param immutable_slug: The immutable_slug of this OrmNotificationConfig.  # noqa: E501
        :type immutable_slug: str
        """

        self._immutable_slug = immutable_slug

    @property
    def notification_config_organization(self):
        """Gets the notification_config_organization of this OrmNotificationConfig.  # noqa: E501


        :return: The notification_config_organization of this OrmNotificationConfig.  # noqa: E501
        :rtype: int
        """
        return self._notification_config_organization

    @notification_config_organization.setter
    def notification_config_organization(self, notification_config_organization):
        """Sets the notification_config_organization of this OrmNotificationConfig.


        :param notification_config_organization: The notification_config_organization of this OrmNotificationConfig.  # noqa: E501
        :type notification_config_organization: int
        """

        self._notification_config_organization = notification_config_organization

    @property
    def notification_config_project(self):
        """Gets the notification_config_project of this OrmNotificationConfig.  # noqa: E501


        :return: The notification_config_project of this OrmNotificationConfig.  # noqa: E501
        :rtype: int
        """
        return self._notification_config_project

    @notification_config_project.setter
    def notification_config_project(self, notification_config_project):
        """Sets the notification_config_project of this OrmNotificationConfig.


        :param notification_config_project: The notification_config_project of this OrmNotificationConfig.  # noqa: E501
        :type notification_config_project: int
        """

        self._notification_config_project = notification_config_project

    @property
    def slack_team_name(self):
        """Gets the slack_team_name of this OrmNotificationConfig.  # noqa: E501


        :return: The slack_team_name of this OrmNotificationConfig.  # noqa: E501
        :rtype: str
        """
        return self._slack_team_name

    @slack_team_name.setter
    def slack_team_name(self, slack_team_name):
        """Sets the slack_team_name of this OrmNotificationConfig.


        :param slack_team_name: The slack_team_name of this OrmNotificationConfig.  # noqa: E501
        :type slack_team_name: str
        """

        self._slack_team_name = slack_team_name

    @property
    def updated_dt(self):
        """Gets the updated_dt of this OrmNotificationConfig.  # noqa: E501


        :return: The updated_dt of this OrmNotificationConfig.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this OrmNotificationConfig.


        :param updated_dt: The updated_dt of this OrmNotificationConfig.  # noqa: E501
        :type updated_dt: datetime
        """

        self._updated_dt = updated_dt

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
        if not isinstance(other, OrmNotificationConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrmNotificationConfig):
            return True

        return self.to_dict() != other.to_dict()
