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
	"time"
)

// Driver A driver object
type Driver struct {
	CarrierSettings *DriverCarrierSettings `json:"carrierSettings,omitempty"`
	// The date and time this driver was created in RFC 3339 format.
	CreatedAtTime          *time.Time              `json:"createdAtTime,omitempty"`
	DriverActivationStatus *DriverActivationStatus `json:"driverActivationStatus,omitempty"`
	// Flag indicating this driver may use Adverse Weather exemptions in ELD logs.
	EldAdverseWeatherExemptionEnabled *bool `json:"eldAdverseWeatherExemptionEnabled,omitempty"`
	// Flag indicating this driver may use Big Day exemption in ELD logs.
	EldBigDayExemptionEnabled *bool `json:"eldBigDayExemptionEnabled,omitempty"`
	// `0` indicating midnight-to-midnight ELD driving hours, `12` to indicate noon-to-noon driving hours.
	EldDayStartHour *int32 `json:"eldDayStartHour,omitempty"`
	// Flag indicating this driver is exempt from the Electronic Logging Mandate.
	EldExempt *bool `json:"eldExempt,omitempty"`
	// Reason that this driver is exempt from the Electronic Logging Mandate (see eldExempt).
	EldExemptReason *string `json:"eldExemptReason,omitempty"`
	// Flag indicating this driver may select the Personal Conveyance duty status in ELD logs.
	EldPcEnabled *bool `json:"eldPcEnabled,omitempty"`
	// Flag indicating this driver may select the Yard Move duty status in ELD logs.
	EldYmEnabled *bool `json:"eldYmEnabled,omitempty"`
	// The [external IDs](https://developers.samsara.com/docs/external-ids) for the given object.
	ExternalIds *map[string]string `json:"externalIds,omitempty"`
	// Samsara ID for the driver.
	Id *string `json:"id,omitempty"`
	// [DEPRECATED] A boolean indicating whether or not the driver is deactivated. Use `driverActivationStatus` instead.
	IsDeactivated *bool `json:"isDeactivated,omitempty"`
	// Driver's state issued license number. The combination of this number and `licenseState` must be unique.
	LicenseNumber *string `json:"licenseNumber,omitempty"`
	// Abbreviation of state that issued driver's license.
	LicenseState *string       `json:"licenseState,omitempty"`
	Locale       *DriverLocale `json:"locale,omitempty"`
	// Driver's name.
	Name *string `json:"name,omitempty"`
	// Notes about the driver.
	Notes *string `json:"notes,omitempty"`
	// Phone number of the driver.
	Phone                 *string                      `json:"phone,omitempty"`
	StaticAssignedVehicle *DriverStaticAssignedVehicle `json:"staticAssignedVehicle,omitempty"`
	// Driver's assigned tachograph card number (Europe specific)
	TachographCardNumber *string `json:"tachographCardNumber,omitempty"`
	// The tags this driver belongs to.
	Tags *[]TagTinyResponse `json:"tags,omitempty"`
	// Home terminal timezone, in order to indicate what time zone should be used to calculate the ELD logs. Driver timezones use [IANA timezone database](https://www.iana.org/time-zones) keys (e.g. `America/Los_Angeles`, `America/New_York`, `Europe/London`, etc.). You can find a mapping of common timezone formats to IANA timezone keys [here](https://unicode.org/cldr/charts/latest/supplemental/zone_tzid.html).
	Timezone *string `json:"timezone,omitempty"`
	// The date and time this driver was last updated in RFC 3339 format.
	UpdatedAtTime *time.Time `json:"updatedAtTime,omitempty"`
	// Driver's login username into the driver app. The username may not contain spaces or the '@' symbol. The username must be unique.
	Username        *string                `json:"username,omitempty"`
	VehicleGroupTag *DriverVehicleGroupTag `json:"vehicleGroupTag,omitempty"`
}

// GetCarrierSettings returns the CarrierSettings field value if set, zero value otherwise.
func (o *Driver) GetCarrierSettings() DriverCarrierSettings {
	if o == nil || o.CarrierSettings == nil {
		var ret DriverCarrierSettings
		return ret
	}
	return *o.CarrierSettings
}

