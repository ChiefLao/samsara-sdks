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

// V1AssetReeferResponseReeferStats struct for V1AssetReeferResponseReeferStats
type V1AssetReeferResponseReeferStats struct {
	// Reefer alarms
	Alarms *[]V1AssetReeferResponseReeferStatsAlarms1 `json:"alarms,omitempty"`
	// Engine hours of the reefer
	EngineHours *[]V1AssetReeferResponseReeferStatsEngineHours `json:"engineHours,omitempty"`
	// Fuel percentage of the reefer
	FuelPercentage *[]V1AssetReeferResponseReeferStatsFuelPercentage `json:"fuelPercentage,omitempty"`
	// Power status of the reefer
	PowerStatus *[]V1AssetReeferResponseReeferStatsPowerStatus `json:"powerStatus,omitempty"`
	// Return air temperature of the reefer
	ReturnAirTemp *[]V1AssetReeferResponseReeferStatsReturnAirTemp `json:"returnAirTemp,omitempty"`
	// Set point temperature of the reefer
	SetPoint *[]V1AssetReeferResponseReeferStatsSetPoint `json:"setPoint,omitempty"`
}

// GetAlarms returns the Alarms field value if set, zero value otherwise.
func (o *V1AssetReeferResponseReeferStats) GetAlarms() []V1AssetReeferResponseReeferStatsAlarms1 {
	if o == nil || o.Alarms == nil {
		var ret []V1AssetReeferResponseReeferStatsAlarms1
		return ret
	}
	return *o.Alarms
}

// GetAlarmsOk returns a tuple with the Alarms field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *V1AssetReeferResponseReeferStats) GetAlarmsOk() ([]V1AssetReeferResponseReeferStatsAlarms1, bool) {
	if o == nil || o.Alarms == nil {
		var ret []V1AssetReeferResponseReeferStatsAlarms1
		return ret, false
	}
	return *o.Alarms, true
}

// HasAlarms returns a boolean if a field has been set.
func (o *V1AssetReeferResponseReeferStats) HasAlarms() bool {
	if o != nil && o.Alarms != nil {
		return true
	}

	return false
}

// SetAlarms gets a reference to the given []V1AssetReeferResponseReeferStatsAlarms1 and assigns it to the Alarms field.
func (o *V1AssetReeferResponseReeferStats) SetAlarms(v []V1AssetReeferResponseReeferStatsAlarms1) {
	o.Alarms = &v
}

// GetEngineHours returns the EngineHours field value if set, zero value otherwise.
func (o *V1AssetReeferResponseReeferStats) GetEngineHours() []V1AssetReeferResponseReeferStatsEngineHours {
	if o == nil || o.EngineHours == nil {
		var ret []V1AssetReeferResponseReeferStatsEngineHours
		return ret
	}
	return *o.EngineHours
}

// GetEngineHoursOk returns a tuple with the EngineHours field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *V1AssetReeferResponseReeferStats) GetEngineHoursOk() ([]V1AssetReeferResponseReeferStatsEngineHours, bool) {
	if o == nil || o.EngineHours == nil {
		var ret []V1AssetReeferResponseReeferStatsEngineHours
		return ret, false
	}
	return *o.EngineHours, true
}

// HasEngineHours returns a boolean if a field has been set.
func (o *V1AssetReeferResponseReeferStats) HasEngineHours() bool {
	if o != nil && o.EngineHours != nil {
		return true
	}

	return false
}

// SetEngineHours gets a reference to the given []V1AssetReeferResponseReeferStatsEngineHours and assigns it to the EngineHours field.
func (o *V1AssetReeferResponseReeferStats) SetEngineHours(v []V1AssetReeferResponseReeferStatsEngineHours) {
	o.EngineHours = &v
}

// GetFuelPercentage returns the FuelPercentage field value if set, zero value otherwise.
func (o *V1AssetReeferResponseReeferStats) GetFuelPercentage() []V1AssetReeferResponseReeferStatsFuelPercentage {
	if o == nil || o.FuelPercentage == nil {
		var ret []V1AssetReeferResponseReeferStatsFuelPercentage
		return ret
	}
	return *o.FuelPercentage
}

// GetFuelPercentageOk returns a tuple with the FuelPercentage field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *V1AssetReeferResponseReeferStats) GetFuelPercentageOk() ([]V1AssetReeferResponseReeferStatsFuelPercentage, bool) {
	if o == nil || o.FuelPercentage == nil {
		var ret []V1AssetReeferResponseReeferStatsFuelPercentage
		return ret, false
	}
	return *o.FuelPercentage, true
}

// HasFuelPercentage returns a boolean if a field has been set.
func (o *V1AssetReeferResponseReeferStats) HasFuelPercentage() bool {
	if o != nil && o.FuelPercentage != nil {
		return true
	}

	return false
}

