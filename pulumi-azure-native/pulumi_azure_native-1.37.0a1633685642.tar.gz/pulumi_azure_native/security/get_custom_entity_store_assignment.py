# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetCustomEntityStoreAssignmentResult',
    'AwaitableGetCustomEntityStoreAssignmentResult',
    'get_custom_entity_store_assignment',
    'get_custom_entity_store_assignment_output',
]

@pulumi.output_type
class GetCustomEntityStoreAssignmentResult:
    """
    Custom entity store assignment
    """
    def __init__(__self__, entity_store_database_link=None, id=None, name=None, principal=None, type=None):
        if entity_store_database_link and not isinstance(entity_store_database_link, str):
            raise TypeError("Expected argument 'entity_store_database_link' to be a str")
        pulumi.set(__self__, "entity_store_database_link", entity_store_database_link)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if principal and not isinstance(principal, str):
            raise TypeError("Expected argument 'principal' to be a str")
        pulumi.set(__self__, "principal", principal)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="entityStoreDatabaseLink")
    def entity_store_database_link(self) -> Optional[str]:
        """
        The link to entity store database.
        """
        return pulumi.get(self, "entity_store_database_link")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def principal(self) -> Optional[str]:
        """
        The principal assigned with entity store. Format of principal is: [AAD type]=[PrincipalObjectId];[TenantId]
        """
        return pulumi.get(self, "principal")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type
        """
        return pulumi.get(self, "type")


class AwaitableGetCustomEntityStoreAssignmentResult(GetCustomEntityStoreAssignmentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCustomEntityStoreAssignmentResult(
            entity_store_database_link=self.entity_store_database_link,
            id=self.id,
            name=self.name,
            principal=self.principal,
            type=self.type)


def get_custom_entity_store_assignment(custom_entity_store_assignment_name: Optional[str] = None,
                                       resource_group_name: Optional[str] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCustomEntityStoreAssignmentResult:
    """
    Custom entity store assignment
    API Version: 2021-07-01-preview.


    :param str custom_entity_store_assignment_name: Name of the custom entity store assignment. Generated name is GUID.
    :param str resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
    """
    __args__ = dict()
    __args__['customEntityStoreAssignmentName'] = custom_entity_store_assignment_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:security:getCustomEntityStoreAssignment', __args__, opts=opts, typ=GetCustomEntityStoreAssignmentResult).value

    return AwaitableGetCustomEntityStoreAssignmentResult(
        entity_store_database_link=__ret__.entity_store_database_link,
        id=__ret__.id,
        name=__ret__.name,
        principal=__ret__.principal,
        type=__ret__.type)


@_utilities.lift_output_func(get_custom_entity_store_assignment)
def get_custom_entity_store_assignment_output(custom_entity_store_assignment_name: Optional[pulumi.Input[str]] = None,
                                              resource_group_name: Optional[pulumi.Input[str]] = None,
                                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCustomEntityStoreAssignmentResult]:
    """
    Custom entity store assignment
    API Version: 2021-07-01-preview.


    :param str custom_entity_store_assignment_name: Name of the custom entity store assignment. Generated name is GUID.
    :param str resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
    """
    ...
