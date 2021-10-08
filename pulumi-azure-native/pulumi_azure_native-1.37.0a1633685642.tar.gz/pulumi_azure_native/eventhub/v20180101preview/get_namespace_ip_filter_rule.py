# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetNamespaceIpFilterRuleResult',
    'AwaitableGetNamespaceIpFilterRuleResult',
    'get_namespace_ip_filter_rule',
    'get_namespace_ip_filter_rule_output',
]

@pulumi.output_type
class GetNamespaceIpFilterRuleResult:
    """
    Single item in a List or Get IpFilterRules operation
    """
    def __init__(__self__, action=None, filter_name=None, id=None, ip_mask=None, name=None, type=None):
        if action and not isinstance(action, str):
            raise TypeError("Expected argument 'action' to be a str")
        pulumi.set(__self__, "action", action)
        if filter_name and not isinstance(filter_name, str):
            raise TypeError("Expected argument 'filter_name' to be a str")
        pulumi.set(__self__, "filter_name", filter_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ip_mask and not isinstance(ip_mask, str):
            raise TypeError("Expected argument 'ip_mask' to be a str")
        pulumi.set(__self__, "ip_mask", ip_mask)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def action(self) -> Optional[str]:
        """
        The IP Filter Action
        """
        return pulumi.get(self, "action")

    @property
    @pulumi.getter(name="filterName")
    def filter_name(self) -> Optional[str]:
        """
        IP Filter name
        """
        return pulumi.get(self, "filter_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ipMask")
    def ip_mask(self) -> Optional[str]:
        """
        IP Mask
        """
        return pulumi.get(self, "ip_mask")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetNamespaceIpFilterRuleResult(GetNamespaceIpFilterRuleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNamespaceIpFilterRuleResult(
            action=self.action,
            filter_name=self.filter_name,
            id=self.id,
            ip_mask=self.ip_mask,
            name=self.name,
            type=self.type)


def get_namespace_ip_filter_rule(ip_filter_rule_name: Optional[str] = None,
                                 namespace_name: Optional[str] = None,
                                 resource_group_name: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNamespaceIpFilterRuleResult:
    """
    Single item in a List or Get IpFilterRules operation


    :param str ip_filter_rule_name: The IP Filter Rule name.
    :param str namespace_name: The Namespace name
    :param str resource_group_name: Name of the resource group within the azure subscription.
    """
    __args__ = dict()
    __args__['ipFilterRuleName'] = ip_filter_rule_name
    __args__['namespaceName'] = namespace_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:eventhub/v20180101preview:getNamespaceIpFilterRule', __args__, opts=opts, typ=GetNamespaceIpFilterRuleResult).value

    return AwaitableGetNamespaceIpFilterRuleResult(
        action=__ret__.action,
        filter_name=__ret__.filter_name,
        id=__ret__.id,
        ip_mask=__ret__.ip_mask,
        name=__ret__.name,
        type=__ret__.type)


@_utilities.lift_output_func(get_namespace_ip_filter_rule)
def get_namespace_ip_filter_rule_output(ip_filter_rule_name: Optional[pulumi.Input[str]] = None,
                                        namespace_name: Optional[pulumi.Input[str]] = None,
                                        resource_group_name: Optional[pulumi.Input[str]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNamespaceIpFilterRuleResult]:
    """
    Single item in a List or Get IpFilterRules operation


    :param str ip_filter_rule_name: The IP Filter Rule name.
    :param str namespace_name: The Namespace name
    :param str resource_group_name: Name of the resource group within the azure subscription.
    """
    ...
