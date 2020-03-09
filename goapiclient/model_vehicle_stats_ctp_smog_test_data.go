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

// VehicleStatsCtpSmogTestData Required data for one CTP smog test.
type VehicleStatsCtpSmogTestData struct {
	// CAN bus communication protocol as detected by the vehicle gateway.
	CommProtocol *string `json:"commProtocol,omitempty"`
	// CTP firmware version as reported by the vehicle gateway.
	DeviceFirmware *string `json:"deviceFirmware,omitempty"`
	// Positive battery voltage as detected by the vehicle gateway reported in millivolts.
	DlcPinVoltageMilliVolts *int32 `json:"dlcPinVoltageMilliVolts,omitempty"`
	// Indicates DlcPinVoltageMilliVolts was successfully read from the CAN bus.
	DlcPinVoltageMilliVoltsValid *bool `json:"dlcPinVoltageMilliVoltsValid,omitempty"`
	// Device serial number.
	LinkId *int32 `json:"linkId,omitempty"`
	// Contains all of the specific OBD data collected for a single ECU present on a vehicle. There can can be multiple ECUs on a vehicle.
	RemoteObdTestRecords *[]RemoteObdTestRecordType `json:"remoteObdTestRecords,omitempty"`
	// UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`.
	TestDateTime *time.Time `json:"testDateTime,omitempty"`
}

// GetCommProtocol returns the CommProtocol field value if set, zero value otherwise.
func (o *VehicleStatsCtpSmogTestData) GetCommProtocol() string {
	if o == nil || o.CommProtocol == nil {
		var ret string
		return ret
	}
	return *o.CommProtocol
}

// GetCommProtocolOk returns a tuple with the CommProtocol field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *VehicleStatsCtpSmogTestData) GetCommProtocolOk() (string, bool) {
	if o == nil || o.CommProtocol == nil {
		var ret string
		return ret, false
	}
	return *o.CommProtocol, true
}

// HasCommProtocol returns a boolean if a field has been set.
func (o *VehicleStatsCtpSmogTestData) HasCommProtocol() bool {
	if o != nil && o.CommProtocol != nil {
		return true
	}

	return false
}

// SetCommProtocol gets a reference to the given string and assigns it to the CommProtocol field.
func (o *VehicleStatsCtpSmogTestData) SetCommProtocol(v string) {
	o.CommProtocol = &v
}

// GetDeviceFirmware returns the DeviceFirmware field value if set, zero value otherwise.
func (o *VehicleStatsCtpSmogTestData) GetDeviceFirmware() string {
	if o == nil || o.DeviceFirmware == nil {
		var ret string
		return ret
	}
	return *o.DeviceFirmware
}

// GetDeviceFirmwareOk returns a tuple with the DeviceFirmware field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *VehicleStatsCtpSmogTestData) GetDeviceFirmwareOk() (string, bool) {
	if o == nil || o.DeviceFirmware == nil {
		var ret string
		return ret, false
	}
	return *o.DeviceFirmware, true
}

// HasDeviceFirmware returns a boolean if a field has been set.
func (o *VehicleStatsCtpSmogTestData) HasDeviceFirmware() bool {
	if o != nil && o.DeviceFirmware != nil {
		return true
	}

	return false
}

// SetDeviceFirmware gets a reference to the given string and assigns it to the DeviceFirmware field.
func (o *VehicleStatsCtpSmogTestData) SetDeviceFirmware(v string) {
	o.DeviceFirmware = &v
}

// GetDlcPinVoltageMilliVolts returns the DlcPinVoltageMilliVolts field value if set, zero value otherwise.
func (o *VehicleStatsCtpSmogTestData) GetDlcPinVoltageMilliVolts() int32 {
	if o == nil || o.DlcPinVoltageMilliVolts == nil {
		var ret int32
		return ret
	}
	return *o.DlcPinVoltageMilliVolts
}

// GetDlcPinVoltageMilliVoltsOk returns a tuple with the DlcPinVoltageMilliVolts field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *VehicleStatsCtpSmogTestData) GetDlcPinVoltageMilliVoltsOk() (int32, bool) {
	if o == nil || o.DlcPinVoltageMilliVolts == nil {
		var ret int32
		return ret, false
	}
	return *o.DlcPinVoltageMilliVolts, true
}

// HasDlcPinVoltageMilliVolts returns a boolean if a field has been set.
func (o *VehicleStatsCtpSmogTestData) HasDlcPinVoltageMilliVolts() bool {
	if o != nil && o.DlcPinVoltageMilliVolts != nil {
		return true
	}

	return false
}

// SetDlcPinVoltageMilliVolts gets a reference to the given int32 and assigns it to the DlcPinVoltageMilliVolts field.
func (o *VehicleStatsCtpSmogTestData) SetDlcPinVoltageMilliVolts(v int32) {
	o.DlcPinVoltageMilliVolts = &v
}

// GetDlcPinVoltageMilliVoltsValid returns the DlcPinVoltageMilliVoltsValid field value if set, zero value otherwise.
func (o *VehicleStatsCtpSmogTestData) GetDlcPinVoltageMilliVoltsValid() bool {
	if o == nil || o.DlcPinVoltageMilliVoltsValid == nil {
		var ret bool
		return ret
	}
	return *o.DlcPinVoltageMilliVoltsValid
}