// GetCarrierSettingsOk returns a tuple with the CarrierSettings field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Driver) GetCarrierSettingsOk() (DriverCarrierSettings, bool) {
	if o == nil || o.CarrierSettings == nil {
		var ret DriverCarrierSettings
		return ret, false
	}
	return *o.CarrierSettings, true
}

// HasCarrierSettings returns a boolean if a field has been set.
func (o *Driver) HasCarrierSettings() bool {
	if o != nil && o.CarrierSettings != nil {
		return true
	}

	return false
}

// SetCarrierSettings gets a reference to the given DriverCarrierSettings and assigns it to the CarrierSettings field.
func (o *Driver) SetCarrierSettings(v DriverCarrierSettings) {
	o.CarrierSettings = &v
}

// GetCreatedAtTime returns the CreatedAtTime field value if set, zero value otherwise.
func (o *Driver) GetCreatedAtTime() time.Time {
	if o == nil || o.CreatedAtTime == nil {
		var ret time.Time
		return ret
	}
	return *o.CreatedAtTime
}

// GetCreatedAtTimeOk returns a tuple with the CreatedAtTime field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Driver) GetCreatedAtTimeOk() (time.Time, bool) {
	if o == nil || o.CreatedAtTime == nil {
		var ret time.Time
		return ret, false
	}
	return *o.CreatedAtTime, true
}

// HasCreatedAtTime returns a boolean if a field has been set.
func (o *Driver) HasCreatedAtTime() bool {
	if o != nil && o.CreatedAtTime != nil {
		return true
	}

	return false
}

// SetCreatedAtTime gets a reference to the given time.Time and assigns it to the CreatedAtTime field.
func (o *Driver) SetCreatedAtTime(v time.Time) {
	o.CreatedAtTime = &v
}

// GetDriverActivationStatus returns the DriverActivationStatus field value if set, zero value otherwise.
func (o *Driver) GetDriverActivationStatus() DriverActivationStatus {
	if o == nil || o.DriverActivationStatus == nil {
		var ret DriverActivationStatus
		return ret
	}
	return *o.DriverActivationStatus
}

// GetDriverActivationStatusOk returns a tuple with the DriverActivationStatus field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Driver) GetDriverActivationStatusOk() (DriverActivationStatus, bool) {
	if o == nil || o.DriverActivationStatus == nil {
		var ret DriverActivationStatus
		return ret, false
	}
	return *o.DriverActivationStatus, true
}

// HasDriverActivationStatus returns a boolean if a field has been set.
func (o *Driver) HasDriverActivationStatus() bool {
	if o != nil && o.DriverActivationStatus != nil {
		return true
	}

	return false
}

// SetDriverActivationStatus gets a reference to the given DriverActivationStatus and assigns it to the DriverActivationStatus field.
func (o *Driver) SetDriverActivationStatus(v DriverActivationStatus) {
	o.DriverActivationStatus = &v
}

// GetEldAdverseWeatherExemptionEnabled returns the EldAdverseWeatherExemptionEnabled field value if set, zero value otherwise.
func (o *Driver) GetEldAdverseWeatherExemptionEnabled() bool {
	if o == nil || o.EldAdverseWeatherExemptionEnabled == nil {
		var ret bool
		return ret
	}
	return *o.EldAdverseWeatherExemptionEnabled
}

// GetEldAdverseWeatherExemptionEnabledOk returns a tuple with the EldAdverseWeatherExemptionEnabled field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Driver) GetEldAdverseWeatherExemptionEnabledOk() (bool, bool) {
	if o == nil || o.EldAdverseWeatherExemptionEnabled == nil {
		var ret bool
		return ret, false
	}
	return *o.EldAdverseWeatherExemptionEnabled, true
}

// HasEldAdverseWeatherExemptionEnabled returns a boolean if a field has been set.
func (o *Driver) HasEldAdverseWeatherExemptionEnabled() bool {
	if o != nil && o.EldAdverseWeatherExemptionEnabled != nil {
		return true
	}

	return false
}

// SetEldAdverseWeatherExemptionEnabled gets a reference to the given bool and assigns it to the EldAdverseWeatherExemptionEnabled field.
func (o *Driver) SetEldAdverseWeatherExemptionEnabled(v bool) {
	o.EldAdverseWeatherExemptionEnabled = &v
}

