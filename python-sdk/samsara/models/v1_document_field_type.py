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


class V1DocumentFieldType(object):
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
        'label': 'str',
        'multiple_choice_value_type_metadata': 'V1DocumentFieldTypeMultipleChoiceValueTypeMetadata',
        'number_value_type_metadata': 'V1DocumentFieldTypeNumberValueTypeMetadata',
        'signature_value_type_metadata': 'V1DocumentFieldTypeSignatureValueTypeMetadata',
        'value_type': 'str'
    }

    attribute_map = {
        'label': 'label',
        'multiple_choice_value_type_metadata': 'multipleChoiceValueTypeMetadata',
        'number_value_type_metadata': 'numberValueTypeMetadata',
        'signature_value_type_metadata': 'signatureValueTypeMetadata',
        'value_type': 'valueType'
    }

    def __init__(self, label=None, multiple_choice_value_type_metadata=None, number_value_type_metadata=None, signature_value_type_metadata=None, value_type=None, local_vars_configuration=None):  # noqa: E501
        """V1DocumentFieldType - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._label = None
        self._multiple_choice_value_type_metadata = None
        self._number_value_type_metadata = None
        self._signature_value_type_metadata = None
        self._value_type = None
        self.discriminator = None

        self.label = label
        if multiple_choice_value_type_metadata is not None:
            self.multiple_choice_value_type_metadata = multiple_choice_value_type_metadata
        if number_value_type_metadata is not None:
            self.number_value_type_metadata = number_value_type_metadata
        if signature_value_type_metadata is not None:
            self.signature_value_type_metadata = signature_value_type_metadata
        self.value_type = value_type

    @property
    def label(self):
        """Gets the label of this V1DocumentFieldType.  # noqa: E501

        Name of this field type.  # noqa: E501

        :return: The label of this V1DocumentFieldType.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this V1DocumentFieldType.

        Name of this field type.  # noqa: E501

        :param label: The label of this V1DocumentFieldType.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and label is None:  # noqa: E501
            raise ValueError("Invalid value for `label`, must not be `None`")  # noqa: E501

        self._label = label

    @property
    def multiple_choice_value_type_metadata(self):
        """Gets the multiple_choice_value_type_metadata of this V1DocumentFieldType.  # noqa: E501


        :return: The multiple_choice_value_type_metadata of this V1DocumentFieldType.  # noqa: E501
        :rtype: V1DocumentFieldTypeMultipleChoiceValueTypeMetadata
        """
        return self._multiple_choice_value_type_metadata

    @multiple_choice_value_type_metadata.setter
    def multiple_choice_value_type_metadata(self, multiple_choice_value_type_metadata):
        """Sets the multiple_choice_value_type_metadata of this V1DocumentFieldType.


        :param multiple_choice_value_type_metadata: The multiple_choice_value_type_metadata of this V1DocumentFieldType.  # noqa: E501
        :type: V1DocumentFieldTypeMultipleChoiceValueTypeMetadata
        """

        self._multiple_choice_value_type_metadata = multiple_choice_value_type_metadata

    @property
    def number_value_type_metadata(self):
        """Gets the number_value_type_metadata of this V1DocumentFieldType.  # noqa: E501


        :return: The number_value_type_metadata of this V1DocumentFieldType.  # noqa: E501
        :rtype: V1DocumentFieldTypeNumberValueTypeMetadata
        """
        return self._number_value_type_metadata

    @number_value_type_metadata.setter
    def number_value_type_metadata(self, number_value_type_metadata):
        """Sets the number_value_type_metadata of this V1DocumentFieldType.


        :param number_value_type_metadata: The number_value_type_metadata of this V1DocumentFieldType.  # noqa: E501
        :type: V1DocumentFieldTypeNumberValueTypeMetadata
        """

        self._number_value_type_metadata = number_value_type_metadata

    @property
    def signature_value_type_metadata(self):
        """Gets the signature_value_type_metadata of this V1DocumentFieldType.  # noqa: E501


        :return: The signature_value_type_metadata of this V1DocumentFieldType.  # noqa: E501
        :rtype: V1DocumentFieldTypeSignatureValueTypeMetadata
        """
        return self._signature_value_type_metadata

    @signature_value_type_metadata.setter
    def signature_value_type_metadata(self, signature_value_type_metadata):
        """Sets the signature_value_type_metadata of this V1DocumentFieldType.


        :param signature_value_type_metadata: The signature_value_type_metadata of this V1DocumentFieldType.  # noqa: E501
        :type: V1DocumentFieldTypeSignatureValueTypeMetadata
        """

        self._signature_value_type_metadata = signature_value_type_metadata

    @property
    def value_type(self):
        """Gets the value_type of this V1DocumentFieldType.  # noqa: E501

        The type of value this field can have. Valid values: `ValueType_Number`, `ValueType_String`, `ValueType_Photo`, `ValueType_MultipleChoice`, `ValueType_Signature`, `ValueType_DateTime`.  # noqa: E501

        :return: The value_type of this V1DocumentFieldType.  # noqa: E501
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """Sets the value_type of this V1DocumentFieldType.

        The type of value this field can have. Valid values: `ValueType_Number`, `ValueType_String`, `ValueType_Photo`, `ValueType_MultipleChoice`, `ValueType_Signature`, `ValueType_DateTime`.  # noqa: E501

        :param value_type: The value_type of this V1DocumentFieldType.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and value_type is None:  # noqa: E501
            raise ValueError("Invalid value for `value_type`, must not be `None`")  # noqa: E501

        self._value_type = value_type

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
        if not isinstance(other, V1DocumentFieldType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1DocumentFieldType):
            return True

        return self.to_dict() != other.to_dict()
