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

__all__ = ['AdaptiveApplicationControlArgs', 'AdaptiveApplicationControl']

@pulumi.input_type
class AdaptiveApplicationControlArgs:
    def __init__(__self__, *,
                 asc_location: pulumi.Input[str],
                 enforcement_mode: Optional[pulumi.Input[str]] = None,
                 group_name: Optional[pulumi.Input[str]] = None,
                 path_recommendations: Optional[pulumi.Input[Sequence[pulumi.Input['PathRecommendationArgs']]]] = None,
                 protection_mode: Optional[pulumi.Input['ProtectionModeArgs']] = None,
                 vm_recommendations: Optional[pulumi.Input[Sequence[pulumi.Input['VmRecommendationArgs']]]] = None):
        """
        The set of arguments for constructing a AdaptiveApplicationControl resource.
        :param pulumi.Input[str] asc_location: The location where ASC stores the data of the subscription. can be retrieved from Get locations
        :param pulumi.Input[str] enforcement_mode: The application control policy enforcement/protection mode of the machine group
        :param pulumi.Input[str] group_name: Name of an application control machine group
        :param pulumi.Input['ProtectionModeArgs'] protection_mode: The protection mode of the collection/file types. Exe/Msi/Script are used for Windows, Executable is used for Linux.
        """
        pulumi.set(__self__, "asc_location", asc_location)
        if enforcement_mode is not None:
            pulumi.set(__self__, "enforcement_mode", enforcement_mode)
        if group_name is not None:
            pulumi.set(__self__, "group_name", group_name)
        if path_recommendations is not None:
            pulumi.set(__self__, "path_recommendations", path_recommendations)
        if protection_mode is not None:
            pulumi.set(__self__, "protection_mode", protection_mode)
        if vm_recommendations is not None:
            pulumi.set(__self__, "vm_recommendations", vm_recommendations)

    @property
    @pulumi.getter(name="ascLocation")
    def asc_location(self) -> pulumi.Input[str]:
        """
        The location where ASC stores the data of the subscription. can be retrieved from Get locations
        """
        return pulumi.get(self, "asc_location")

    @asc_location.setter
    def asc_location(self, value: pulumi.Input[str]):
        pulumi.set(self, "asc_location", value)

    @property
    @pulumi.getter(name="enforcementMode")
    def enforcement_mode(self) -> Optional[pulumi.Input[str]]:
        """
        The application control policy enforcement/protection mode of the machine group
        """
        return pulumi.get(self, "enforcement_mode")

    @enforcement_mode.setter
    def enforcement_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "enforcement_mode", value)

    @property
    @pulumi.getter(name="groupName")
    def group_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of an application control machine group
        """
        return pulumi.get(self, "group_name")

    @group_name.setter
    def group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group_name", value)

    @property
    @pulumi.getter(name="pathRecommendations")
    def path_recommendations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PathRecommendationArgs']]]]:
        return pulumi.get(self, "path_recommendations")

    @path_recommendations.setter
    def path_recommendations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PathRecommendationArgs']]]]):
        pulumi.set(self, "path_recommendations", value)

    @property
    @pulumi.getter(name="protectionMode")
    def protection_mode(self) -> Optional[pulumi.Input['ProtectionModeArgs']]:
        """
        The protection mode of the collection/file types. Exe/Msi/Script are used for Windows, Executable is used for Linux.
        """
        return pulumi.get(self, "protection_mode")

    @protection_mode.setter
    def protection_mode(self, value: Optional[pulumi.Input['ProtectionModeArgs']]):
        pulumi.set(self, "protection_mode", value)

    @property
    @pulumi.getter(name="vmRecommendations")
    def vm_recommendations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['VmRecommendationArgs']]]]:
        return pulumi.get(self, "vm_recommendations")

    @vm_recommendations.setter
    def vm_recommendations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['VmRecommendationArgs']]]]):
        pulumi.set(self, "vm_recommendations", value)


class AdaptiveApplicationControl(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 asc_location: Optional[pulumi.Input[str]] = None,
                 enforcement_mode: Optional[pulumi.Input[str]] = None,
                 group_name: Optional[pulumi.Input[str]] = None,
                 path_recommendations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PathRecommendationArgs']]]]] = None,
                 protection_mode: Optional[pulumi.Input[pulumi.InputType['ProtectionModeArgs']]] = None,
                 vm_recommendations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VmRecommendationArgs']]]]] = None,
                 __props__=None):
        """
        Create a AdaptiveApplicationControl resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] asc_location: The location where ASC stores the data of the subscription. can be retrieved from Get locations
        :param pulumi.Input[str] enforcement_mode: The application control policy enforcement/protection mode of the machine group
        :param pulumi.Input[str] group_name: Name of an application control machine group
        :param pulumi.Input[pulumi.InputType['ProtectionModeArgs']] protection_mode: The protection mode of the collection/file types. Exe/Msi/Script are used for Windows, Executable is used for Linux.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AdaptiveApplicationControlArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a AdaptiveApplicationControl resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param AdaptiveApplicationControlArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AdaptiveApplicationControlArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 asc_location: Optional[pulumi.Input[str]] = None,
                 enforcement_mode: Optional[pulumi.Input[str]] = None,
                 group_name: Optional[pulumi.Input[str]] = None,
                 path_recommendations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PathRecommendationArgs']]]]] = None,
                 protection_mode: Optional[pulumi.Input[pulumi.InputType['ProtectionModeArgs']]] = None,
                 vm_recommendations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VmRecommendationArgs']]]]] = None,
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
            __props__ = AdaptiveApplicationControlArgs.__new__(AdaptiveApplicationControlArgs)

            if asc_location is None and not opts.urn:
                raise TypeError("Missing required property 'asc_location'")
            __props__.__dict__["asc_location"] = asc_location
            __props__.__dict__["enforcement_mode"] = enforcement_mode
            __props__.__dict__["group_name"] = group_name
            __props__.__dict__["path_recommendations"] = path_recommendations
            __props__.__dict__["protection_mode"] = protection_mode
            __props__.__dict__["vm_recommendations"] = vm_recommendations
            __props__.__dict__["configuration_status"] = None
            __props__.__dict__["issues"] = None
            __props__.__dict__["location"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["recommendation_status"] = None
            __props__.__dict__["source_system"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:security/v20200101:AdaptiveApplicationControl"), pulumi.Alias(type_="azure-native:security:AdaptiveApplicationControl"), pulumi.Alias(type_="azure-nextgen:security:AdaptiveApplicationControl"), pulumi.Alias(type_="azure-native:security/v20150601preview:AdaptiveApplicationControl"), pulumi.Alias(type_="azure-nextgen:security/v20150601preview:AdaptiveApplicationControl")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(AdaptiveApplicationControl, __self__).__init__(
            'azure-native:security/v20200101:AdaptiveApplicationControl',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AdaptiveApplicationControl':
        """
        Get an existing AdaptiveApplicationControl resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AdaptiveApplicationControlArgs.__new__(AdaptiveApplicationControlArgs)

        __props__.__dict__["configuration_status"] = None
        __props__.__dict__["enforcement_mode"] = None
        __props__.__dict__["issues"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["path_recommendations"] = None
        __props__.__dict__["protection_mode"] = None
        __props__.__dict__["recommendation_status"] = None
        __props__.__dict__["source_system"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["vm_recommendations"] = None
        return AdaptiveApplicationControl(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="configurationStatus")
    def configuration_status(self) -> pulumi.Output[str]:
        """
        The configuration status of the machines group or machine or rule
        """
        return pulumi.get(self, "configuration_status")

    @property
    @pulumi.getter(name="enforcementMode")
    def enforcement_mode(self) -> pulumi.Output[Optional[str]]:
        """
        The application control policy enforcement/protection mode of the machine group
        """
        return pulumi.get(self, "enforcement_mode")

    @property
    @pulumi.getter
    def issues(self) -> pulumi.Output[Sequence['outputs.AdaptiveApplicationControlIssueSummaryResponse']]:
        return pulumi.get(self, "issues")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Location where the resource is stored
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
    @pulumi.getter(name="pathRecommendations")
    def path_recommendations(self) -> pulumi.Output[Optional[Sequence['outputs.PathRecommendationResponse']]]:
        return pulumi.get(self, "path_recommendations")

    @property
    @pulumi.getter(name="protectionMode")
    def protection_mode(self) -> pulumi.Output[Optional['outputs.ProtectionModeResponse']]:
        """
        The protection mode of the collection/file types. Exe/Msi/Script are used for Windows, Executable is used for Linux.
        """
        return pulumi.get(self, "protection_mode")

    @property
    @pulumi.getter(name="recommendationStatus")
    def recommendation_status(self) -> pulumi.Output[str]:
        """
        The initial recommendation status of the machine group or machine
        """
        return pulumi.get(self, "recommendation_status")

    @property
    @pulumi.getter(name="sourceSystem")
    def source_system(self) -> pulumi.Output[str]:
        """
        The source type of the machine group
        """
        return pulumi.get(self, "source_system")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="vmRecommendations")
    def vm_recommendations(self) -> pulumi.Output[Optional[Sequence['outputs.VmRecommendationResponse']]]:
        return pulumi.get(self, "vm_recommendations")

