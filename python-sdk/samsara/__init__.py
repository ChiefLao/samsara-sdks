# coding: utf-8

# flake8: noqa

"""
    Samsara API

    Integrate your data with the Samsara API, customize the Samsara experience, and join a community of developers building with Samsara.  # noqa: E501

    The version of the OpenAPI document: 2019-12-12
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.0.0"

# import apis into sdk package
from samsara.api.default_api import DefaultApi

# import ApiClient
from samsara.api_client import ApiClient
from samsara.configuration import Configuration
from samsara.exceptions import OpenApiException
from samsara.exceptions import ApiTypeError
from samsara.exceptions import ApiValueError
from samsara.exceptions import ApiKeyError
from samsara.exceptions import ApiException
# import models into sdk package
from samsara.models.address import Address
from samsara.models.address_external_ids import AddressExternalIds
from samsara.models.address_geofence import AddressGeofence
from samsara.models.address_geofence_circle import AddressGeofenceCircle
from samsara.models.address_geofence_polygon import AddressGeofencePolygon
from samsara.models.address_geofence_polygon_vertices import AddressGeofencePolygonVertices
from samsara.models.address_response import AddressResponse
from samsara.models.contact import Contact
from samsara.models.contact_response import ContactResponse
from samsara.models.contact_tiny_response import ContactTinyResponse
from samsara.models.create_address_request import CreateAddressRequest
from samsara.models.create_contact_request import CreateContactRequest
from samsara.models.create_driver_request import CreateDriverRequest
from samsara.models.create_tag_request import CreateTagRequest
from samsara.models.create_user_request import CreateUserRequest
from samsara.models.driver import Driver
from samsara.models.driver_carrier_settings import DriverCarrierSettings
from samsara.models.driver_external_ids import DriverExternalIds
from samsara.models.driver_locale import DriverLocale
from samsara.models.driver_response import DriverResponse
from samsara.models.driver_static_assigned_vehicle import DriverStaticAssignedVehicle
from samsara.models.driver_tiny_response import DriverTinyResponse
from samsara.models.driver_vehicle_group_tag import DriverVehicleGroupTag
from samsara.models.list_addresses_response import ListAddressesResponse
from samsara.models.list_contacts_response import ListContactsResponse
from samsara.models.list_drivers_response import ListDriversResponse
from samsara.models.list_tags_response import ListTagsResponse
from samsara.models.list_user_roles_response import ListUserRolesResponse
from samsara.models.list_users_response import ListUsersResponse
from samsara.models.list_vehicles_response import ListVehiclesResponse
from samsara.models.pagination_response import PaginationResponse
from samsara.models.parent_tag import ParentTag
from samsara.models.replace_tag_request import ReplaceTagRequest
from samsara.models.standard_error_response import StandardErrorResponse
from samsara.models.tag import Tag
from samsara.models.tag_all_of import TagAllOf
from samsara.models.tag_response import TagResponse
from samsara.models.tag_tiny_response import TagTinyResponse
from samsara.models.tagged_object import TaggedObject
from samsara.models.tiny_tag import TinyTag
from samsara.models.update_address_request import UpdateAddressRequest
from samsara.models.update_contact_request import UpdateContactRequest
from samsara.models.update_driver_request import UpdateDriverRequest
from samsara.models.update_user_request import UpdateUserRequest
from samsara.models.update_vehicle_request import UpdateVehicleRequest
from samsara.models.user import User
from samsara.models.user_auth_type import UserAuthType
from samsara.models.user_response import UserResponse
from samsara.models.user_role import UserRole
from samsara.models.vehicle import Vehicle
from samsara.models.vehicle_aux_input_type import VehicleAuxInputType
from samsara.models.vehicle_aux_input_type1 import VehicleAuxInputType1
from samsara.models.vehicle_aux_input_type2 import VehicleAuxInputType2
from samsara.models.vehicle_external_ids import VehicleExternalIds
from samsara.models.vehicle_harsh_acceleration_setting_type import VehicleHarshAccelerationSettingType
from samsara.models.vehicle_location import VehicleLocation
from samsara.models.vehicle_location_reverse_geo import VehicleLocationReverseGeo
from samsara.models.vehicle_location_time import VehicleLocationTime
from samsara.models.vehicle_locations_list_response import VehicleLocationsListResponse
from samsara.models.vehicle_locations_list_response_data import VehicleLocationsListResponseData
from samsara.models.vehicle_locations_response import VehicleLocationsResponse
from samsara.models.vehicle_locations_response_data import VehicleLocationsResponseData
from samsara.models.vehicle_response import VehicleResponse
from samsara.models.vehicle_static_assigned_driver import VehicleStaticAssignedDriver
from samsara.models.vehicle_stats_engine_state import VehicleStatsEngineState
from samsara.models.vehicle_stats_fuel_percent import VehicleStatsFuelPercent
from samsara.models.vehicle_stats_gps_distance_meters import VehicleStatsGpsDistanceMeters
from samsara.models.vehicle_stats_gps_odometer_meters import VehicleStatsGpsOdometerMeters
from samsara.models.vehicle_stats_list_response import VehicleStatsListResponse
from samsara.models.vehicle_stats_list_response_data import VehicleStatsListResponseData
from samsara.models.vehicle_stats_obd_engine_seconds import VehicleStatsObdEngineSeconds
from samsara.models.vehicle_stats_obd_odometer_meters import VehicleStatsObdOdometerMeters
from samsara.models.vehicle_stats_response import VehicleStatsResponse
from samsara.models.vehicle_stats_response_data import VehicleStatsResponseData
from samsara.models.vehicle_stats_time import VehicleStatsTime
from samsara.models.vehicle_tiny_response import VehicleTinyResponse

