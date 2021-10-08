# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = ['WorkspaceConnectionArgs', 'WorkspaceConnection']

@pulumi.input_type
class WorkspaceConnectionArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 workspace_name: pulumi.Input[str],
                 auth_type: Optional[pulumi.Input[str]] = None,
                 category: Optional[pulumi.Input[str]] = None,
                 connection_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 target: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 value_format: Optional[pulumi.Input[Union[str, 'ValueFormat']]] = None):
        """
        The set of arguments for constructing a WorkspaceConnection resource.
        :param pulumi.Input[str] resource_group_name: Name of the resource group in which workspace is located.
        :param pulumi.Input[str] workspace_name: Name of Azure Machine Learning workspace.
        :param pulumi.Input[str] auth_type: Authorization type of the workspace connection.
        :param pulumi.Input[str] category: Category of the workspace connection.
        :param pulumi.Input[str] connection_name: Friendly name of the workspace connection
        :param pulumi.Input[str] name: Friendly name of the workspace connection
        :param pulumi.Input[str] target: Target of the workspace connection.
        :param pulumi.Input[str] value: Value details of the workspace connection.
        :param pulumi.Input[Union[str, 'ValueFormat']] value_format: format for the workspace connection value
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if auth_type is not None:
            pulumi.set(__self__, "auth_type", auth_type)
        if category is not None:
            pulumi.set(__self__, "category", category)
        if connection_name is not None:
            pulumi.set(__self__, "connection_name", connection_name)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if target is not None:
            pulumi.set(__self__, "target", target)
        if value is not None:
            pulumi.set(__self__, "value", value)
        if value_format is not None:
            pulumi.set(__self__, "value_format", value_format)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the resource group in which workspace is located.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[str]:
        """
        Name of Azure Machine Learning workspace.
        """
        return pulumi.get(self, "workspace_name")

    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_name", value)

    @property
    @pulumi.getter(name="authType")
    def auth_type(self) -> Optional[pulumi.Input[str]]:
        """
        Authorization type of the workspace connection.
        """
        return pulumi.get(self, "auth_type")

    @auth_type.setter
    def auth_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "auth_type", value)

    @property
    @pulumi.getter
    def category(self) -> Optional[pulumi.Input[str]]:
        """
        Category of the workspace connection.
        """
        return pulumi.get(self, "category")

    @category.setter
    def category(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "category", value)

    @property
    @pulumi.getter(name="connectionName")
    def connection_name(self) -> Optional[pulumi.Input[str]]:
        """
        Friendly name of the workspace connection
        """
        return pulumi.get(self, "connection_name")

    @connection_name.setter
    def connection_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connection_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Friendly name of the workspace connection
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[str]]:
        """
        Target of the workspace connection.
        """
        return pulumi.get(self, "target")

    @target.setter
    def target(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        """
        Value details of the workspace connection.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)

    @property
    @pulumi.getter(name="valueFormat")
    def value_format(self) -> Optional[pulumi.Input[Union[str, 'ValueFormat']]]:
        """
        format for the workspace connection value
        """
        return pulumi.get(self, "value_format")

    @value_format.setter
    def value_format(self, value: Optional[pulumi.Input[Union[str, 'ValueFormat']]]):
        pulumi.set(self, "value_format", value)


