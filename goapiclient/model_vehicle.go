/*
 * Samsara API
 *
 * <style type=\"text/css\"> n {     padding: 1em;     width: 100%;     display: block;     margin: 28px 0; } n.info {     background-color: rgba(0, 51, 160, 0.1); } n.warning {     background-color: #fdf6e3; } i:before {     margin-right: 6px; } nh {     font-size: 1.5rem;     font-weight: 700;     line-height: 1.1;     display: block; } nb {     margin-top: 10px;     padding-left: 22px;     display: block; } </style>  # Overview  <n class=\"info\"> <nh> <i class=\"fa fa-info-circle\"></i> Something new! </nh> <nb> Welcome Samsara's new and improved API. Check out our FAQ [here](https://developers.samsara.com/docs/introducing-our-next-generation-api) to see what's changed and learn how to get started.<br> <br> Want to access the legacy API docs? You can find them [here](https://www.samsara.com/api-legacy).<br> <br> *Note: Because this is a new set of APIs, we have not transitioned all endpoints over to this standard. Endpoints that still use the legacy standards are indicated in the reference documentation. If you can't find an API that you're looking for, we encourage you to look for it in our [legacy API docs](https://www.samsara.com/api-legacy) as we continue to transition all endpoints over. Check back here for updates!*<br> <br> Submit your feedback [here](https://forms.gle/r4bs6HQshQAvBuwv6)! </nb> </n>  Samsara provides API endpoints so that you can build powerful applications and custom solutions with sensor data. Samsara has endpoints available to track and analyze sensors, vehicles, and entire fleets.  The Samsara API is a [RESTful API](https://en.wikipedia.org/wiki/Representational_state_transfer). It uses standard [HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol) authentication, verbs, and response codes, and it returns [JSON](http://www.json.org/) response bodies. If you're familiar with what you can build with a REST API, then this will be your go-to API reference.  Visit [developers.samsara.com](https://developers.samsara.com) to find getting started guides and an API overview.  If you have any questions, reach out to us at [support@samsara.com](mailto:support@samsara.com).  ## Endpoints  All our APIs can be accessed through HTTP requests to URLs like:  ``` https://api.samsara.com/<endpoint> ```  For EU customers, this URL will be:  ``` https://api.eu.samsara.com/<endpoint> ```  <n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> Note </nh> <nb> Legacy endpoints will have the URL: `https://api.samsara.com/v1/<endpoint>` or `https://api.eu.samsara.com/v1/<endpoint>` </nb> </n>  ## Authentication  To authenticate your API request you will need to include your secret token. You can manage your API tokens in the [Dashboard](https://cloud.samsara.com). They are visible under `Settings->Organization->API Tokens`.  Your API tokens carry many privileges, so be sure to keep them secure. Do not share your secret API tokens in publicly accessible areas such as GitHub, client-side code, and so on.  Authentication to the API is performed via Bearer Token in the HTTP Authorization header. Provide your API token as the `access_token` value in an `Authorization: Bearer` header. You do not need to provide a password:  ```curl Authorization: Bearer {access_token} ```  All API requests must be made over [HTTPS](https://en.wikipedia.org/wiki/HTTPS). Calls made over plain HTTP or without authentication will fail.  ## Common Patterns  You can find more info about request methods, response codes, error codes, versioning, pagination, timestamps, and mini-objects [here](https://developers.samsara.com/docs/common-structures).
 *
 * API version: 2019-12-12
 * Generated by: OpenAPI Generator (https://openapi-generator.tech)
 */

package goapiclient

import (
	"bytes"
	"encoding/json"
)

