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

// EquipmentLocation struct for EquipmentLocation
type EquipmentLocation struct {
	// GPS latitude represented in degrees
	Latitude float64 `json:"latitude"`
	// GPS longitude represented in degrees
	Longitude float64 `json:"longitude"`
	// Heading of the equipment in degrees.
	Heading *float64 `json:"heading,omitempty"`
	// Speed of the equipment in miles per hour.
	Speed *float64 `json:"speed,omitempty"`
	// UTC timestamp of the time the data point was generated by the equipment, in RFC3339 format.
	Time string `json:"time"`
}

// GetLatitude returns the Latitude field value
func (o *EquipmentLocation) GetLatitude() float64 {
	if o == nil {
		var ret float64
		return ret
	}

	return o.Latitude
}

// SetLatitude sets field value
func (o *EquipmentLocation) SetLatitude(v float64) {
	o.Latitude = v
}

// GetLongitude returns the Longitude field value
func (o *EquipmentLocation) GetLongitude() float64 {
	if o == nil {
		var ret float64
		return ret
	}

	return o.Longitude
}

// SetLongitude sets field value
func (o *EquipmentLocation) SetLongitude(v float64) {
	o.Longitude = v
}

// GetHeading returns the Heading field value if set, zero value otherwise.
func (o *EquipmentLocation) GetHeading() float64 {
	if o == nil || o.Heading == nil {
		var ret float64
		return ret
	}
	return *o.Heading
}

// GetHeadingOk returns a tuple with the Heading field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *EquipmentLocation) GetHeadingOk() (float64, bool) {
	if o == nil || o.Heading == nil {
		var ret float64
		return ret, false
	}
	return *o.Heading, true
}

// HasHeading returns a boolean if a field has been set.
func (o *EquipmentLocation) HasHeading() bool {
	if o != nil && o.Heading != nil {
		return true
	}

	return false
}

// SetHeading gets a reference to the given float64 and assigns it to the Heading field.
func (o *EquipmentLocation) SetHeading(v float64) {
	o.Heading = &v
}

// GetSpeed returns the Speed field value if set, zero value otherwise.
func (o *EquipmentLocation) GetSpeed() float64 {
	if o == nil || o.Speed == nil {
		var ret float64
		return ret
	}
	return *o.Speed
}

// GetSpeedOk returns a tuple with the Speed field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *EquipmentLocation) GetSpeedOk() (float64, bool) {
	if o == nil || o.Speed == nil {
		var ret float64
		return ret, false
	}
	return *o.Speed, true
}

// HasSpeed returns a boolean if a field has been set.
func (o *EquipmentLocation) HasSpeed() bool {
	if o != nil && o.Speed != nil {
		return true
	}

	return false
}

// SetSpeed gets a reference to the given float64 and assigns it to the Speed field.
func (o *EquipmentLocation) SetSpeed(v float64) {
	o.Speed = &v
}

// GetTime returns the Time field value
func (o *EquipmentLocation) GetTime() string {
	if o == nil {
		var ret string
		return ret
	}

	return o.Time
}

// SetTime sets field value
func (o *EquipmentLocation) SetTime(v string) {
	o.Time = v
}

type NullableEquipmentLocation struct {
	Value        EquipmentLocation
	ExplicitNull bool
}

func (v NullableEquipmentLocation) MarshalJSON() ([]byte, error) {
	switch {
	case v.ExplicitNull:
		return []byte("null"), nil
	default:
		return json.Marshal(v.Value)
	}
}

func (v *NullableEquipmentLocation) UnmarshalJSON(src []byte) error {
	if bytes.Equal(src, []byte("null")) {
		v.ExplicitNull = true
		return nil
	}

	return json.Unmarshal(src, &v.Value)
}