# coding: utf-8

# flake8: noqa

"""
    Samsara API

    <style type=\"text/css\"> n {     padding: 1em;     width: 100%;     display: block;     margin: 28px 0; } n.info {     background-color: rgba(0, 51, 160, 0.1); } n.warning {     background-color: #fdf6e3; } i:before {     margin-right: 6px; } nh {     font-size: 1.5rem;     font-weight: 700;     line-height: 1.1;     display: block; } nb {     margin-top: 10px;     padding-left: 22px;     display: block; } </style>  # Overview  <n class=\"info\"> <nh> <i class=\"fa fa-info-circle\"></i> Something new! </nh> <nb> Welcome Samsara's new and improved API. Check out our FAQ [here](https://developers.samsara.com/docs/introducing-our-next-generation-api) to see what's changed and learn how to get started.<br> <br> Want to access the legacy API docs? You can find them [here](https://www.samsara.com/api).<br> <br> *Note: Because this is a new set of APIs, we have not transitioned all endpoints over to this standard. Endpoints that still use the legacy standards are indicated in the reference documentation. If you can't find an API that you're looking for, we encourage you to look for it in our [legacy API docs](https://www.samsara.com/api) as we continue to transition all endpoints over. Check back here for updates!*<br> <br> Submit your feedback [here](https://forms.gle/r4bs6HQshQAvBuwv6)! </nb> </n>  Samsara provides API endpoints so that you can build powerful applications and custom solutions with sensor data. Samsara has endpoints available to track and analyze sensors, vehicles, and entire fleets.  The Samsara API is a [RESTful API](https://en.wikipedia.org/wiki/Representational_state_transfer). It uses standard [HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol) authentication, verbs, and response codes, and it returns [JSON](http://www.json.org/) response bodies. If you're familiar with what you can build with a REST API, then this will be your go-to API reference.  Visit [developers.samsara.com](https://developers.samsara.com) to find getting started guides and an API overview.  If you have any questions, reach out to us at [support@samsara.com](mailto:support@samsara.com).  ## Endpoints  All our APIs can be accessed through HTTP requests to URLs like:  ``` https://api.samsara.com/<endpoint> ```  For EU customers, this URL will be:  ``` https://api.eu.samsara.com/<endpoint> ```  <n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> Note </nh> <nb> Legacy endpoints will have the URL: `https://api.samsara.com/v1/<endpoint>` or `https://api.eu.samsara.com/v1/<endpoint>` </nb> </n>  ## Authentication  To authenticate your API request you will need to include your secret token. You can manage your API tokens in the [Dashboard](https://cloud.samsara.com). They are visible under `Settings->Organization->API Tokens`.  Your API tokens carry many privileges, so be sure to keep them secure. Do not share your secret API tokens in publicly accessible areas such as GitHub, client-side code, and so on.  Authentication to the API is performed via Bearer Token in the HTTP Authorization header. Provide your API token as the `access_token` value in an `Authorization: Bearer` header. You do not need to provide a password:  ```curl Authorization: Bearer {access_token} ```  All API requests must be made over [HTTPS](https://en.wikipedia.org/wiki/HTTPS). Calls made over plain HTTP or without authentication will fail.  ## Common Patterns  You can find more info about request methods, response codes, error codes, versioning, pagination, timestamps, and mini-objects [here](https://developers.samsara.com/docs/common-structures).   # noqa: E501

    OpenAPI spec version: 2019-09-13
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from swagger_client.api.addresses_api import AddressesApi
from swagger_client.api.contacts_api import ContactsApi
from swagger_client.api.documents_api import DocumentsApi
from swagger_client.api.drivers_api import DriversApi
from swagger_client.api.hours_of_service_api import HoursOfServiceApi
from swagger_client.api.industrial_api import IndustrialApi
from swagger_client.api.maintenance_api import MaintenanceApi
from swagger_client.api.messages_api import MessagesApi
from swagger_client.api.routes_api import RoutesApi
from swagger_client.api.safety_api import SafetyApi
from swagger_client.api.sensors_api import SensorsApi
from swagger_client.api.tags_api import TagsApi
from swagger_client.api.trips_api import TripsApi
from swagger_client.api.users_api import UsersApi
from swagger_client.api.vehicles_api import VehiclesApi
# import ApiClient
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration
# import models into sdk package
from swagger_client.models.address import Address
from swagger_client.models.address_core import AddressCore
from swagger_client.models.address_create import AddressCreate
from swagger_client.models.address_geofence_request import AddressGeofenceRequest
from swagger_client.models.address_geofence_response import AddressGeofenceResponse
from swagger_client.models.address_patch import AddressPatch
from swagger_client.models.address_request_core import AddressRequestCore
from swagger_client.models.address_response_core import AddressResponseCore
from swagger_client.models.contact import Contact
from swagger_client.models.contact_input import ContactInput
from swagger_client.models.contact_tiny_response import ContactTinyResponse
from swagger_client.models.driver import Driver
from swagger_client.models.driver_base import DriverBase
from swagger_client.models.driver_create import DriverCreate
from swagger_client.models.driver_tiny_response import DriverTinyResponse
from swagger_client.models.driver_update import DriverUpdate
from swagger_client.models.external_ids import ExternalIds
from swagger_client.models.location import Location
from swagger_client.models.locations_wrapper import LocationsWrapper
from swagger_client.models.pagination_response import PaginationResponse
from swagger_client.models.parent_tag import ParentTag
from swagger_client.models.remote_obd_test_records import RemoteObdTestRecords
from swagger_client.models.standard_error_response import StandardErrorResponse
from swagger_client.models.tag import Tag
from swagger_client.models.tag_tiny_response import TagTinyResponse
from swagger_client.models.tag_update import TagUpdate
from swagger_client.models.tagged_object import TaggedObject
from swagger_client.models.tagged_object_id import TaggedObjectId
from swagger_client.models.time import Time
from swagger_client.models.tiny_tag import TinyTag
from swagger_client.models.user import User
from swagger_client.models.user_create import UserCreate
from swagger_client.models.user_role import UserRole
from swagger_client.models.user_role_input import UserRoleInput
from swagger_client.models.user_role_response import UserRoleResponse
from swagger_client.models.user_role_tiny_response import UserRoleTinyResponse
from swagger_client.models.user_update import UserUpdate
from swagger_client.models.v1_cargo_response import V1CargoResponse
from swagger_client.models.v1_data_input_history_response import V1DataInputHistoryResponse
from swagger_client.models.v1_dispatch_job import V1DispatchJob
from swagger_client.models.v1_dispatch_job_create import V1DispatchJobCreate
from swagger_client.models.v1_dispatch_job_document_info import V1DispatchJobDocumentInfo
from swagger_client.models.v1_dispatch_job_update import V1DispatchJobUpdate
from swagger_client.models.v1_dispatch_job_without_eta import V1DispatchJobWithoutETA
from swagger_client.models.v1_dispatch_route import V1DispatchRoute
from swagger_client.models.v1_dispatch_route_base import V1DispatchRouteBase
from swagger_client.models.v1_dispatch_route_create import V1DispatchRouteCreate
from swagger_client.models.v1_dispatch_route_create_base import V1DispatchRouteCreateBase
from swagger_client.models.v1_dispatch_route_historical_entry import V1DispatchRouteHistoricalEntry
from swagger_client.models.v1_dispatch_route_history import V1DispatchRouteHistory
from swagger_client.models.v1_dispatch_route_update import V1DispatchRouteUpdate
from swagger_client.models.v1_dispatch_route_update_base import V1DispatchRouteUpdateBase
from swagger_client.models.v1_dispatch_route_without_eta import V1DispatchRouteWithoutETA
from swagger_client.models.v1_dispatch_routes import V1DispatchRoutes
from swagger_client.models.v1_document import V1Document
from swagger_client.models.v1_document_base import V1DocumentBase
from swagger_client.models.v1_document_create import V1DocumentCreate
from swagger_client.models.v1_document_create_base import V1DocumentCreateBase
from swagger_client.models.v1_document_field import V1DocumentField
from swagger_client.models.v1_document_field_create import V1DocumentFieldCreate
from swagger_client.models.v1_document_field_type import V1DocumentFieldType
from swagger_client.models.v1_document_type import V1DocumentType
from swagger_client.models.v1_document_types import V1DocumentTypes
from swagger_client.models.v1_documents import V1Documents
from swagger_client.models.v1_door_response import V1DoorResponse
from swagger_client.models.v1_driver_daily_log_response import V1DriverDailyLogResponse
from swagger_client.models.v1_driver_safety_score_response import V1DriverSafetyScoreResponse
from swagger_client.models.v1_dvir_base import V1DvirBase
from swagger_client.models.v1_dvir_defect_base import V1DvirDefectBase
from swagger_client.models.v1_dvir_list_response import V1DvirListResponse
from swagger_client.models.v1_error_response import V1ErrorResponse
from swagger_client.models.v1_fleet_vehicle_location import V1FleetVehicleLocation
from swagger_client.models.v1_fleet_vehicle_locations import V1FleetVehicleLocations
from swagger_client.models.v1_fleet_vehicles_locations import V1FleetVehiclesLocations
from swagger_client.models.v1_hos_authentication_logs_response import V1HosAuthenticationLogsResponse
from swagger_client.models.v1_hos_logs_response import V1HosLogsResponse
from swagger_client.models.v1_hos_logs_summary_response import V1HosLogsSummaryResponse
from swagger_client.models.v1_humidity_response import V1HumidityResponse
from swagger_client.models.v1_machine import V1Machine
from swagger_client.models.v1_machine_history_response import V1MachineHistoryResponse
from swagger_client.models.v1_message import V1Message
from swagger_client.models.v1_message_response import V1MessageResponse
from swagger_client.models.v1_message_sender import V1MessageSender
from swagger_client.models.v1_messages import V1Messages
from swagger_client.models.v1_messages_response import V1MessagesResponse
from swagger_client.models.v1_programs_for_the_camera_response import V1ProgramsForTheCameraResponse
from swagger_client.models.v1_safety_report_harsh_event import V1SafetyReportHarshEvent
from swagger_client.models.v1_sensor import V1Sensor
from swagger_client.models.v1_sensor_history_response import V1SensorHistoryResponse
from swagger_client.models.v1_temperature_response import V1TemperatureResponse
from swagger_client.models.v1_trip_response import V1TripResponse
from swagger_client.models.v1_vehicle_harsh_event_response import V1VehicleHarshEventResponse
from swagger_client.models.v1_vehicle_location import V1VehicleLocation
from swagger_client.models.v1_vehicle_maintenance import V1VehicleMaintenance
from swagger_client.models.v1_vehicle_safety_score_response import V1VehicleSafetyScoreResponse
from swagger_client.models.v1_vision_cameras_response import V1VisionCamerasResponse
from swagger_client.models.v1_vision_run_by_camera_response import V1VisionRunByCameraResponse
from swagger_client.models.v1_vision_runs_by_camera_and_program_response import V1VisionRunsByCameraAndProgramResponse
from swagger_client.models.v1_vision_runs_by_camera_response import V1VisionRunsByCameraResponse
from swagger_client.models.v1_vision_runs_response import V1VisionRunsResponse
from swagger_client.models.v1_vision_step_results import V1VisionStepResults
from swagger_client.models.v1all_route_job_updates import V1allRouteJobUpdates
from swagger_client.models.v1job_status import V1jobStatus
from swagger_client.models.v1job_update_object import V1jobUpdateObject
from swagger_client.models.v1prev_job_status import V1prevJobStatus
from swagger_client.models.vehicle_ctp_smog_test_data import VehicleCtpSmogTestData
from swagger_client.models.vehicle_ctp_smog_test_data_wrapper import VehicleCtpSmogTestDataWrapper
from swagger_client.models.vehicle_engine_state import VehicleEngineState
from swagger_client.models.vehicle_engine_states_wrapper import VehicleEngineStatesWrapper
from swagger_client.models.vehicle_fuel_percent import VehicleFuelPercent
from swagger_client.models.vehicle_fuel_percents_wrapper import VehicleFuelPercentsWrapper
from swagger_client.models.vehicle_gps_odometer_meters import VehicleGpsOdometerMeters
from swagger_client.models.vehicle_gps_odometer_meters_wrapper import VehicleGpsOdometerMetersWrapper
from swagger_client.models.vehicle_list_response import VehicleListResponse
from swagger_client.models.vehicle_location import VehicleLocation
from swagger_client.models.vehicle_location_wrapper import VehicleLocationWrapper
from swagger_client.models.vehicle_locations_list_response import VehicleLocationsListResponse
from swagger_client.models.vehicle_locations_snapshot_response import VehicleLocationsSnapshotResponse
from swagger_client.models.vehicle_locations_wrapper import VehicleLocationsWrapper
from swagger_client.models.vehicle_obd_engine_seconds import VehicleObdEngineSeconds
from swagger_client.models.vehicle_obd_engine_seconds_wrapper import VehicleObdEngineSecondsWrapper
from swagger_client.models.vehicle_obd_odometer_meters import VehicleObdOdometerMeters
from swagger_client.models.vehicle_obd_odometer_meters_wrapper import VehicleObdOdometerMetersWrapper
from swagger_client.models.vehicle_patch import VehiclePatch
from swagger_client.models.vehicle_response import VehicleResponse
from swagger_client.models.vehicle_stats_list_response import VehicleStatsListResponse
from swagger_client.models.vehicle_stats_snapshot_response import VehicleStatsSnapshotResponse
from swagger_client.models.vehicle_tiny_response import VehicleTinyResponse
