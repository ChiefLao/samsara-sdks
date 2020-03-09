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

// V1VehicleMaintenancePassenger Passenger vehicle data. Null if no data is available.
type V1VehicleMaintenancePassenger struct {
	CheckEngineLight *V1VehicleMaintenancePassengerCheckEngineLight `json:"checkEngineLight,omitempty"`
	// Passenger vehicle DTCs.
	DiagnosticTroubleCodes *[]V1VehicleMaintenancePassengerDiagnosticTroubleCodes `json:"diagnosticTroubleCodes,omitempty"`
}

// GetCheckEngineLight returns the CheckEngineLight field value if set, zero value otherwise.
func (o *V1VehicleMaintenancePassenger) GetCheckEngineLight() V1VehicleMaintenancePassengerCheckEngineLight {
	if o == nil || o.CheckEngineLight == nil {
		var ret V1VehicleMaintenancePassengerCheckEngineLight
		return ret
	}
	return *o.CheckEngineLight
}

// GetCheckEngineLightOk returns a tuple with the CheckEngineLight field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *V1VehicleMaintenancePassenger) GetCheckEngineLightOk() (V1VehicleMaintenancePassengerCheckEngineLight, bool) {
	if o == nil || o.CheckEngineLight == nil {
		var ret V1VehicleMaintenancePassengerCheckEngineLight
		return ret, false
	}
	return *o.CheckEngineLight, true
}

// HasCheckEngineLight returns a boolean if a field has been set.
func (o *V1VehicleMaintenancePassenger) HasCheckEngineLight() bool {
	if o != nil && o.CheckEngineLight != nil {
		return true
	}

	return false
}

// SetCheckEngineLight gets a reference to the given V1VehicleMaintenancePassengerCheckEngineLight and assigns it to the CheckEngineLight field.
func (o *V1VehicleMaintenancePassenger) SetCheckEngineLight(v V1VehicleMaintenancePassengerCheckEngineLight) {
	o.CheckEngineLight = &v
}

// GetDiagnosticTroubleCodes returns the DiagnosticTroubleCodes field value if set, zero value otherwise.
func (o *V1VehicleMaintenancePassenger) GetDiagnosticTroubleCodes() []V1VehicleMaintenancePassengerDiagnosticTroubleCodes {
	if o == nil || o.DiagnosticTroubleCodes == nil {
		var ret []V1VehicleMaintenancePassengerDiagnosticTroubleCodes
		return ret
	}
	return *o.DiagnosticTroubleCodes
}

// GetDiagnosticTroubleCodesOk returns a tuple with the DiagnosticTroubleCodes field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *V1VehicleMaintenancePassenger) GetDiagnosticTroubleCodesOk() ([]V1VehicleMaintenancePassengerDiagnosticTroubleCodes, bool) {
	if o == nil || o.DiagnosticTroubleCodes == nil {
		var ret []V1VehicleMaintenancePassengerDiagnosticTroubleCodes
		return ret, false
	}
	return *o.DiagnosticTroubleCodes, true
}

// HasDiagnosticTroubleCodes returns a boolean if a field has been set.
func (o *V1VehicleMaintenancePassenger) HasDiagnosticTroubleCodes() bool {
	if o != nil && o.DiagnosticTroubleCodes != nil {
		return true
	}

	return false
}

// SetDiagnosticTroubleCodes gets a reference to the given []V1VehicleMaintenancePassengerDiagnosticTroubleCodes and assigns it to the DiagnosticTroubleCodes field.
func (o *V1VehicleMaintenancePassenger) SetDiagnosticTroubleCodes(v []V1VehicleMaintenancePassengerDiagnosticTroubleCodes) {
	o.DiagnosticTroubleCodes = &v
}

type NullableV1VehicleMaintenancePassenger struct {
	Value        V1VehicleMaintenancePassenger
	ExplicitNull bool
}

func (v NullableV1VehicleMaintenancePassenger) MarshalJSON() ([]byte, error) {
	switch {
	case v.ExplicitNull:
		return []byte("null"), nil
	default:
		return json.Marshal(v.Value)
	}
}

func (v *NullableV1VehicleMaintenancePassenger) UnmarshalJSON(src []byte) error {
	if bytes.Equal(src, []byte("null")) {
		v.ExplicitNull = true
		return nil
	}

	return json.Unmarshal(src, &v.Value)
}