// SetFuelPercentage gets a reference to the given []V1AssetReeferResponseReeferStatsFuelPercentage and assigns it to the FuelPercentage field.
func (o *V1AssetReeferResponseReeferStats) SetFuelPercentage(v []V1AssetReeferResponseReeferStatsFuelPercentage) {
	o.FuelPercentage = &v
}

// GetPowerStatus returns the PowerStatus field value if set, zero value otherwise.
func (o *V1AssetReeferResponseReeferStats) GetPowerStatus() []V1AssetReeferResponseReeferStatsPowerStatus {
	if o == nil || o.PowerStatus == nil {
		var ret []V1AssetReeferResponseReeferStatsPowerStatus
		return ret
	}
	return *o.PowerStatus
}

// GetPowerStatusOk returns a tuple with the PowerStatus field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *V1AssetReeferResponseReeferStats) GetPowerStatusOk() ([]V1AssetReeferResponseReeferStatsPowerStatus, bool) {
	if o == nil || o.PowerStatus == nil {
		var ret []V1AssetReeferResponseReeferStatsPowerStatus
		return ret, false
	}
	return *o.PowerStatus, true
}

// HasPowerStatus returns a boolean if a field has been set.
func (o *V1AssetReeferResponseReeferStats) HasPowerStatus() bool {
	if o != nil && o.PowerStatus != nil {
		return true
	}

	return false
}

// SetPowerStatus gets a reference to the given []V1AssetReeferResponseReeferStatsPowerStatus and assigns it to the PowerStatus field.
func (o *V1AssetReeferResponseReeferStats) SetPowerStatus(v []V1AssetReeferResponseReeferStatsPowerStatus) {
	o.PowerStatus = &v
}

// GetReturnAirTemp returns the ReturnAirTemp field value if set, zero value otherwise.
func (o *V1AssetReeferResponseReeferStats) GetReturnAirTemp() []V1AssetReeferResponseReeferStatsReturnAirTemp {
	if o == nil || o.ReturnAirTemp == nil {
		var ret []V1AssetReeferResponseReeferStatsReturnAirTemp
		return ret
	}
	return *o.ReturnAirTemp
}

// GetReturnAirTempOk returns a tuple with the ReturnAirTemp field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *V1AssetReeferResponseReeferStats) GetReturnAirTempOk() ([]V1AssetReeferResponseReeferStatsReturnAirTemp, bool) {
	if o == nil || o.ReturnAirTemp == nil {
		var ret []V1AssetReeferResponseReeferStatsReturnAirTemp
		return ret, false
	}
	return *o.ReturnAirTemp, true
}

// HasReturnAirTemp returns a boolean if a field has been set.
func (o *V1AssetReeferResponseReeferStats) HasReturnAirTemp() bool {
	if o != nil && o.ReturnAirTemp != nil {
		return true
	}

	return false
}

// SetReturnAirTemp gets a reference to the given []V1AssetReeferResponseReeferStatsReturnAirTemp and assigns it to the ReturnAirTemp field.
func (o *V1AssetReeferResponseReeferStats) SetReturnAirTemp(v []V1AssetReeferResponseReeferStatsReturnAirTemp) {
	o.ReturnAirTemp = &v
}

// GetSetPoint returns the SetPoint field value if set, zero value otherwise.
func (o *V1AssetReeferResponseReeferStats) GetSetPoint() []V1AssetReeferResponseReeferStatsSetPoint {
	if o == nil || o.SetPoint == nil {
		var ret []V1AssetReeferResponseReeferStatsSetPoint
		return ret
	}
	return *o.SetPoint
}

// GetSetPointOk returns a tuple with the SetPoint field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *V1AssetReeferResponseReeferStats) GetSetPointOk() ([]V1AssetReeferResponseReeferStatsSetPoint, bool) {
	if o == nil || o.SetPoint == nil {
		var ret []V1AssetReeferResponseReeferStatsSetPoint
		return ret, false
	}
	return *o.SetPoint, true
}

// HasSetPoint returns a boolean if a field has been set.
func (o *V1AssetReeferResponseReeferStats) HasSetPoint() bool {
	if o != nil && o.SetPoint != nil {
		return true
	}

	return false
}

// SetSetPoint gets a reference to the given []V1AssetReeferResponseReeferStatsSetPoint and assigns it to the SetPoint field.
func (o *V1AssetReeferResponseReeferStats) SetSetPoint(v []V1AssetReeferResponseReeferStatsSetPoint) {
	o.SetPoint = &v
}

type NullableV1AssetReeferResponseReeferStats struct {
	Value        V1AssetReeferResponseReeferStats
	ExplicitNull bool
}

func (v NullableV1AssetReeferResponseReeferStats) MarshalJSON() ([]byte, error) {
	switch {
	case v.ExplicitNull:
		return []byte("null"), nil
	default:
		return json.Marshal(v.Value)
	}
}

func (v *NullableV1AssetReeferResponseReeferStats) UnmarshalJSON(src []byte) error {
	if bytes.Equal(src, []byte("null")) {
		v.ExplicitNull = true
		return nil
	}

	return json.Unmarshal(src, &v.Value)
}