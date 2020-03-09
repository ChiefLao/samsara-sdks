# V1DocumentField

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Descriptive name of this field. | 
**value** | [**object**](.md) | DEPRECATED: Please use stringValue, numberValue, or photoValue instead. Value of this field. Depending on what kind of field it is, this may be one of the following: an array of image urls, a float, an integer, or a string. | [optional] 
**date_time_value** | **str** | Value of this field if this document field has valueType: ValueType_DateTime. | [optional] 
**multiple_choice_value** | [**list[V1DocumentFieldCreateMultipleChoiceValue]**](V1DocumentFieldCreateMultipleChoiceValue.md) | Value of this field if this document field has valueType: ValueType_MultipleChoice. Array of objects containing two fields: the string value of the multiple choice option and a boolean representing whether or not the choice was selected | [optional] 
**number_value** | **float** | Value of this field if this document field has valueType: ValueType_Number. | [optional] 
**photo_value** | [**list[V1DocumentFieldCreatePhotoValue]**](V1DocumentFieldCreatePhotoValue.md) | Value of this field if this document field has valueType: ValueType_Photo. Array of photo objects where each object contains a URL for a photo. | [optional] 
**string_value** | **str** | Value of this field if this document field has valueType: ValueType_String. | [optional] 
**value_type** | **str** | Determines the type of this field and what type of value this field has. It should be either ValueType_Number, ValueType_String, ValueType_Photo, ValueType_MultipleChoice or ValueType_DateTime. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