// Vehicle The vehicle object.
type Vehicle struct {
	AuxInputType1 *VehicleAuxInputType `json:"auxInputType1,omitempty"`
	AuxInputType2 *VehicleAuxInputType `json:"auxInputType2,omitempty"`
	// The [external IDs](https://developers.samsara.com/docs/external-ids) for the given object.
	ExternalIds                  *map[string]string                   `json:"externalIds,omitempty"`
	HarshAccelerationSettingType *VehicleHarshAccelerationSettingType `json:"harshAccelerationSettingType,omitempty"`
	// The unique Samsara ID of the Vehicle. This is automatically generated when the Vehicle object is created. It cannot be changed.
	Id string `json:"id"`
	// The license plate of the Vehicle. **By default**: empty. Can be set or updated through the Samsara Dashboard or the API at any time.
	LicensePlate *string `json:"licensePlate,omitempty"`
	// The Vehicle’s manufacturing make. Automatically read from the engine computer if available. Empty if not available. Cannot be manually set.
	Make *string `json:"make,omitempty"`
	// The Vehicle’s manufacturing model. Automatically read from the engine computer if available. Empty if not available. Cannot be manually set.
	Model *string `json:"model,omitempty"`
	// The human-readable name of the Vehicle. This is set by a fleet administrator and will appear in both Samsara’s cloud dashboard as well as the Samsara Driver mobile app. **By default**, this name is the serial number of the Samsara Vehicle Gateway. It can be set or updated through the Samsara Dashboard or through the API at any time.
	Name *string `json:"name,omitempty"`
	// These are generic notes about the Vehicle. Empty by default. Can be set or updated through the Samsara Dashboard or the API at any time.
	Notes                *string             `json:"notes,omitempty"`
	StaticAssignedDriver *DriverTinyResponse `json:"staticAssignedDriver,omitempty"`
	// The list of [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting) associated with the Vehicle. **By default**: empty. Can be set or updated through the Samsara Dashboard or the API at any time.
	Tags *[]TagTinyResponse `json:"tags,omitempty"`
	// The VIN of the Vehicle. Most of the time, this will be automatically read from the engine computer by the Samsara Vehicle Gateway. It will be empty if it cannot be read. It can be set or updated through the Samsara Dashboard or the API at any time.
	Vin *string `json:"vin,omitempty"`
	// The Vehicle’s manufacturing model. Automatically read from the engine computer if available. Empty if not available. Cannot be manually set.
	Year *string `json:"year,omitempty"`
}

// GetAuxInputType1 returns the AuxInputType1 field value if set, zero value otherwise.
func (o *Vehicle) GetAuxInputType1() VehicleAuxInputType {
	if o == nil || o.AuxInputType1 == nil {
		var ret VehicleAuxInputType
		return ret
	}
	return *o.AuxInputType1
}

// GetAuxInputType1Ok returns a tuple with the AuxInputType1 field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Vehicle) GetAuxInputType1Ok() (VehicleAuxInputType, bool) {
	if o == nil || o.AuxInputType1 == nil {
		var ret VehicleAuxInputType
		return ret, false
	}
	return *o.AuxInputType1, true
}

// HasAuxInputType1 returns a boolean if a field has been set.
func (o *Vehicle) HasAuxInputType1() bool {
	if o != nil && o.AuxInputType1 != nil {
		return true
	}

	return false
}

// SetAuxInputType1 gets a reference to the given VehicleAuxInputType and assigns it to the AuxInputType1 field.
func (o *Vehicle) SetAuxInputType1(v VehicleAuxInputType) {
	o.AuxInputType1 = &v
}

// GetAuxInputType2 returns the AuxInputType2 field value if set, zero value otherwise.
func (o *Vehicle) GetAuxInputType2() VehicleAuxInputType {
	if o == nil || o.AuxInputType2 == nil {
		var ret VehicleAuxInputType
		return ret
	}
	return *o.AuxInputType2
}

// GetAuxInputType2Ok returns a tuple with the AuxInputType2 field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Vehicle) GetAuxInputType2Ok() (VehicleAuxInputType, bool) {
	if o == nil || o.AuxInputType2 == nil {
		var ret VehicleAuxInputType
		return ret, false
	}
	return *o.AuxInputType2, true
}

// HasAuxInputType2 returns a boolean if a field has been set.
func (o *Vehicle) HasAuxInputType2() bool {
	if o != nil && o.AuxInputType2 != nil {
		return true
	}

	return false
}

// SetAuxInputType2 gets a reference to the given VehicleAuxInputType and assigns it to the AuxInputType2 field.
func (o *Vehicle) SetAuxInputType2(v VehicleAuxInputType) {
	o.AuxInputType2 = &v
}

// GetExternalIds returns the ExternalIds field value if set, zero value otherwise.
func (o *Vehicle) GetExternalIds() map[string]string {
	if o == nil || o.ExternalIds == nil {
		var ret map[string]string
		return ret
	}
	return *o.ExternalIds
}

// GetExternalIdsOk returns a tuple with the ExternalIds field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Vehicle) GetExternalIdsOk() (map[string]string, bool) {
	if o == nil || o.ExternalIds == nil {
		var ret map[string]string
		return ret, false
	}
	return *o.ExternalIds, true
}

// HasExternalIds returns a boolean if a field has been set.
func (o *Vehicle) HasExternalIds() bool {
	if o != nil && o.ExternalIds != nil {
		return true
	}

	return false
}

// SetExternalIds gets a reference to the given map[string]string and assigns it to the ExternalIds field.
func (o *Vehicle) SetExternalIds(v map[string]string) {
	o.ExternalIds = &v
}

