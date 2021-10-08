# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['StorageAccountArgs', 'StorageAccount']

@pulumi.input_type
class StorageAccountArgs:
    def __init__(__self__, *,
                 kind: pulumi.Input['Kind'],
                 resource_group_name: pulumi.Input[str],
                 sku: pulumi.Input['SkuArgs'],
                 access_tier: Optional[pulumi.Input['AccessTier']] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 custom_domain: Optional[pulumi.Input['CustomDomainArgs']] = None,
                 enable_https_traffic_only: Optional[pulumi.Input[bool]] = None,
                 encryption: Optional[pulumi.Input['EncryptionArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a StorageAccount resource.
        :param pulumi.Input['Kind'] kind: Required. Indicates the type of storage account.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
        :param pulumi.Input['SkuArgs'] sku: Required. Gets or sets the sku name.
        :param pulumi.Input['AccessTier'] access_tier: Required for storage accounts where kind = BlobStorage. The access tier used for billing.
        :param pulumi.Input[str] account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
        :param pulumi.Input['CustomDomainArgs'] custom_domain: User domain assigned to the storage account. Name is the CNAME source. Only one custom domain is supported per storage account at this time. To clear the existing custom domain, use an empty string for the custom domain name property.
        :param pulumi.Input[bool] enable_https_traffic_only: Allows https traffic only to storage service if sets to true.
        :param pulumi.Input['EncryptionArgs'] encryption: Provides the encryption settings on the account. If left unspecified the account encryption settings will remain the same. The default setting is unencrypted.
        :param pulumi.Input[str] location: Required. Gets or sets the location of the resource. This will be one of the supported and registered Azure Geo Regions (e.g. West US, East US, Southeast Asia, etc.). The geo region of a resource cannot be changed once it is created, but if an identical geo region is specified on update, the request will succeed.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Gets or sets a list of key value pairs that describe the resource. These tags can be used for viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key with a length no greater than 128 characters and a value with a length no greater than 256 characters.
        """
        pulumi.set(__self__, "kind", kind)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "sku", sku)
        if access_tier is not None:
            pulumi.set(__self__, "access_tier", access_tier)
        if account_name is not None:
            pulumi.set(__self__, "account_name", account_name)
        if custom_domain is not None:
            pulumi.set(__self__, "custom_domain", custom_domain)
        if enable_https_traffic_only is None:
            enable_https_traffic_only = False
        if enable_https_traffic_only is not None:
            pulumi.set(__self__, "enable_https_traffic_only", enable_https_traffic_only)
        if encryption is not None:
            pulumi.set(__self__, "encryption", encryption)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Input['Kind']:
        """
        Required. Indicates the type of storage account.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: pulumi.Input['Kind']):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group within the user's subscription. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Input['SkuArgs']:
        """
        Required. Gets or sets the sku name.
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: pulumi.Input['SkuArgs']):
        pulumi.set(self, "sku", value)

    @property
    @pulumi.getter(name="accessTier")
    def access_tier(self) -> Optional[pulumi.Input['AccessTier']]:
        """
        Required for storage accounts where kind = BlobStorage. The access tier used for billing.
        """
        return pulumi.get(self, "access_tier")

    @access_tier.setter
    def access_tier(self, value: Optional[pulumi.Input['AccessTier']]):
        pulumi.set(self, "access_tier", value)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter(name="customDomain")
    def custom_domain(self) -> Optional[pulumi.Input['CustomDomainArgs']]:
        """
        User domain assigned to the storage account. Name is the CNAME source. Only one custom domain is supported per storage account at this time. To clear the existing custom domain, use an empty string for the custom domain name property.
        """
        return pulumi.get(self, "custom_domain")

    @custom_domain.setter
    def custom_domain(self, value: Optional[pulumi.Input['CustomDomainArgs']]):
        pulumi.set(self, "custom_domain", value)

    @property
    @pulumi.getter(name="enableHttpsTrafficOnly")
    def enable_https_traffic_only(self) -> Optional[pulumi.Input[bool]]:
        """
        Allows https traffic only to storage service if sets to true.
        """
        return pulumi.get(self, "enable_https_traffic_only")

    @enable_https_traffic_only.setter
    def enable_https_traffic_only(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_https_traffic_only", value)

    @property
    @pulumi.getter
    def encryption(self) -> Optional[pulumi.Input['EncryptionArgs']]:
        """
        Provides the encryption settings on the account. If left unspecified the account encryption settings will remain the same. The default setting is unencrypted.
        """
        return pulumi.get(self, "encryption")

    @encryption.setter
    def encryption(self, value: Optional[pulumi.Input['EncryptionArgs']]):
        pulumi.set(self, "encryption", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Required. Gets or sets the location of the resource. This will be one of the supported and registered Azure Geo Regions (e.g. West US, East US, Southeast Asia, etc.). The geo region of a resource cannot be changed once it is created, but if an identical geo region is specified on update, the request will succeed.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Gets or sets a list of key value pairs that describe the resource. These tags can be used for viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key with a length no greater than 128 characters and a value with a length no greater than 256 characters.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class StorageAccount(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_tier: Optional[pulumi.Input['AccessTier']] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 custom_domain: Optional[pulumi.Input[pulumi.InputType['CustomDomainArgs']]] = None,
                 enable_https_traffic_only: Optional[pulumi.Input[bool]] = None,
                 encryption: Optional[pulumi.Input[pulumi.InputType['EncryptionArgs']]] = None,
                 kind: Optional[pulumi.Input['Kind']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        The storage account.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input['AccessTier'] access_tier: Required for storage accounts where kind = BlobStorage. The access tier used for billing.
        :param pulumi.Input[str] account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
        :param pulumi.Input[pulumi.InputType['CustomDomainArgs']] custom_domain: User domain assigned to the storage account. Name is the CNAME source. Only one custom domain is supported per storage account at this time. To clear the existing custom domain, use an empty string for the custom domain name property.
        :param pulumi.Input[bool] enable_https_traffic_only: Allows https traffic only to storage service if sets to true.
        :param pulumi.Input[pulumi.InputType['EncryptionArgs']] encryption: Provides the encryption settings on the account. If left unspecified the account encryption settings will remain the same. The default setting is unencrypted.
        :param pulumi.Input['Kind'] kind: Required. Indicates the type of storage account.
        :param pulumi.Input[str] location: Required. Gets or sets the location of the resource. This will be one of the supported and registered Azure Geo Regions (e.g. West US, East US, Southeast Asia, etc.). The geo region of a resource cannot be changed once it is created, but if an identical geo region is specified on update, the request will succeed.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
        :param pulumi.Input[pulumi.InputType['SkuArgs']] sku: Required. Gets or sets the sku name.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Gets or sets a list of key value pairs that describe the resource. These tags can be used for viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key with a length no greater than 128 characters and a value with a length no greater than 256 characters.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: StorageAccountArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The storage account.

        :param str resource_name: The name of the resource.
        :param StorageAccountArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(StorageAccountArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_tier: Optional[pulumi.Input['AccessTier']] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 custom_domain: Optional[pulumi.Input[pulumi.InputType['CustomDomainArgs']]] = None,
                 enable_https_traffic_only: Optional[pulumi.Input[bool]] = None,
                 encryption: Optional[pulumi.Input[pulumi.InputType['EncryptionArgs']]] = None,
                 kind: Optional[pulumi.Input['Kind']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
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
            __props__ = StorageAccountArgs.__new__(StorageAccountArgs)

            __props__.__dict__["access_tier"] = access_tier
            __props__.__dict__["account_name"] = account_name
            __props__.__dict__["custom_domain"] = custom_domain
            if enable_https_traffic_only is None:
                enable_https_traffic_only = False
            __props__.__dict__["enable_https_traffic_only"] = enable_https_traffic_only
            __props__.__dict__["encryption"] = encryption
            if kind is None and not opts.urn:
                raise TypeError("Missing required property 'kind'")
            __props__.__dict__["kind"] = kind
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if sku is None and not opts.urn:
                raise TypeError("Missing required property 'sku'")
            __props__.__dict__["sku"] = sku
            __props__.__dict__["tags"] = tags
            __props__.__dict__["creation_time"] = None
            __props__.__dict__["last_geo_failover_time"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["primary_endpoints"] = None
            __props__.__dict__["primary_location"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["secondary_endpoints"] = None
            __props__.__dict__["secondary_location"] = None
            __props__.__dict__["status_of_primary"] = None
            __props__.__dict__["status_of_secondary"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:storage/v20161201:StorageAccount"), pulumi.Alias(type_="azure-native:storage:StorageAccount"), pulumi.Alias(type_="azure-nextgen:storage:StorageAccount"), pulumi.Alias(type_="azure-native:storage/v20150501preview:StorageAccount"), pulumi.Alias(type_="azure-nextgen:storage/v20150501preview:StorageAccount"), pulumi.Alias(type_="azure-native:storage/v20150615:StorageAccount"), pulumi.Alias(type_="azure-nextgen:storage/v20150615:StorageAccount"), pulumi.Alias(type_="azure-native:storage/v20160101:StorageAccount"), pulumi.Alias(type_="azure-nextgen:storage/v20160101:StorageAccount"), pulumi.Alias(type_="azure-native:storage/v20160501:StorageAccount"), pulumi.Alias(type_="azure-nextgen:storage/v20160501:StorageAccount"), pulumi.Alias(type_="azure-native:storage/v20170601:StorageAccount"), pulumi.Alias(type_="azure-nextgen:storage/v20170601:StorageAccount"), pulumi.Alias(type_="azure-native:storage/v20171001:StorageAccount"), pulumi.Alias(type_="azure-nextgen:storage/v20171001:StorageAccount"), pulumi.Alias(type_="azure-native:storage/v20180201:StorageAccount"), pulumi.Alias(type_="azure-nextgen:storage/v20180201:StorageAccount"), pulumi.Alias(type_="azure-native:storage/v20180301preview:StorageAccount"), pulumi.Alias(type_="azure-nextgen:storage/v20180301preview:StorageAccount"), pulumi.Alias(type_="azure-native:storage/v20180701:StorageAccount"), pulumi.Alias(type_="azure-nextgen:storage/v20180701:StorageAccount"), pulumi.Alias(type_="azure-native:storage/v20181101:StorageAccount"), pulumi.Alias(type_="azure-nextgen:storage/v20181101:StorageAccount"), pulumi.Alias(type_="azure-native:storage/v20190401:StorageAccount"), pulumi.Alias(type_="azure-nextgen:storage/v20190401:StorageAccount"), pulumi.Alias(type_="azure-native:storage/v20190601:StorageAccount"), pulumi.Alias(type_="azure-nextgen:storage/v20190601:StorageAccount"), pulumi.Alias(type_="azure-native:storage/v20200801preview:StorageAccount"), pulumi.Alias(type_="azure-nextgen:storage/v20200801preview:StorageAccount"), pulumi.Alias(type_="azure-native:storage/v20210101:StorageAccount"), pulumi.Alias(type_="azure-nextgen:storage/v20210101:StorageAccount"), pulumi.Alias(type_="azure-native:storage/v20210201:StorageAccount"), pulumi.Alias(type_="azure-nextgen:storage/v20210201:StorageAccount"), pulumi.Alias(type_="azure-native:storage/v20210401:StorageAccount"), pulumi.Alias(type_="azure-nextgen:storage/v20210401:StorageAccount"), pulumi.Alias(type_="azure-native:storage/v20210601:StorageAccount"), pulumi.Alias(type_="azure-nextgen:storage/v20210601:StorageAccount")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(StorageAccount, __self__).__init__(
            'azure-native:storage/v20161201:StorageAccount',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'StorageAccount':
        """
        Get an existing StorageAccount resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = StorageAccountArgs.__new__(StorageAccountArgs)

        __props__.__dict__["access_tier"] = None
        __props__.__dict__["creation_time"] = None
        __props__.__dict__["custom_domain"] = None
        __props__.__dict__["enable_https_traffic_only"] = None
        __props__.__dict__["encryption"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["last_geo_failover_time"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["primary_endpoints"] = None
        __props__.__dict__["primary_location"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["secondary_endpoints"] = None
        __props__.__dict__["secondary_location"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["status_of_primary"] = None
        __props__.__dict__["status_of_secondary"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return StorageAccount(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessTier")
    def access_tier(self) -> pulumi.Output[str]:
        """
        Required for storage accounts where kind = BlobStorage. The access tier used for billing.
        """
        return pulumi.get(self, "access_tier")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[str]:
        """
        Gets the creation date and time of the storage account in UTC.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="customDomain")
    def custom_domain(self) -> pulumi.Output['outputs.CustomDomainResponse']:
        """
        Gets the custom domain the user assigned to this storage account.
        """
        return pulumi.get(self, "custom_domain")

    @property
    @pulumi.getter(name="enableHttpsTrafficOnly")
    def enable_https_traffic_only(self) -> pulumi.Output[Optional[bool]]:
        """
        Allows https traffic only to storage service if sets to true.
        """
        return pulumi.get(self, "enable_https_traffic_only")

    @property
    @pulumi.getter
    def encryption(self) -> pulumi.Output['outputs.EncryptionResponse']:
        """
        Gets the encryption settings on the account. If unspecified, the account is unencrypted.
        """
        return pulumi.get(self, "encryption")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        Gets the Kind.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="lastGeoFailoverTime")
    def last_geo_failover_time(self) -> pulumi.Output[str]:
        """
        Gets the timestamp of the most recent instance of a failover to the secondary location. Only the most recent timestamp is retained. This element is not returned if there has never been a failover instance. Only available if the accountType is Standard_GRS or Standard_RAGRS.
        """
        return pulumi.get(self, "last_geo_failover_time")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="primaryEndpoints")
    def primary_endpoints(self) -> pulumi.Output['outputs.EndpointsResponse']:
        """
        Gets the URLs that are used to perform a retrieval of a public blob, queue, or table object. Note that Standard_ZRS and Premium_LRS accounts only return the blob endpoint.
        """
        return pulumi.get(self, "primary_endpoints")

    @property
    @pulumi.getter(name="primaryLocation")
    def primary_location(self) -> pulumi.Output[str]:
        """
        Gets the location of the primary data center for the storage account.
        """
        return pulumi.get(self, "primary_location")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Gets the status of the storage account at the time the operation was called.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="secondaryEndpoints")
    def secondary_endpoints(self) -> pulumi.Output['outputs.EndpointsResponse']:
        """
        Gets the URLs that are used to perform a retrieval of a public blob, queue, or table object from the secondary location of the storage account. Only available if the SKU name is Standard_RAGRS.
        """
        return pulumi.get(self, "secondary_endpoints")

    @property
    @pulumi.getter(name="secondaryLocation")
    def secondary_location(self) -> pulumi.Output[str]:
        """
        Gets the location of the geo-replicated secondary for the storage account. Only available if the accountType is Standard_GRS or Standard_RAGRS.
        """
        return pulumi.get(self, "secondary_location")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output['outputs.SkuResponse']:
        """
        Gets the SKU.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="statusOfPrimary")
    def status_of_primary(self) -> pulumi.Output[str]:
        """
        Gets the status indicating whether the primary location of the storage account is available or unavailable.
        """
        return pulumi.get(self, "status_of_primary")

    @property
    @pulumi.getter(name="statusOfSecondary")
    def status_of_secondary(self) -> pulumi.Output[str]:
        """
        Gets the status indicating whether the secondary location of the storage account is available or unavailable. Only available if the SKU name is Standard_GRS or Standard_RAGRS.
        """
        return pulumi.get(self, "status_of_secondary")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Tags assigned to a resource; can be used for viewing and grouping a resource (across resource groups).
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

