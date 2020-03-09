# V1CargoResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**GroupId** | Pointer to **int64** | Deprecated. | [optional] 
**Sensors** | Pointer to [**[]V1CargoResponseSensors**](V1CargoResponse_sensors.md) |  | [optional] 

## Methods

### GetGroupId

`func (o *V1CargoResponse) GetGroupId() int64`

GetGroupId returns the GroupId field if non-nil, zero value otherwise.

### GetGroupIdOk

`func (o *V1CargoResponse) GetGroupIdOk() (int64, bool)`

GetGroupIdOk returns a tuple with the GroupId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasGroupId

`func (o *V1CargoResponse) HasGroupId() bool`

HasGroupId returns a boolean if a field has been set.

### SetGroupId

`func (o *V1CargoResponse) SetGroupId(v int64)`

SetGroupId gets a reference to the given int64 and assigns it to the GroupId field.

### GetSensors

`func (o *V1CargoResponse) GetSensors() []V1CargoResponseSensors`

GetSensors returns the Sensors field if non-nil, zero value otherwise.

### GetSensorsOk

`func (o *V1CargoResponse) GetSensorsOk() ([]V1CargoResponseSensors, bool)`

GetSensorsOk returns a tuple with the Sensors field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasSensors

`func (o *V1CargoResponse) HasSensors() bool`

HasSensors returns a boolean if a field has been set.

### SetSensors

`func (o *V1CargoResponse) SetSensors(v []V1CargoResponseSensors)`

SetSensors gets a reference to the given []V1CargoResponseSensors and assigns it to the Sensors field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

