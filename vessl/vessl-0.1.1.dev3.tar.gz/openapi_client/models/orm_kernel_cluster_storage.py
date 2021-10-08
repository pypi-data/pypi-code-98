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


class OrmKernelClusterStorage(object):
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
        'edges': 'OrmKernelClusterStorageEdges',
        'id': 'int',
        'immutable_slug': 'str',
        'kernel_cluster_storage_kernel_cluster': 'int',
        'kernel_cluster_storage_storage': 'int',
        'storage_config': 'dict(str, object)',
        'storage_type': 'str',
        'updated_dt': 'datetime'
    }

    attribute_map = {
        'created_dt': 'created_dt',
        'edges': 'edges',
        'id': 'id',
        'immutable_slug': 'immutable_slug',
        'kernel_cluster_storage_kernel_cluster': 'kernel_cluster_storage_kernel_cluster',
        'kernel_cluster_storage_storage': 'kernel_cluster_storage_storage',
        'storage_config': 'storage_config',
        'storage_type': 'storage_type',
        'updated_dt': 'updated_dt'
    }

    def __init__(self, created_dt=None, edges=None, id=None, immutable_slug=None, kernel_cluster_storage_kernel_cluster=None, kernel_cluster_storage_storage=None, storage_config=None, storage_type=None, updated_dt=None, local_vars_configuration=None):  # noqa: E501
        """OrmKernelClusterStorage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._created_dt = None
        self._edges = None
        self._id = None
        self._immutable_slug = None
        self._kernel_cluster_storage_kernel_cluster = None
        self._kernel_cluster_storage_storage = None
        self._storage_config = None
        self._storage_type = None
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
        if kernel_cluster_storage_kernel_cluster is not None:
            self.kernel_cluster_storage_kernel_cluster = kernel_cluster_storage_kernel_cluster
        if kernel_cluster_storage_storage is not None:
            self.kernel_cluster_storage_storage = kernel_cluster_storage_storage
        if storage_config is not None:
            self.storage_config = storage_config
        if storage_type is not None:
            self.storage_type = storage_type
        if updated_dt is not None:
            self.updated_dt = updated_dt

    @property
    def created_dt(self):
        """Gets the created_dt of this OrmKernelClusterStorage.  # noqa: E501


        :return: The created_dt of this OrmKernelClusterStorage.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this OrmKernelClusterStorage.


        :param created_dt: The created_dt of this OrmKernelClusterStorage.  # noqa: E501
        :type created_dt: datetime
        """

        self._created_dt = created_dt

    @property
    def edges(self):
        """Gets the edges of this OrmKernelClusterStorage.  # noqa: E501


        :return: The edges of this OrmKernelClusterStorage.  # noqa: E501
        :rtype: OrmKernelClusterStorageEdges
        """
        return self._edges

    @edges.setter
    def edges(self, edges):
        """Sets the edges of this OrmKernelClusterStorage.


        :param edges: The edges of this OrmKernelClusterStorage.  # noqa: E501
        :type edges: OrmKernelClusterStorageEdges
        """

        self._edges = edges

    @property
    def id(self):
        """Gets the id of this OrmKernelClusterStorage.  # noqa: E501


        :return: The id of this OrmKernelClusterStorage.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrmKernelClusterStorage.


        :param id: The id of this OrmKernelClusterStorage.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def immutable_slug(self):
        """Gets the immutable_slug of this OrmKernelClusterStorage.  # noqa: E501


        :return: The immutable_slug of this OrmKernelClusterStorage.  # noqa: E501
        :rtype: str
        """
        return self._immutable_slug

    @immutable_slug.setter
    def immutable_slug(self, immutable_slug):
        """Sets the immutable_slug of this OrmKernelClusterStorage.


        :param immutable_slug: The immutable_slug of this OrmKernelClusterStorage.  # noqa: E501
        :type immutable_slug: str
        """

        self._immutable_slug = immutable_slug

    @property
    def kernel_cluster_storage_kernel_cluster(self):
        """Gets the kernel_cluster_storage_kernel_cluster of this OrmKernelClusterStorage.  # noqa: E501


        :return: The kernel_cluster_storage_kernel_cluster of this OrmKernelClusterStorage.  # noqa: E501
        :rtype: int
        """
        return self._kernel_cluster_storage_kernel_cluster

    @kernel_cluster_storage_kernel_cluster.setter
    def kernel_cluster_storage_kernel_cluster(self, kernel_cluster_storage_kernel_cluster):
        """Sets the kernel_cluster_storage_kernel_cluster of this OrmKernelClusterStorage.


        :param kernel_cluster_storage_kernel_cluster: The kernel_cluster_storage_kernel_cluster of this OrmKernelClusterStorage.  # noqa: E501
        :type kernel_cluster_storage_kernel_cluster: int
        """

        self._kernel_cluster_storage_kernel_cluster = kernel_cluster_storage_kernel_cluster

    @property
    def kernel_cluster_storage_storage(self):
        """Gets the kernel_cluster_storage_storage of this OrmKernelClusterStorage.  # noqa: E501


        :return: The kernel_cluster_storage_storage of this OrmKernelClusterStorage.  # noqa: E501
        :rtype: int
        """
        return self._kernel_cluster_storage_storage

    @kernel_cluster_storage_storage.setter
    def kernel_cluster_storage_storage(self, kernel_cluster_storage_storage):
        """Sets the kernel_cluster_storage_storage of this OrmKernelClusterStorage.


        :param kernel_cluster_storage_storage: The kernel_cluster_storage_storage of this OrmKernelClusterStorage.  # noqa: E501
        :type kernel_cluster_storage_storage: int
        """

        self._kernel_cluster_storage_storage = kernel_cluster_storage_storage

    @property
    def storage_config(self):
        """Gets the storage_config of this OrmKernelClusterStorage.  # noqa: E501


        :return: The storage_config of this OrmKernelClusterStorage.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._storage_config

    @storage_config.setter
    def storage_config(self, storage_config):
        """Sets the storage_config of this OrmKernelClusterStorage.


        :param storage_config: The storage_config of this OrmKernelClusterStorage.  # noqa: E501
        :type storage_config: dict(str, object)
        """

        self._storage_config = storage_config

    @property
    def storage_type(self):
        """Gets the storage_type of this OrmKernelClusterStorage.  # noqa: E501


        :return: The storage_type of this OrmKernelClusterStorage.  # noqa: E501
        :rtype: str
        """
        return self._storage_type

    @storage_type.setter
    def storage_type(self, storage_type):
        """Sets the storage_type of this OrmKernelClusterStorage.


        :param storage_type: The storage_type of this OrmKernelClusterStorage.  # noqa: E501
        :type storage_type: str
        """

        self._storage_type = storage_type

    @property
    def updated_dt(self):
        """Gets the updated_dt of this OrmKernelClusterStorage.  # noqa: E501


        :return: The updated_dt of this OrmKernelClusterStorage.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this OrmKernelClusterStorage.


        :param updated_dt: The updated_dt of this OrmKernelClusterStorage.  # noqa: E501
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
        if not isinstance(other, OrmKernelClusterStorage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrmKernelClusterStorage):
            return True

        return self.to_dict() != other.to_dict()
