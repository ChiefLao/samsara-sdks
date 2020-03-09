# V1DispatchJobWithoutETA

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arrived_at_ms** | **int** | The time at which the driver arrived at the job destination. | [optional] 
**completed_at_ms** | **int** | The time at which the job was marked complete (e.g. started driving to the next destination). | [optional] 
**dispatch_route_id** | **int** | ID of the route that this job belongs to. | 
**documents** | [**list[V1DispatchJobDocumentInfo]**](V1DispatchJobDocumentInfo.md) | Document submissions associated with this job. | [optional] 
**driver_id** | **int** | ID of the driver assigned to the dispatch job. | [optional] 
**en_route_at_ms** | **int** | The time at which the assigned driver started fulfilling the job (e.g. started driving to the destination). | [optional] 
**fleet_viewer_url** | **str** | Fleet viewer url of the dispatch job. | [optional] 
**group_id** | **int** | Deprecated. | [optional] 
**id** | **int** | ID of the Samsara dispatch job. | 
**job_state** | [**V1jobStatus**](V1jobStatus.md) |  | 
**skipped_at_ms** | **int** | The time at which the job was marked skipped. | [optional] 
**vehicle_id** | **int** | ID of the vehicle used for the dispatch job. | [optional] 
**destination_address** | **str** | The address of the job destination, as it would be recognized if provided to maps.google.com. Optional if a valid destination address ID is provided. | [optional] 
**destination_address_id** | **int** | ID of the job destination associated with an address book entry. Optional if valid values are provided for destination address and latitude/longitude. If a valid destination address ID is provided, address/latitude/longitude will be used from the address book entry. Name of the address book entry will only be used if the destination name is not provided. | [optional] 
**destination_lat** | **float** | Latitude of the destination in decimal degrees. Optional if a valid destination address ID is provided. | [optional] 
**destination_lng** | **float** | Longitude of the destination in decimal degrees. Optional if a valid destination address ID is provided. | [optional] 
**destination_name** | **str** | The name of the job destination. If provided, it will take precedence over the name of the address book entry. | [optional] 
**notes** | **str** | Notes regarding the details of this job, maximum of 2000 characters; newline characters (&#39;\\n&#39;)can be used for formatting. | [optional] 
**scheduled_arrival_time_ms** | **int** | The time at which the assigned driver is scheduled to arrive at the job destination. | 
**scheduled_departure_time_ms** | **int** | The time at which the assigned driver is scheduled to depart from the job destination. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

