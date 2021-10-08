# coding: utf-8

"""
    ARLAS Exploration API

    Explore the content of ARLAS collections  # noqa: E501

    OpenAPI spec version: 19.0.6
    Contact: contact@gisaia.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CollectionReferenceParameters(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'index_name': 'str',
        'id_path': 'str',
        'geometry_path': 'str',
        'centroid_path': 'str',
        'h3_path': 'str',
        'timestamp_path': 'str',
        'exclude_fields': 'str',
        'update_max_hits': 'int',
        'taggable_fields': 'str',
        'exclude_wfs_fields': 'str',
        'custom_params': 'dict(str, str)',
        'atom_feed': 'Feed',
        'open_search': 'OpenSearch',
        'inspire': 'Inspire',
        'dublin_core_element_name': 'DublinCoreElementName',
        'raster_tile_url': 'RasterTileURL',
        'raster_tile_width': 'int',
        'raster_tile_height': 'int',
        'filter': 'Filter'
    }

    attribute_map = {
        'index_name': 'index_name',
        'id_path': 'id_path',
        'geometry_path': 'geometry_path',
        'centroid_path': 'centroid_path',
        'h3_path': 'h3_path',
        'timestamp_path': 'timestamp_path',
        'exclude_fields': 'exclude_fields',
        'update_max_hits': 'update_max_hits',
        'taggable_fields': 'taggable_fields',
        'exclude_wfs_fields': 'exclude_wfs_fields',
        'custom_params': 'custom_params',
        'atom_feed': 'atom_feed',
        'open_search': 'open_search',
        'inspire': 'inspire',
        'dublin_core_element_name': 'dublin_core_element_name',
        'raster_tile_url': 'raster_tile_url',
        'raster_tile_width': 'raster_tile_width',
        'raster_tile_height': 'raster_tile_height',
        'filter': 'filter'
    }

    def __init__(self, index_name=None, id_path=None, geometry_path=None, centroid_path=None, h3_path=None, timestamp_path=None, exclude_fields=None, update_max_hits=None, taggable_fields=None, exclude_wfs_fields=None, custom_params=None, atom_feed=None, open_search=None, inspire=None, dublin_core_element_name=None, raster_tile_url=None, raster_tile_width=None, raster_tile_height=None, filter=None):  # noqa: E501
        """CollectionReferenceParameters - a model defined in Swagger"""  # noqa: E501

        self._index_name = None
        self._id_path = None
        self._geometry_path = None
        self._centroid_path = None
        self._h3_path = None
        self._timestamp_path = None
        self._exclude_fields = None
        self._update_max_hits = None
        self._taggable_fields = None
        self._exclude_wfs_fields = None
        self._custom_params = None
        self._atom_feed = None
        self._open_search = None
        self._inspire = None
        self._dublin_core_element_name = None
        self._raster_tile_url = None
        self._raster_tile_width = None
        self._raster_tile_height = None
        self._filter = None
        self.discriminator = None

        self.index_name = index_name
        self.id_path = id_path
        self.geometry_path = geometry_path
        self.centroid_path = centroid_path
        if h3_path is not None:
            self.h3_path = h3_path
        self.timestamp_path = timestamp_path
        if exclude_fields is not None:
            self.exclude_fields = exclude_fields
        if update_max_hits is not None:
            self.update_max_hits = update_max_hits
        if taggable_fields is not None:
            self.taggable_fields = taggable_fields
        if exclude_wfs_fields is not None:
            self.exclude_wfs_fields = exclude_wfs_fields
        if custom_params is not None:
            self.custom_params = custom_params
        if atom_feed is not None:
            self.atom_feed = atom_feed
        if open_search is not None:
            self.open_search = open_search
        if inspire is not None:
            self.inspire = inspire
        if dublin_core_element_name is not None:
            self.dublin_core_element_name = dublin_core_element_name
        if raster_tile_url is not None:
            self.raster_tile_url = raster_tile_url
        if raster_tile_width is not None:
            self.raster_tile_width = raster_tile_width
        if raster_tile_height is not None:
            self.raster_tile_height = raster_tile_height
        if filter is not None:
            self.filter = filter

    @property
    def index_name(self):
        """Gets the index_name of this CollectionReferenceParameters.  # noqa: E501


        :return: The index_name of this CollectionReferenceParameters.  # noqa: E501
        :rtype: str
        """
        return self._index_name

    @index_name.setter
    def index_name(self, index_name):
        """Sets the index_name of this CollectionReferenceParameters.


        :param index_name: The index_name of this CollectionReferenceParameters.  # noqa: E501
        :type: str
        """
        if index_name is None:
            raise ValueError("Invalid value for `index_name`, must not be `None`")  # noqa: E501

        self._index_name = index_name

    @property
    def id_path(self):
        """Gets the id_path of this CollectionReferenceParameters.  # noqa: E501


        :return: The id_path of this CollectionReferenceParameters.  # noqa: E501
        :rtype: str
        """
        return self._id_path

    @id_path.setter
    def id_path(self, id_path):
        """Sets the id_path of this CollectionReferenceParameters.


        :param id_path: The id_path of this CollectionReferenceParameters.  # noqa: E501
        :type: str
        """
        if id_path is None:
            raise ValueError("Invalid value for `id_path`, must not be `None`")  # noqa: E501

        self._id_path = id_path

    @property
    def geometry_path(self):
        """Gets the geometry_path of this CollectionReferenceParameters.  # noqa: E501


        :return: The geometry_path of this CollectionReferenceParameters.  # noqa: E501
        :rtype: str
        """
        return self._geometry_path

    @geometry_path.setter
    def geometry_path(self, geometry_path):
        """Sets the geometry_path of this CollectionReferenceParameters.


        :param geometry_path: The geometry_path of this CollectionReferenceParameters.  # noqa: E501
        :type: str
        """
        if geometry_path is None:
            raise ValueError("Invalid value for `geometry_path`, must not be `None`")  # noqa: E501

        self._geometry_path = geometry_path

    @property
    def centroid_path(self):
        """Gets the centroid_path of this CollectionReferenceParameters.  # noqa: E501


        :return: The centroid_path of this CollectionReferenceParameters.  # noqa: E501
        :rtype: str
        """
        return self._centroid_path

    @centroid_path.setter
    def centroid_path(self, centroid_path):
        """Sets the centroid_path of this CollectionReferenceParameters.


        :param centroid_path: The centroid_path of this CollectionReferenceParameters.  # noqa: E501
        :type: str
        """
        if centroid_path is None:
            raise ValueError("Invalid value for `centroid_path`, must not be `None`")  # noqa: E501

        self._centroid_path = centroid_path

    @property
    def h3_path(self):
        """Gets the h3_path of this CollectionReferenceParameters.  # noqa: E501


        :return: The h3_path of this CollectionReferenceParameters.  # noqa: E501
        :rtype: str
        """
        return self._h3_path

    @h3_path.setter
    def h3_path(self, h3_path):
        """Sets the h3_path of this CollectionReferenceParameters.


        :param h3_path: The h3_path of this CollectionReferenceParameters.  # noqa: E501
        :type: str
        """

        self._h3_path = h3_path

    @property
    def timestamp_path(self):
        """Gets the timestamp_path of this CollectionReferenceParameters.  # noqa: E501


        :return: The timestamp_path of this CollectionReferenceParameters.  # noqa: E501
        :rtype: str
        """
        return self._timestamp_path

    @timestamp_path.setter
    def timestamp_path(self, timestamp_path):
        """Sets the timestamp_path of this CollectionReferenceParameters.


        :param timestamp_path: The timestamp_path of this CollectionReferenceParameters.  # noqa: E501
        :type: str
        """
        if timestamp_path is None:
            raise ValueError("Invalid value for `timestamp_path`, must not be `None`")  # noqa: E501

        self._timestamp_path = timestamp_path

    @property
    def exclude_fields(self):
        """Gets the exclude_fields of this CollectionReferenceParameters.  # noqa: E501


        :return: The exclude_fields of this CollectionReferenceParameters.  # noqa: E501
        :rtype: str
        """
        return self._exclude_fields

    @exclude_fields.setter
    def exclude_fields(self, exclude_fields):
        """Sets the exclude_fields of this CollectionReferenceParameters.


        :param exclude_fields: The exclude_fields of this CollectionReferenceParameters.  # noqa: E501
        :type: str
        """

        self._exclude_fields = exclude_fields

    @property
    def update_max_hits(self):
        """Gets the update_max_hits of this CollectionReferenceParameters.  # noqa: E501


        :return: The update_max_hits of this CollectionReferenceParameters.  # noqa: E501
        :rtype: int
        """
        return self._update_max_hits

    @update_max_hits.setter
    def update_max_hits(self, update_max_hits):
        """Sets the update_max_hits of this CollectionReferenceParameters.


        :param update_max_hits: The update_max_hits of this CollectionReferenceParameters.  # noqa: E501
        :type: int
        """

        self._update_max_hits = update_max_hits

    @property
    def taggable_fields(self):
        """Gets the taggable_fields of this CollectionReferenceParameters.  # noqa: E501


        :return: The taggable_fields of this CollectionReferenceParameters.  # noqa: E501
        :rtype: str
        """
        return self._taggable_fields

    @taggable_fields.setter
    def taggable_fields(self, taggable_fields):
        """Sets the taggable_fields of this CollectionReferenceParameters.


        :param taggable_fields: The taggable_fields of this CollectionReferenceParameters.  # noqa: E501
        :type: str
        """

        self._taggable_fields = taggable_fields

    @property
    def exclude_wfs_fields(self):
        """Gets the exclude_wfs_fields of this CollectionReferenceParameters.  # noqa: E501


        :return: The exclude_wfs_fields of this CollectionReferenceParameters.  # noqa: E501
        :rtype: str
        """
        return self._exclude_wfs_fields

    @exclude_wfs_fields.setter
    def exclude_wfs_fields(self, exclude_wfs_fields):
        """Sets the exclude_wfs_fields of this CollectionReferenceParameters.


        :param exclude_wfs_fields: The exclude_wfs_fields of this CollectionReferenceParameters.  # noqa: E501
        :type: str
        """

        self._exclude_wfs_fields = exclude_wfs_fields

    @property
    def custom_params(self):
        """Gets the custom_params of this CollectionReferenceParameters.  # noqa: E501


        :return: The custom_params of this CollectionReferenceParameters.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._custom_params

    @custom_params.setter
    def custom_params(self, custom_params):
        """Sets the custom_params of this CollectionReferenceParameters.


        :param custom_params: The custom_params of this CollectionReferenceParameters.  # noqa: E501
        :type: dict(str, str)
        """

        self._custom_params = custom_params

    @property
    def atom_feed(self):
        """Gets the atom_feed of this CollectionReferenceParameters.  # noqa: E501


        :return: The atom_feed of this CollectionReferenceParameters.  # noqa: E501
        :rtype: Feed
        """
        return self._atom_feed

    @atom_feed.setter
    def atom_feed(self, atom_feed):
        """Sets the atom_feed of this CollectionReferenceParameters.


        :param atom_feed: The atom_feed of this CollectionReferenceParameters.  # noqa: E501
        :type: Feed
        """

        self._atom_feed = atom_feed

    @property
    def open_search(self):
        """Gets the open_search of this CollectionReferenceParameters.  # noqa: E501


        :return: The open_search of this CollectionReferenceParameters.  # noqa: E501
        :rtype: OpenSearch
        """
        return self._open_search

    @open_search.setter
    def open_search(self, open_search):
        """Sets the open_search of this CollectionReferenceParameters.


        :param open_search: The open_search of this CollectionReferenceParameters.  # noqa: E501
        :type: OpenSearch
        """

        self._open_search = open_search

    @property
    def inspire(self):
        """Gets the inspire of this CollectionReferenceParameters.  # noqa: E501


        :return: The inspire of this CollectionReferenceParameters.  # noqa: E501
        :rtype: Inspire
        """
        return self._inspire

    @inspire.setter
    def inspire(self, inspire):
        """Sets the inspire of this CollectionReferenceParameters.


        :param inspire: The inspire of this CollectionReferenceParameters.  # noqa: E501
        :type: Inspire
        """

        self._inspire = inspire

    @property
    def dublin_core_element_name(self):
        """Gets the dublin_core_element_name of this CollectionReferenceParameters.  # noqa: E501


        :return: The dublin_core_element_name of this CollectionReferenceParameters.  # noqa: E501
        :rtype: DublinCoreElementName
        """
        return self._dublin_core_element_name

    @dublin_core_element_name.setter
    def dublin_core_element_name(self, dublin_core_element_name):
        """Sets the dublin_core_element_name of this CollectionReferenceParameters.


        :param dublin_core_element_name: The dublin_core_element_name of this CollectionReferenceParameters.  # noqa: E501
        :type: DublinCoreElementName
        """

        self._dublin_core_element_name = dublin_core_element_name

    @property
    def raster_tile_url(self):
        """Gets the raster_tile_url of this CollectionReferenceParameters.  # noqa: E501


        :return: The raster_tile_url of this CollectionReferenceParameters.  # noqa: E501
        :rtype: RasterTileURL
        """
        return self._raster_tile_url

    @raster_tile_url.setter
    def raster_tile_url(self, raster_tile_url):
        """Sets the raster_tile_url of this CollectionReferenceParameters.


        :param raster_tile_url: The raster_tile_url of this CollectionReferenceParameters.  # noqa: E501
        :type: RasterTileURL
        """

        self._raster_tile_url = raster_tile_url

    @property
    def raster_tile_width(self):
        """Gets the raster_tile_width of this CollectionReferenceParameters.  # noqa: E501


        :return: The raster_tile_width of this CollectionReferenceParameters.  # noqa: E501
        :rtype: int
        """
        return self._raster_tile_width

    @raster_tile_width.setter
    def raster_tile_width(self, raster_tile_width):
        """Sets the raster_tile_width of this CollectionReferenceParameters.


        :param raster_tile_width: The raster_tile_width of this CollectionReferenceParameters.  # noqa: E501
        :type: int
        """

        self._raster_tile_width = raster_tile_width

    @property
    def raster_tile_height(self):
        """Gets the raster_tile_height of this CollectionReferenceParameters.  # noqa: E501


        :return: The raster_tile_height of this CollectionReferenceParameters.  # noqa: E501
        :rtype: int
        """
        return self._raster_tile_height

    @raster_tile_height.setter
    def raster_tile_height(self, raster_tile_height):
        """Sets the raster_tile_height of this CollectionReferenceParameters.


        :param raster_tile_height: The raster_tile_height of this CollectionReferenceParameters.  # noqa: E501
        :type: int
        """

        self._raster_tile_height = raster_tile_height

    @property
    def filter(self):
        """Gets the filter of this CollectionReferenceParameters.  # noqa: E501


        :return: The filter of this CollectionReferenceParameters.  # noqa: E501
        :rtype: Filter
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this CollectionReferenceParameters.


        :param filter: The filter of this CollectionReferenceParameters.  # noqa: E501
        :type: Filter
        """

        self._filter = filter

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(CollectionReferenceParameters, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CollectionReferenceParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