// GetEldBigDayExemptionEnabled returns the EldBigDayExemptionEnabled field value if set, zero value otherwise.
func (o *Driver) GetEldBigDayExemptionEnabled() bool {
	if o == nil || o.EldBigDayExemptionEnabled == nil {
		var ret bool
		return ret
	}
	return *o.EldBigDayExemptionEnabled
}

// GetEldBigDayExemptionEnabledOk returns a tuple with the EldBigDayExemptionEnabled field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Driver) GetEldBigDayExemptionEnabledOk() (bool, bool) {
	if o == nil || o.EldBigDayExemptionEnabled == nil {
		var ret bool
		return ret, false
	}
	return *o.EldBigDayExemptionEnabled, true
}

// HasEldBigDayExemptionEnabled returns a boolean if a field has been set.
func (o *Driver) HasEldBigDayExemptionEnabled() bool {
	if o != nil && o.EldBigDayExemptionEnabled != nil {
		return true
	}

	return false
}

// SetEldBigDayExemptionEnabled gets a reference to the given bool and assigns it to the EldBigDayExemptionEnabled field.
func (o *Driver) SetEldBigDayExemptionEnabled(v bool) {
	o.EldBigDayExemptionEnabled = &v
}

// GetEldDayStartHour returns the EldDayStartHour field value if set, zero value otherwise.
func (o *Driver) GetEldDayStartHour() int32 {
	if o == nil || o.EldDayStartHour == nil {
		var ret int32
		return ret
	}
	return *o.EldDayStartHour
}

// GetEldDayStartHourOk returns a tuple with the EldDayStartHour field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Driver) GetEldDayStartHourOk() (int32, bool) {
	if o == nil || o.EldDayStartHour == nil {
		var ret int32
		return ret, false
	}
	return *o.EldDayStartHour, true
}

// HasEldDayStartHour returns a boolean if a field has been set.
func (o *Driver) HasEldDayStartHour() bool {
	if o != nil && o.EldDayStartHour != nil {
		return true
	}

	return false
}

// SetEldDayStartHour gets a reference to the given int32 and assigns it to the EldDayStartHour field.
func (o *Driver) SetEldDayStartHour(v int32) {
	o.EldDayStartHour = &v
}

// GetEldExempt returns the EldExempt field value if set, zero value otherwise.
func (o *Driver) GetEldExempt() bool {
	if o == nil || o.EldExempt == nil {
		var ret bool
		return ret
	}
	return *o.EldExempt
}

// GetEldExemptOk returns a tuple with the EldExempt field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Driver) GetEldExemptOk() (bool, bool) {
	if o == nil || o.EldExempt == nil {
		var ret bool
		return ret, false
	}
	return *o.EldExempt, true
}

// HasEldExempt returns a boolean if a field has been set.
func (o *Driver) HasEldExempt() bool {
	if o != nil && o.EldExempt != nil {
		return true
	}

	return false
}

// SetEldExempt gets a reference to the given bool and assigns it to the EldExempt field.
func (o *Driver) SetEldExempt(v bool) {
	o.EldExempt = &v
}

// GetEldExemptReason returns the EldExemptReason field value if set, zero value otherwise.
func (o *Driver) GetEldExemptReason() string {
	if o == nil || o.EldExemptReason == nil {
		var ret string
		return ret
	}
	return *o.EldExemptReason
}

// GetEldExemptReasonOk returns a tuple with the EldExemptReason field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Driver) GetEldExemptReasonOk() (string, bool) {
	if o == nil || o.EldExemptReason == nil {
		var ret string
		return ret, false
	}
	return *o.EldExemptReason, true
}

// HasEldExemptReason returns a boolean if a field has been set.
func (o *Driver) HasEldExemptReason() bool {
	if o != nil && o.EldExemptReason != nil {
		return true
	}

	return false
}

// SetEldExemptReason gets a reference to the given string and assigns it to the EldExemptReason field.
func (o *Driver) SetEldExemptReason(v string) {
	o.EldExemptReason = &v
}

