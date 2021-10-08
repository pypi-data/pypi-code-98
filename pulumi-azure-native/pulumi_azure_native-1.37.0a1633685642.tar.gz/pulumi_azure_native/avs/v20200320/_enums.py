# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'InternetEnum',
    'SslEnum',
]


class InternetEnum(str, Enum):
    """
    Connectivity to internet is enabled or disabled
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class SslEnum(str, Enum):
    """
    Protect LDAP communication using SSL certificate (LDAPS)
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"
