# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetApplicationResult',
    'AwaitableGetApplicationResult',
    'get_application',
    'get_application_output',
]

@pulumi.output_type
class GetApplicationResult:
    """
    Schema for Application properties.
    """
    def __init__(__self__, command_line_arguments=None, command_line_setting=None, description=None, file_path=None, friendly_name=None, icon_content=None, icon_hash=None, icon_index=None, icon_path=None, id=None, name=None, show_in_portal=None, type=None):
        if command_line_arguments and not isinstance(command_line_arguments, str):
            raise TypeError("Expected argument 'command_line_arguments' to be a str")
        pulumi.set(__self__, "command_line_arguments", command_line_arguments)
        if command_line_setting and not isinstance(command_line_setting, str):
            raise TypeError("Expected argument 'command_line_setting' to be a str")
        pulumi.set(__self__, "command_line_setting", command_line_setting)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if file_path and not isinstance(file_path, str):
            raise TypeError("Expected argument 'file_path' to be a str")
        pulumi.set(__self__, "file_path", file_path)
        if friendly_name and not isinstance(friendly_name, str):
            raise TypeError("Expected argument 'friendly_name' to be a str")
        pulumi.set(__self__, "friendly_name", friendly_name)
        if icon_content and not isinstance(icon_content, str):
            raise TypeError("Expected argument 'icon_content' to be a str")
        pulumi.set(__self__, "icon_content", icon_content)
        if icon_hash and not isinstance(icon_hash, str):
            raise TypeError("Expected argument 'icon_hash' to be a str")
        pulumi.set(__self__, "icon_hash", icon_hash)
        if icon_index and not isinstance(icon_index, int):
            raise TypeError("Expected argument 'icon_index' to be a int")
        pulumi.set(__self__, "icon_index", icon_index)
        if icon_path and not isinstance(icon_path, str):
            raise TypeError("Expected argument 'icon_path' to be a str")
        pulumi.set(__self__, "icon_path", icon_path)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if show_in_portal and not isinstance(show_in_portal, bool):
            raise TypeError("Expected argument 'show_in_portal' to be a bool")
        pulumi.set(__self__, "show_in_portal", show_in_portal)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="commandLineArguments")
    def command_line_arguments(self) -> Optional[str]:
        """
        Command Line Arguments for Application.
        """
        return pulumi.get(self, "command_line_arguments")

    @property
    @pulumi.getter(name="commandLineSetting")
    def command_line_setting(self) -> str:
        """
        Specifies whether this published application can be launched with command line arguments provided by the client, command line arguments specified at publish time, or no command line arguments at all.
        """
        return pulumi.get(self, "command_line_setting")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Description of Application.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="filePath")
    def file_path(self) -> Optional[str]:
        """
        Specifies a path for the executable file for the application.
        """
        return pulumi.get(self, "file_path")

    @property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[str]:
        """
        Friendly name of Application.
        """
        return pulumi.get(self, "friendly_name")

    @property
    @pulumi.getter(name="iconContent")
    def icon_content(self) -> str:
        """
        the icon a 64 bit string as a byte array.
        """
        return pulumi.get(self, "icon_content")

    @property
    @pulumi.getter(name="iconHash")
    def icon_hash(self) -> str:
        """
        Hash of the icon.
        """
        return pulumi.get(self, "icon_hash")

    @property
    @pulumi.getter(name="iconIndex")
    def icon_index(self) -> Optional[int]:
        """
        Index of the icon.
        """
        return pulumi.get(self, "icon_index")

    @property
    @pulumi.getter(name="iconPath")
    def icon_path(self) -> Optional[str]:
        """
        Path to icon.
        """
        return pulumi.get(self, "icon_path")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="showInPortal")
    def show_in_portal(self) -> Optional[bool]:
        """
        Specifies whether to show the RemoteApp program in the RD Web Access server.
        """
        return pulumi.get(self, "show_in_portal")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetApplicationResult(GetApplicationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetApplicationResult(
            command_line_arguments=self.command_line_arguments,
            command_line_setting=self.command_line_setting,
            description=self.description,
            file_path=self.file_path,
            friendly_name=self.friendly_name,
            icon_content=self.icon_content,
            icon_hash=self.icon_hash,
            icon_index=self.icon_index,
            icon_path=self.icon_path,
            id=self.id,
            name=self.name,
            show_in_portal=self.show_in_portal,
            type=self.type)


def get_application(application_group_name: Optional[str] = None,
                    application_name: Optional[str] = None,
                    resource_group_name: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetApplicationResult:
    """
    Schema for Application properties.


    :param str application_group_name: The name of the application group
    :param str application_name: The name of the application within the specified application group
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['applicationGroupName'] = application_group_name
    __args__['applicationName'] = application_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:desktopvirtualization/v20190924preview:getApplication', __args__, opts=opts, typ=GetApplicationResult).value

    return AwaitableGetApplicationResult(
        command_line_arguments=__ret__.command_line_arguments,
        command_line_setting=__ret__.command_line_setting,
        description=__ret__.description,
        file_path=__ret__.file_path,
        friendly_name=__ret__.friendly_name,
        icon_content=__ret__.icon_content,
        icon_hash=__ret__.icon_hash,
        icon_index=__ret__.icon_index,
        icon_path=__ret__.icon_path,
        id=__ret__.id,
        name=__ret__.name,
        show_in_portal=__ret__.show_in_portal,
        type=__ret__.type)


@_utilities.lift_output_func(get_application)
def get_application_output(application_group_name: Optional[pulumi.Input[str]] = None,
                           application_name: Optional[pulumi.Input[str]] = None,
                           resource_group_name: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetApplicationResult]:
    """
    Schema for Application properties.


    :param str application_group_name: The name of the application group
    :param str application_name: The name of the application within the specified application group
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