// GetEldPcEnabled returns the EldPcEnabled field value if set, zero value otherwise.
func (o *Driver) GetEldPcEnabled() bool {
	if o == nil || o.EldPcEnabled == nil {
		var ret bool
		return ret
	}
	return *o.EldPcEnabled
}

// GetEldPcEnabledOk returns a tuple with the EldPcEnabled field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Driver) GetEldPcEnabledOk() (bool, bool) {
	if o == nil || o.EldPcEnabled == nil {
		var ret bool
		return ret, false
	}
	return *o.EldPcEnabled, true
}

// HasEldPcEnabled returns a boolean if a field has been set.
func (o *Driver) HasEldPcEnabled() bool {
	if o != nil && o.EldPcEnabled != nil {
		return true
	}

	return false
}

// SetEldPcEnabled gets a reference to the given bool and assigns it to the EldPcEnabled field.
func (o *Driver) SetEldPcEnabled(v bool) {
	o.EldPcEnabled = &v
}

// GetEldYmEnabled returns the EldYmEnabled field value if set, zero value otherwise.
func (o *Driver) GetEldYmEnabled() bool {
	if o == nil || o.EldYmEnabled == nil {
		var ret bool
		return ret
	}
	return *o.EldYmEnabled
}

// GetEldYmEnabledOk returns a tuple with the EldYmEnabled field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Driver) GetEldYmEnabledOk() (bool, bool) {
	if o == nil || o.EldYmEnabled == nil {
		var ret bool
		return ret, false
	}
	return *o.EldYmEnabled, true
}

// HasEldYmEnabled returns a boolean if a field has been set.
func (o *Driver) HasEldYmEnabled() bool {
	if o != nil && o.EldYmEnabled != nil {
		return true
	}

	return false
}

// SetEldYmEnabled gets a reference to the given bool and assigns it to the EldYmEnabled field.
func (o *Driver) SetEldYmEnabled(v bool) {
	o.EldYmEnabled = &v
}

// GetExternalIds returns the ExternalIds field value if set, zero value otherwise.
func (o *Driver) GetExternalIds() map[string]string {
	if o == nil || o.ExternalIds == nil {
		var ret map[string]string
		return ret
	}
	return *o.ExternalIds
}

// GetExternalIdsOk returns a tuple with the ExternalIds field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Driver) GetExternalIdsOk() (map[string]string, bool) {
	if o == nil || o.ExternalIds == nil {
		var ret map[string]string
		return ret, false
	}
	return *o.ExternalIds, true
}

// HasExternalIds returns a boolean if a field has been set.
func (o *Driver) HasExternalIds() bool {
	if o != nil && o.ExternalIds != nil {
		return true
	}

	return false
}

// SetExternalIds gets a reference to the given map[string]string and assigns it to the ExternalIds field.
func (o *Driver) SetExternalIds(v map[string]string) {
	o.ExternalIds = &v
}

// GetId returns the Id field value if set, zero value otherwise.
func (o *Driver) GetId() string {
	if o == nil || o.Id == nil {
		var ret string
		return ret
	}
	return *o.Id
}

// GetIdOk returns a tuple with the Id field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Driver) GetIdOk() (string, bool) {
	if o == nil || o.Id == nil {
		var ret string
		return ret, false
	}
	return *o.Id, true
}

// HasId returns a boolean if a field has been set.
func (o *Driver) HasId() bool {
	if o != nil && o.Id != nil {
		return true
	}

	return false
}

// SetId gets a reference to the given string and assigns it to the Id field.
func (o *Driver) SetId(v string) {
	o.Id = &v
}

// GetIsDeactivated returns the IsDeactivated field value if set, zero value otherwise.
func (o *Driver) GetIsDeactivated() bool {
	if o == nil || o.IsDeactivated == nil {
		var ret bool
		return ret
	}
	return *o.IsDeactivated
}

// GetIsDeactivatedOk returns a tuple with the IsDeactivated field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Driver) GetIsDeactivatedOk() (bool, bool) {
	if o == nil || o.IsDeactivated == nil {
		var ret bool
		return ret, false
	}
	return *o.IsDeactivated, true
}

