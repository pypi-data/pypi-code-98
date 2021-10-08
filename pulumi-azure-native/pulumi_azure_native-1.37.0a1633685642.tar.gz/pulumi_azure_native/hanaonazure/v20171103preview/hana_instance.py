# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._inputs import *

__all__ = ['HanaInstanceArgs', 'HanaInstance']

@pulumi.input_type
class HanaInstanceArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 hana_instance_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 network_profile: Optional[pulumi.Input['NetworkProfileArgs']] = None,
                 os_profile: Optional[pulumi.Input['OSProfileArgs']] = None,
                 partner_node_id: Optional[pulumi.Input[str]] = None,
                 storage_profile: Optional[pulumi.Input['StorageProfileArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a HanaInstance resource.
        :param pulumi.Input[str] resource_group_name: Name of the resource group.
        :param pulumi.Input[str] hana_instance_name: Name of the SAP HANA on Azure instance.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input['NetworkProfileArgs'] network_profile: Specifies the network settings for the HANA instance.
        :param pulumi.Input['OSProfileArgs'] os_profile: Specifies the operating system settings for the HANA instance.
        :param pulumi.Input[str] partner_node_id: ARM ID of another HanaInstance that will share a network with this HanaInstance
        :param pulumi.Input['StorageProfileArgs'] storage_profile: Specifies the storage settings for the HANA instance disks.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if hana_instance_name is not None:
            pulumi.set(__self__, "hana_instance_name", hana_instance_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if network_profile is not None:
            pulumi.set(__self__, "network_profile", network_profile)
        if os_profile is not None:
            pulumi.set(__self__, "os_profile", os_profile)
        if partner_node_id is not None:
            pulumi.set(__self__, "partner_node_id", partner_node_id)
        if storage_profile is not None:
            pulumi.set(__self__, "storage_profile", storage_profile)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="hanaInstanceName")
    def hana_instance_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the SAP HANA on Azure instance.
        """
        return pulumi.get(self, "hana_instance_name")

    @hana_instance_name.setter
    def hana_instance_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hana_instance_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> Optional[pulumi.Input['NetworkProfileArgs']]:
        """
        Specifies the network settings for the HANA instance.
        """
        return pulumi.get(self, "network_profile")

    @network_profile.setter
    def network_profile(self, value: Optional[pulumi.Input['NetworkProfileArgs']]):
        pulumi.set(self, "network_profile", value)

    @property
    @pulumi.getter(name="osProfile")
    def os_profile(self) -> Optional[pulumi.Input['OSProfileArgs']]:
        """
        Specifies the operating system settings for the HANA instance.
        """
        return pulumi.get(self, "os_profile")

    @os_profile.setter
    def os_profile(self, value: Optional[pulumi.Input['OSProfileArgs']]):
        pulumi.set(self, "os_profile", value)

    @property
    @pulumi.getter(name="partnerNodeId")
    def partner_node_id(self) -> Optional[pulumi.Input[str]]:
        """
        ARM ID of another HanaInstance that will share a network with this HanaInstance
        """
        return pulumi.get(self, "partner_node_id")

    @partner_node_id.setter
    def partner_node_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "partner_node_id", value)

    @property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> Optional[pulumi.Input['StorageProfileArgs']]:
        """
        Specifies the storage settings for the HANA instance disks.
        """
        return pulumi.get(self, "storage_profile")

    @storage_profile.setter
    def storage_profile(self, value: Optional[pulumi.Input['StorageProfileArgs']]):
        pulumi.set(self, "storage_profile", value)

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


class HanaInstance(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 hana_instance_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 network_profile: Optional[pulumi.Input[pulumi.InputType['NetworkProfileArgs']]] = None,
                 os_profile: Optional[pulumi.Input[pulumi.InputType['OSProfileArgs']]] = None,
                 partner_node_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 storage_profile: Optional[pulumi.Input[pulumi.InputType['StorageProfileArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        HANA instance info on Azure (ARM properties and HANA properties)

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] hana_instance_name: Name of the SAP HANA on Azure instance.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[pulumi.InputType['NetworkProfileArgs']] network_profile: Specifies the network settings for the HANA instance.
        :param pulumi.Input[pulumi.InputType['OSProfileArgs']] os_profile: Specifies the operating system settings for the HANA instance.
        :param pulumi.Input[str] partner_node_id: ARM ID of another HanaInstance that will share a network with this HanaInstance
        :param pulumi.Input[str] resource_group_name: Name of the resource group.
        :param pulumi.Input[pulumi.InputType['StorageProfileArgs']] storage_profile: Specifies the storage settings for the HANA instance disks.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: HanaInstanceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        HANA instance info on Azure (ARM properties and HANA properties)

        :param str resource_name: The name of the resource.
        :param HanaInstanceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(HanaInstanceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 hana_instance_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 network_profile: Optional[pulumi.Input[pulumi.InputType['NetworkProfileArgs']]] = None,
                 os_profile: Optional[pulumi.Input[pulumi.InputType['OSProfileArgs']]] = None,
                 partner_node_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 storage_profile: Optional[pulumi.Input[pulumi.InputType['StorageProfileArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
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
            __props__ = HanaInstanceArgs.__new__(HanaInstanceArgs)

            __props__.__dict__["hana_instance_name"] = hana_instance_name
            __props__.__dict__["location"] = location
            __props__.__dict__["network_profile"] = network_profile
            __props__.__dict__["os_profile"] = os_profile
            __props__.__dict__["partner_node_id"] = partner_node_id
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["storage_profile"] = storage_profile
            __props__.__dict__["tags"] = tags
            __props__.__dict__["hana_instance_id"] = None
            __props__.__dict__["hardware_profile"] = None
            __props__.__dict__["hw_revision"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["power_state"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["proximity_placement_group"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:hanaonazure/v20171103preview:HanaInstance"), pulumi.Alias(type_="azure-native:hanaonazure:HanaInstance"), pulumi.Alias(type_="azure-nextgen:hanaonazure:HanaInstance")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(HanaInstance, __self__).__init__(
            'azure-native:hanaonazure/v20171103preview:HanaInstance',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'HanaInstance':
        """
        Get an existing HanaInstance resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = HanaInstanceArgs.__new__(HanaInstanceArgs)

        __props__.__dict__["hana_instance_id"] = None
        __props__.__dict__["hardware_profile"] = None
        __props__.__dict__["hw_revision"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network_profile"] = None
        __props__.__dict__["os_profile"] = None
        __props__.__dict__["partner_node_id"] = None
        __props__.__dict__["power_state"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["proximity_placement_group"] = None
        __props__.__dict__["storage_profile"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return HanaInstance(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="hanaInstanceId")
    def hana_instance_id(self) -> pulumi.Output[str]:
        """
        Specifies the HANA instance unique ID.
        """
        return pulumi.get(self, "hana_instance_id")

    @property
    @pulumi.getter(name="hardwareProfile")
    def hardware_profile(self) -> pulumi.Output[Optional['outputs.HardwareProfileResponse']]:
        """
        Specifies the hardware settings for the HANA instance.
        """
        return pulumi.get(self, "hardware_profile")

    @property
    @pulumi.getter(name="hwRevision")
    def hw_revision(self) -> pulumi.Output[str]:
        """
        Hardware revision of a HANA instance
        """
        return pulumi.get(self, "hw_revision")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> pulumi.Output[Optional['outputs.NetworkProfileResponse']]:
        """
        Specifies the network settings for the HANA instance.
        """
        return pulumi.get(self, "network_profile")

    @property
    @pulumi.getter(name="osProfile")
    def os_profile(self) -> pulumi.Output[Optional['outputs.OSProfileResponse']]:
        """
        Specifies the operating system settings for the HANA instance.
        """
        return pulumi.get(self, "os_profile")

    @property
    @pulumi.getter(name="partnerNodeId")
    def partner_node_id(self) -> pulumi.Output[Optional[str]]:
        """
        ARM ID of another HanaInstance that will share a network with this HanaInstance
        """
        return pulumi.get(self, "partner_node_id")

    @property
    @pulumi.getter(name="powerState")
    def power_state(self) -> pulumi.Output[str]:
        """
        Resource power state
        """
        return pulumi.get(self, "power_state")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        State of provisioning of the HanaInstance
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="proximityPlacementGroup")
    def proximity_placement_group(self) -> pulumi.Output[str]:
        """
        Resource proximity placement group
        """
        return pulumi.get(self, "proximity_placement_group")

    @property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> pulumi.Output[Optional['outputs.StorageProfileResponse']]:
        """
        Specifies the storage settings for the HANA instance disks.
        """
        return pulumi.get(self, "storage_profile")

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
        Resource type
        """
        return pulumi.get(self, "type")

