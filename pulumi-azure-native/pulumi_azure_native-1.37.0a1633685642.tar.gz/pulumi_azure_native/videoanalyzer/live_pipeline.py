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

__all__ = ['LivePipelineArgs', 'LivePipeline']

@pulumi.input_type
class LivePipelineArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 bitrate_kbps: pulumi.Input[int],
                 resource_group_name: pulumi.Input[str],
                 topology_name: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 live_pipeline_name: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Sequence[pulumi.Input['ParameterDefinitionArgs']]]] = None):
        """
        The set of arguments for constructing a LivePipeline resource.
        :param pulumi.Input[str] account_name: The Azure Video Analyzer account name.
        :param pulumi.Input[int] bitrate_kbps: Maximum bitrate capacity in Kbps reserved for the live pipeline. The allowed range is from 500 to 3000 Kbps in increments of 100 Kbps. If the RTSP camera exceeds this capacity, then the service will disconnect temporarily from the camera. It will retry to re-establish connection (with exponential backoff), checking to see if the camera bitrate is now below the reserved capacity. Doing so will ensure that one 'noisy neighbor' does not affect other live pipelines in your account.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] topology_name: The reference to an existing pipeline topology defined for real-time content processing. When activated, this live pipeline will process content according to the pipeline topology definition.
        :param pulumi.Input[str] description: An optional description for the pipeline.
        :param pulumi.Input[str] live_pipeline_name: Live pipeline unique identifier.
        :param pulumi.Input[Sequence[pulumi.Input['ParameterDefinitionArgs']]] parameters: List of the instance level parameter values for the user-defined topology parameters. A pipeline can only define or override parameters values for parameters which have been declared in the referenced topology. Topology parameters without a default value must be defined. Topology parameters with a default value can be optionally be overridden.
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "bitrate_kbps", bitrate_kbps)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "topology_name", topology_name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if live_pipeline_name is not None:
            pulumi.set(__self__, "live_pipeline_name", live_pipeline_name)
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[str]:
        """
        The Azure Video Analyzer account name.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter(name="bitrateKbps")
    def bitrate_kbps(self) -> pulumi.Input[int]:
        """
        Maximum bitrate capacity in Kbps reserved for the live pipeline. The allowed range is from 500 to 3000 Kbps in increments of 100 Kbps. If the RTSP camera exceeds this capacity, then the service will disconnect temporarily from the camera. It will retry to re-establish connection (with exponential backoff), checking to see if the camera bitrate is now below the reserved capacity. Doing so will ensure that one 'noisy neighbor' does not affect other live pipelines in your account.
        """
        return pulumi.get(self, "bitrate_kbps")

    @bitrate_kbps.setter
    def bitrate_kbps(self, value: pulumi.Input[int]):
        pulumi.set(self, "bitrate_kbps", value)

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
    @pulumi.getter(name="topologyName")
    def topology_name(self) -> pulumi.Input[str]:
        """
        The reference to an existing pipeline topology defined for real-time content processing. When activated, this live pipeline will process content according to the pipeline topology definition.
        """
        return pulumi.get(self, "topology_name")

    @topology_name.setter
    def topology_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "topology_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        An optional description for the pipeline.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="livePipelineName")
    def live_pipeline_name(self) -> Optional[pulumi.Input[str]]:
        """
        Live pipeline unique identifier.
        """
        return pulumi.get(self, "live_pipeline_name")

    @live_pipeline_name.setter
    def live_pipeline_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "live_pipeline_name", value)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ParameterDefinitionArgs']]]]:
        """
        List of the instance level parameter values for the user-defined topology parameters. A pipeline can only define or override parameters values for parameters which have been declared in the referenced topology. Topology parameters without a default value must be defined. Topology parameters with a default value can be optionally be overridden.
        """
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ParameterDefinitionArgs']]]]):
        pulumi.set(self, "parameters", value)


