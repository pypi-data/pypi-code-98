# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['HubArgs', 'Hub']

@pulumi.input_type
class HubArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 hub_billing_info: Optional[pulumi.Input['HubBillingInfoFormatArgs']] = None,
                 hub_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tenant_features: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a Hub resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input['HubBillingInfoFormatArgs'] hub_billing_info: Billing settings of the hub.
        :param pulumi.Input[str] hub_name: The name of the Hub.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[int] tenant_features: The bit flags for enabled hub features. Bit 0 is set to 1 indicates graph is enabled, or disabled if set to 0. Bit 1 is set to 1 indicates the hub is disabled, or enabled if set to 0.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if hub_billing_info is not None:
            pulumi.set(__self__, "hub_billing_info", hub_billing_info)
        if hub_name is not None:
            pulumi.set(__self__, "hub_name", hub_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tenant_features is not None:
            pulumi.set(__self__, "tenant_features", tenant_features)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="hubBillingInfo")
    def hub_billing_info(self) -> Optional[pulumi.Input['HubBillingInfoFormatArgs']]:
        """
        Billing settings of the hub.
        """
        return pulumi.get(self, "hub_billing_info")

    @hub_billing_info.setter
    def hub_billing_info(self, value: Optional[pulumi.Input['HubBillingInfoFormatArgs']]):
        pulumi.set(self, "hub_billing_info", value)

    @property
    @pulumi.getter(name="hubName")
    def hub_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Hub.
        """
        return pulumi.get(self, "hub_name")

    @hub_name.setter
    def hub_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hub_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="tenantFeatures")
    def tenant_features(self) -> Optional[pulumi.Input[int]]:
        """
        The bit flags for enabled hub features. Bit 0 is set to 1 indicates graph is enabled, or disabled if set to 0. Bit 1 is set to 1 indicates the hub is disabled, or enabled if set to 0.
        """
        return pulumi.get(self, "tenant_features")

    @tenant_features.setter
    def tenant_features(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "tenant_features", value)


class Hub(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 hub_billing_info: Optional[pulumi.Input[pulumi.InputType['HubBillingInfoFormatArgs']]] = None,
                 hub_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tenant_features: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Hub resource.
        API Version: 2017-04-26.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['HubBillingInfoFormatArgs']] hub_billing_info: Billing settings of the hub.
        :param pulumi.Input[str] hub_name: The name of the Hub.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[int] tenant_features: The bit flags for enabled hub features. Bit 0 is set to 1 indicates graph is enabled, or disabled if set to 0. Bit 1 is set to 1 indicates the hub is disabled, or enabled if set to 0.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: HubArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Hub resource.
        API Version: 2017-04-26.

        :param str resource_name: The name of the resource.
        :param HubArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(HubArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 hub_billing_info: Optional[pulumi.Input[pulumi.InputType['HubBillingInfoFormatArgs']]] = None,
                 hub_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tenant_features: Optional[pulumi.Input[int]] = None,
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
            __props__ = HubArgs.__new__(HubArgs)

            __props__.__dict__["hub_billing_info"] = hub_billing_info
            __props__.__dict__["hub_name"] = hub_name
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["tenant_features"] = tenant_features
            __props__.__dict__["api_endpoint"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["web_endpoint"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:customerinsights:Hub"), pulumi.Alias(type_="azure-native:customerinsights/v20170101:Hub"), pulumi.Alias(type_="azure-nextgen:customerinsights/v20170101:Hub"), pulumi.Alias(type_="azure-native:customerinsights/v20170426:Hub"), pulumi.Alias(type_="azure-nextgen:customerinsights/v20170426:Hub")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Hub, __self__).__init__(
            'azure-native:customerinsights:Hub',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Hub':
        """
        Get an existing Hub resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = HubArgs.__new__(HubArgs)

        __props__.__dict__["api_endpoint"] = None
        __props__.__dict__["hub_billing_info"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["tenant_features"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["web_endpoint"] = None
        return Hub(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiEndpoint")
    def api_endpoint(self) -> pulumi.Output[str]:
        """
        API endpoint URL of the hub.
        """
        return pulumi.get(self, "api_endpoint")

    @property
    @pulumi.getter(name="hubBillingInfo")
    def hub_billing_info(self) -> pulumi.Output[Optional['outputs.HubBillingInfoFormatResponse']]:
        """
        Billing settings of the hub.
        """
        return pulumi.get(self, "hub_billing_info")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state of the hub.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tenantFeatures")
    def tenant_features(self) -> pulumi.Output[Optional[int]]:
        """
        The bit flags for enabled hub features. Bit 0 is set to 1 indicates graph is enabled, or disabled if set to 0. Bit 1 is set to 1 indicates the hub is disabled, or enabled if set to 0.
        """
        return pulumi.get(self, "tenant_features")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="webEndpoint")
    def web_endpoint(self) -> pulumi.Output[str]:
        """
        Web endpoint URL of the hub.
        """
        return pulumi.get(self, "web_endpoint")

