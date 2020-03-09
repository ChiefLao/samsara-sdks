# VehicleLocationsListResponseData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **string** | The unique Samsara ID of the Vehicle. This is automatically generated when the Vehicle object is created. It cannot be changed. | 
**Locations** | Pointer to [**[]VehicleLocation**](VehicleLocation.md) | A list of location events for the given vehicle. | 
**Name** | Pointer to **string** | The human-readable name of the Vehicle. This is set by a fleet administrator and will appear in both Samsara’s cloud dashboard as well as the Samsara Driver mobile app. **By default**, this name is the serial number of the Samsara Vehicle Gateway. It can be set or updated through the Samsara Dashboard or through the API at any time. | 

## Methods

### GetId

`func (o *VehicleLocationsListResponseData) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *VehicleLocationsListResponseData) GetIdOk() (string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasId

`func (o *VehicleLocationsListResponseData) HasId() bool`

HasId returns a boolean if a field has been set.

### SetId

`func (o *VehicleLocationsListResponseData) SetId(v string)`

SetId gets a reference to the given string and assigns it to the Id field.

### GetLocations

`func (o *VehicleLocationsListResponseData) GetLocations() []VehicleLocation`

GetLocations returns the Locations field if non-nil, zero value otherwise.

### GetLocationsOk

`func (o *VehicleLocationsListResponseData) GetLocationsOk() ([]VehicleLocation, bool)`

GetLocationsOk returns a tuple with the Locations field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasLocations

`func (o *VehicleLocationsListResponseData) HasLocations() bool`

HasLocations returns a boolean if a field has been set.

### SetLocations

`func (o *VehicleLocationsListResponseData) SetLocations(v []VehicleLocation)`

SetLocations gets a reference to the given []VehicleLocation and assigns it to the Locations field.

### GetName

`func (o *VehicleLocationsListResponseData) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *VehicleLocationsListResponseData) GetNameOk() (string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasName

`func (o *VehicleLocationsListResponseData) HasName() bool`

HasName returns a boolean if a field has been set.

### SetName

`func (o *VehicleLocationsListResponseData) SetName(v string)`

SetName gets a reference to the given string and assigns it to the Name field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


