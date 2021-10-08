# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetCustomAssessmentAutomationResult',
    'AwaitableGetCustomAssessmentAutomationResult',
    'get_custom_assessment_automation',
    'get_custom_assessment_automation_output',
]

@pulumi.output_type
class GetCustomAssessmentAutomationResult:
    """
    Custom Assessment Automation
    """
    def __init__(__self__, compressed_query=None, description=None, id=None, implementation_effort=None, name=None, remediation_description=None, severity=None, supported_cloud=None, type=None, user_impact=None):
        if compressed_query and not isinstance(compressed_query, str):
            raise TypeError("Expected argument 'compressed_query' to be a str")
        pulumi.set(__self__, "compressed_query", compressed_query)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if implementation_effort and not isinstance(implementation_effort, str):
            raise TypeError("Expected argument 'implementation_effort' to be a str")
        pulumi.set(__self__, "implementation_effort", implementation_effort)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if remediation_description and not isinstance(remediation_description, str):
            raise TypeError("Expected argument 'remediation_description' to be a str")
        pulumi.set(__self__, "remediation_description", remediation_description)
        if severity and not isinstance(severity, str):
            raise TypeError("Expected argument 'severity' to be a str")
        pulumi.set(__self__, "severity", severity)
        if supported_cloud and not isinstance(supported_cloud, str):
            raise TypeError("Expected argument 'supported_cloud' to be a str")
        pulumi.set(__self__, "supported_cloud", supported_cloud)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if user_impact and not isinstance(user_impact, str):
            raise TypeError("Expected argument 'user_impact' to be a str")
        pulumi.set(__self__, "user_impact", user_impact)

    @property
    @pulumi.getter(name="compressedQuery")
    def compressed_query(self) -> Optional[str]:
        """
        GZip encoded KQL query representing the assessment automation results required.
        """
        return pulumi.get(self, "compressed_query")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description to relate to the assessments generated by this assessment automation.
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
    @pulumi.getter(name="implementationEffort")
    def implementation_effort(self) -> Optional[str]:
        """
        The implementation effort to relate to the assessments generated by this assessment automation.
        """
        return pulumi.get(self, "implementation_effort")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="remediationDescription")
    def remediation_description(self) -> Optional[str]:
        """
        The remediation description to relate to the assessments generated by this assessment automation.
        """
        return pulumi.get(self, "remediation_description")

    @property
    @pulumi.getter
    def severity(self) -> Optional[str]:
        """
        The severity to relate to the assessments generated by this assessment automation.
        """
        return pulumi.get(self, "severity")

    @property
    @pulumi.getter(name="supportedCloud")
    def supported_cloud(self) -> Optional[str]:
        """
        Relevant cloud for the custom assessment automation.
        """
        return pulumi.get(self, "supported_cloud")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="userImpact")
    def user_impact(self) -> Optional[str]:
        """
        The user impact to relate to the assessments generated by this assessment automation.
        """
        return pulumi.get(self, "user_impact")


class AwaitableGetCustomAssessmentAutomationResult(GetCustomAssessmentAutomationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCustomAssessmentAutomationResult(
            compressed_query=self.compressed_query,
            description=self.description,
            id=self.id,
            implementation_effort=self.implementation_effort,
            name=self.name,
            remediation_description=self.remediation_description,
            severity=self.severity,
            supported_cloud=self.supported_cloud,
            type=self.type,
            user_impact=self.user_impact)


def get_custom_assessment_automation(custom_assessment_automation_name: Optional[str] = None,
                                     resource_group_name: Optional[str] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCustomAssessmentAutomationResult:
    """
    Custom Assessment Automation


    :param str custom_assessment_automation_name: Name of the Custom Assessment Automation.
    :param str resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
    """
    __args__ = dict()
    __args__['customAssessmentAutomationName'] = custom_assessment_automation_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:security/v20210701preview:getCustomAssessmentAutomation', __args__, opts=opts, typ=GetCustomAssessmentAutomationResult).value

    return AwaitableGetCustomAssessmentAutomationResult(
        compressed_query=__ret__.compressed_query,
        description=__ret__.description,
        id=__ret__.id,
        implementation_effort=__ret__.implementation_effort,
        name=__ret__.name,
        remediation_description=__ret__.remediation_description,
        severity=__ret__.severity,
        supported_cloud=__ret__.supported_cloud,
        type=__ret__.type,
        user_impact=__ret__.user_impact)


@_utilities.lift_output_func(get_custom_assessment_automation)
def get_custom_assessment_automation_output(custom_assessment_automation_name: Optional[pulumi.Input[str]] = None,
                                            resource_group_name: Optional[pulumi.Input[str]] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCustomAssessmentAutomationResult]:
    """
    Custom Assessment Automation


    :param str custom_assessment_automation_name: Name of the Custom Assessment Automation.
    :param str resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
    """
    ...
