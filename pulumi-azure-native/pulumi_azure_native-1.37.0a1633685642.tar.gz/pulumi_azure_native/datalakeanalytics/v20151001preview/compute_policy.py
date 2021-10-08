# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = ['ComputePolicyArgs', 'ComputePolicy']

@pulumi.input_type
class ComputePolicyArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 object_id: pulumi.Input[str],
                 object_type: pulumi.Input[Union[str, 'AADObjectType']],
                 resource_group_name: pulumi.Input[str],
                 compute_policy_name: Optional[pulumi.Input[str]] = None,
                 max_degree_of_parallelism_per_job: Optional[pulumi.Input[int]] = None,
                 min_priority_per_job: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a ComputePolicy resource.
        :param pulumi.Input[str] account_name: The name of the Data Lake Analytics account.
        :param pulumi.Input[str] object_id: The AAD object identifier for the entity to create a policy for.
        :param pulumi.Input[Union[str, 'AADObjectType']] object_type: The type of AAD object the object identifier refers to.
        :param pulumi.Input[str] resource_group_name: The name of the Azure resource group.
        :param pulumi.Input[str] compute_policy_name: The name of the compute policy to create or update.
        :param pulumi.Input[int] max_degree_of_parallelism_per_job: The maximum degree of parallelism per job this user can use to submit jobs. This property, the min priority per job property, or both must be passed.
        :param pulumi.Input[int] min_priority_per_job: The minimum priority per job this user can use to submit jobs. This property, the max degree of parallelism per job property, or both must be passed.
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "object_id", object_id)
        pulumi.set(__self__, "object_type", object_type)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if compute_policy_name is not None:
            pulumi.set(__self__, "compute_policy_name", compute_policy_name)
        if max_degree_of_parallelism_per_job is not None:
            pulumi.set(__self__, "max_degree_of_parallelism_per_job", max_degree_of_parallelism_per_job)
        if min_priority_per_job is not None:
            pulumi.set(__self__, "min_priority_per_job", min_priority_per_job)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[str]:
        """
        The name of the Data Lake Analytics account.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter(name="objectId")
    def object_id(self) -> pulumi.Input[str]:
        """
        The AAD object identifier for the entity to create a policy for.
        """
        return pulumi.get(self, "object_id")

    @object_id.setter
    def object_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "object_id", value)

    @property
    @pulumi.getter(name="objectType")
    def object_type(self) -> pulumi.Input[Union[str, 'AADObjectType']]:
        """
        The type of AAD object the object identifier refers to.
        """
        return pulumi.get(self, "object_type")

    @object_type.setter
    def object_type(self, value: pulumi.Input[Union[str, 'AADObjectType']]):
        pulumi.set(self, "object_type", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the Azure resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="computePolicyName")
    def compute_policy_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the compute policy to create or update.
        """
        return pulumi.get(self, "compute_policy_name")

    @compute_policy_name.setter
    def compute_policy_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "compute_policy_name", value)

    @property
    @pulumi.getter(name="maxDegreeOfParallelismPerJob")
    def max_degree_of_parallelism_per_job(self) -> Optional[pulumi.Input[int]]:
        """
        The maximum degree of parallelism per job this user can use to submit jobs. This property, the min priority per job property, or both must be passed.
        """
        return pulumi.get(self, "max_degree_of_parallelism_per_job")

    @max_degree_of_parallelism_per_job.setter
    def max_degree_of_parallelism_per_job(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_degree_of_parallelism_per_job", value)

    @property
    @pulumi.getter(name="minPriorityPerJob")
    def min_priority_per_job(self) -> Optional[pulumi.Input[int]]:
        """
        The minimum priority per job this user can use to submit jobs. This property, the max degree of parallelism per job property, or both must be passed.
        """
        return pulumi.get(self, "min_priority_per_job")

    @min_priority_per_job.setter
    def min_priority_per_job(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "min_priority_per_job", value)


class ComputePolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 compute_policy_name: Optional[pulumi.Input[str]] = None,
                 max_degree_of_parallelism_per_job: Optional[pulumi.Input[int]] = None,
                 min_priority_per_job: Optional[pulumi.Input[int]] = None,
                 object_id: Optional[pulumi.Input[str]] = None,
                 object_type: Optional[pulumi.Input[Union[str, 'AADObjectType']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Data Lake Analytics compute policy information.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: The name of the Data Lake Analytics account.
        :param pulumi.Input[str] compute_policy_name: The name of the compute policy to create or update.
        :param pulumi.Input[int] max_degree_of_parallelism_per_job: The maximum degree of parallelism per job this user can use to submit jobs. This property, the min priority per job property, or both must be passed.
        :param pulumi.Input[int] min_priority_per_job: The minimum priority per job this user can use to submit jobs. This property, the max degree of parallelism per job property, or both must be passed.
        :param pulumi.Input[str] object_id: The AAD object identifier for the entity to create a policy for.
        :param pulumi.Input[Union[str, 'AADObjectType']] object_type: The type of AAD object the object identifier refers to.
        :param pulumi.Input[str] resource_group_name: The name of the Azure resource group.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ComputePolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Data Lake Analytics compute policy information.

        :param str resource_name: The name of the resource.
        :param ComputePolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ComputePolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 compute_policy_name: Optional[pulumi.Input[str]] = None,
                 max_degree_of_parallelism_per_job: Optional[pulumi.Input[int]] = None,
                 min_priority_per_job: Optional[pulumi.Input[int]] = None,
                 object_id: Optional[pulumi.Input[str]] = None,
                 object_type: Optional[pulumi.Input[Union[str, 'AADObjectType']]] = None,
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
            __props__ = ComputePolicyArgs.__new__(ComputePolicyArgs)

            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__.__dict__["account_name"] = account_name
            __props__.__dict__["compute_policy_name"] = compute_policy_name
            __props__.__dict__["max_degree_of_parallelism_per_job"] = max_degree_of_parallelism_per_job
            __props__.__dict__["min_priority_per_job"] = min_priority_per_job
            if object_id is None and not opts.urn:
                raise TypeError("Missing required property 'object_id'")
            __props__.__dict__["object_id"] = object_id
            if object_type is None and not opts.urn:
                raise TypeError("Missing required property 'object_type'")
            __props__.__dict__["object_type"] = object_type
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:datalakeanalytics/v20151001preview:ComputePolicy"), pulumi.Alias(type_="azure-native:datalakeanalytics:ComputePolicy"), pulumi.Alias(type_="azure-nextgen:datalakeanalytics:ComputePolicy"), pulumi.Alias(type_="azure-native:datalakeanalytics/v20161101:ComputePolicy"), pulumi.Alias(type_="azure-nextgen:datalakeanalytics/v20161101:ComputePolicy"), pulumi.Alias(type_="azure-native:datalakeanalytics/v20191101preview:ComputePolicy"), pulumi.Alias(type_="azure-nextgen:datalakeanalytics/v20191101preview:ComputePolicy")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ComputePolicy, __self__).__init__(
            'azure-native:datalakeanalytics/v20151001preview:ComputePolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ComputePolicy':
        """
        Get an existing ComputePolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ComputePolicyArgs.__new__(ComputePolicyArgs)

        __props__.__dict__["max_degree_of_parallelism_per_job"] = None
        __props__.__dict__["min_priority_per_job"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["object_id"] = None
        __props__.__dict__["object_type"] = None
        __props__.__dict__["type"] = None
        return ComputePolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="maxDegreeOfParallelismPerJob")
    def max_degree_of_parallelism_per_job(self) -> pulumi.Output[int]:
        """
        The maximum degree of parallelism per job this user can use to submit jobs.
        """
        return pulumi.get(self, "max_degree_of_parallelism_per_job")

    @property
    @pulumi.getter(name="minPriorityPerJob")
    def min_priority_per_job(self) -> pulumi.Output[int]:
        """
        The minimum priority per job this user can use to submit jobs.
        """
        return pulumi.get(self, "min_priority_per_job")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="objectId")
    def object_id(self) -> pulumi.Output[str]:
        """
        The AAD object identifier for the entity to create a policy for.
        """
        return pulumi.get(self, "object_id")

    @property
    @pulumi.getter(name="objectType")
    def object_type(self) -> pulumi.Output[str]:
        """
        The type of AAD object the object identifier refers to.
        """
        return pulumi.get(self, "object_type")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The resource type.
        """
        return pulumi.get(self, "type")

