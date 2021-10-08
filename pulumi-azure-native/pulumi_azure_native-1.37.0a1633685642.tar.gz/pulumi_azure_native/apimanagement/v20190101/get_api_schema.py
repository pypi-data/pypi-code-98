# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetApiSchemaResult',
    'AwaitableGetApiSchemaResult',
    'get_api_schema',
    'get_api_schema_output',
]

@pulumi.output_type
class GetApiSchemaResult:
    """
    Schema Contract details.
    """
    def __init__(__self__, content_type=None, document=None, id=None, name=None, type=None):
        if content_type and not isinstance(content_type, str):
            raise TypeError("Expected argument 'content_type' to be a str")
        pulumi.set(__self__, "content_type", content_type)
        if document and not isinstance(document, dict):
            raise TypeError("Expected argument 'document' to be a dict")
        pulumi.set(__self__, "document", document)
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
    @pulumi.getter(name="contentType")
    def content_type(self) -> str:
        """
        Must be a valid a media type used in a Content-Type header as defined in the RFC 2616. Media type of the schema document (e.g. application/json, application/xml). </br> - `Swagger` Schema use `application/vnd.ms-azure-apim.swagger.definitions+json` </br> - `WSDL` Schema use `application/vnd.ms-azure-apim.xsd+xml` </br> - `OpenApi` Schema use `application/vnd.oai.openapi.components+json` </br> - `WADL Schema` use `application/vnd.ms-azure-apim.wadl.grammars+xml`. 
        """
        return pulumi.get(self, "content_type")

    @property
    @pulumi.getter
    def document(self) -> Optional[Any]:
        """
        Properties of the Schema Document.
        """
        return pulumi.get(self, "document")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

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
        Resource type for API Management resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetApiSchemaResult(GetApiSchemaResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetApiSchemaResult(
            content_type=self.content_type,
            document=self.document,
            id=self.id,
            name=self.name,
            type=self.type)


def get_api_schema(api_id: Optional[str] = None,
                   resource_group_name: Optional[str] = None,
                   schema_id: Optional[str] = None,
                   service_name: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetApiSchemaResult:
    """
    Schema Contract details.


    :param str api_id: API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
    :param str resource_group_name: The name of the resource group.
    :param str schema_id: Schema identifier within an API. Must be unique in the current API Management service instance.
    :param str service_name: The name of the API Management service.
    """
    __args__ = dict()
    __args__['apiId'] = api_id
    __args__['resourceGroupName'] = resource_group_name
    __args__['schemaId'] = schema_id
    __args__['serviceName'] = service_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:apimanagement/v20190101:getApiSchema', __args__, opts=opts, typ=GetApiSchemaResult).value

    return AwaitableGetApiSchemaResult(
        content_type=__ret__.content_type,
        document=__ret__.document,
        id=__ret__.id,
        name=__ret__.name,
        type=__ret__.type)


@_utilities.lift_output_func(get_api_schema)
def get_api_schema_output(api_id: Optional[pulumi.Input[str]] = None,
                          resource_group_name: Optional[pulumi.Input[str]] = None,
                          schema_id: Optional[pulumi.Input[str]] = None,
                          service_name: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetApiSchemaResult]:
    """
    Schema Contract details.


    :param str api_id: API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
    :param str resource_group_name: The name of the resource group.
    :param str schema_id: Schema identifier within an API. Must be unique in the current API Management service instance.
    :param str service_name: The name of the API Management service.
    """
    ...