// HasIsDeactivated returns a boolean if a field has been set.
func (o *Driver) HasIsDeactivated() bool {
	if o != nil && o.IsDeactivated != nil {
		return true
	}

	return false
}

// SetIsDeactivated gets a reference to the given bool and assigns it to the IsDeactivated field.
func (o *Driver) SetIsDeactivated(v bool) {
	o.IsDeactivated = &v
}

// GetLicenseNumber returns the LicenseNumber field value if set, zero value otherwise.
func (o *Driver) GetLicenseNumber() string {
	if o == nil || o.LicenseNumber == nil {
		var ret string
		return ret
	}
	return *o.LicenseNumber
}

// GetLicenseNumberOk returns a tuple with the LicenseNumber field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Driver) GetLicenseNumberOk() (string, bool) {
	if o == nil || o.LicenseNumber == nil {
		var ret string
		return ret, false
	}
	return *o.LicenseNumber, true
}

// HasLicenseNumber returns a boolean if a field has been set.
func (o *Driver) HasLicenseNumber() bool {
	if o != nil && o.LicenseNumber != nil {
		return true
	}

	return false
}

// SetLicenseNumber gets a reference to the given string and assigns it to the LicenseNumber field.
func (o *Driver) SetLicenseNumber(v string) {
	o.LicenseNumber = &v
}

// GetLicenseState returns the LicenseState field value if set, zero value otherwise.
func (o *Driver) GetLicenseState() string {
	if o == nil || o.LicenseState == nil {
		var ret string
		return ret
	}
	return *o.LicenseState
}

// GetLicenseStateOk returns a tuple with the LicenseState field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Driver) GetLicenseStateOk() (string, bool) {
	if o == nil || o.LicenseState == nil {
		var ret string
		return ret, false
	}
	return *o.LicenseState, true
}

// HasLicenseState returns a boolean if a field has been set.
func (o *Driver) HasLicenseState() bool {
	if o != nil && o.LicenseState != nil {
		return true
	}

	return false
}

// SetLicenseState gets a reference to the given string and assigns it to the LicenseState field.
func (o *Driver) SetLicenseState(v string) {
	o.LicenseState = &v
}

// GetLocale returns the Locale field value if set, zero value otherwise.
func (o *Driver) GetLocale() DriverLocale {
	if o == nil || o.Locale == nil {
		var ret DriverLocale
		return ret
	}
	return *o.Locale
}

// GetLocaleOk returns a tuple with the Locale field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Driver) GetLocaleOk() (DriverLocale, bool) {
	if o == nil || o.Locale == nil {
		var ret DriverLocale
		return ret, false
	}
	return *o.Locale, true
}

// HasLocale returns a boolean if a field has been set.
func (o *Driver) HasLocale() bool {
	if o != nil && o.Locale != nil {
		return true
	}

	return false
}

// SetLocale gets a reference to the given DriverLocale and assigns it to the Locale field.
func (o *Driver) SetLocale(v DriverLocale) {
	o.Locale = &v
}

// GetName returns the Name field value if set, zero value otherwise.
func (o *Driver) GetName() string {
	if o == nil || o.Name == nil {
		var ret string
		return ret
	}
	return *o.Name
}

// GetNameOk returns a tuple with the Name field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Driver) GetNameOk() (string, bool) {
	if o == nil || o.Name == nil {
		var ret string
		return ret, false
	}
	return *o.Name, true
}

// HasName returns a boolean if a field has been set.
func (o *Driver) HasName() bool {
	if o != nil && o.Name != nil {
		return true
	}

	return false
}

// SetName gets a reference to the given string and assigns it to the Name field.
func (o *Driver) SetName(v string) {
	o.Name = &v
}

// GetNotes returns the Notes field value if set, zero value otherwise.
func (o *Driver) GetNotes() string {
	if o == nil || o.Notes == nil {
		var ret string
		return ret
	}
	return *o.Notes
}

// GetNotesOk returns a tuple with the Notes field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Driver) GetNotesOk() (string, bool) {
	if o == nil || o.Notes == nil {
		var ret string
		return ret, false
	}
	return *o.Notes, true
}

// HasNotes returns a boolean if a field has been set.
func (o *Driver) HasNotes() bool {
	if o != nil && o.Notes != nil {
		return true
	}

	return false
}