class LivePipeline(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 bitrate_kbps: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 live_pipeline_name: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ParameterDefinitionArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 topology_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Live pipeline represents a unique instance of a live topology, used for real-time ingestion, archiving and publishing of content for a unique RTSP camera.
        API Version: 2021-11-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: The Azure Video Analyzer account name.
        :param pulumi.Input[int] bitrate_kbps: Maximum bitrate capacity in Kbps reserved for the live pipeline. The allowed range is from 500 to 3000 Kbps in increments of 100 Kbps. If the RTSP camera exceeds this capacity, then the service will disconnect temporarily from the camera. It will retry to re-establish connection (with exponential backoff), checking to see if the camera bitrate is now below the reserved capacity. Doing so will ensure that one 'noisy neighbor' does not affect other live pipelines in your account.
        :param pulumi.Input[str] description: An optional description for the pipeline.
        :param pulumi.Input[str] live_pipeline_name: Live pipeline unique identifier.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ParameterDefinitionArgs']]]] parameters: List of the instance level parameter values for the user-defined topology parameters. A pipeline can only define or override parameters values for parameters which have been declared in the referenced topology. Topology parameters without a default value must be defined. Topology parameters with a default value can be optionally be overridden.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] topology_name: The reference to an existing pipeline topology defined for real-time content processing. When activated, this live pipeline will process content according to the pipeline topology definition.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LivePipelineArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Live pipeline represents a unique instance of a live topology, used for real-time ingestion, archiving and publishing of content for a unique RTSP camera.
        API Version: 2021-11-01-preview.

        :param str resource_name: The name of the resource.
        :param LivePipelineArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LivePipelineArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 bitrate_kbps: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 live_pipeline_name: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ParameterDefinitionArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 topology_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = LivePipelineArgs.__new__(LivePipelineArgs)

            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__.__dict__["account_name"] = account_name
            if bitrate_kbps is None and not opts.urn:
                raise TypeError("Missing required property 'bitrate_kbps'")
            __props__.__dict__["bitrate_kbps"] = bitrate_kbps
            __props__.__dict__["description"] = description
            __props__.__dict__["live_pipeline_name"] = live_pipeline_name
            __props__.__dict__["parameters"] = parameters
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if topology_name is None and not opts.urn:
                raise TypeError("Missing required property 'topology_name'")
            __props__.__dict__["topology_name"] = topology_name
            __props__.__dict__["name"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:videoanalyzer:LivePipeline"), pulumi.Alias(type_="azure-native:videoanalyzer/v20211101preview:LivePipeline"), pulumi.Alias(type_="azure-nextgen:videoanalyzer/v20211101preview:LivePipeline")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(LivePipeline, __self__).__init__(
            'azure-native:videoanalyzer:LivePipeline',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'LivePipeline':
        """
        Get an existing LivePipeline resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = LivePipelineArgs.__new__(LivePipelineArgs)

        __props__.__dict__["bitrate_kbps"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["parameters"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["topology_name"] = None
        __props__.__dict__["type"] = None
        return LivePipeline(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="bitrateKbps")
    def bitrate_kbps(self) -> pulumi.Output[int]:
        """
        Maximum bitrate capacity in Kbps reserved for the live pipeline. The allowed range is from 500 to 3000 Kbps in increments of 100 Kbps. If the RTSP camera exceeds this capacity, then the service will disconnect temporarily from the camera. It will retry to re-establish connection (with exponential backoff), checking to see if the camera bitrate is now below the reserved capacity. Doing so will ensure that one 'noisy neighbor' does not affect other live pipelines in your account.
        """
        return pulumi.get(self, "bitrate_kbps")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        An optional description for the pipeline.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional[Sequence['outputs.ParameterDefinitionResponse']]]:
        """
        List of the instance level parameter values for the user-defined topology parameters. A pipeline can only define or override parameters values for parameters which have been declared in the referenced topology. Topology parameters without a default value must be defined. Topology parameters with a default value can be optionally be overridden.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        Current state of the pipeline (read-only).
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="topologyName")
    def topology_name(self) -> pulumi.Output[str]:
        """
        The reference to an existing pipeline topology defined for real-time content processing. When activated, this live pipeline will process content according to the pipeline topology definition.
        """
        return pulumi.get(self, "topology_name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

