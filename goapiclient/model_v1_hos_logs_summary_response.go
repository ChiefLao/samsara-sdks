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

// V1HosLogsSummaryResponse struct for V1HosLogsSummaryResponse
type V1HosLogsSummaryResponse struct {
	Drivers    *[]V1HosLogsSummaryResponseDrivers  `json:"drivers,omitempty"`
	Pagination *V1HosLogsSummaryResponsePagination `json:"pagination,omitempty"`
}

// GetDrivers returns the Drivers field value if set, zero value otherwise.
func (o *V1HosLogsSummaryResponse) GetDrivers() []V1HosLogsSummaryResponseDrivers {
	if o == nil || o.Drivers == nil {
		var ret []V1HosLogsSummaryResponseDrivers
		return ret
	}
	return *o.Drivers
}

// GetDriversOk returns a tuple with the Drivers field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *V1HosLogsSummaryResponse) GetDriversOk() ([]V1HosLogsSummaryResponseDrivers, bool) {
	if o == nil || o.Drivers == nil {
		var ret []V1HosLogsSummaryResponseDrivers
		return ret, false
	}
	return *o.Drivers, true
}

// HasDrivers returns a boolean if a field has been set.
func (o *V1HosLogsSummaryResponse) HasDrivers() bool {
	if o != nil && o.Drivers != nil {
		return true
	}

	return false
}

// SetDrivers gets a reference to the given []V1HosLogsSummaryResponseDrivers and assigns it to the Drivers field.
func (o *V1HosLogsSummaryResponse) SetDrivers(v []V1HosLogsSummaryResponseDrivers) {
	o.Drivers = &v
}

// GetPagination returns the Pagination field value if set, zero value otherwise.
func (o *V1HosLogsSummaryResponse) GetPagination() V1HosLogsSummaryResponsePagination {
	if o == nil || o.Pagination == nil {
		var ret V1HosLogsSummaryResponsePagination
		return ret
	}
	return *o.Pagination
}

// GetPaginationOk returns a tuple with the Pagination field value if set, zero value otherwise
// and a boolean to check if the value has been set.
func (o *V1HosLogsSummaryResponse) GetPaginationOk() (V1HosLogsSummaryResponsePagination, bool) {
	if o == nil || o.Pagination == nil {
		var ret V1HosLogsSummaryResponsePagination
		return ret, false
	}
	return *o.Pagination, true
}

// HasPagination returns a boolean if a field has been set.
func (o *V1HosLogsSummaryResponse) HasPagination() bool {
	if o != nil && o.Pagination != nil {
		return true
	}

	return false
}

// SetPagination gets a reference to the given V1HosLogsSummaryResponsePagination and assigns it to the Pagination field.
func (o *V1HosLogsSummaryResponse) SetPagination(v V1HosLogsSummaryResponsePagination) {
	o.Pagination = &v
}

type NullableV1HosLogsSummaryResponse struct {
	Value        V1HosLogsSummaryResponse
	ExplicitNull bool
}

func (v NullableV1HosLogsSummaryResponse) MarshalJSON() ([]byte, error) {
	switch {
	case v.ExplicitNull:
		return []byte("null"), nil
	default:
		return json.Marshal(v.Value)
	}
}

func (v *NullableV1HosLogsSummaryResponse) UnmarshalJSON(src []byte) error {
	if bytes.Equal(src, []byte("null")) {
		v.ExplicitNull = true
		return nil
	}

	return json.Unmarshal(src, &v.Value)
}