// GetHarshAccelerationSettingType returns the HarshAccelerationSettingType field value if set, zero value otherwise.
func (o *Vehicle) GetHarshAccelerationSettingType() VehicleHarshAccelerationSettingType {
	if o == nil || o.HarshAccelerationSettingType == nil {
		var ret VehicleHarshAccelerationSettingType
		return ret
	}
	return *o.HarshAccelerationSettingType
}

// GetHarshAccelerationSettingTypeOk returns a tuple with the HarshAccelerationSettingType field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Vehicle) GetHarshAccelerationSettingTypeOk() (VehicleHarshAccelerationSettingType, bool) {
	if o == nil || o.HarshAccelerationSettingType == nil {
		var ret VehicleHarshAccelerationSettingType
		return ret, false
	}
	return *o.HarshAccelerationSettingType, true
}

// HasHarshAccelerationSettingType returns a boolean if a field has been set.
func (o *Vehicle) HasHarshAccelerationSettingType() bool {
	if o != nil && o.HarshAccelerationSettingType != nil {
		return true
	}

	return false
}

// SetHarshAccelerationSettingType gets a reference to the given VehicleHarshAccelerationSettingType and assigns it to the HarshAccelerationSettingType field.
func (o *Vehicle) SetHarshAccelerationSettingType(v VehicleHarshAccelerationSettingType) {
	o.HarshAccelerationSettingType = &v
}

// GetId returns the Id field value
func (o *Vehicle) GetId() string {
	if o == nil {
		var ret string
		return ret
	}

	return o.Id
}

// SetId sets field value
func (o *Vehicle) SetId(v string) {
	o.Id = v
}

// GetLicensePlate returns the LicensePlate field value if set, zero value otherwise.
func (o *Vehicle) GetLicensePlate() string {
	if o == nil || o.LicensePlate == nil {
		var ret string
		return ret
	}
	return *o.LicensePlate
}

// GetLicensePlateOk returns a tuple with the LicensePlate field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Vehicle) GetLicensePlateOk() (string, bool) {
	if o == nil || o.LicensePlate == nil {
		var ret string
		return ret, false
	}
	return *o.LicensePlate, true
}

// HasLicensePlate returns a boolean if a field has been set.
func (o *Vehicle) HasLicensePlate() bool {
	if o != nil && o.LicensePlate != nil {
		return true
	}

	return false
}

// SetLicensePlate gets a reference to the given string and assigns it to the LicensePlate field.
func (o *Vehicle) SetLicensePlate(v string) {
	o.LicensePlate = &v
}

// GetMake returns the Make field value if set, zero value otherwise.
func (o *Vehicle) GetMake() string {
	if o == nil || o.Make == nil {
		var ret string
		return ret
	}
	return *o.Make
}

// GetMakeOk returns a tuple with the Make field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Vehicle) GetMakeOk() (string, bool) {
	if o == nil || o.Make == nil {
		var ret string
		return ret, false
	}
	return *o.Make, true
}

// HasMake returns a boolean if a field has been set.
func (o *Vehicle) HasMake() bool {
	if o != nil && o.Make != nil {
		return true
	}

	return false
}

// SetMake gets a reference to the given string and assigns it to the Make field.
func (o *Vehicle) SetMake(v string) {
	o.Make = &v
}

// GetModel returns the Model field value if set, zero value otherwise.
func (o *Vehicle) GetModel() string {
	if o == nil || o.Model == nil {
		var ret string
		return ret
	}
	return *o.Model
}

// GetModelOk returns a tuple with the Model field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Vehicle) GetModelOk() (string, bool) {
	if o == nil || o.Model == nil {
		var ret string
		return ret, false
	}
	return *o.Model, true
}

// HasModel returns a boolean if a field has been set.
func (o *Vehicle) HasModel() bool {
	if o != nil && o.Model != nil {
		return true
	}

	return false
}

// SetModel gets a reference to the given string and assigns it to the Model field.
func (o *Vehicle) SetModel(v string) {
	o.Model = &v
}

// GetName returns the Name field value if set, zero value otherwise.
func (o *Vehicle) GetName() string {
	if o == nil || o.Name == nil {
		var ret string
		return ret
	}
	return *o.Name
}

// GetNameOk returns a tuple with the Name field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Vehicle) GetNameOk() (string, bool) {
	if o == nil || o.Name == nil {
		var ret string
		return ret, false
	}
	return *o.Name, true
}

// HasName returns a boolean if a field has been set.
func (o *Vehicle) HasName() bool {
	if o != nil && o.Name != nil {
		return true
	}

	return false
}

// SetName gets a reference to the given string and assigns it to the Name field.
func (o *Vehicle) SetName(v string) {
	o.Name = &v
}

// GetNotes returns the Notes field value if set, zero value otherwise.
func (o *Vehicle) GetNotes() string {
	if o == nil || o.Notes == nil {
		var ret string
		return ret
	}
	return *o.Notes
}

