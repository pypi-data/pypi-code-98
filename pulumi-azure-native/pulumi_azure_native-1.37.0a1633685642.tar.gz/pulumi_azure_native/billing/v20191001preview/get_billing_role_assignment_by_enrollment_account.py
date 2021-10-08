# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetBillingRoleAssignmentByEnrollmentAccountResult',
    'AwaitableGetBillingRoleAssignmentByEnrollmentAccountResult',
    'get_billing_role_assignment_by_enrollment_account',
    'get_billing_role_assignment_by_enrollment_account_output',
]

@pulumi.output_type
class GetBillingRoleAssignmentByEnrollmentAccountResult:
    """
    The role assignment
    """
    def __init__(__self__, created_by_principal_id=None, created_by_principal_tenant_id=None, created_by_user_email_address=None, created_on=None, id=None, name=None, principal_id=None, principal_tenant_id=None, role_definition_id=None, scope=None, type=None, user_authentication_type=None, user_email_address=None):
        if created_by_principal_id and not isinstance(created_by_principal_id, str):
            raise TypeError("Expected argument 'created_by_principal_id' to be a str")
        pulumi.set(__self__, "created_by_principal_id", created_by_principal_id)
        if created_by_principal_tenant_id and not isinstance(created_by_principal_tenant_id, str):
            raise TypeError("Expected argument 'created_by_principal_tenant_id' to be a str")
        pulumi.set(__self__, "created_by_principal_tenant_id", created_by_principal_tenant_id)
        if created_by_user_email_address and not isinstance(created_by_user_email_address, str):
            raise TypeError("Expected argument 'created_by_user_email_address' to be a str")
        pulumi.set(__self__, "created_by_user_email_address", created_by_user_email_address)
        if created_on and not isinstance(created_on, str):
            raise TypeError("Expected argument 'created_on' to be a str")
        pulumi.set(__self__, "created_on", created_on)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if principal_id and not isinstance(principal_id, str):
            raise TypeError("Expected argument 'principal_id' to be a str")
        pulumi.set(__self__, "principal_id", principal_id)
        if principal_tenant_id and not isinstance(principal_tenant_id, str):
            raise TypeError("Expected argument 'principal_tenant_id' to be a str")
        pulumi.set(__self__, "principal_tenant_id", principal_tenant_id)
        if role_definition_id and not isinstance(role_definition_id, str):
            raise TypeError("Expected argument 'role_definition_id' to be a str")
        pulumi.set(__self__, "role_definition_id", role_definition_id)
        if scope and not isinstance(scope, str):
            raise TypeError("Expected argument 'scope' to be a str")
        pulumi.set(__self__, "scope", scope)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if user_authentication_type and not isinstance(user_authentication_type, str):
            raise TypeError("Expected argument 'user_authentication_type' to be a str")
        pulumi.set(__self__, "user_authentication_type", user_authentication_type)
        if user_email_address and not isinstance(user_email_address, str):
            raise TypeError("Expected argument 'user_email_address' to be a str")
        pulumi.set(__self__, "user_email_address", user_email_address)

    @property
    @pulumi.getter(name="createdByPrincipalId")
    def created_by_principal_id(self) -> str:
        """
        The principal Id of the user who created the role assignment.
        """
        return pulumi.get(self, "created_by_principal_id")

    @property
    @pulumi.getter(name="createdByPrincipalTenantId")
    def created_by_principal_tenant_id(self) -> str:
        """
        The tenant Id of the user who created the role assignment.
        """
        return pulumi.get(self, "created_by_principal_tenant_id")

    @property
    @pulumi.getter(name="createdByUserEmailAddress")
    def created_by_user_email_address(self) -> str:
        """
        The email address of the user who created the role assignment. This is supported only for billing accounts with agreement type Enterprise Agreement.
        """
        return pulumi.get(self, "created_by_user_email_address")

    @property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> str:
        """
        The date the role assignment was created.
        """
        return pulumi.get(self, "created_on")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id.
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
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[str]:
        """
        The principal id of the user to whom the role was assigned.
        """
        return pulumi.get(self, "principal_id")

    @property
    @pulumi.getter(name="principalTenantId")
    def principal_tenant_id(self) -> Optional[str]:
        """
        The principal tenant id of the user to whom the role was assigned.
        """
        return pulumi.get(self, "principal_tenant_id")

    @property
    @pulumi.getter(name="roleDefinitionId")
    def role_definition_id(self) -> Optional[str]:
        """
        The ID of the role definition.
        """
        return pulumi.get(self, "role_definition_id")

    @property
    @pulumi.getter
    def scope(self) -> str:
        """
        The scope at which the role was assigned.
        """
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="userAuthenticationType")
    def user_authentication_type(self) -> Optional[str]:
        """
        The authentication type of the user, whether Organization or MSA, of the user to whom the role was assigned. This is supported only for billing accounts with agreement type Enterprise Agreement.
        """
        return pulumi.get(self, "user_authentication_type")

    @property
    @pulumi.getter(name="userEmailAddress")
    def user_email_address(self) -> Optional[str]:
        """
        The email address of the user to whom the role was assigned. This is supported only for billing accounts with agreement type Enterprise Agreement.
        """
        return pulumi.get(self, "user_email_address")


