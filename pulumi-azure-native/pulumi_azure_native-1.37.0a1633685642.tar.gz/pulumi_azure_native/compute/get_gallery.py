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
    'GetGalleryResult',
    'AwaitableGetGalleryResult',
    'get_gallery',
    'get_gallery_output',
]

@pulumi.output_type
class GetGalleryResult:
    """
    Specifies information about the Shared Image Gallery that you want to create or update.
    """
    def __init__(__self__, description=None, id=None, identifier=None, location=None, name=None, provisioning_state=None, sharing_profile=None, tags=None, type=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identifier and not isinstance(identifier, dict):
            raise TypeError("Expected argument 'identifier' to be a dict")
        pulumi.set(__self__, "identifier", identifier)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if sharing_profile and not isinstance(sharing_profile, dict):
            raise TypeError("Expected argument 'sharing_profile' to be a dict")
        pulumi.set(__self__, "sharing_profile", sharing_profile)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of this Shared Image Gallery resource. This property is updatable.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identifier(self) -> Optional['outputs.GalleryIdentifierResponse']:
        """
        Describes the gallery unique name.
        """
        return pulumi.get(self, "identifier")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state, which only appears in the response.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="sharingProfile")
    def sharing_profile(self) -> Optional['outputs.SharingProfileResponse']:
        """
        Profile for gallery sharing to subscription or tenant
        """
        return pulumi.get(self, "sharing_profile")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type
        """
        return pulumi.get(self, "type")


class AwaitableGetGalleryResult(GetGalleryResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGalleryResult(
            description=self.description,
            id=self.id,
            identifier=self.identifier,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            sharing_profile=self.sharing_profile,
            tags=self.tags,
            type=self.type)


def get_gallery(gallery_name: Optional[str] = None,
                resource_group_name: Optional[str] = None,
                select: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGalleryResult:
    """
    Specifies information about the Shared Image Gallery that you want to create or update.
    API Version: 2020-09-30.


    :param str gallery_name: The name of the Shared Image Gallery.
    :param str resource_group_name: The name of the resource group.
    :param str select: The select expression to apply on the operation.
    """
    __args__ = dict()
    __args__['galleryName'] = gallery_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['select'] = select
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:compute:getGallery', __args__, opts=opts, typ=GetGalleryResult).value

    return AwaitableGetGalleryResult(
        description=__ret__.description,
        id=__ret__.id,
        identifier=__ret__.identifier,
        location=__ret__.location,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        sharing_profile=__ret__.sharing_profile,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_gallery)
def get_gallery_output(gallery_name: Optional[pulumi.Input[str]] = None,
                       resource_group_name: Optional[pulumi.Input[str]] = None,
                       select: Optional[pulumi.Input[Optional[str]]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetGalleryResult]:
    """
    Specifies information about the Shared Image Gallery that you want to create or update.
    API Version: 2020-09-30.


    :param str gallery_name: The name of the Shared Image Gallery.
    :param str resource_group_name: The name of the resource group.
    :param str select: The select expression to apply on the operation.
    """
    ...
