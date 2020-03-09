# V1DispatchJobDocumentInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DriverId** | Pointer to **int32** | ID of driver that submitted the document. | 
**Id** | Pointer to **string** | ID of document. This can be used to query for the document&#39;s info via the /v1/fleet/drivers/{driver_id}/documents/{document_id} endpoint | 

## Methods

### GetDriverId

`func (o *V1DispatchJobDocumentInfo) GetDriverId() int32`

GetDriverId returns the DriverId field if non-nil, zero value otherwise.

### GetDriverIdOk

`func (o *V1DispatchJobDocumentInfo) GetDriverIdOk() (int32, bool)`

GetDriverIdOk returns a tuple with the DriverId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDriverId

`func (o *V1DispatchJobDocumentInfo) HasDriverId() bool`

HasDriverId returns a boolean if a field has been set.

### SetDriverId

`func (o *V1DispatchJobDocumentInfo) SetDriverId(v int32)`

SetDriverId gets a reference to the given int32 and assigns it to the DriverId field.

### GetId

`func (o *V1DispatchJobDocumentInfo) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *V1DispatchJobDocumentInfo) GetIdOk() (string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasId

`func (o *V1DispatchJobDocumentInfo) HasId() bool`

HasId returns a boolean if a field has been set.

### SetId

`func (o *V1DispatchJobDocumentInfo) SetId(v string)`

SetId gets a reference to the given string and assigns it to the Id field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