// SetNotes gets a reference to the given string and assigns it to the Notes field.
func (o *Driver) SetNotes(v string) {
	o.Notes = &v
}

// GetPhone returns the Phone field value if set, zero value otherwise.
func (o *Driver) GetPhone() string {
	if o == nil || o.Phone == nil {
		var ret string
		return ret
	}
	return *o.Phone
}

// GetPhoneOk returns a tuple with the Phone field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Driver) GetPhoneOk() (string, bool) {
	if o == nil || o.Phone == nil {
		var ret string
		return ret, false
	}
	return *o.Phone, true
}

// HasPhone returns a boolean if a field has been set.
func (o *Driver) HasPhone() bool {
	if o != nil && o.Phone != nil {
		return true
	}

	return false
}

// SetPhone gets a reference to the given string and assigns it to the Phone field.
func (o *Driver) SetPhone(v string) {
	o.Phone = &v
}

// GetStaticAssignedVehicle returns the StaticAssignedVehicle field value if set, zero value otherwise.
func (o *Driver) GetStaticAssignedVehicle() DriverStaticAssignedVehicle {
	if o == nil || o.StaticAssignedVehicle == nil {
		var ret DriverStaticAssignedVehicle
		return ret
	}
	return *o.StaticAssignedVehicle
}

// GetStaticAssignedVehicleOk returns a tuple with the StaticAssignedVehicle field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Driver) GetStaticAssignedVehicleOk() (DriverStaticAssignedVehicle, bool) {
	if o == nil || o.StaticAssignedVehicle == nil {
		var ret DriverStaticAssignedVehicle
		return ret, false
	}
	return *o.StaticAssignedVehicle, true
}

// HasStaticAssignedVehicle returns a boolean if a field has been set.
func (o *Driver) HasStaticAssignedVehicle() bool {
	if o != nil && o.StaticAssignedVehicle != nil {
		return true
	}

	return false
}

// SetStaticAssignedVehicle gets a reference to the given DriverStaticAssignedVehicle and assigns it to the StaticAssignedVehicle field.
func (o *Driver) SetStaticAssignedVehicle(v DriverStaticAssignedVehicle) {
	o.StaticAssignedVehicle = &v
}

// GetTachographCardNumber returns the TachographCardNumber field value if set, zero value otherwise.
func (o *Driver) GetTachographCardNumber() string {
	if o == nil || o.TachographCardNumber == nil {
		var ret string
		return ret
	}
	return *o.TachographCardNumber
}

// GetTachographCardNumberOk returns a tuple with the TachographCardNumber field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Driver) GetTachographCardNumberOk() (string, bool) {
	if o == nil || o.TachographCardNumber == nil {
		var ret string
		return ret, false
	}
	return *o.TachographCardNumber, true
}

// HasTachographCardNumber returns a boolean if a field has been set.
func (o *Driver) HasTachographCardNumber() bool {
	if o != nil && o.TachographCardNumber != nil {
		return true
	}

	return false
}

// SetTachographCardNumber gets a reference to the given string and assigns it to the TachographCardNumber field.
func (o *Driver) SetTachographCardNumber(v string) {
	o.TachographCardNumber = &v
}

// GetTags returns the Tags field value if set, zero value otherwise.
func (o *Driver) GetTags() []TagTinyResponse {
	if o == nil || o.Tags == nil {
		var ret []TagTinyResponse
		return ret
	}
	return *o.Tags
}

// GetTagsOk returns a tuple with the Tags field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Driver) GetTagsOk() ([]TagTinyResponse, bool) {
	if o == nil || o.Tags == nil {
		var ret []TagTinyResponse
		return ret, false
	}
	return *o.Tags, true
}

// HasTags returns a boolean if a field has been set.
func (o *Driver) HasTags() bool {
	if o != nil && o.Tags != nil {
		return true
	}

	return false
}

// SetTags gets a reference to the given []TagTinyResponse and assigns it to the Tags field.
func (o *Driver) SetTags(v []TagTinyResponse) {
	o.Tags = &v
}

// GetTimezone returns the Timezone field value if set, zero value otherwise.
func (o *Driver) GetTimezone() string {
	if o == nil || o.Timezone == nil {
		var ret string
		return ret
	}
	return *o.Timezone
}

