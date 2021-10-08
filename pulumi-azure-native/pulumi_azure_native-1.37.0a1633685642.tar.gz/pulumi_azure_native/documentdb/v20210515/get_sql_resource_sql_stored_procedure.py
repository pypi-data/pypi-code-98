# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'GetSqlResourceSqlStoredProcedureResult',
    'AwaitableGetSqlResourceSqlStoredProcedureResult',
    'get_sql_resource_sql_stored_procedure',
    'get_sql_resource_sql_stored_procedure_output',
]

@pulumi.output_type
class GetSqlResourceSqlStoredProcedureResult:
    """
    An Azure Cosmos DB storedProcedure.
    """
    def __init__(__self__, id=None, location=None, name=None, resource=None, tags=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if resource and not isinstance(resource, dict):
            raise TypeError("Expected argument 'resource' to be a dict")
        pulumi.set(__self__, "resource", resource)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The unique resource identifier of the ARM resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        The location of the resource group to which the resource belongs.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the ARM resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def resource(self) -> Optional['outputs.SqlStoredProcedureGetPropertiesResponseResource']:
        return pulumi.get(self, "resource")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB".
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of Azure resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetSqlResourceSqlStoredProcedureResult(GetSqlResourceSqlStoredProcedureResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSqlResourceSqlStoredProcedureResult(
            id=self.id,
            location=self.location,
            name=self.name,
            resource=self.resource,
            tags=self.tags,
            type=self.type)


def get_sql_resource_sql_stored_procedure(account_name: Optional[str] = None,
                                          container_name: Optional[str] = None,
                                          database_name: Optional[str] = None,
                                          resource_group_name: Optional[str] = None,
                                          stored_procedure_name: Optional[str] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSqlResourceSqlStoredProcedureResult:
    """
    An Azure Cosmos DB storedProcedure.


    :param str account_name: Cosmos DB database account name.
    :param str container_name: Cosmos DB container name.
    :param str database_name: Cosmos DB database name.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str stored_procedure_name: Cosmos DB storedProcedure name.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['containerName'] = container_name
    __args__['databaseName'] = database_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['storedProcedureName'] = stored_procedure_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:documentdb/v20210515:getSqlResourceSqlStoredProcedure', __args__, opts=opts, typ=GetSqlResourceSqlStoredProcedureResult).value

    return AwaitableGetSqlResourceSqlStoredProcedureResult(
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        resource=__ret__.resource,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_sql_resource_sql_stored_procedure)
def get_sql_resource_sql_stored_procedure_output(account_name: Optional[pulumi.Input[str]] = None,
                                                 container_name: Optional[pulumi.Input[str]] = None,
                                                 database_name: Optional[pulumi.Input[str]] = None,
                                                 resource_group_name: Optional[pulumi.Input[str]] = None,
                                                 stored_procedure_name: Optional[pulumi.Input[str]] = None,
                                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSqlResourceSqlStoredProcedureResult]:
    """
    An Azure Cosmos DB storedProcedure.


    :param str account_name: Cosmos DB database account name.
    :param str container_name: Cosmos DB container name.
    :param str database_name: Cosmos DB database name.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str stored_procedure_name: Cosmos DB storedProcedure name.
    """
    ...