// GetNotesOk returns a tuple with the Notes field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Vehicle) GetNotesOk() (string, bool) {
	if o == nil || o.Notes == nil {
		var ret string
		return ret, false
	}
	return *o.Notes, true
}

// HasNotes returns a boolean if a field has been set.
func (o *Vehicle) HasNotes() bool {
	if o != nil && o.Notes != nil {
		return true
	}

	return false
}

// SetNotes gets a reference to the given string and assigns it to the Notes field.
func (o *Vehicle) SetNotes(v string) {
	o.Notes = &v
}

// GetStaticAssignedDriver returns the StaticAssignedDriver field value if set, zero value otherwise.
func (o *Vehicle) GetStaticAssignedDriver() DriverTinyResponse {
	if o == nil || o.StaticAssignedDriver == nil {
		var ret DriverTinyResponse
		return ret
	}
	return *o.StaticAssignedDriver
}

// GetStaticAssignedDriverOk returns a tuple with the StaticAssignedDriver field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Vehicle) GetStaticAssignedDriverOk() (DriverTinyResponse, bool) {
	if o == nil || o.StaticAssignedDriver == nil {
		var ret DriverTinyResponse
		return ret, false
	}
	return *o.StaticAssignedDriver, true
}

// HasStaticAssignedDriver returns a boolean if a field has been set.
func (o *Vehicle) HasStaticAssignedDriver() bool {
	if o != nil && o.StaticAssignedDriver != nil {
		return true
	}

	return false
}

// SetStaticAssignedDriver gets a reference to the given DriverTinyResponse and assigns it to the StaticAssignedDriver field.
func (o *Vehicle) SetStaticAssignedDriver(v DriverTinyResponse) {
	o.StaticAssignedDriver = &v
}

// GetTags returns the Tags field value if set, zero value otherwise.
func (o *Vehicle) GetTags() []TagTinyResponse {
	if o == nil || o.Tags == nil {
		var ret []TagTinyResponse
		return ret
	}
	return *o.Tags
}

// GetTagsOk returns a tuple with the Tags field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Vehicle) GetTagsOk() ([]TagTinyResponse, bool) {
	if o == nil || o.Tags == nil {
		var ret []TagTinyResponse
		return ret, false
	}
	return *o.Tags, true
}

// HasTags returns a boolean if a field has been set.
func (o *Vehicle) HasTags() bool {
	if o != nil && o.Tags != nil {
		return true
	}

	return false
}

// SetTags gets a reference to the given []TagTinyResponse and assigns it to the Tags field.
func (o *Vehicle) SetTags(v []TagTinyResponse) {
	o.Tags = &v
}

// GetVin returns the Vin field value if set, zero value otherwise.
func (o *Vehicle) GetVin() string {
	if o == nil || o.Vin == nil {
		var ret string
		return ret
	}
	return *o.Vin
}

// GetVinOk returns a tuple with the Vin field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Vehicle) GetVinOk() (string, bool) {
	if o == nil || o.Vin == nil {
		var ret string
		return ret, false
	}
	return *o.Vin, true
}

// HasVin returns a boolean if a field has been set.
func (o *Vehicle) HasVin() bool {
	if o != nil && o.Vin != nil {
		return true
	}

	return false
}

// SetVin gets a reference to the given string and assigns it to the Vin field.
func (o *Vehicle) SetVin(v string) {
	o.Vin = &v
}

// GetYear returns the Year field value if set, zero value otherwise.
func (o *Vehicle) GetYear() string {
	if o == nil || o.Year == nil {
		var ret string
		return ret
	}
	return *o.Year
}

// GetYearOk returns a tuple with the Year field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Vehicle) GetYearOk() (string, bool) {
	if o == nil || o.Year == nil {
		var ret string
		return ret, false
	}
	return *o.Year, true
}

// HasYear returns a boolean if a field has been set.
func (o *Vehicle) HasYear() bool {
	if o != nil && o.Year != nil {
		return true
	}

	return false
}

// SetYear gets a reference to the given string and assigns it to the Year field.
func (o *Vehicle) SetYear(v string) {
	o.Year = &v
}

type NullableVehicle struct {
	Value        Vehicle
	ExplicitNull bool
}

func (v NullableVehicle) MarshalJSON() ([]byte, error) {
	switch {
	case v.ExplicitNull:
		return []byte("null"), nil
	default:
		return json.Marshal(v.Value)
	}
}

func (v *NullableVehicle) UnmarshalJSON(src []byte) error {
	if bytes.Equal(src, []byte("null")) {
		v.ExplicitNull = true
		return nil
	}

	return json.Unmarshal(src, &v.Value)
}
