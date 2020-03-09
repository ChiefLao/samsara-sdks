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

// V1Document struct for V1Document
type V1Document struct {
	// Name of the document type.
	DocumentType string `json:"documentType"`
	// The time in Unix epoch milliseconds that the document was created in the driver app.
	DriverCreatedAtMs int64 `json:"driverCreatedAtMs"`
	// ID of the driver for whom the document is submitted.
	DriverId int64 `json:"driverId"`
	// The fields associated with this document.
	Fields []V1DocumentField `json:"fields"`
	// ID of the document.
	Id string `json:"id"`
	// Organization ID that the document belongs to.
	OrgId int64 `json:"orgId"`
	// The time in Unix epoch milliseconds that the document was received by the server.
	ServerCreatedAtMs int64 `json:"serverCreatedAtMs"`
	// The time in Unix epoch milliseconds that the document was updated on the server.
	ServerUpdatedAtMs int64 `json:"serverUpdatedAtMs"`
	// ID of the vehicle the driver was signed into when the document was submitted. Will be `null` if the document `state` is `Required`.
	VehicleId int64 `json:"vehicleId"`
	// ID of the Samsara dispatch job for which the document is submitted.
	DispatchJobId int64 `json:"dispatchJobId"`
	// Notes submitted with this document.
	Notes string `json:"notes"`
	// The condition of the document created for the driver. Can be either `Required` or `Submitted`. If no value is specified, `state` defaults to `Required`. `Required` documents are pre-populated documents for the Driver to fill out in the Driver App and have not yet been submitted. `Submitted` documents have been submitted by the driver in the Driver App.
	State *string `json:"state,omitempty"`
}

// GetDocumentType returns the DocumentType field value
func (o *V1Document) GetDocumentType() string {
	if o == nil {
		var ret string
		return ret
	}

	return o.DocumentType
}

// SetDocumentType sets field value
func (o *V1Document) SetDocumentType(v string) {
	o.DocumentType = v
}

// GetDriverCreatedAtMs returns the DriverCreatedAtMs field value
func (o *V1Document) GetDriverCreatedAtMs() int64 {
	if o == nil {
		var ret int64
		return ret
	}

	return o.DriverCreatedAtMs
}

// SetDriverCreatedAtMs sets field value
func (o *V1Document) SetDriverCreatedAtMs(v int64) {
	o.DriverCreatedAtMs = v
}

// GetDriverId returns the DriverId field value
func (o *V1Document) GetDriverId() int64 {
	if o == nil {
		var ret int64
		return ret
	}

	return o.DriverId
}

// SetDriverId sets field value
func (o *V1Document) SetDriverId(v int64) {
	o.DriverId = v
}

// GetFields returns the Fields field value
func (o *V1Document) GetFields() []V1DocumentField {
	if o == nil {
		var ret []V1DocumentField
		return ret
	}

	return o.Fields
}

// SetFields sets field value
func (o *V1Document) SetFields(v []V1DocumentField) {
	o.Fields = v
}

// GetId returns the Id field value
func (o *V1Document) GetId() string {
	if o == nil {
		var ret string
		return ret
	}

	return o.Id
}

// SetId sets field value
func (o *V1Document) SetId(v string) {
	o.Id = v
}

// GetOrgId returns the OrgId field value
func (o *V1Document) GetOrgId() int64 {
	if o == nil {
		var ret int64
		return ret
	}

	return o.OrgId
}

// SetOrgId sets field value
func (o *V1Document) SetOrgId(v int64) {
	o.OrgId = v
}

// GetServerCreatedAtMs returns the ServerCreatedAtMs field value
func (o *V1Document) GetServerCreatedAtMs() int64 {
	if o == nil {
		var ret int64
		return ret
	}

	return o.ServerCreatedAtMs
}

// SetServerCreatedAtMs sets field value
func (o *V1Document) SetServerCreatedAtMs(v int64) {
	o.ServerCreatedAtMs = v
}

// GetServerUpdatedAtMs returns the ServerUpdatedAtMs field value
func (o *V1Document) GetServerUpdatedAtMs() int64 {
	if o == nil {
		var ret int64
		return ret
	}

	return o.ServerUpdatedAtMs
}

// SetServerUpdatedAtMs sets field value
func (o *V1Document) SetServerUpdatedAtMs(v int64) {
	o.ServerUpdatedAtMs = v
}

// GetVehicleId returns the VehicleId field value
func (o *V1Document) GetVehicleId() int64 {
	if o == nil {
		var ret int64
		return ret
	}

	return o.VehicleId
}

// SetVehicleId sets field value
func (o *V1Document) SetVehicleId(v int64) {
	o.VehicleId = v
}

// GetDispatchJobId returns the DispatchJobId field value
func (o *V1Document) GetDispatchJobId() int64 {
	if o == nil {
		var ret int64
		return ret
	}

	return o.DispatchJobId
}

// SetDispatchJobId sets field value
func (o *V1Document) SetDispatchJobId(v int64) {
	o.DispatchJobId = v
}

// GetNotes returns the Notes field value
func (o *V1Document) GetNotes() string {
	if o == nil {
		var ret string
		return ret
	}

	return o.Notes
}

// SetNotes sets field value
func (o *V1Document) SetNotes(v string) {
	o.Notes = v
}

// GetState returns the State field value if set, zero value otherwise.
func (o *V1Document) GetState() string {
	if o == nil || o.State == nil {
		var ret string
		return ret
	}
	return *o.State
}

// GetStateOk returns a tuple with the State field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *V1Document) GetStateOk() (string, bool) {
	if o == nil || o.State == nil {
		var ret string
		return ret, false
	}
	return *o.State, true
}

// HasState returns a boolean if a field has been set.
func (o *V1Document) HasState() bool {
	if o != nil && o.State != nil {
		return true
	}

	return false
}

// SetState gets a reference to the given string and assigns it to the State field.
func (o *V1Document) SetState(v string) {
	o.State = &v
}

type NullableV1Document struct {
	Value        V1Document
	ExplicitNull bool
}

func (v NullableV1Document) MarshalJSON() ([]byte, error) {
	switch {
	case v.ExplicitNull:
		return []byte("null"), nil
	default:
		return json.Marshal(v.Value)
	}
}

func (v *NullableV1Document) UnmarshalJSON(src []byte) error {
	if bytes.Equal(src, []byte("null")) {
		v.ExplicitNull = true
		return nil
	}

	return json.Unmarshal(src, &v.Value)
}