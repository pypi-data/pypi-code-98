# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._enums import *

__all__ = ['KustoPoolDatabasePrincipalAssignmentArgs', 'KustoPoolDatabasePrincipalAssignment']

@pulumi.input_type
class KustoPoolDatabasePrincipalAssignmentArgs:
    def __init__(__self__, *,
                 database_name: pulumi.Input[str],
                 kusto_pool_name: pulumi.Input[str],
                 principal_id: pulumi.Input[str],
                 principal_type: pulumi.Input[Union[str, 'PrincipalType']],
                 resource_group_name: pulumi.Input[str],
                 role: pulumi.Input[Union[str, 'DatabasePrincipalRole']],
                 workspace_name: pulumi.Input[str],
                 principal_assignment_name: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a KustoPoolDatabasePrincipalAssignment resource.
        :param pulumi.Input[str] database_name: The name of the database in the Kusto pool.
        :param pulumi.Input[str] kusto_pool_name: The name of the Kusto pool.
        :param pulumi.Input[str] principal_id: The principal ID assigned to the database principal. It can be a user email, application ID, or security group name.
        :param pulumi.Input[Union[str, 'PrincipalType']] principal_type: Principal type.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Union[str, 'DatabasePrincipalRole']] role: Database principal role.
        :param pulumi.Input[str] workspace_name: The name of the workspace
        :param pulumi.Input[str] principal_assignment_name: The name of the Kusto principalAssignment.
        :param pulumi.Input[str] tenant_id: The tenant id of the principal
        """
        pulumi.set(__self__, "database_name", database_name)
        pulumi.set(__self__, "kusto_pool_name", kusto_pool_name)
        pulumi.set(__self__, "principal_id", principal_id)
        pulumi.set(__self__, "principal_type", principal_type)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "role", role)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if principal_assignment_name is not None:
            pulumi.set(__self__, "principal_assignment_name", principal_assignment_name)
        if tenant_id is not None:
            pulumi.set(__self__, "tenant_id", tenant_id)

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[str]:
        """
        The name of the database in the Kusto pool.
        """
        return pulumi.get(self, "database_name")

    @database_name.setter
    def database_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "database_name", value)

    @property
    @pulumi.getter(name="kustoPoolName")
    def kusto_pool_name(self) -> pulumi.Input[str]:
        """
        The name of the Kusto pool.
        """
        return pulumi.get(self, "kusto_pool_name")

    @kusto_pool_name.setter
    def kusto_pool_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "kusto_pool_name", value)

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> pulumi.Input[str]:
        """
        The principal ID assigned to the database principal. It can be a user email, application ID, or security group name.
        """
        return pulumi.get(self, "principal_id")

    @principal_id.setter
    def principal_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "principal_id", value)

    @property
    @pulumi.getter(name="principalType")
    def principal_type(self) -> pulumi.Input[Union[str, 'PrincipalType']]:
        """
        Principal type.
        """
        return pulumi.get(self, "principal_type")

    @principal_type.setter
    def principal_type(self, value: pulumi.Input[Union[str, 'PrincipalType']]):
        pulumi.set(self, "principal_type", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def role(self) -> pulumi.Input[Union[str, 'DatabasePrincipalRole']]:
        """
        Database principal role.
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: pulumi.Input[Union[str, 'DatabasePrincipalRole']]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[str]:
        """
        The name of the workspace
        """
        return pulumi.get(self, "workspace_name")

    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_name", value)

    @property
    @pulumi.getter(name="principalAssignmentName")
    def principal_assignment_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Kusto principalAssignment.
        """
        return pulumi.get(self, "principal_assignment_name")

    @principal_assignment_name.setter
    def principal_assignment_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "principal_assignment_name", value)

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[str]]:
        """
        The tenant id of the principal
        """
        return pulumi.get(self, "tenant_id")

    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tenant_id", value)


class KustoPoolDatabasePrincipalAssignment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 kusto_pool_name: Optional[pulumi.Input[str]] = None,
                 principal_assignment_name: Optional[pulumi.Input[str]] = None,
                 principal_id: Optional[pulumi.Input[str]] = None,
                 principal_type: Optional[pulumi.Input[Union[str, 'PrincipalType']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[Union[str, 'DatabasePrincipalRole']]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Class representing a database principal assignment.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] database_name: The name of the database in the Kusto pool.
        :param pulumi.Input[str] kusto_pool_name: The name of the Kusto pool.
        :param pulumi.Input[str] principal_assignment_name: The name of the Kusto principalAssignment.
        :param pulumi.Input[str] principal_id: The principal ID assigned to the database principal. It can be a user email, application ID, or security group name.
        :param pulumi.Input[Union[str, 'PrincipalType']] principal_type: Principal type.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Union[str, 'DatabasePrincipalRole']] role: Database principal role.
        :param pulumi.Input[str] tenant_id: The tenant id of the principal
        :param pulumi.Input[str] workspace_name: The name of the workspace
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: KustoPoolDatabasePrincipalAssignmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Class representing a database principal assignment.

        :param str resource_name: The name of the resource.
        :param KustoPoolDatabasePrincipalAssignmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(KustoPoolDatabasePrincipalAssignmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 kusto_pool_name: Optional[pulumi.Input[str]] = None,
                 principal_assignment_name: Optional[pulumi.Input[str]] = None,
                 principal_id: Optional[pulumi.Input[str]] = None,
                 principal_type: Optional[pulumi.Input[Union[str, 'PrincipalType']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[Union[str, 'DatabasePrincipalRole']]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = KustoPoolDatabasePrincipalAssignmentArgs.__new__(KustoPoolDatabasePrincipalAssignmentArgs)

            if database_name is None and not opts.urn:
                raise TypeError("Missing required property 'database_name'")
            __props__.__dict__["database_name"] = database_name
            if kusto_pool_name is None and not opts.urn:
                raise TypeError("Missing required property 'kusto_pool_name'")
            __props__.__dict__["kusto_pool_name"] = kusto_pool_name
            __props__.__dict__["principal_assignment_name"] = principal_assignment_name
            if principal_id is None and not opts.urn:
                raise TypeError("Missing required property 'principal_id'")
            __props__.__dict__["principal_id"] = principal_id
            if principal_type is None and not opts.urn:
                raise TypeError("Missing required property 'principal_type'")
            __props__.__dict__["principal_type"] = principal_type
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if role is None and not opts.urn:
                raise TypeError("Missing required property 'role'")
            __props__.__dict__["role"] = role
            __props__.__dict__["tenant_id"] = tenant_id
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["name"] = None
            __props__.__dict__["principal_name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["tenant_name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:synapse/v20210601preview:KustoPoolDatabasePrincipalAssignment"), pulumi.Alias(type_="azure-native:synapse:KustoPoolDatabasePrincipalAssignment"), pulumi.Alias(type_="azure-nextgen:synapse:KustoPoolDatabasePrincipalAssignment"), pulumi.Alias(type_="azure-native:synapse/v20210401preview:KustoPoolDatabasePrincipalAssignment"), pulumi.Alias(type_="azure-nextgen:synapse/v20210401preview:KustoPoolDatabasePrincipalAssignment")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(KustoPoolDatabasePrincipalAssignment, __self__).__init__(
            'azure-native:synapse/v20210601preview:KustoPoolDatabasePrincipalAssignment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'KustoPoolDatabasePrincipalAssignment':
        """
        Get an existing KustoPoolDatabasePrincipalAssignment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = KustoPoolDatabasePrincipalAssignmentArgs.__new__(KustoPoolDatabasePrincipalAssignmentArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["principal_id"] = None
        __props__.__dict__["principal_name"] = None
        __props__.__dict__["principal_type"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["role"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tenant_id"] = None
        __props__.__dict__["tenant_name"] = None
        __props__.__dict__["type"] = None
        return KustoPoolDatabasePrincipalAssignment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> pulumi.Output[str]:
        """
        The principal ID assigned to the database principal. It can be a user email, application ID, or security group name.
        """
        return pulumi.get(self, "principal_id")

    @property
    @pulumi.getter(name="principalName")
    def principal_name(self) -> pulumi.Output[str]:
        """
        The principal name
        """
        return pulumi.get(self, "principal_name")

    @property
    @pulumi.getter(name="principalType")
    def principal_type(self) -> pulumi.Output[str]:
        """
        Principal type.
        """
        return pulumi.get(self, "principal_type")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioned state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def role(self) -> pulumi.Output[str]:
        """
        Database principal role.
        """
        return pulumi.get(self, "role")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[Optional[str]]:
        """
        The tenant id of the principal
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter(name="tenantName")
    def tenant_name(self) -> pulumi.Output[str]:
        """
        The tenant name of the principal
        """
        return pulumi.get(self, "tenant_name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

