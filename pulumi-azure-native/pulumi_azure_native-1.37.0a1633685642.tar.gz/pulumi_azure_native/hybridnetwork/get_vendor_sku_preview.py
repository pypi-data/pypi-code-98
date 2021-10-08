# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetVendorSkuPreviewResult',
    'AwaitableGetVendorSkuPreviewResult',
    'get_vendor_sku_preview',
    'get_vendor_sku_preview_output',
]

@pulumi.output_type
class GetVendorSkuPreviewResult:
    """
    Customer subscription which can use a sku.
    """
    def __init__(__self__, id=None, name=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ARM ID of the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The preview subscription ID.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetVendorSkuPreviewResult(GetVendorSkuPreviewResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVendorSkuPreviewResult(
            id=self.id,
            name=self.name,
            type=self.type)


def get_vendor_sku_preview(preview_subscription: Optional[str] = None,
                           sku_name: Optional[str] = None,
                           vendor_name: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVendorSkuPreviewResult:
    """
    Customer subscription which can use a sku.
    API Version: 2020-01-01-preview.


    :param str preview_subscription: Preview subscription ID.
    :param str sku_name: The name of the vendor sku.
    :param str vendor_name: The name of the vendor.
    """
    __args__ = dict()
    __args__['previewSubscription'] = preview_subscription
    __args__['skuName'] = sku_name
    __args__['vendorName'] = vendor_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:hybridnetwork:getVendorSkuPreview', __args__, opts=opts, typ=GetVendorSkuPreviewResult).value

    return AwaitableGetVendorSkuPreviewResult(
        id=__ret__.id,
        name=__ret__.name,
        type=__ret__.type)


@_utilities.lift_output_func(get_vendor_sku_preview)
def get_vendor_sku_preview_output(preview_subscription: Optional[pulumi.Input[str]] = None,
                                  sku_name: Optional[pulumi.Input[str]] = None,
                                  vendor_name: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVendorSkuPreviewResult]:
    """
    Customer subscription which can use a sku.
    API Version: 2020-01-01-preview.


    :param str preview_subscription: Preview subscription ID.
    :param str sku_name: The name of the vendor sku.
    :param str vendor_name: The name of the vendor.
    """
    ...
