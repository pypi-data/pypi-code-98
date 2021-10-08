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

__all__ = ['PipelineTopologyArgs', 'PipelineTopology']

@pulumi.input_type
class PipelineTopologyArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 kind: pulumi.Input[Union[str, 'Kind']],
                 resource_group_name: pulumi.Input[str],
                 sinks: pulumi.Input[Sequence[pulumi.Input['VideoSinkArgs']]],
                 sku: pulumi.Input['SkuArgs'],
                 sources: pulumi.Input[Sequence[pulumi.Input[Union['RtspSourceArgs', 'VideoSourceArgs']]]],
                 description: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Sequence[pulumi.Input['ParameterDeclarationArgs']]]] = None,
                 pipeline_topology_name: Optional[pulumi.Input[str]] = None,
                 processors: Optional[pulumi.Input[Sequence[pulumi.Input['EncoderProcessorArgs']]]] = None):
        """
        The set of arguments for constructing a PipelineTopology resource.
        :param pulumi.Input[str] account_name: The Azure Video Analyzer account name.
        :param pulumi.Input[Union[str, 'Kind']] kind: Topology kind.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Sequence[pulumi.Input['VideoSinkArgs']]] sinks: List of the topology sink nodes. Sink nodes allow pipeline data to be stored or exported.
        :param pulumi.Input['SkuArgs'] sku: Describes the properties of a SKU.
        :param pulumi.Input[Sequence[pulumi.Input[Union['RtspSourceArgs', 'VideoSourceArgs']]]] sources: List of the topology source nodes. Source nodes enable external data to be ingested by the pipeline.
        :param pulumi.Input[str] description: An optional description of the pipeline topology. It is recommended that the expected use of the topology to be described here.
        :param pulumi.Input[Sequence[pulumi.Input['ParameterDeclarationArgs']]] parameters: List of the topology parameter declarations. Parameters declared here can be referenced throughout the topology nodes through the use of "${PARAMETER_NAME}" string pattern. Parameters can have optional default values and can later be defined in individual instances of the pipeline.
        :param pulumi.Input[str] pipeline_topology_name: Pipeline topology unique identifier.
        :param pulumi.Input[Sequence[pulumi.Input['EncoderProcessorArgs']]] processors: List of the topology processor nodes. Processor nodes enable pipeline data to be analyzed, processed or transformed.
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "kind", kind)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "sinks", sinks)
        pulumi.set(__self__, "sku", sku)
        pulumi.set(__self__, "sources", sources)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)
        if pipeline_topology_name is not None:
            pulumi.set(__self__, "pipeline_topology_name", pipeline_topology_name)
        if processors is not None:
            pulumi.set(__self__, "processors", processors)

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
    @pulumi.getter
    def kind(self) -> pulumi.Input[Union[str, 'Kind']]:
        """
        Topology kind.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: pulumi.Input[Union[str, 'Kind']]):
        pulumi.set(self, "kind", value)

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
    def sinks(self) -> pulumi.Input[Sequence[pulumi.Input['VideoSinkArgs']]]:
        """
        List of the topology sink nodes. Sink nodes allow pipeline data to be stored or exported.
        """
        return pulumi.get(self, "sinks")

    @sinks.setter
    def sinks(self, value: pulumi.Input[Sequence[pulumi.Input['VideoSinkArgs']]]):
        pulumi.set(self, "sinks", value)

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Input['SkuArgs']:
        """
        Describes the properties of a SKU.
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: pulumi.Input['SkuArgs']):
        pulumi.set(self, "sku", value)

    @property
    @pulumi.getter
    def sources(self) -> pulumi.Input[Sequence[pulumi.Input[Union['RtspSourceArgs', 'VideoSourceArgs']]]]:
        """
        List of the topology source nodes. Source nodes enable external data to be ingested by the pipeline.
        """
        return pulumi.get(self, "sources")

    @sources.setter
    def sources(self, value: pulumi.Input[Sequence[pulumi.Input[Union['RtspSourceArgs', 'VideoSourceArgs']]]]):
        pulumi.set(self, "sources", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        An optional description of the pipeline topology. It is recommended that the expected use of the topology to be described here.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ParameterDeclarationArgs']]]]:
        """
        List of the topology parameter declarations. Parameters declared here can be referenced throughout the topology nodes through the use of "${PARAMETER_NAME}" string pattern. Parameters can have optional default values and can later be defined in individual instances of the pipeline.
        """
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ParameterDeclarationArgs']]]]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter(name="pipelineTopologyName")
    def pipeline_topology_name(self) -> Optional[pulumi.Input[str]]:
        """
        Pipeline topology unique identifier.
        """
        return pulumi.get(self, "pipeline_topology_name")

    @pipeline_topology_name.setter
    def pipeline_topology_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pipeline_topology_name", value)

    @property
    @pulumi.getter
    def processors(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['EncoderProcessorArgs']]]]:
        """
        List of the topology processor nodes. Processor nodes enable pipeline data to be analyzed, processed or transformed.
        """
        return pulumi.get(self, "processors")

    @processors.setter
    def processors(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['EncoderProcessorArgs']]]]):
        pulumi.set(self, "processors", value)


class PipelineTopology(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[Union[str, 'Kind']]] = None,
                 parameters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ParameterDeclarationArgs']]]]] = None,
                 pipeline_topology_name: Optional[pulumi.Input[str]] = None,
                 processors: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EncoderProcessorArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sinks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VideoSinkArgs']]]]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 sources: Optional[pulumi.Input[Sequence[pulumi.Input[Union[pulumi.InputType['RtspSourceArgs'], pulumi.InputType['VideoSourceArgs']]]]]] = None,
                 __props__=None):
        """
        Pipeline topology describes the processing steps to be applied when processing content for a particular outcome. The topology should be defined according to the scenario to be achieved and can be reused across many pipeline instances which share the same processing characteristics. For instance, a pipeline topology which captures content from a RTSP camera and archives the content can be reused across many different cameras, as long as the same processing is to be applied across all the cameras. Individual instance properties can be defined through the use of user-defined parameters, which allow for a topology to be parameterized. This allows  individual pipelines refer to different values, such as individual cameras' RTSP endpoints and credentials. Overall a topology is composed of the following:

          - Parameters: list of user defined parameters that can be references across the topology nodes.
          - Sources: list of one or more data sources nodes such as an RTSP source which allows for content to be ingested from cameras.
          - Processors: list of nodes which perform data analysis or transformations.
          - Sinks: list of one or more data sinks which allow for data to be stored or exported to other destinations.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: The Azure Video Analyzer account name.
        :param pulumi.Input[str] description: An optional description of the pipeline topology. It is recommended that the expected use of the topology to be described here.
        :param pulumi.Input[Union[str, 'Kind']] kind: Topology kind.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ParameterDeclarationArgs']]]] parameters: List of the topology parameter declarations. Parameters declared here can be referenced throughout the topology nodes through the use of "${PARAMETER_NAME}" string pattern. Parameters can have optional default values and can later be defined in individual instances of the pipeline.
        :param pulumi.Input[str] pipeline_topology_name: Pipeline topology unique identifier.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EncoderProcessorArgs']]]] processors: List of the topology processor nodes. Processor nodes enable pipeline data to be analyzed, processed or transformed.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VideoSinkArgs']]]] sinks: List of the topology sink nodes. Sink nodes allow pipeline data to be stored or exported.
        :param pulumi.Input[pulumi.InputType['SkuArgs']] sku: Describes the properties of a SKU.
        :param pulumi.Input[Sequence[pulumi.Input[Union[pulumi.InputType['RtspSourceArgs'], pulumi.InputType['VideoSourceArgs']]]]] sources: List of the topology source nodes. Source nodes enable external data to be ingested by the pipeline.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PipelineTopologyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Pipeline topology describes the processing steps to be applied when processing content for a particular outcome. The topology should be defined according to the scenario to be achieved and can be reused across many pipeline instances which share the same processing characteristics. For instance, a pipeline topology which captures content from a RTSP camera and archives the content can be reused across many different cameras, as long as the same processing is to be applied across all the cameras. Individual instance properties can be defined through the use of user-defined parameters, which allow for a topology to be parameterized. This allows  individual pipelines refer to different values, such as individual cameras' RTSP endpoints and credentials. Overall a topology is composed of the following:

          - Parameters: list of user defined parameters that can be references across the topology nodes.
          - Sources: list of one or more data sources nodes such as an RTSP source which allows for content to be ingested from cameras.
          - Processors: list of nodes which perform data analysis or transformations.
          - Sinks: list of one or more data sinks which allow for data to be stored or exported to other destinations.

        :param str resource_name: The name of the resource.
        :param PipelineTopologyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PipelineTopologyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[Union[str, 'Kind']]] = None,
                 parameters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ParameterDeclarationArgs']]]]] = None,
                 pipeline_topology_name: Optional[pulumi.Input[str]] = None,
                 processors: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EncoderProcessorArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sinks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VideoSinkArgs']]]]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 sources: Optional[pulumi.Input[Sequence[pulumi.Input[Union[pulumi.InputType['RtspSourceArgs'], pulumi.InputType['VideoSourceArgs']]]]]] = None,
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
            __props__ = PipelineTopologyArgs.__new__(PipelineTopologyArgs)

            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__.__dict__["account_name"] = account_name
            __props__.__dict__["description"] = description
            if kind is None and not opts.urn:
                raise TypeError("Missing required property 'kind'")
            __props__.__dict__["kind"] = kind
            __props__.__dict__["parameters"] = parameters
            __props__.__dict__["pipeline_topology_name"] = pipeline_topology_name
            __props__.__dict__["processors"] = processors
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if sinks is None and not opts.urn:
                raise TypeError("Missing required property 'sinks'")
            __props__.__dict__["sinks"] = sinks
            if sku is None and not opts.urn:
                raise TypeError("Missing required property 'sku'")
            __props__.__dict__["sku"] = sku
            if sources is None and not opts.urn:
                raise TypeError("Missing required property 'sources'")
            __props__.__dict__["sources"] = sources
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:videoanalyzer/v20211101preview:PipelineTopology"), pulumi.Alias(type_="azure-native:videoanalyzer:PipelineTopology"), pulumi.Alias(type_="azure-nextgen:videoanalyzer:PipelineTopology")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(PipelineTopology, __self__).__init__(
            'azure-native:videoanalyzer/v20211101preview:PipelineTopology',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PipelineTopology':
        """
        Get an existing PipelineTopology resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PipelineTopologyArgs.__new__(PipelineTopologyArgs)

        __props__.__dict__["description"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["parameters"] = None
        __props__.__dict__["processors"] = None
        __props__.__dict__["sinks"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["sources"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return PipelineTopology(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        An optional description of the pipeline topology. It is recommended that the expected use of the topology to be described here.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        Topology kind.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional[Sequence['outputs.ParameterDeclarationResponse']]]:
        """
        List of the topology parameter declarations. Parameters declared here can be referenced throughout the topology nodes through the use of "${PARAMETER_NAME}" string pattern. Parameters can have optional default values and can later be defined in individual instances of the pipeline.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter
    def processors(self) -> pulumi.Output[Optional[Sequence['outputs.EncoderProcessorResponse']]]:
        """
        List of the topology processor nodes. Processor nodes enable pipeline data to be analyzed, processed or transformed.
        """
        return pulumi.get(self, "processors")

    @property
    @pulumi.getter
    def sinks(self) -> pulumi.Output[Sequence['outputs.VideoSinkResponse']]:
        """
        List of the topology sink nodes. Sink nodes allow pipeline data to be stored or exported.
        """
        return pulumi.get(self, "sinks")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output['outputs.SkuResponse']:
        """
        Describes the properties of a SKU.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def sources(self) -> pulumi.Output[Sequence[Any]]:
        """
        List of the topology source nodes. Source nodes enable external data to be ingested by the pipeline.
        """
        return pulumi.get(self, "sources")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

