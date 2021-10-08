# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetHubResult',
    'AwaitableGetHubResult',
    'get_hub',
    'get_hub_output',
]

@pulumi.output_type
class GetHubResult:
    """
    Hub resource.
    """
    def __init__(__self__, api_endpoint=None, hub_billing_info=None, id=None, location=None, name=None, provisioning_state=None, tags=None, tenant_features=None, type=None, web_endpoint=None):
        if api_endpoint and not isinstance(api_endpoint, str):
            raise TypeError("Expected argument 'api_endpoint' to be a str")
        pulumi.set(__self__, "api_endpoint", api_endpoint)
        if hub_billing_info and not isinstance(hub_billing_info, dict):
            raise TypeError("Expected argument 'hub_billing_info' to be a dict")
        pulumi.set(__self__, "hub_billing_info", hub_billing_info)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if tenant_features and not isinstance(tenant_features, int):
            raise TypeError("Expected argument 'tenant_features' to be a int")
        pulumi.set(__self__, "tenant_features", tenant_features)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if web_endpoint and not isinstance(web_endpoint, str):
            raise TypeError("Expected argument 'web_endpoint' to be a str")
        pulumi.set(__self__, "web_endpoint", web_endpoint)

    @property
    @pulumi.getter(name="apiEndpoint")
    def api_endpoint(self) -> str:
        """
        API endpoint URL of the hub.
        """
        return pulumi.get(self, "api_endpoint")

    @property
    @pulumi.getter(name="hubBillingInfo")
    def hub_billing_info(self) -> Optional['outputs.HubBillingInfoFormatResponse']:
        """
        Billing settings of the hub.
        """
        return pulumi.get(self, "hub_billing_info")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the hub.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tenantFeatures")
    def tenant_features(self) -> Optional[int]:
        """
        The bit flags for enabled hub features. Bit 0 is set to 1 indicates graph is enabled, or disabled if set to 0. Bit 1 is set to 1 indicates the hub is disabled, or enabled if set to 0.
        """
        return pulumi.get(self, "tenant_features")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="webEndpoint")
    def web_endpoint(self) -> str:
        """
        Web endpoint URL of the hub.
        """
        return pulumi.get(self, "web_endpoint")


class AwaitableGetHubResult(GetHubResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetHubResult(
            api_endpoint=self.api_endpoint,
            hub_billing_info=self.hub_billing_info,
            id=self.id,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            tags=self.tags,
            tenant_features=self.tenant_features,
            type=self.type,
            web_endpoint=self.web_endpoint)


def get_hub(hub_name: Optional[str] = None,
            resource_group_name: Optional[str] = None,
            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetHubResult:
    """
    Hub resource.
    API Version: 2017-04-26.


    :param str hub_name: The name of the hub.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['hubName'] = hub_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:customerinsights:getHub', __args__, opts=opts, typ=GetHubResult).value

    return AwaitableGetHubResult(
        api_endpoint=__ret__.api_endpoint,
        hub_billing_info=__ret__.hub_billing_info,
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        tags=__ret__.tags,
        tenant_features=__ret__.tenant_features,
        type=__ret__.type,
        web_endpoint=__ret__.web_endpoint)


@_utilities.lift_output_func(get_hub)
def get_hub_output(hub_name: Optional[pulumi.Input[str]] = None,
                   resource_group_name: Optional[pulumi.Input[str]] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetHubResult]:
    """
    Hub resource.
    API Version: 2017-04-26.


    :param str hub_name: The name of the hub.
    :param str resource_group_name: The name of the resource group.
    """
    ...