class WorkspaceConnection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auth_type: Optional[pulumi.Input[str]] = None,
                 category: Optional[pulumi.Input[str]] = None,
                 connection_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 target: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 value_format: Optional[pulumi.Input[Union[str, 'ValueFormat']]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Workspace connection.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] auth_type: Authorization type of the workspace connection.
        :param pulumi.Input[str] category: Category of the workspace connection.
        :param pulumi.Input[str] connection_name: Friendly name of the workspace connection
        :param pulumi.Input[str] name: Friendly name of the workspace connection
        :param pulumi.Input[str] resource_group_name: Name of the resource group in which workspace is located.
        :param pulumi.Input[str] target: Target of the workspace connection.
        :param pulumi.Input[str] value: Value details of the workspace connection.
        :param pulumi.Input[Union[str, 'ValueFormat']] value_format: format for the workspace connection value
        :param pulumi.Input[str] workspace_name: Name of Azure Machine Learning workspace.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WorkspaceConnectionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Workspace connection.

        :param str resource_name: The name of the resource.
        :param WorkspaceConnectionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WorkspaceConnectionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auth_type: Optional[pulumi.Input[str]] = None,
                 category: Optional[pulumi.Input[str]] = None,
                 connection_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 target: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 value_format: Optional[pulumi.Input[Union[str, 'ValueFormat']]] = None,
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
            __props__ = WorkspaceConnectionArgs.__new__(WorkspaceConnectionArgs)

            __props__.__dict__["auth_type"] = auth_type
            __props__.__dict__["category"] = category
            __props__.__dict__["connection_name"] = connection_name
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["target"] = target
            __props__.__dict__["value"] = value
            __props__.__dict__["value_format"] = value_format
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:machinelearningservices/v20210401:WorkspaceConnection"), pulumi.Alias(type_="azure-native:machinelearningservices:WorkspaceConnection"), pulumi.Alias(type_="azure-nextgen:machinelearningservices:WorkspaceConnection"), pulumi.Alias(type_="azure-native:machinelearningservices/v20200601:WorkspaceConnection"), pulumi.Alias(type_="azure-nextgen:machinelearningservices/v20200601:WorkspaceConnection"), pulumi.Alias(type_="azure-native:machinelearningservices/v20200801:WorkspaceConnection"), pulumi.Alias(type_="azure-nextgen:machinelearningservices/v20200801:WorkspaceConnection"), pulumi.Alias(type_="azure-native:machinelearningservices/v20200901preview:WorkspaceConnection"), pulumi.Alias(type_="azure-nextgen:machinelearningservices/v20200901preview:WorkspaceConnection"), pulumi.Alias(type_="azure-native:machinelearningservices/v20210101:WorkspaceConnection"), pulumi.Alias(type_="azure-nextgen:machinelearningservices/v20210101:WorkspaceConnection"), pulumi.Alias(type_="azure-native:machinelearningservices/v20210301preview:WorkspaceConnection"), pulumi.Alias(type_="azure-nextgen:machinelearningservices/v20210301preview:WorkspaceConnection"), pulumi.Alias(type_="azure-native:machinelearningservices/v20210701:WorkspaceConnection"), pulumi.Alias(type_="azure-nextgen:machinelearningservices/v20210701:WorkspaceConnection")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(WorkspaceConnection, __self__).__init__(
            'azure-native:machinelearningservices/v20210401:WorkspaceConnection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'WorkspaceConnection':
        """
        Get an existing WorkspaceConnection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WorkspaceConnectionArgs.__new__(WorkspaceConnectionArgs)

        __props__.__dict__["auth_type"] = None
        __props__.__dict__["category"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["target"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["value"] = None
        __props__.__dict__["value_format"] = None
        return WorkspaceConnection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="authType")
    def auth_type(self) -> pulumi.Output[Optional[str]]:
        """
        Authorization type of the workspace connection.
        """
        return pulumi.get(self, "auth_type")

    @property
    @pulumi.getter
    def category(self) -> pulumi.Output[Optional[str]]:
        """
        Category of the workspace connection.
        """
        return pulumi.get(self, "category")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Friendly name of the workspace connection.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def target(self) -> pulumi.Output[Optional[str]]:
        """
        Target of the workspace connection.
        """
        return pulumi.get(self, "target")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type of workspace connection.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def value(self) -> pulumi.Output[Optional[str]]:
        """
        Value details of the workspace connection.
        """
        return pulumi.get(self, "value")

    @property
    @pulumi.getter(name="valueFormat")
    def value_format(self) -> pulumi.Output[Optional[str]]:
        """
        format for the workspace connection value
        """
        return pulumi.get(self, "value_format")

