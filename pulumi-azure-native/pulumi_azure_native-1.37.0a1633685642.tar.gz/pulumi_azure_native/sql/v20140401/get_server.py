# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetServerResult',
    'AwaitableGetServerResult',
    'get_server',
    'get_server_output',
]

@pulumi.output_type
class GetServerResult:
    """
    Represents a server.
    """
    def __init__(__self__, administrator_login=None, external_administrator_login=None, external_administrator_sid=None, fully_qualified_domain_name=None, id=None, kind=None, location=None, name=None, state=None, tags=None, type=None, version=None):
        if administrator_login and not isinstance(administrator_login, str):
            raise TypeError("Expected argument 'administrator_login' to be a str")
        pulumi.set(__self__, "administrator_login", administrator_login)
        if external_administrator_login and not isinstance(external_administrator_login, str):
            raise TypeError("Expected argument 'external_administrator_login' to be a str")
        pulumi.set(__self__, "external_administrator_login", external_administrator_login)
        if external_administrator_sid and not isinstance(external_administrator_sid, str):
            raise TypeError("Expected argument 'external_administrator_sid' to be a str")
        pulumi.set(__self__, "external_administrator_sid", external_administrator_sid)
        if fully_qualified_domain_name and not isinstance(fully_qualified_domain_name, str):
            raise TypeError("Expected argument 'fully_qualified_domain_name' to be a str")
        pulumi.set(__self__, "fully_qualified_domain_name", fully_qualified_domain_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="administratorLogin")
    def administrator_login(self) -> Optional[str]:
        """
        Administrator username for the server. Can only be specified when the server is being created (and is required for creation).
        """
        return pulumi.get(self, "administrator_login")

    @property
    @pulumi.getter(name="externalAdministratorLogin")
    def external_administrator_login(self) -> str:
        """
        The display name of the Azure Active Directory object with admin permissions on this server. Legacy parameter, always null. To check for Active Directory admin, query .../servers/{serverName}/administrators
        """
        return pulumi.get(self, "external_administrator_login")

    @property
    @pulumi.getter(name="externalAdministratorSid")
    def external_administrator_sid(self) -> str:
        """
        The ID of the Active Azure Directory object with admin permissions on this server. Legacy parameter, always null. To check for Active Directory admin, query .../servers/{serverName}/administrators.
        """
        return pulumi.get(self, "external_administrator_sid")

    @property
    @pulumi.getter(name="fullyQualifiedDomainName")
    def fully_qualified_domain_name(self) -> str:
        """
        The fully qualified domain name of the server.
        """
        return pulumi.get(self, "fully_qualified_domain_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Kind of sql server.  This is metadata used for the Azure portal experience.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> str:
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
    @pulumi.getter
    def state(self) -> str:
        """
        The state of the server.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> Optional[str]:
        """
        The version of the server.
        """
        return pulumi.get(self, "version")


class AwaitableGetServerResult(GetServerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServerResult(
            administrator_login=self.administrator_login,
            external_administrator_login=self.external_administrator_login,
            external_administrator_sid=self.external_administrator_sid,
            fully_qualified_domain_name=self.fully_qualified_domain_name,
            id=self.id,
            kind=self.kind,
            location=self.location,
            name=self.name,
            state=self.state,
            tags=self.tags,
            type=self.type,
            version=self.version)


def get_server(resource_group_name: Optional[str] = None,
               server_name: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetServerResult:
    """
    Represents a server.


    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str server_name: The name of the server.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['serverName'] = server_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:sql/v20140401:getServer', __args__, opts=opts, typ=GetServerResult).value

    return AwaitableGetServerResult(
        administrator_login=__ret__.administrator_login,
        external_administrator_login=__ret__.external_administrator_login,
        external_administrator_sid=__ret__.external_administrator_sid,
        fully_qualified_domain_name=__ret__.fully_qualified_domain_name,
        id=__ret__.id,
        kind=__ret__.kind,
        location=__ret__.location,
        name=__ret__.name,
        state=__ret__.state,
        tags=__ret__.tags,
        type=__ret__.type,
        version=__ret__.version)


@_utilities.lift_output_func(get_server)
def get_server_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                      server_name: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetServerResult]:
    """
    Represents a server.


    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str server_name: The name of the server.
    """
    ...