// GetDlcPinVoltageMilliVoltsValidOk returns a tuple with the DlcPinVoltageMilliVoltsValid field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *VehicleStatsCtpSmogTestData) GetDlcPinVoltageMilliVoltsValidOk() (bool, bool) {
	if o == nil || o.DlcPinVoltageMilliVoltsValid == nil {
		var ret bool
		return ret, false
	}
	return *o.DlcPinVoltageMilliVoltsValid, true
}

// HasDlcPinVoltageMilliVoltsValid returns a boolean if a field has been set.
func (o *VehicleStatsCtpSmogTestData) HasDlcPinVoltageMilliVoltsValid() bool {
	if o != nil && o.DlcPinVoltageMilliVoltsValid != nil {
		return true
	}

	return false
}

// SetDlcPinVoltageMilliVoltsValid gets a reference to the given bool and assigns it to the DlcPinVoltageMilliVoltsValid field.
func (o *VehicleStatsCtpSmogTestData) SetDlcPinVoltageMilliVoltsValid(v bool) {
	o.DlcPinVoltageMilliVoltsValid = &v
}

// GetLinkId returns the LinkId field value if set, zero value otherwise.
func (o *VehicleStatsCtpSmogTestData) GetLinkId() int32 {
	if o == nil || o.LinkId == nil {
		var ret int32
		return ret
	}
	return *o.LinkId
}

// GetLinkIdOk returns a tuple with the LinkId field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *VehicleStatsCtpSmogTestData) GetLinkIdOk() (int32, bool) {
	if o == nil || o.LinkId == nil {
		var ret int32
		return ret, false
	}
	return *o.LinkId, true
}

// HasLinkId returns a boolean if a field has been set.
func (o *VehicleStatsCtpSmogTestData) HasLinkId() bool {
	if o != nil && o.LinkId != nil {
		return true
	}

	return false
}

// SetLinkId gets a reference to the given int32 and assigns it to the LinkId field.
func (o *VehicleStatsCtpSmogTestData) SetLinkId(v int32) {
	o.LinkId = &v
}

// GetRemoteObdTestRecords returns the RemoteObdTestRecords field value if set, zero value otherwise.
func (o *VehicleStatsCtpSmogTestData) GetRemoteObdTestRecords() []RemoteObdTestRecordType {
	if o == nil || o.RemoteObdTestRecords == nil {
		var ret []RemoteObdTestRecordType
		return ret
	}
	return *o.RemoteObdTestRecords
}

// GetRemoteObdTestRecordsOk returns a tuple with the RemoteObdTestRecords field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *VehicleStatsCtpSmogTestData) GetRemoteObdTestRecordsOk() ([]RemoteObdTestRecordType, bool) {
	if o == nil || o.RemoteObdTestRecords == nil {
		var ret []RemoteObdTestRecordType
		return ret, false
	}
	return *o.RemoteObdTestRecords, true
}

// HasRemoteObdTestRecords returns a boolean if a field has been set.
func (o *VehicleStatsCtpSmogTestData) HasRemoteObdTestRecords() bool {
	if o != nil && o.RemoteObdTestRecords != nil {
		return true
	}

	return false
}

// SetRemoteObdTestRecords gets a reference to the given []RemoteObdTestRecordType and assigns it to the RemoteObdTestRecords field.
func (o *VehicleStatsCtpSmogTestData) SetRemoteObdTestRecords(v []RemoteObdTestRecordType) {
	o.RemoteObdTestRecords = &v
}

// GetTestDateTime returns the TestDateTime field value if set, zero value otherwise.
func (o *VehicleStatsCtpSmogTestData) GetTestDateTime() time.Time {
	if o == nil || o.TestDateTime == nil {
		var ret time.Time
		return ret
	}
	return *o.TestDateTime
}

// GetTestDateTimeOk returns a tuple with the TestDateTime field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *VehicleStatsCtpSmogTestData) GetTestDateTimeOk() (time.Time, bool) {
	if o == nil || o.TestDateTime == nil {
		var ret time.Time
		return ret, false
	}
	return *o.TestDateTime, true
}

// HasTestDateTime returns a boolean if a field has been set.
func (o *VehicleStatsCtpSmogTestData) HasTestDateTime() bool {
	if o != nil && o.TestDateTime != nil {
		return true
	}

	return false
}

// SetTestDateTime gets a reference to the given time.Time and assigns it to the TestDateTime field.
func (o *VehicleStatsCtpSmogTestData) SetTestDateTime(v time.Time) {
	o.TestDateTime = &v
}

type NullableVehicleStatsCtpSmogTestData struct {
	Value        VehicleStatsCtpSmogTestData
	ExplicitNull bool
}

func (v NullableVehicleStatsCtpSmogTestData) MarshalJSON() ([]byte, error) {
	switch {
	case v.ExplicitNull:
		return []byte("null"), nil
	default:
		return json.Marshal(v.Value)
	}
}

func (v *NullableVehicleStatsCtpSmogTestData) UnmarshalJSON(src []byte) error {
	if bytes.Equal(src, []byte("null")) {
		v.ExplicitNull = true
		return nil
	}

	return json.Unmarshal(src, &v.Value)
}