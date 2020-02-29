# coding: utf-8

"""
    Samsara API

    This is the Samsara API.  # noqa: E501

    The version of the OpenAPI document: 2019-12-12
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from samsara.configuration import Configuration


class UpdateContactRequest(object):
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
        'email': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'phone': 'str'
    }

    attribute_map = {
        'email': 'email',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'phone': 'phone'
    }

    def __init__(self, email=None, first_name=None, last_name=None, phone=None, local_vars_configuration=None):  # noqa: E501
        """UpdateContactRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._email = None
        self._first_name = None
        self._last_name = None
        self._phone = None
        self.discriminator = None

        if email is not None:
            self.email = email
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if phone is not None:
            self.phone = phone

    @property
    def email(self):
        """Gets the email of this UpdateContactRequest.  # noqa: E501

        Email address of the contact.  # noqa: E501

        :return: The email of this UpdateContactRequest.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UpdateContactRequest.

        Email address of the contact.  # noqa: E501

        :param email: The email of this UpdateContactRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                email is not None and len(email) > 255):
            raise ValueError("Invalid value for `email`, length must be less than or equal to `255`")  # noqa: E501

        self._email = email

    @property
    def first_name(self):
        """Gets the first_name of this UpdateContactRequest.  # noqa: E501

        First name of the contact.  # noqa: E501

        :return: The first_name of this UpdateContactRequest.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this UpdateContactRequest.

        First name of the contact.  # noqa: E501

        :param first_name: The first_name of this UpdateContactRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                first_name is not None and len(first_name) > 255):
            raise ValueError("Invalid value for `first_name`, length must be less than or equal to `255`")  # noqa: E501

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this UpdateContactRequest.  # noqa: E501

        Last name of the contact.  # noqa: E501

        :return: The last_name of this UpdateContactRequest.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this UpdateContactRequest.

        Last name of the contact.  # noqa: E501

        :param last_name: The last_name of this UpdateContactRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                last_name is not None and len(last_name) > 255):
            raise ValueError("Invalid value for `last_name`, length must be less than or equal to `255`")  # noqa: E501

        self._last_name = last_name

    @property
    def phone(self):
        """Gets the phone of this UpdateContactRequest.  # noqa: E501

        Phone number of the contact.  # noqa: E501

        :return: The phone of this UpdateContactRequest.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this UpdateContactRequest.

        Phone number of the contact.  # noqa: E501

        :param phone: The phone of this UpdateContactRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                phone is not None and len(phone) > 255):
            raise ValueError("Invalid value for `phone`, length must be less than or equal to `255`")  # noqa: E501

        self._phone = phone

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
        if not isinstance(other, UpdateContactRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateContactRequest):
            return True

        return self.to_dict() != other.to_dict()
