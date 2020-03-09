# TachographActivityListWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Activity** | Pointer to [**[]TachographActivity**](TachographActivity.md) | List of all driver tachograph activities in a specified time range. | [optional] 
**Driver** | Pointer to [**DriverTinyResponse**](driverTinyResponse.md) |  | [optional] 

## Methods

### GetActivity

`func (o *TachographActivityListWrapper) GetActivity() []TachographActivity`

GetActivity returns the Activity field if non-nil, zero value otherwise.

### GetActivityOk

`func (o *TachographActivityListWrapper) GetActivityOk() ([]TachographActivity, bool)`

GetActivityOk returns a tuple with the Activity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasActivity

`func (o *TachographActivityListWrapper) HasActivity() bool`

HasActivity returns a boolean if a field has been set.

### SetActivity

`func (o *TachographActivityListWrapper) SetActivity(v []TachographActivity)`

SetActivity gets a reference to the given []TachographActivity and assigns it to the Activity field.

### GetDriver

`func (o *TachographActivityListWrapper) GetDriver() DriverTinyResponse`

GetDriver returns the Driver field if non-nil, zero value otherwise.

### GetDriverOk

`func (o *TachographActivityListWrapper) GetDriverOk() (DriverTinyResponse, bool)`

GetDriverOk returns a tuple with the Driver field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDriver

`func (o *TachographActivityListWrapper) HasDriver() bool`

HasDriver returns a boolean if a field has been set.

### SetDriver

`func (o *TachographActivityListWrapper) SetDriver(v DriverTinyResponse)`

SetDriver gets a reference to the given DriverTinyResponse and assigns it to the Driver field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

