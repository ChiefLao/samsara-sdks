# V1DispatchRoute

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DispatchJobs** | Pointer to [**[]V1DispatchJob**](V1DispatchJob.md) | The dispatch jobs associated with this route. | [optional] 
**Id** | Pointer to **int64** | ID of the Samsara dispatch route. | [optional] 
**ActualEndMs** | Pointer to **int64** | The time in Unix epoch milliseconds that the route actually ended. | [optional] 
**ActualStartMs** | Pointer to **int64** | The time in Unix epoch milliseconds that the route actually started. | [optional] 
**DriverId** | Pointer to **int64** | ID of the driver assigned to the dispatch route. Note that driver_id and vehicle_id are mutually exclusive. If neither is specified, then the route is unassigned. | [optional] 
**GroupId** | Pointer to **int64** | Deprecated. | [optional] 
**Name** | Pointer to **string** | Descriptive name of this route. | [optional] 
**Notes** | Pointer to **string** | Notes regarding the details of this route; maximum of 2000 characters; newline characters (&#39;\\n&#39;)can be used for formatting. | [optional] 
**OdometerEndMeters** | Pointer to **int64** | Odometer reading at the end of the route. Will not be returned if Route is not completed or if Odometer information is not available for the relevant vehicle. | [optional] 
**OdometerStartMeters** | Pointer to **int64** | Odometer reading at the start of the route. Will not be returned if Route has not started or if Odometer information is not available for the relevant vehicle. | [optional] 
**ScheduledEndMs** | Pointer to **int64** | The time in Unix epoch milliseconds that the last job in the route is scheduled to end. | [optional] 
**ScheduledMeters** | Pointer to **int64** | The distance expected to be traveled for this route in meters. | [optional] 
**ScheduledStartMs** | Pointer to **int64** | The time in Unix epoch milliseconds that the route is scheduled to start. | [optional] 
**StartLocationAddress** | Pointer to **string** | The address of the route&#39;s starting location, as it would be recognized if provided to maps.google.com. Optional if a valid start location address ID is provided. | [optional] 
**StartLocationAddressId** | Pointer to **int64** | ID of the start location associated with an address book entry. Optional if valid values are provided for start location address and latitude/longitude. If a valid start location address ID is provided, address/latitude/longitude will be used from the address book entry. Name of the address book entry will only be used if the start location name is not provided. | [optional] 
**StartLocationLat** | Pointer to **float64** | Latitude of the start location in decimal degrees. Optional if a valid start location address ID is provided. | [optional] 
**StartLocationLng** | Pointer to **float64** | Longitude of the start location in decimal degrees. Optional if a valid start location address ID is provided. | [optional] 
**StartLocationName** | Pointer to **string** | The name of the route&#39;s starting location. If provided, it will take precedence over the name of the address book entry. | [optional] 
**TrailerId** | Pointer to **int64** | ID of the trailer assigned to the dispatch route. Note that trailers can only be assigned to routes that have a Vehicle or Driver assigned to them. | [optional] 
**VehicleId** | Pointer to **int64** | ID of the vehicle assigned to the dispatch route. Note that vehicle_id and driver_id are mutually exclusive. If neither is specified, then the route is unassigned. | [optional] 

## Methods

### GetDispatchJobs

`func (o *V1DispatchRoute) GetDispatchJobs() []V1DispatchJob`

GetDispatchJobs returns the DispatchJobs field if non-nil, zero value otherwise.

### GetDispatchJobsOk

`func (o *V1DispatchRoute) GetDispatchJobsOk() ([]V1DispatchJob, bool)`

GetDispatchJobsOk returns a tuple with the DispatchJobs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDispatchJobs

`func (o *V1DispatchRoute) HasDispatchJobs() bool`

HasDispatchJobs returns a boolean if a field has been set.

### SetDispatchJobs

`func (o *V1DispatchRoute) SetDispatchJobs(v []V1DispatchJob)`

SetDispatchJobs gets a reference to the given []V1DispatchJob and assigns it to the DispatchJobs field.

### GetId

`func (o *V1DispatchRoute) GetId() int64`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *V1DispatchRoute) GetIdOk() (int64, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasId

`func (o *V1DispatchRoute) HasId() bool`

HasId returns a boolean if a field has been set.

### SetId

`func (o *V1DispatchRoute) SetId(v int64)`

SetId gets a reference to the given int64 and assigns it to the Id field.

### GetActualEndMs

`func (o *V1DispatchRoute) GetActualEndMs() int64`

GetActualEndMs returns the ActualEndMs field if non-nil, zero value otherwise.

### GetActualEndMsOk

`func (o *V1DispatchRoute) GetActualEndMsOk() (int64, bool)`

GetActualEndMsOk returns a tuple with the ActualEndMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasActualEndMs

`func (o *V1DispatchRoute) HasActualEndMs() bool`

HasActualEndMs returns a boolean if a field has been set.

### SetActualEndMs

`func (o *V1DispatchRoute) SetActualEndMs(v int64)`

SetActualEndMs gets a reference to the given int64 and assigns it to the ActualEndMs field.

### GetActualStartMs

`func (o *V1DispatchRoute) GetActualStartMs() int64`

GetActualStartMs returns the ActualStartMs field if non-nil, zero value otherwise.

### GetActualStartMsOk

`func (o *V1DispatchRoute) GetActualStartMsOk() (int64, bool)`

GetActualStartMsOk returns a tuple with the ActualStartMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasActualStartMs

`func (o *V1DispatchRoute) HasActualStartMs() bool`

HasActualStartMs returns a boolean if a field has been set.

### SetActualStartMs

`func (o *V1DispatchRoute) SetActualStartMs(v int64)`

SetActualStartMs gets a reference to the given int64 and assigns it to the ActualStartMs field.

### GetDriverId

`func (o *V1DispatchRoute) GetDriverId() int64`

GetDriverId returns the DriverId field if non-nil, zero value otherwise.

### GetDriverIdOk

`func (o *V1DispatchRoute) GetDriverIdOk() (int64, bool)`

GetDriverIdOk returns a tuple with the DriverId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasDriverId

`func (o *V1DispatchRoute) HasDriverId() bool`

HasDriverId returns a boolean if a field has been set.

### SetDriverId

`func (o *V1DispatchRoute) SetDriverId(v int64)`

SetDriverId gets a reference to the given int64 and assigns it to the DriverId field.

### GetGroupId

`func (o *V1DispatchRoute) GetGroupId() int64`

GetGroupId returns the GroupId field if non-nil, zero value otherwise.

### GetGroupIdOk

`func (o *V1DispatchRoute) GetGroupIdOk() (int64, bool)`

GetGroupIdOk returns a tuple with the GroupId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasGroupId

`func (o *V1DispatchRoute) HasGroupId() bool`

HasGroupId returns a boolean if a field has been set.

### SetGroupId

`func (o *V1DispatchRoute) SetGroupId(v int64)`

SetGroupId gets a reference to the given int64 and assigns it to the GroupId field.

### GetName

`func (o *V1DispatchRoute) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *V1DispatchRoute) GetNameOk() (string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasName

`func (o *V1DispatchRoute) HasName() bool`

HasName returns a boolean if a field has been set.

### SetName

`func (o *V1DispatchRoute) SetName(v string)`

SetName gets a reference to the given string and assigns it to the Name field.

### GetNotes

`func (o *V1DispatchRoute) GetNotes() string`

GetNotes returns the Notes field if non-nil, zero value otherwise.

### GetNotesOk

`func (o *V1DispatchRoute) GetNotesOk() (string, bool)`

GetNotesOk returns a tuple with the Notes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasNotes

`func (o *V1DispatchRoute) HasNotes() bool`

HasNotes returns a boolean if a field has been set.

### SetNotes

`func (o *V1DispatchRoute) SetNotes(v string)`

SetNotes gets a reference to the given string and assigns it to the Notes field.

### GetOdometerEndMeters

`func (o *V1DispatchRoute) GetOdometerEndMeters() int64`

GetOdometerEndMeters returns the OdometerEndMeters field if non-nil, zero value otherwise.

### GetOdometerEndMetersOk

`func (o *V1DispatchRoute) GetOdometerEndMetersOk() (int64, bool)`

GetOdometerEndMetersOk returns a tuple with the OdometerEndMeters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasOdometerEndMeters

`func (o *V1DispatchRoute) HasOdometerEndMeters() bool`

HasOdometerEndMeters returns a boolean if a field has been set.

### SetOdometerEndMeters

`func (o *V1DispatchRoute) SetOdometerEndMeters(v int64)`

SetOdometerEndMeters gets a reference to the given int64 and assigns it to the OdometerEndMeters field.

### GetOdometerStartMeters

`func (o *V1DispatchRoute) GetOdometerStartMeters() int64`

GetOdometerStartMeters returns the OdometerStartMeters field if non-nil, zero value otherwise.

### GetOdometerStartMetersOk

`func (o *V1DispatchRoute) GetOdometerStartMetersOk() (int64, bool)`

GetOdometerStartMetersOk returns a tuple with the OdometerStartMeters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasOdometerStartMeters

`func (o *V1DispatchRoute) HasOdometerStartMeters() bool`

HasOdometerStartMeters returns a boolean if a field has been set.

### SetOdometerStartMeters

`func (o *V1DispatchRoute) SetOdometerStartMeters(v int64)`

SetOdometerStartMeters gets a reference to the given int64 and assigns it to the OdometerStartMeters field.

### GetScheduledEndMs

`func (o *V1DispatchRoute) GetScheduledEndMs() int64`

GetScheduledEndMs returns the ScheduledEndMs field if non-nil, zero value otherwise.

### GetScheduledEndMsOk

`func (o *V1DispatchRoute) GetScheduledEndMsOk() (int64, bool)`

GetScheduledEndMsOk returns a tuple with the ScheduledEndMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasScheduledEndMs

`func (o *V1DispatchRoute) HasScheduledEndMs() bool`

HasScheduledEndMs returns a boolean if a field has been set.

### SetScheduledEndMs

`func (o *V1DispatchRoute) SetScheduledEndMs(v int64)`

SetScheduledEndMs gets a reference to the given int64 and assigns it to the ScheduledEndMs field.

### GetScheduledMeters

`func (o *V1DispatchRoute) GetScheduledMeters() int64`

GetScheduledMeters returns the ScheduledMeters field if non-nil, zero value otherwise.

### GetScheduledMetersOk

`func (o *V1DispatchRoute) GetScheduledMetersOk() (int64, bool)`

GetScheduledMetersOk returns a tuple with the ScheduledMeters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasScheduledMeters

`func (o *V1DispatchRoute) HasScheduledMeters() bool`

HasScheduledMeters returns a boolean if a field has been set.

### SetScheduledMeters

`func (o *V1DispatchRoute) SetScheduledMeters(v int64)`

SetScheduledMeters gets a reference to the given int64 and assigns it to the ScheduledMeters field.

### GetScheduledStartMs

`func (o *V1DispatchRoute) GetScheduledStartMs() int64`

GetScheduledStartMs returns the ScheduledStartMs field if non-nil, zero value otherwise.

### GetScheduledStartMsOk

`func (o *V1DispatchRoute) GetScheduledStartMsOk() (int64, bool)`

GetScheduledStartMsOk returns a tuple with the ScheduledStartMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasScheduledStartMs

`func (o *V1DispatchRoute) HasScheduledStartMs() bool`

HasScheduledStartMs returns a boolean if a field has been set.

### SetScheduledStartMs

`func (o *V1DispatchRoute) SetScheduledStartMs(v int64)`

SetScheduledStartMs gets a reference to the given int64 and assigns it to the ScheduledStartMs field.

### GetStartLocationAddress

`func (o *V1DispatchRoute) GetStartLocationAddress() string`

GetStartLocationAddress returns the StartLocationAddress field if non-nil, zero value otherwise.

### GetStartLocationAddressOk

`func (o *V1DispatchRoute) GetStartLocationAddressOk() (string, bool)`

GetStartLocationAddressOk returns a tuple with the StartLocationAddress field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasStartLocationAddress

`func (o *V1DispatchRoute) HasStartLocationAddress() bool`

HasStartLocationAddress returns a boolean if a field has been set.

### SetStartLocationAddress

`func (o *V1DispatchRoute) SetStartLocationAddress(v string)`

SetStartLocationAddress gets a reference to the given string and assigns it to the StartLocationAddress field.

### GetStartLocationAddressId

`func (o *V1DispatchRoute) GetStartLocationAddressId() int64`

GetStartLocationAddressId returns the StartLocationAddressId field if non-nil, zero value otherwise.

### GetStartLocationAddressIdOk

`func (o *V1DispatchRoute) GetStartLocationAddressIdOk() (int64, bool)`

GetStartLocationAddressIdOk returns a tuple with the StartLocationAddressId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasStartLocationAddressId

`func (o *V1DispatchRoute) HasStartLocationAddressId() bool`

HasStartLocationAddressId returns a boolean if a field has been set.

### SetStartLocationAddressId

`func (o *V1DispatchRoute) SetStartLocationAddressId(v int64)`

SetStartLocationAddressId gets a reference to the given int64 and assigns it to the StartLocationAddressId field.

### GetStartLocationLat

`func (o *V1DispatchRoute) GetStartLocationLat() float64`

GetStartLocationLat returns the StartLocationLat field if non-nil, zero value otherwise.

### GetStartLocationLatOk

`func (o *V1DispatchRoute) GetStartLocationLatOk() (float64, bool)`

GetStartLocationLatOk returns a tuple with the StartLocationLat field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasStartLocationLat

`func (o *V1DispatchRoute) HasStartLocationLat() bool`

HasStartLocationLat returns a boolean if a field has been set.

### SetStartLocationLat

`func (o *V1DispatchRoute) SetStartLocationLat(v float64)`

SetStartLocationLat gets a reference to the given float64 and assigns it to the StartLocationLat field.

### GetStartLocationLng

`func (o *V1DispatchRoute) GetStartLocationLng() float64`

GetStartLocationLng returns the StartLocationLng field if non-nil, zero value otherwise.

### GetStartLocationLngOk

`func (o *V1DispatchRoute) GetStartLocationLngOk() (float64, bool)`

GetStartLocationLngOk returns a tuple with the StartLocationLng field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasStartLocationLng

`func (o *V1DispatchRoute) HasStartLocationLng() bool`

HasStartLocationLng returns a boolean if a field has been set.

### SetStartLocationLng

`func (o *V1DispatchRoute) SetStartLocationLng(v float64)`

SetStartLocationLng gets a reference to the given float64 and assigns it to the StartLocationLng field.

### GetStartLocationName

`func (o *V1DispatchRoute) GetStartLocationName() string`

GetStartLocationName returns the StartLocationName field if non-nil, zero value otherwise.

### GetStartLocationNameOk

`func (o *V1DispatchRoute) GetStartLocationNameOk() (string, bool)`

GetStartLocationNameOk returns a tuple with the StartLocationName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasStartLocationName

`func (o *V1DispatchRoute) HasStartLocationName() bool`

HasStartLocationName returns a boolean if a field has been set.

### SetStartLocationName

`func (o *V1DispatchRoute) SetStartLocationName(v string)`

SetStartLocationName gets a reference to the given string and assigns it to the StartLocationName field.

### GetTrailerId

`func (o *V1DispatchRoute) GetTrailerId() int64`

GetTrailerId returns the TrailerId field if non-nil, zero value otherwise.

### GetTrailerIdOk

`func (o *V1DispatchRoute) GetTrailerIdOk() (int64, bool)`

GetTrailerIdOk returns a tuple with the TrailerId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasTrailerId

`func (o *V1DispatchRoute) HasTrailerId() bool`

HasTrailerId returns a boolean if a field has been set.

### SetTrailerId

`func (o *V1DispatchRoute) SetTrailerId(v int64)`

SetTrailerId gets a reference to the given int64 and assigns it to the TrailerId field.

### GetVehicleId

`func (o *V1DispatchRoute) GetVehicleId() int64`

GetVehicleId returns the VehicleId field if non-nil, zero value otherwise.

### GetVehicleIdOk

`func (o *V1DispatchRoute) GetVehicleIdOk() (int64, bool)`

GetVehicleIdOk returns a tuple with the VehicleId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### HasVehicleId

`func (o *V1DispatchRoute) HasVehicleId() bool`

HasVehicleId returns a boolean if a field has been set.

### SetVehicleId

`func (o *V1DispatchRoute) SetVehicleId(v int64)`

SetVehicleId gets a reference to the given int64 and assigns it to the VehicleId field.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

