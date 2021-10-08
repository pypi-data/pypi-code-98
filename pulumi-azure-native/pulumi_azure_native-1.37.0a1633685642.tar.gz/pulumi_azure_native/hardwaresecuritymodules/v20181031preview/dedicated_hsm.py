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
from ._inputs import *

__all__ = ['DedicatedHsmArgs', 'DedicatedHsm']

@pulumi.input_type
class DedicatedHsmArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 sku: pulumi.Input['SkuArgs'],
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_profile: Optional[pulumi.Input['NetworkProfileArgs']] = None,
                 stamp_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a DedicatedHsm resource.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group to which the resource belongs.
        :param pulumi.Input['SkuArgs'] sku: SKU details
        :param pulumi.Input[str] location: The supported Azure location where the dedicated HSM should be created.
        :param pulumi.Input[str] name: Name of the dedicated Hsm
        :param pulumi.Input['NetworkProfileArgs'] network_profile: Specifies the network interfaces of the dedicated hsm.
        :param pulumi.Input[str] stamp_id: This field will be used when RP does not support Availability zones.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[Sequence[pulumi.Input[str]]] zones: The Dedicated Hsm zones.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "sku", sku)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if network_profile is not None:
            pulumi.set(__self__, "network_profile", network_profile)
        if stamp_id is not None:
            pulumi.set(__self__, "stamp_id", stamp_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if zones is not None:
            pulumi.set(__self__, "zones", zones)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the Resource Group to which the resource belongs.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Input['SkuArgs']:
        """
        SKU details
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: pulumi.Input['SkuArgs']):
        pulumi.set(self, "sku", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The supported Azure location where the dedicated HSM should be created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the dedicated Hsm
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> Optional[pulumi.Input['NetworkProfileArgs']]:
        """
        Specifies the network interfaces of the dedicated hsm.
        """
        return pulumi.get(self, "network_profile")

    @network_profile.setter
    def network_profile(self, value: Optional[pulumi.Input['NetworkProfileArgs']]):
        pulumi.set(self, "network_profile", value)

    @property
    @pulumi.getter(name="stampId")
    def stamp_id(self) -> Optional[pulumi.Input[str]]:
        """
        This field will be used when RP does not support Availability zones.
        """
        return pulumi.get(self, "stamp_id")

    @stamp_id.setter
    def stamp_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "stamp_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def zones(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The Dedicated Hsm zones.
        """
        return pulumi.get(self, "zones")

    @zones.setter
    def zones(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "zones", value)


class DedicatedHsm(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_profile: Optional[pulumi.Input[pulumi.InputType['NetworkProfileArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 stamp_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Resource information with extended details.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] location: The supported Azure location where the dedicated HSM should be created.
        :param pulumi.Input[str] name: Name of the dedicated Hsm
        :param pulumi.Input[pulumi.InputType['NetworkProfileArgs']] network_profile: Specifies the network interfaces of the dedicated hsm.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group to which the resource belongs.
        :param pulumi.Input[pulumi.InputType['SkuArgs']] sku: SKU details
        :param pulumi.Input[str] stamp_id: This field will be used when RP does not support Availability zones.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[Sequence[pulumi.Input[str]]] zones: The Dedicated Hsm zones.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DedicatedHsmArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource information with extended details.

        :param str resource_name: The name of the resource.
        :param DedicatedHsmArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DedicatedHsmArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_profile: Optional[pulumi.Input[pulumi.InputType['NetworkProfileArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 stamp_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
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
            __props__ = DedicatedHsmArgs.__new__(DedicatedHsmArgs)

            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            __props__.__dict__["network_profile"] = network_profile
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if sku is None and not opts.urn:
                raise TypeError("Missing required property 'sku'")
            __props__.__dict__["sku"] = sku
            __props__.__dict__["stamp_id"] = stamp_id
            __props__.__dict__["tags"] = tags
            __props__.__dict__["zones"] = zones
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["status_message"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:hardwaresecuritymodules/v20181031preview:DedicatedHsm"), pulumi.Alias(type_="azure-native:hardwaresecuritymodules:DedicatedHsm"), pulumi.Alias(type_="azure-nextgen:hardwaresecuritymodules:DedicatedHsm")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(DedicatedHsm, __self__).__init__(
            'azure-native:hardwaresecuritymodules/v20181031preview:DedicatedHsm',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DedicatedHsm':
        """
        Get an existing DedicatedHsm resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DedicatedHsmArgs.__new__(DedicatedHsmArgs)

        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network_profile"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["stamp_id"] = None
        __props__.__dict__["status_message"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["zones"] = None
        return DedicatedHsm(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The supported Azure location where the dedicated HSM should be created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the dedicated HSM.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> pulumi.Output[Optional['outputs.NetworkProfileResponse']]:
        """
        Specifies the network interfaces of the dedicated hsm.
        """
        return pulumi.get(self, "network_profile")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output['outputs.SkuResponse']:
        """
        SKU details
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="stampId")
    def stamp_id(self) -> pulumi.Output[Optional[str]]:
        """
        This field will be used when RP does not support Availability zones.
        """
        return pulumi.get(self, "stamp_id")

    @property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> pulumi.Output[str]:
        """
        Resource Status Message.
        """
        return pulumi.get(self, "status_message")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The resource type of the dedicated HSM.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def zones(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The Dedicated Hsm zones.
        """
        return pulumi.get(self, "zones")

