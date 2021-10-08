# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'GetDpsCertificateResult',
    'AwaitableGetDpsCertificateResult',
    'get_dps_certificate',
    'get_dps_certificate_output',
]

@pulumi.output_type
class GetDpsCertificateResult:
    """
    The X509 Certificate.
    """
    def __init__(__self__, etag=None, id=None, name=None, properties=None, type=None):
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        The entity tag.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The resource identifier.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the certificate.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> 'outputs.CertificatePropertiesResponse':
        """
        properties of a certificate
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetDpsCertificateResult(GetDpsCertificateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDpsCertificateResult(
            etag=self.etag,
            id=self.id,
            name=self.name,
            properties=self.properties,
            type=self.type)


def get_dps_certificate(certificate_name: Optional[str] = None,
                        provisioning_service_name: Optional[str] = None,
                        resource_group_name: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDpsCertificateResult:
    """
    The X509 Certificate.


    :param str certificate_name: Name of the certificate to retrieve.
    :param str provisioning_service_name: Name of the provisioning service the certificate is associated with.
    :param str resource_group_name: Resource group identifier.
    """
    __args__ = dict()
    __args__['certificateName'] = certificate_name
    __args__['provisioningServiceName'] = provisioning_service_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:devices/v20200301:getDpsCertificate', __args__, opts=opts, typ=GetDpsCertificateResult).value

    return AwaitableGetDpsCertificateResult(
        etag=__ret__.etag,
        id=__ret__.id,
        name=__ret__.name,
        properties=__ret__.properties,
        type=__ret__.type)


@_utilities.lift_output_func(get_dps_certificate)
def get_dps_certificate_output(certificate_name: Optional[pulumi.Input[str]] = None,
                               provisioning_service_name: Optional[pulumi.Input[str]] = None,
                               resource_group_name: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDpsCertificateResult]:
    """
    The X509 Certificate.


    :param str certificate_name: Name of the certificate to retrieve.
    :param str provisioning_service_name: Name of the provisioning service the certificate is associated with.
    :param str resource_group_name: Resource group identifier.
    """
    ...
