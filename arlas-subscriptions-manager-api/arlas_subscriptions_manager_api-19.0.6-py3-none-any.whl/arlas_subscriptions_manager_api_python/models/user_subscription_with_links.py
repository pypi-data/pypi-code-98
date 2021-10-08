# coding: utf-8

"""
    ARLAS Subscriptions Manager API

    Manage ARLAS subscriptions on ARLAS collections' events.

    OpenAPI spec version: 19.0.6
    Contact: contact@gisaia.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class UserSubscriptionWithLinks(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'created_at': 'int',
        'modified_at': 'int',
        'created_by_admin': 'bool',
        'deleted': 'bool',
        'created_by': 'str',
        'active': 'bool',
        'starts_at': 'int',
        'expires_at': 'int',
        'title': 'str',
        'subscription': 'Subscription',
        'user_metadatas': 'dict(str, object)',
        'links': 'dict(str, Link)'
    }

    attribute_map = {
        'id': 'id',
        'created_at': 'created_at',
        'modified_at': 'modified_at',
        'created_by_admin': 'created_by_admin',
        'deleted': 'deleted',
        'created_by': 'created_by',
        'active': 'active',
        'starts_at': 'starts_at',
        'expires_at': 'expires_at',
        'title': 'title',
        'subscription': 'subscription',
        'user_metadatas': 'userMetadatas',
        'links': '_links'
    }

    def __init__(self, id=None, created_at=None, modified_at=None, created_by_admin=None, deleted=None, created_by=None, active=None, starts_at=None, expires_at=None, title=None, subscription=None, user_metadatas=None, links=None):
        """
        UserSubscriptionWithLinks - a model defined in Swagger
        """

        self._id = None
        self._created_at = None
        self._modified_at = None
        self._created_by_admin = None
        self._deleted = None
        self._created_by = None
        self._active = None
        self._starts_at = None
        self._expires_at = None
        self._title = None
        self._subscription = None
        self._user_metadatas = None
        self._links = None

        if id is not None:
          self.id = id
        if created_at is not None:
          self.created_at = created_at
        if modified_at is not None:
          self.modified_at = modified_at
        if created_by_admin is not None:
          self.created_by_admin = created_by_admin
        if deleted is not None:
          self.deleted = deleted
        self.created_by = created_by
        self.active = active
        self.starts_at = starts_at
        self.expires_at = expires_at
        self.title = title
        self.subscription = subscription
        if user_metadatas is not None:
          self.user_metadatas = user_metadatas
        if links is not None:
          self.links = links

    @property
    def id(self):
        """
        Gets the id of this UserSubscriptionWithLinks.

        :return: The id of this UserSubscriptionWithLinks.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UserSubscriptionWithLinks.

        :param id: The id of this UserSubscriptionWithLinks.
        :type: str
        """

        self._id = id

    @property
    def created_at(self):
        """
        Gets the created_at of this UserSubscriptionWithLinks.

        :return: The created_at of this UserSubscriptionWithLinks.
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this UserSubscriptionWithLinks.

        :param created_at: The created_at of this UserSubscriptionWithLinks.
        :type: int
        """

        self._created_at = created_at

    @property
    def modified_at(self):
        """
        Gets the modified_at of this UserSubscriptionWithLinks.

        :return: The modified_at of this UserSubscriptionWithLinks.
        :rtype: int
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """
        Sets the modified_at of this UserSubscriptionWithLinks.

        :param modified_at: The modified_at of this UserSubscriptionWithLinks.
        :type: int
        """

        self._modified_at = modified_at

    @property
    def created_by_admin(self):
        """
        Gets the created_by_admin of this UserSubscriptionWithLinks.

        :return: The created_by_admin of this UserSubscriptionWithLinks.
        :rtype: bool
        """
        return self._created_by_admin

    @created_by_admin.setter
    def created_by_admin(self, created_by_admin):
        """
        Sets the created_by_admin of this UserSubscriptionWithLinks.

        :param created_by_admin: The created_by_admin of this UserSubscriptionWithLinks.
        :type: bool
        """

        self._created_by_admin = created_by_admin

    @property
    def deleted(self):
        """
        Gets the deleted of this UserSubscriptionWithLinks.

        :return: The deleted of this UserSubscriptionWithLinks.
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """
        Sets the deleted of this UserSubscriptionWithLinks.

        :param deleted: The deleted of this UserSubscriptionWithLinks.
        :type: bool
        """

        self._deleted = deleted

    @property
    def created_by(self):
        """
        Gets the created_by of this UserSubscriptionWithLinks.

        :return: The created_by of this UserSubscriptionWithLinks.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this UserSubscriptionWithLinks.

        :param created_by: The created_by of this UserSubscriptionWithLinks.
        :type: str
        """
        if created_by is None:
            raise ValueError("Invalid value for `created_by`, must not be `None`")

        self._created_by = created_by

    @property
    def active(self):
        """
        Gets the active of this UserSubscriptionWithLinks.

        :return: The active of this UserSubscriptionWithLinks.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this UserSubscriptionWithLinks.

        :param active: The active of this UserSubscriptionWithLinks.
        :type: bool
        """
        if active is None:
            raise ValueError("Invalid value for `active`, must not be `None`")

        self._active = active

    @property
    def starts_at(self):
        """
        Gets the starts_at of this UserSubscriptionWithLinks.

        :return: The starts_at of this UserSubscriptionWithLinks.
        :rtype: int
        """
        return self._starts_at

    @starts_at.setter
    def starts_at(self, starts_at):
        """
        Sets the starts_at of this UserSubscriptionWithLinks.

        :param starts_at: The starts_at of this UserSubscriptionWithLinks.
        :type: int
        """
        if starts_at is None:
            raise ValueError("Invalid value for `starts_at`, must not be `None`")

        self._starts_at = starts_at

    @property
    def expires_at(self):
        """
        Gets the expires_at of this UserSubscriptionWithLinks.

        :return: The expires_at of this UserSubscriptionWithLinks.
        :rtype: int
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """
        Sets the expires_at of this UserSubscriptionWithLinks.

        :param expires_at: The expires_at of this UserSubscriptionWithLinks.
        :type: int
        """
        if expires_at is None:
            raise ValueError("Invalid value for `expires_at`, must not be `None`")

        self._expires_at = expires_at

    @property
    def title(self):
        """
        Gets the title of this UserSubscriptionWithLinks.

        :return: The title of this UserSubscriptionWithLinks.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this UserSubscriptionWithLinks.

        :param title: The title of this UserSubscriptionWithLinks.
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")

        self._title = title

    @property
    def subscription(self):
        """
        Gets the subscription of this UserSubscriptionWithLinks.

        :return: The subscription of this UserSubscriptionWithLinks.
        :rtype: Subscription
        """
        return self._subscription

    @subscription.setter
    def subscription(self, subscription):
        """
        Sets the subscription of this UserSubscriptionWithLinks.

        :param subscription: The subscription of this UserSubscriptionWithLinks.
        :type: Subscription
        """
        if subscription is None:
            raise ValueError("Invalid value for `subscription`, must not be `None`")

        self._subscription = subscription

    @property
    def user_metadatas(self):
        """
        Gets the user_metadatas of this UserSubscriptionWithLinks.

        :return: The user_metadatas of this UserSubscriptionWithLinks.
        :rtype: dict(str, object)
        """
        return self._user_metadatas

    @user_metadatas.setter
    def user_metadatas(self, user_metadatas):
        """
        Sets the user_metadatas of this UserSubscriptionWithLinks.

        :param user_metadatas: The user_metadatas of this UserSubscriptionWithLinks.
        :type: dict(str, object)
        """

        self._user_metadatas = user_metadatas

    @property
    def links(self):
        """
        Gets the links of this UserSubscriptionWithLinks.

        :return: The links of this UserSubscriptionWithLinks.
        :rtype: dict(str, Link)
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this UserSubscriptionWithLinks.

        :param links: The links of this UserSubscriptionWithLinks.
        :type: dict(str, Link)
        """

        self._links = links

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, UserSubscriptionWithLinks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
