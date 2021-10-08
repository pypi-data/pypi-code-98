# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = ['DomainTopicArgs', 'DomainTopic']

@pulumi.input_type
class DomainTopicArgs:
    def __init__(__self__, *,
                 domain_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 domain_topic_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DomainTopic resource.
        :param pulumi.Input[str] domain_name: Name of the domain.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription.
        :param pulumi.Input[str] domain_topic_name: Name of the domain topic.
        """
        pulumi.set(__self__, "domain_name", domain_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if domain_topic_name is not None:
            pulumi.set(__self__, "domain_topic_name", domain_topic_name)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[str]:
        """
        Name of the domain.
        """
        return pulumi.get(self, "domain_name")

    @domain_name.setter
    def domain_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group within the user's subscription.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="domainTopicName")
    def domain_topic_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the domain topic.
        """
        return pulumi.get(self, "domain_topic_name")

    @domain_topic_name.setter
    def domain_topic_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain_topic_name", value)


class DomainTopic(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 domain_topic_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Domain Topic.
        API Version: 2020-06-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] domain_name: Name of the domain.
        :param pulumi.Input[str] domain_topic_name: Name of the domain topic.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DomainTopicArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Domain Topic.
        API Version: 2020-06-01.

        :param str resource_name: The name of the resource.
        :param DomainTopicArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DomainTopicArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 domain_topic_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = DomainTopicArgs.__new__(DomainTopicArgs)

            if domain_name is None and not opts.urn:
                raise TypeError("Missing required property 'domain_name'")
            __props__.__dict__["domain_name"] = domain_name
            __props__.__dict__["domain_topic_name"] = domain_topic_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:eventgrid:DomainTopic"), pulumi.Alias(type_="azure-native:eventgrid/v20190201preview:DomainTopic"), pulumi.Alias(type_="azure-nextgen:eventgrid/v20190201preview:DomainTopic"), pulumi.Alias(type_="azure-native:eventgrid/v20190601:DomainTopic"), pulumi.Alias(type_="azure-nextgen:eventgrid/v20190601:DomainTopic"), pulumi.Alias(type_="azure-native:eventgrid/v20200101preview:DomainTopic"), pulumi.Alias(type_="azure-nextgen:eventgrid/v20200101preview:DomainTopic"), pulumi.Alias(type_="azure-native:eventgrid/v20200401preview:DomainTopic"), pulumi.Alias(type_="azure-nextgen:eventgrid/v20200401preview:DomainTopic"), pulumi.Alias(type_="azure-native:eventgrid/v20200601:DomainTopic"), pulumi.Alias(type_="azure-nextgen:eventgrid/v20200601:DomainTopic"), pulumi.Alias(type_="azure-native:eventgrid/v20201015preview:DomainTopic"), pulumi.Alias(type_="azure-nextgen:eventgrid/v20201015preview:DomainTopic"), pulumi.Alias(type_="azure-native:eventgrid/v20210601preview:DomainTopic"), pulumi.Alias(type_="azure-nextgen:eventgrid/v20210601preview:DomainTopic")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(DomainTopic, __self__).__init__(
            'azure-native:eventgrid:DomainTopic',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DomainTopic':
        """
        Get an existing DomainTopic resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DomainTopicArgs.__new__(DomainTopicArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return DomainTopic(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state of the domain topic.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        The system metadata relating to Domain Topic resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Type of the resource.
        """
        return pulumi.get(self, "type")

