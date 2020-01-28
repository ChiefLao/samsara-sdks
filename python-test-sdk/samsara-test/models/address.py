# coding: utf-8

"""
    Samsara API

    Integrate your data with the Samsara API, customize the Samsara experience, and join a community of developers building with Samsara.  # noqa: E501

    The version of the OpenAPI document: 2019-12-12
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from samsara-test.configuration import Configuration


class Address(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'str',
        'contacts': 'list[ContactTinyResponse]',
        'tags': 'list[TagTinyResponse]',
        'external_ids': 'dict(str, str)',
        'latitude': 'float',
        'longitude': 'float',
        'geofence': 'AddressGeofenceResponse',
        'formatted_address': 'str',
        'name': 'str',
        'notes': 'str',
        'address_types': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'contacts': 'contacts',
        'tags': 'tags',
        'external_ids': 'externalIds',
        'latitude': 'latitude',
        'longitude': 'longitude',
        'geofence': 'geofence',
        'formatted_address': 'formattedAddress',
        'name': 'name',
        'notes': 'notes',
        'address_types': 'addressTypes'
    }

    def __init__(self, id=None, contacts=None, tags=None, external_ids=None, latitude=None, longitude=None, geofence=None, formatted_address=None, name=None, notes=None, address_types=None, local_vars_configuration=None):  # noqa: E501
        """Address - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._contacts = None
        self._tags = None
        self._external_ids = None
        self._latitude = None
        self._longitude = None
        self._geofence = None
        self._formatted_address = None
        self._name = None
        self._notes = None
        self._address_types = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if contacts is not None:
            self.contacts = contacts
        if tags is not None:
            self.tags = tags
        if external_ids is not None:
            self.external_ids = external_ids
        if latitude is not None:
            self.latitude = latitude
        if longitude is not None:
            self.longitude = longitude
        if geofence is not None:
            self.geofence = geofence
        if formatted_address is not None:
            self.formatted_address = formatted_address
        if name is not None:
            self.name = name
        if notes is not None:
            self.notes = notes
        if address_types is not None:
            self.address_types = address_types

    @property
    def id(self):
        """Gets the id of this Address.  # noqa: E501

        Unique Samsara ID for the address.  # noqa: E501

        :return: The id of this Address.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Address.

        Unique Samsara ID for the address.  # noqa: E501

        :param id: The id of this Address.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def contacts(self):
        """Gets the contacts of this Address.  # noqa: E501

        An array of all contact mini-objects that are associated with the given address entry.  # noqa: E501

        :return: The contacts of this Address.  # noqa: E501
        :rtype: list[ContactTinyResponse]
        """
        return self._contacts

    @contacts.setter
    def contacts(self, contacts):
        """Sets the contacts of this Address.

        An array of all contact mini-objects that are associated with the given address entry.  # noqa: E501

        :param contacts: The contacts of this Address.  # noqa: E501
        :type: list[ContactTinyResponse]
        """

        self._contacts = contacts

    @property
    def tags(self):
        """Gets the tags of this Address.  # noqa: E501

        An array of all tag mini-objects that are associated with the given address entry.  # noqa: E501

        :return: The tags of this Address.  # noqa: E501
        :rtype: list[TagTinyResponse]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Address.

        An array of all tag mini-objects that are associated with the given address entry.  # noqa: E501

        :param tags: The tags of this Address.  # noqa: E501
        :type: list[TagTinyResponse]
        """

        self._tags = tags

    @property
    def external_ids(self):
        """Gets the external_ids of this Address.  # noqa: E501

        User-defined dictionary of external IDs (key-value pairs). Both the keys and the values of the dictionary are of type string and must be alphanumeric. Each organization can have at most 10 unique external ID keys. To delete an external ID, set its value to null or the empty string (`\"\"`). An external ID can be used as a path parameter to retrieve or update that resource.  # noqa: E501

        :return: The external_ids of this Address.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._external_ids

    @external_ids.setter
    def external_ids(self, external_ids):
        """Sets the external_ids of this Address.

        User-defined dictionary of external IDs (key-value pairs). Both the keys and the values of the dictionary are of type string and must be alphanumeric. Each organization can have at most 10 unique external ID keys. To delete an external ID, set its value to null or the empty string (`\"\"`). An external ID can be used as a path parameter to retrieve or update that resource.  # noqa: E501

        :param external_ids: The external_ids of this Address.  # noqa: E501
        :type: dict(str, str)
        """

        self._external_ids = external_ids

    @property
    def latitude(self):
        """Gets the latitude of this Address.  # noqa: E501

        Latitude of the address. Either inferred from the formatted address or defined on address creation.  # noqa: E501

        :return: The latitude of this Address.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this Address.

        Latitude of the address. Either inferred from the formatted address or defined on address creation.  # noqa: E501

        :param latitude: The latitude of this Address.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this Address.  # noqa: E501

        Longitude of the address. Either inferred from the formatted address or defined on address creation.  # noqa: E501

        :return: The longitude of this Address.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this Address.

        Longitude of the address. Either inferred from the formatted address or defined on address creation.  # noqa: E501

        :param longitude: The longitude of this Address.  # noqa: E501
        :type: float
        """

        self._longitude = longitude

    @property
    def geofence(self):
        """Gets the geofence of this Address.  # noqa: E501


        :return: The geofence of this Address.  # noqa: E501
        :rtype: AddressGeofenceResponse
        """
        return self._geofence

    @geofence.setter
    def geofence(self, geofence):
        """Sets the geofence of this Address.


        :param geofence: The geofence of this Address.  # noqa: E501
        :type: AddressGeofenceResponse
        """

        self._geofence = geofence

    @property
    def formatted_address(self):
        """Gets the formatted_address of this Address.  # noqa: E501

        The full street address for this address/geofence, as it might be recognized by Google Maps.  # noqa: E501

        :return: The formatted_address of this Address.  # noqa: E501
        :rtype: str
        """
        return self._formatted_address

    @formatted_address.setter
    def formatted_address(self, formatted_address):
        """Sets the formatted_address of this Address.

        The full street address for this address/geofence, as it might be recognized by Google Maps.  # noqa: E501

        :param formatted_address: The formatted_address of this Address.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                formatted_address is not None and len(formatted_address) > 1024):
            raise ValueError("Invalid value for `formatted_address`, length must be less than or equal to `1024`")  # noqa: E501

        self._formatted_address = formatted_address

    @property
    def name(self):
        """Gets the name of this Address.  # noqa: E501

        Name of the address.  # noqa: E501

        :return: The name of this Address.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Address.

        Name of the address.  # noqa: E501

        :param name: The name of this Address.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501

        self._name = name

    @property
    def notes(self):
        """Gets the notes of this Address.  # noqa: E501

        Notes about the address.  # noqa: E501

        :return: The notes of this Address.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this Address.

        Notes about the address.  # noqa: E501

        :param notes: The notes of this Address.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                notes is not None and len(notes) > 280):
            raise ValueError("Invalid value for `notes`, length must be less than or equal to `280`")  # noqa: E501

        self._notes = notes

    @property
    def address_types(self):
        """Gets the address_types of this Address.  # noqa: E501

        Reporting location type associated with the address (used for ELD reporting purposes).  # noqa: E501

        :return: The address_types of this Address.  # noqa: E501
        :rtype: list[str]
        """
        return self._address_types

    @address_types.setter
    def address_types(self, address_types):
        """Sets the address_types of this Address.

        Reporting location type associated with the address (used for ELD reporting purposes).  # noqa: E501

        :param address_types: The address_types of this Address.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["yard", "shortHaul"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(address_types).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `address_types` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(address_types) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._address_types = address_types

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Address):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Address):
            return True

        return self.to_dict() != other.to_dict()