// GetTimezoneOk returns a tuple with the Timezone field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Driver) GetTimezoneOk() (string, bool) {
	if o == nil || o.Timezone == nil {
		var ret string
		return ret, false
	}
	return *o.Timezone, true
}

// HasTimezone returns a boolean if a field has been set.
func (o *Driver) HasTimezone() bool {
	if o != nil && o.Timezone != nil {
		return true
	}

	return false
}

// SetTimezone gets a reference to the given string and assigns it to the Timezone field.
func (o *Driver) SetTimezone(v string) {
	o.Timezone = &v
}

// GetUpdatedAtTime returns the UpdatedAtTime field value if set, zero value otherwise.
func (o *Driver) GetUpdatedAtTime() time.Time {
	if o == nil || o.UpdatedAtTime == nil {
		var ret time.Time
		return ret
	}
	return *o.UpdatedAtTime
}

// GetUpdatedAtTimeOk returns a tuple with the UpdatedAtTime field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Driver) GetUpdatedAtTimeOk() (time.Time, bool) {
	if o == nil || o.UpdatedAtTime == nil {
		var ret time.Time
		return ret, false
	}
	return *o.UpdatedAtTime, true
}

// HasUpdatedAtTime returns a boolean if a field has been set.
func (o *Driver) HasUpdatedAtTime() bool {
	if o != nil && o.UpdatedAtTime != nil {
		return true
	}

	return false
}

// SetUpdatedAtTime gets a reference to the given time.Time and assigns it to the UpdatedAtTime field.
func (o *Driver) SetUpdatedAtTime(v time.Time) {
	o.UpdatedAtTime = &v
}

// GetUsername returns the Username field value if set, zero value otherwise.
func (o *Driver) GetUsername() string {
	if o == nil || o.Username == nil {
		var ret string
		return ret
	}
	return *o.Username
}

// GetUsernameOk returns a tuple with the Username field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Driver) GetUsernameOk() (string, bool) {
	if o == nil || o.Username == nil {
		var ret string
		return ret, false
	}
	return *o.Username, true
}

// HasUsername returns a boolean if a field has been set.
func (o *Driver) HasUsername() bool {
	if o != nil && o.Username != nil {
		return true
	}

	return false
}

// SetUsername gets a reference to the given string and assigns it to the Username field.
func (o *Driver) SetUsername(v string) {
	o.Username = &v
}

// GetVehicleGroupTag returns the VehicleGroupTag field value if set, zero value otherwise.
func (o *Driver) GetVehicleGroupTag() DriverVehicleGroupTag {
	if o == nil || o.VehicleGroupTag == nil {
		var ret DriverVehicleGroupTag
		return ret
	}
	return *o.VehicleGroupTag
}

// GetVehicleGroupTagOk returns a tuple with the VehicleGroupTag field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *Driver) GetVehicleGroupTagOk() (DriverVehicleGroupTag, bool) {
	if o == nil || o.VehicleGroupTag == nil {
		var ret DriverVehicleGroupTag
		return ret, false
	}
	return *o.VehicleGroupTag, true
}

// HasVehicleGroupTag returns a boolean if a field has been set.
func (o *Driver) HasVehicleGroupTag() bool {
	if o != nil && o.VehicleGroupTag != nil {
		return true
	}

	return false
}

// SetVehicleGroupTag gets a reference to the given DriverVehicleGroupTag and assigns it to the VehicleGroupTag field.
func (o *Driver) SetVehicleGroupTag(v DriverVehicleGroupTag) {
	o.VehicleGroupTag = &v
}

type NullableDriver struct {
	Value        Driver
	ExplicitNull bool
}

func (v NullableDriver) MarshalJSON() ([]byte, error) {
	switch {
	case v.ExplicitNull:
		return []byte("null"), nil
	default:
		return json.Marshal(v.Value)
	}
}

func (v *NullableDriver) UnmarshalJSON(src []byte) error {
	if bytes.Equal(src, []byte("null")) {
		v.ExplicitNull = true
		return nil
	}

	return json.Unmarshal(src, &v.Value)
}