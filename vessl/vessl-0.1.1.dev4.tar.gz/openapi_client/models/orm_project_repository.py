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


class OrmProjectRepository(object):
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
        'cached_git_default_branch': 'str',
        'cached_git_http_url_to_repo': 'str',
        'cached_git_owner_slug': 'str',
        'cached_git_repo_slug': 'str',
        'cached_git_ssh_url_to_repo': 'str',
        'created_dt': 'datetime',
        'edges': 'OrmProjectRepositoryEdges',
        'git_provider': 'str',
        'id': 'int',
        'immutable_slug': 'str',
        'project_repository_organization_credentials': 'int',
        'project_repository_project': 'int',
        'updated_dt': 'datetime'
    }

    attribute_map = {
        'cached_git_default_branch': 'cached_git_default_branch',
        'cached_git_http_url_to_repo': 'cached_git_http_url_to_repo',
        'cached_git_owner_slug': 'cached_git_owner_slug',
        'cached_git_repo_slug': 'cached_git_repo_slug',
        'cached_git_ssh_url_to_repo': 'cached_git_ssh_url_to_repo',
        'created_dt': 'created_dt',
        'edges': 'edges',
        'git_provider': 'git_provider',
        'id': 'id',
        'immutable_slug': 'immutable_slug',
        'project_repository_organization_credentials': 'project_repository_organization_credentials',
        'project_repository_project': 'project_repository_project',
        'updated_dt': 'updated_dt'
    }

    def __init__(self, cached_git_default_branch=None, cached_git_http_url_to_repo=None, cached_git_owner_slug=None, cached_git_repo_slug=None, cached_git_ssh_url_to_repo=None, created_dt=None, edges=None, git_provider=None, id=None, immutable_slug=None, project_repository_organization_credentials=None, project_repository_project=None, updated_dt=None, local_vars_configuration=None):  # noqa: E501
        """OrmProjectRepository - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._cached_git_default_branch = None
        self._cached_git_http_url_to_repo = None
        self._cached_git_owner_slug = None
        self._cached_git_repo_slug = None
        self._cached_git_ssh_url_to_repo = None
        self._created_dt = None
        self._edges = None
        self._git_provider = None
        self._id = None
        self._immutable_slug = None
        self._project_repository_organization_credentials = None
        self._project_repository_project = None
        self._updated_dt = None
        self.discriminator = None

        if cached_git_default_branch is not None:
            self.cached_git_default_branch = cached_git_default_branch
        self.cached_git_http_url_to_repo = cached_git_http_url_to_repo
        if cached_git_owner_slug is not None:
            self.cached_git_owner_slug = cached_git_owner_slug
        if cached_git_repo_slug is not None:
            self.cached_git_repo_slug = cached_git_repo_slug
        self.cached_git_ssh_url_to_repo = cached_git_ssh_url_to_repo
        if created_dt is not None:
            self.created_dt = created_dt
        if edges is not None:
            self.edges = edges
        if git_provider is not None:
            self.git_provider = git_provider
        if id is not None:
            self.id = id
        if immutable_slug is not None:
            self.immutable_slug = immutable_slug
        if project_repository_organization_credentials is not None:
            self.project_repository_organization_credentials = project_repository_organization_credentials
        if project_repository_project is not None:
            self.project_repository_project = project_repository_project
        if updated_dt is not None:
            self.updated_dt = updated_dt

    @property
    def cached_git_default_branch(self):
        """Gets the cached_git_default_branch of this OrmProjectRepository.  # noqa: E501


        :return: The cached_git_default_branch of this OrmProjectRepository.  # noqa: E501
        :rtype: str
        """
        return self._cached_git_default_branch

    @cached_git_default_branch.setter
    def cached_git_default_branch(self, cached_git_default_branch):
        """Sets the cached_git_default_branch of this OrmProjectRepository.


        :param cached_git_default_branch: The cached_git_default_branch of this OrmProjectRepository.  # noqa: E501
        :type cached_git_default_branch: str
        """

        self._cached_git_default_branch = cached_git_default_branch

    @property
    def cached_git_http_url_to_repo(self):
        """Gets the cached_git_http_url_to_repo of this OrmProjectRepository.  # noqa: E501


        :return: The cached_git_http_url_to_repo of this OrmProjectRepository.  # noqa: E501
        :rtype: str
        """
        return self._cached_git_http_url_to_repo

    @cached_git_http_url_to_repo.setter
    def cached_git_http_url_to_repo(self, cached_git_http_url_to_repo):
        """Sets the cached_git_http_url_to_repo of this OrmProjectRepository.


        :param cached_git_http_url_to_repo: The cached_git_http_url_to_repo of this OrmProjectRepository.  # noqa: E501
        :type cached_git_http_url_to_repo: str
        """

        self._cached_git_http_url_to_repo = cached_git_http_url_to_repo

    @property
    def cached_git_owner_slug(self):
        """Gets the cached_git_owner_slug of this OrmProjectRepository.  # noqa: E501


        :return: The cached_git_owner_slug of this OrmProjectRepository.  # noqa: E501
        :rtype: str
        """
        return self._cached_git_owner_slug

    @cached_git_owner_slug.setter
    def cached_git_owner_slug(self, cached_git_owner_slug):
        """Sets the cached_git_owner_slug of this OrmProjectRepository.


        :param cached_git_owner_slug: The cached_git_owner_slug of this OrmProjectRepository.  # noqa: E501
        :type cached_git_owner_slug: str
        """

        self._cached_git_owner_slug = cached_git_owner_slug

    @property
    def cached_git_repo_slug(self):
        """Gets the cached_git_repo_slug of this OrmProjectRepository.  # noqa: E501


        :return: The cached_git_repo_slug of this OrmProjectRepository.  # noqa: E501
        :rtype: str
        """
        return self._cached_git_repo_slug

    @cached_git_repo_slug.setter
    def cached_git_repo_slug(self, cached_git_repo_slug):
        """Sets the cached_git_repo_slug of this OrmProjectRepository.


        :param cached_git_repo_slug: The cached_git_repo_slug of this OrmProjectRepository.  # noqa: E501
        :type cached_git_repo_slug: str
        """

        self._cached_git_repo_slug = cached_git_repo_slug

    @property
    def cached_git_ssh_url_to_repo(self):
        """Gets the cached_git_ssh_url_to_repo of this OrmProjectRepository.  # noqa: E501


        :return: The cached_git_ssh_url_to_repo of this OrmProjectRepository.  # noqa: E501
        :rtype: str
        """
        return self._cached_git_ssh_url_to_repo

    @cached_git_ssh_url_to_repo.setter
    def cached_git_ssh_url_to_repo(self, cached_git_ssh_url_to_repo):
        """Sets the cached_git_ssh_url_to_repo of this OrmProjectRepository.


        :param cached_git_ssh_url_to_repo: The cached_git_ssh_url_to_repo of this OrmProjectRepository.  # noqa: E501
        :type cached_git_ssh_url_to_repo: str
        """

        self._cached_git_ssh_url_to_repo = cached_git_ssh_url_to_repo

    @property
    def created_dt(self):
        """Gets the created_dt of this OrmProjectRepository.  # noqa: E501


        :return: The created_dt of this OrmProjectRepository.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this OrmProjectRepository.


        :param created_dt: The created_dt of this OrmProjectRepository.  # noqa: E501
        :type created_dt: datetime
        """

        self._created_dt = created_dt

    @property
    def edges(self):
        """Gets the edges of this OrmProjectRepository.  # noqa: E501


        :return: The edges of this OrmProjectRepository.  # noqa: E501
        :rtype: OrmProjectRepositoryEdges
        """
        return self._edges

    @edges.setter
    def edges(self, edges):
        """Sets the edges of this OrmProjectRepository.


        :param edges: The edges of this OrmProjectRepository.  # noqa: E501
        :type edges: OrmProjectRepositoryEdges
        """

        self._edges = edges

    @property
    def git_provider(self):
        """Gets the git_provider of this OrmProjectRepository.  # noqa: E501


        :return: The git_provider of this OrmProjectRepository.  # noqa: E501
        :rtype: str
        """
        return self._git_provider

    @git_provider.setter
    def git_provider(self, git_provider):
        """Sets the git_provider of this OrmProjectRepository.


        :param git_provider: The git_provider of this OrmProjectRepository.  # noqa: E501
        :type git_provider: str
        """

        self._git_provider = git_provider

    @property
    def id(self):
        """Gets the id of this OrmProjectRepository.  # noqa: E501


        :return: The id of this OrmProjectRepository.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrmProjectRepository.


        :param id: The id of this OrmProjectRepository.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def immutable_slug(self):
        """Gets the immutable_slug of this OrmProjectRepository.  # noqa: E501


        :return: The immutable_slug of this OrmProjectRepository.  # noqa: E501
        :rtype: str
        """
        return self._immutable_slug

    @immutable_slug.setter
    def immutable_slug(self, immutable_slug):
        """Sets the immutable_slug of this OrmProjectRepository.


        :param immutable_slug: The immutable_slug of this OrmProjectRepository.  # noqa: E501
        :type immutable_slug: str
        """

        self._immutable_slug = immutable_slug

    @property
    def project_repository_organization_credentials(self):
        """Gets the project_repository_organization_credentials of this OrmProjectRepository.  # noqa: E501


        :return: The project_repository_organization_credentials of this OrmProjectRepository.  # noqa: E501
        :rtype: int
        """
        return self._project_repository_organization_credentials

    @project_repository_organization_credentials.setter
    def project_repository_organization_credentials(self, project_repository_organization_credentials):
        """Sets the project_repository_organization_credentials of this OrmProjectRepository.


        :param project_repository_organization_credentials: The project_repository_organization_credentials of this OrmProjectRepository.  # noqa: E501
        :type project_repository_organization_credentials: int
        """

        self._project_repository_organization_credentials = project_repository_organization_credentials

    @property
    def project_repository_project(self):
        """Gets the project_repository_project of this OrmProjectRepository.  # noqa: E501


        :return: The project_repository_project of this OrmProjectRepository.  # noqa: E501
        :rtype: int
        """
        return self._project_repository_project

    @project_repository_project.setter
    def project_repository_project(self, project_repository_project):
        """Sets the project_repository_project of this OrmProjectRepository.


        :param project_repository_project: The project_repository_project of this OrmProjectRepository.  # noqa: E501
        :type project_repository_project: int
        """

        self._project_repository_project = project_repository_project

    @property
    def updated_dt(self):
        """Gets the updated_dt of this OrmProjectRepository.  # noqa: E501


        :return: The updated_dt of this OrmProjectRepository.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this OrmProjectRepository.


        :param updated_dt: The updated_dt of this OrmProjectRepository.  # noqa: E501
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
        if not isinstance(other, OrmProjectRepository):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrmProjectRepository):
            return True

        return self.to_dict() != other.to_dict()