class AwaitableGetBillingRoleAssignmentByEnrollmentAccountResult(GetBillingRoleAssignmentByEnrollmentAccountResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBillingRoleAssignmentByEnrollmentAccountResult(
            created_by_principal_id=self.created_by_principal_id,
            created_by_principal_tenant_id=self.created_by_principal_tenant_id,
            created_by_user_email_address=self.created_by_user_email_address,
            created_on=self.created_on,
            id=self.id,
            name=self.name,
            principal_id=self.principal_id,
            principal_tenant_id=self.principal_tenant_id,
            role_definition_id=self.role_definition_id,
            scope=self.scope,
            type=self.type,
            user_authentication_type=self.user_authentication_type,
            user_email_address=self.user_email_address)


def get_billing_role_assignment_by_enrollment_account(billing_account_name: Optional[str] = None,
                                                      billing_role_assignment_name: Optional[str] = None,
                                                      enrollment_account_name: Optional[str] = None,
                                                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBillingRoleAssignmentByEnrollmentAccountResult:
    """
    The role assignment


    :param str billing_account_name: The ID that uniquely identifies a billing account.
    :param str billing_role_assignment_name: The ID that uniquely identifies a role assignment.
    :param str enrollment_account_name: The ID that uniquely identifies an enrollment account.
    """
    __args__ = dict()
    __args__['billingAccountName'] = billing_account_name
    __args__['billingRoleAssignmentName'] = billing_role_assignment_name
    __args__['enrollmentAccountName'] = enrollment_account_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:billing/v20191001preview:getBillingRoleAssignmentByEnrollmentAccount', __args__, opts=opts, typ=GetBillingRoleAssignmentByEnrollmentAccountResult).value

    return AwaitableGetBillingRoleAssignmentByEnrollmentAccountResult(
        created_by_principal_id=__ret__.created_by_principal_id,
        created_by_principal_tenant_id=__ret__.created_by_principal_tenant_id,
        created_by_user_email_address=__ret__.created_by_user_email_address,
        created_on=__ret__.created_on,
        id=__ret__.id,
        name=__ret__.name,
        principal_id=__ret__.principal_id,
        principal_tenant_id=__ret__.principal_tenant_id,
        role_definition_id=__ret__.role_definition_id,
        scope=__ret__.scope,
        type=__ret__.type,
        user_authentication_type=__ret__.user_authentication_type,
        user_email_address=__ret__.user_email_address)


@_utilities.lift_output_func(get_billing_role_assignment_by_enrollment_account)
def get_billing_role_assignment_by_enrollment_account_output(billing_account_name: Optional[pulumi.Input[str]] = None,
                                                             billing_role_assignment_name: Optional[pulumi.Input[str]] = None,
                                                             enrollment_account_name: Optional[pulumi.Input[str]] = None,
                                                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBillingRoleAssignmentByEnrollmentAccountResult]:
    """
    The role assignment


    :param str billing_account_name: The ID that uniquely identifies a billing account.
    :param str billing_role_assignment_name: The ID that uniquely identifies a role assignment.
    :param str enrollment_account_name: The ID that uniquely identifies an enrollment account.
    """
    ...
