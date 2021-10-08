# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'ListDeviceRegistrationKeyResult',
    'AwaitableListDeviceRegistrationKeyResult',
    'list_device_registration_key',
    'list_device_registration_key_output',
]

@pulumi.output_type
class ListDeviceRegistrationKeyResult:
    """
    The device registration key.
    """
    def __init__(__self__, registration_key=None):
        if registration_key and not isinstance(registration_key, str):
            raise TypeError("Expected argument 'registration_key' to be a str")
        pulumi.set(__self__, "registration_key", registration_key)

    @property
    @pulumi.getter(name="registrationKey")
    def registration_key(self) -> str:
        """
        The registration key for the device.
        """
        return pulumi.get(self, "registration_key")


class AwaitableListDeviceRegistrationKeyResult(ListDeviceRegistrationKeyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListDeviceRegistrationKeyResult(
            registration_key=self.registration_key)


def list_device_registration_key(device_name: Optional[str] = None,
                                 resource_group_name: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListDeviceRegistrationKeyResult:
    """
    The device registration key.


    :param str device_name: The name of the device resource.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['deviceName'] = device_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:hybridnetwork/v20200101preview:listDeviceRegistrationKey', __args__, opts=opts, typ=ListDeviceRegistrationKeyResult).value

    return AwaitableListDeviceRegistrationKeyResult(
        registration_key=__ret__.registration_key)


@_utilities.lift_output_func(list_device_registration_key)
def list_device_registration_key_output(device_name: Optional[pulumi.Input[str]] = None,
                                        resource_group_name: Optional[pulumi.Input[str]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListDeviceRegistrationKeyResult]:
    """
    The device registration key.


    :param str device_name: The name of the device resource.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
